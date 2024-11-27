# Service绑定服务

特点：

- 组件（如Activity）可以向Service（也就是服务端）发送请求，或者调用Service（服务端）的方法，此时被绑定的Service（服务端）会接收信息并响应，甚至可以通过绑定服务进行执行进程间通信。
- 绑定服务的生命周期通常只在为其他应用组件(如Activity)服务时处于活动状态，不会无限期在后台运行，也就是说宿主(如Activity)解除绑定后，绑定服务就会被销毁

该如何实现呢？实际上我们必须提供一个 IBinder接口的实现类，该类用以提供客户端用来与服务进行交互的编程接口，该接口可以通过三种方法定义接口：

## 三种方法

**扩展 Binder 类**

如果服务是<u>提供给自有应用专用</u>的，并且Service(服务端)与客户端相同的进程中运行（常见情况），则应通过扩展 Binder 类并从 onBind() 返回它的一个实例来创建接口。

客户端收到 Binder 后，可利用它直接访问 Binder 实现中以及Service 中可用的公共方法。

如果我们的服务只是自有应用的后台工作线程，则优先采用这种方法。 不采用该方式创建接口的唯一原因是，服务被其他应用或不同的进程调用。

**使用 Messenger**

Messenger可以翻译为信使，通过它可以在<u>不同的进程</u>中共传递Message对象(Handler中的Messager，因此 Handler 是 Messenger 的基础)，在Message中可以存放我们需要传递的数据，然后在进程间传递。

如果需要让接口跨不同的进程工作，则可使用 Messenger 为服务创建接口，客户端就可利用 Message 对象向服务发送命令。

同时客户端也可定义自有 Messenger，以便服务回传消息。这是执行进程间通信 (IPC) 的最简单方法，因为 Messenger 会在单一线程中创建包含所有请求的队列，也就是说Messenger是<u>以串行的方式处理客户端发来的消息</u>，这样我们就不必对服务进行线程安全设计了。

**使用 AIDL**

由于Messenger是以串行的方式处理客户端发来的消息，如果当前有<u>大量消息</u>同时发送到Service(服务端)，Service仍然只能一个个处理，这也就是Messenger跨进程通信的缺点了，因此如果有大量并发请求，Messenger就会显得力不从心了，这时AIDL（Android 接口定义语言）就派上用场了， 但实际上<u>Messenger 的跨进程方式其底层实现 就是AIDL</u>，只不过android系统帮我们封装成透明的Messenger罢了 。因此，如果我们想让服务同时处理多个请求，则应该使用 AIDL。 在此情况下，<u>服务必须具备多线程处理能力，并采用线程安全式设计</u>。使用AIDL必须创建一个定义编程接口的 .aidl 文件。Android SDK 工具利用该文件生成一个实现接口并处理 IPC 的抽象类，随后可在服务内对其进行扩展。

## 扩展 Binder 类

开发步骤：

1. 创建服务端，继承自Service并在类中，创建一个实现IBinder 接口的实例对象并提供公共方法给客户端调用。

2. 从 onBind() 回调方法返回此 Binder 实例。

3. 在客户端中，从 onServiceConnected() 回调方法接收 Binder，并使用提供的方法调用绑定服务。

注意：此方式只有在客户端和服务位于<u>同一应用和进程内</u>才有效，如对于需要将 Activity 绑定到在后台播放音乐的自有服务的音乐应用，此方式非常有效。另一点之所以要求服务和客户端必须在同一应用内，是为了便于客户端转换返回的对象和正确调用其 API。服务和客户端还必须在同一进程内，因为此方式不执行任何跨进程编组。
以下是一个扩展 Binder 类的实例，先看看Service端的实现BindService.java

```java
package com.zejian.ipctest.service;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.util.Log;

/**
 * Created by zejian
 * Time 2016/10/2.
 * Description:绑定服务简单实例--服务端
 */
public class LocalService extends Service{
    private final static String TAG = "wzj";
    private int count;
    private boolean quit;
    private Thread thread;
    private LocalBinder binder = new LocalBinder();

    /**
     * 创建Binder对象，返回给客户端即Activity使用，提供数据交换的接口
     */
    public class LocalBinder extends Binder {
        // 声明一个方法，getService。（提供给客户端调用）
        LocalService getService() {
            // 返回当前对象LocalService,这样我们就可在客户端端调用Service的公共方法了
            return LocalService.this;
        }
    }

    /**
     * 把Binder类返回给客户端
     */
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return binder;
    }


    @Override
    public void onCreate() {
        super.onCreate();
        Log.i(TAG, "Service is invoke Created");
        thread = new Thread(new Runnable() {
            @Override
            public void run() {
                // 每间隔一秒count加1 ，直到quit为true。
                while (!quit) {
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    count++;
                }
            }
        });
        thread.start();
    }

    /**
     * 公共方法
     * @return
     */
    public int getCount(){
        return count;
    }
    /**
     * 解除绑定时调用
     * @return
     */
     @Override
    public boolean onUnbind(Intent intent) {
        Log.i(TAG, "Service is invoke onUnbind");
        return super.onUnbind(intent);
    }

    @Override
    public void onDestroy() {
        Log.i(TAG, "Service is invoke Destroyed");
        this.quit = true;
        super.onDestroy();
    }
}
```

LocalService类继承自Service，在该类中创建了一个LocalBinder继承自Binder类，LocalBinder中声明了一个getService方法，客户端可访问该方法获取LocalService对象的实例，只要客户端获取到LocalService对象的实例就可调用LocalService服务端的公共方法，如getCount方法，值得注意的是，我们在onBind方法中返回了binder对象，该对象便是LocalBinder的具体实例，而binder对象最终会返回给客户端，客户端通过返回的binder对象便可以与服务端实现交互。接着看看客户端BindActivity的实现：

```java
package com.zejian.ipctest.service;

import android.app.Activity;
import android.app.Service;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.zejian.ipctest.R;

/**
 * Created by zejian
 * Time 2016/10/2.
 * Description:绑定服务实例--客户端
 */
public class BindActivity extends Activity {
    protected static final String TAG = "wzj";
    Button btnBind;
    Button btnUnBind;
    Button btnGetDatas;
    /**
     * ServiceConnection代表与服务的连接，它只有两个方法，
     * onServiceConnected和onServiceDisconnected，
     * 前者是在操作者在连接一个服务成功时被调用，而后者是在服务崩溃或被杀死导致的连接中断时被调用
     */
    private ServiceConnection conn;
    private LocalService mService;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bind);
        btnBind = (Button) findViewById(R.id.BindService);
        btnUnBind = (Button) findViewById(R.id.unBindService);
        btnGetDatas = (Button) findViewById(R.id.getServiceDatas);
        //创建绑定对象
        final Intent intent = new Intent(this, LocalService.class);

        // 开启绑定
        btnBind.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "绑定调用：bindService");
                //调用绑定方法
                bindService(intent, conn, Service.BIND_AUTO_CREATE);
            }
        });
        // 解除绑定
        btnUnBind.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "解除绑定调用：unbindService");
                // 解除绑定
                if(mService!=null) {
                    mService = null;
                    unbindService(conn);
                }
            }
        });

        // 获取数据
        btnGetDatas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (mService != null) {
                    // 通过绑定服务传递的Binder对象，获取Service暴露出来的数据

                    Log.d(TAG, "从服务端获取数据：" + mService.getCount());
                } else {

                    Log.d(TAG, "还没绑定呢，先绑定,无法从服务端获取数据");
                }
            }
        });


        conn = new ServiceConnection() {
            /**
             * 与服务器端交互的接口方法 绑定服务的时候被回调，在这个方法获取绑定Service传递过来的IBinder对象，
             * 通过这个IBinder对象，实现宿主和Service的交互。
             */
            @Override
            public void onServiceConnected(ComponentName name, IBinder service) {
                Log.d(TAG, "绑定成功调用：onServiceConnected");
                // 获取Binder
                LocalService.LocalBinder binder = (LocalService.LocalBinder) service;
                mService = binder.getService();
            }
            /**
             * 当取消绑定的时候被回调。但正常情况下是不被调用的，它的调用时机是当Service服务被意外销毁时，
             * 例如内存的资源不足时这个方法才被自动调用。
             */
            @Override
            public void onServiceDisconnected(ComponentName name) {
                mService=null;
            }
        };
    }
}
```

在客户端中我们创建了一个ServiceConnection对象，该代表与服务的连接，它只有两个方法， onServiceConnected和onServiceDisconnected，其含义如下：

**onServiceConnected(ComponentName name, IBinder service)**

系统会调用该方法以传递服务的　onBind() 方法返回的 IBinder。其中service便是服务端返回的IBinder实现类对象，通过该对象我们便可以调用获取LocalService实例对象，进而调用服务端的公共方法。而ComponentName是一个封装了组件(Activity, Service, BroadcastReceiver, or ContentProvider信息的类，如包名，组件描述等信息，较少使用该参数。

**onServiceDisconnected(ComponentName name)**

Android 系统会在与服务的连接意外中断时（例如当服务崩溃或被终止时）调用该方法。注意:<u>当客户端取消绑定时，系统“绝对不会”调用该方法</u>。

```java
conn = new ServiceConnection() {
            @Override
            public void onServiceConnected(ComponentName name, IBinder service) {
                Log.d(TAG, "绑定成功调用：onServiceConnected");
                // 获取Binder
                LocalService.LocalBinder binder = (LocalService.LocalBinder) service;
                mService = binder.getService();
            }

            @Override
            public void onServiceDisconnected(ComponentName name) {
                mService=null;
            }
        };
```

在onServiceConnected()被回调前，我们还需先把当前Activity绑定到服务LocalService上，绑定服务是通过通过bindService()方法，解绑服务则使用unbindService()方法，这两个方法解析如下：

**bindService(Intent service, ServiceConnection conn, int flags)**

该方法执行绑定服务操作，其中Intent是我们要绑定的服务(也就是LocalService)的意图，而ServiceConnection代表与服务的连接，它只有两个方法，前面已分析过，flags则是指定绑定时是否自动创建Service。0代表不自动创建、BIND_AUTO_CREATE则代表自动创建。

**unbindService(ServiceConnection conn)**

该方法执行解除绑定的操作，其中ServiceConnection代表与服务的连接，它只有两个方法，前面已分析过。

Activity通过bindService()绑定到LocalService后，ServiceConnection#onServiceConnected()便会被回调并可以获取到LocalService实例对象mService，之后我们就可以调用LocalService服务端的公共方法了，最后还需要在清单文件中声明该Service。而客户端布局文件实现如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent">

    <Button
        android:id="@+id/BindService"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="绑定服务器"/>

    <Button
        android:id="@+id/unBindService"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="解除绑定"/>

    <Button
        android:id="@+id/getServiceDatas"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="获取服务方数据"/>
    
</LinearLayout>
```

我们运行程序，点击绑定服务并多次点击绑定服务接着多次调用LocalService中的getCount()获取数据，最后调用解除绑定的方法移除服务，其结果如下：

![这里写图片描述](Service-绑定方法_imgs\20161003123125076.png)

通过Log可知，当我们第一次点击绑定服务时，LocalService服务端的onCreate()、onBind方法会依次被调用，此时客户端的ServiceConnection#onServiceConnected()被调用并返回LocalBinder对象，接着调用LocalBinder#getService方法返回LocalService实例对象，此时客户端便持有了LocalService的实例对象，也就可以任意调用LocalService类中的声明公共方法了。

更值得注意的是，我们多次调用bindService方法绑定LocalService服务端，而LocalService得onBind方法只调用了一次，那就是在第一次调用bindService时才会回调onBind方法。接着我们点击获取服务端的数据，从Log中看出我们点击了3次通过getCount()获取了服务端的3个不同数据，最后点击解除绑定，此时LocalService的onUnBind、onDestroy方法依次被回调，并且多次绑定只需一次解绑即可。此情景也就说明了绑定状态下的Service生命周期方法的调用依次为<u>onCreate()、onBind()、onUnBind()、onDestroy()</u>。

## 使用Messenger

前面了解了如何使用IBinder应用内同一进程的通信后，我们接着来了解服务与远程进程（即不同进程间）通信，而不同进程间的通信，最简单的方式就是使用 Messenger 服务提供通信接口，利用此方式，我们无需使用 AIDL 便可执行进程间通信 (IPC)。以下是 Messenger 使用的主要步骤：

1. 服务实现一个 Handler，由其接收来自客户端的每个调用的回调

2. Handler 用于创建 Messenger 对象（对 Handler 的引用）

3. Messenger 创建一个 IBinder，服务通过 onBind() 使其返回客户端

4. 客户端使用 IBinder 将 Messenger（引用服务的 Handler）实例化，然后使用Messenger将 Message 对象发送给服务

5. 服务在其 Handler 中（在 handleMessage() 方法中）接收每个 Message

以下是一个使用 Messenger 接口的简单服务示例，服务端进程实现如下：

```java
package com.zejian.ipctest.messenger;

import android.app.Service;
import android.content.Intent;
import android.os.Handler;
import android.os.IBinder;
import android.os.Message;
import android.os.Messenger;
import android.util.Log;

/**
 * Created by zejian
 * Time 2016/10/3.
 * Description:Messenger服务端简单实例,服务端进程
 */
public class MessengerService extends Service {

    /** Command to the service to display a message */
    static final int MSG_SAY_HELLO = 1;
    private static final String TAG ="wzj" ;

    /**
     * 用于接收从客户端传递过来的数据
     */
    class IncomingHandler extends Handler {
        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                case MSG_SAY_HELLO:
                    Log.i(TAG, "thanks,Service had receiver message from client!");
                    break;
                default:
                    super.handleMessage(msg);
            }
        }
    }

    /**
     * 创建Messenger并传入Handler实例对象
     */
    final Messenger mMessenger = new Messenger(new IncomingHandler());

    /**
     * 当绑定Service时,该方法被调用,将通过mMessenger返回一个实现
     * IBinder接口的实例对象
     */
    @Override
    public IBinder onBind(Intent intent) {
        Log.i(TAG, "Service is invoke onBind");
        return mMessenger.getBinder();
    }
}
```

首先我们同样需要创建一个服务类MessengerService继承自Service，同时创建一个继承自Handler的IncomingHandler对象来接收客户端进程发送过来的消息并通过其handleMessage(Message msg)进行消息处理。接着通过IncomingHandler对象创建一个Messenger对象，该对象是与客户端交互的特殊对象，然后在Service的onBind中返回这个Messenger对象的底层Binder即可。下面看看客户端进程的实现：

```java
package com.zejian.ipctest.messenger;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.Message;
import android.os.Messenger;
import android.os.RemoteException;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.zejian.ipctest.R;

/**
 * Created by zejian
 * Time 2016/10/3.
 * Description: 与服务器交互的客户端
 */
public class ActivityMessenger extends Activity {
    /**
     * 与服务端交互的Messenger
     */
    Messenger mService = null;

    /** Flag indicating whether we have called bind on the service. */
    boolean mBound;

    /**
     * 实现与服务端链接的对象
     */
    private ServiceConnection mConnection = new ServiceConnection() {
        public void onServiceConnected(ComponentName className, IBinder service) {
            /**
             * 通过服务端传递的IBinder对象,创建相应的Messenger
             * 通过该Messenger对象与服务端进行交互
             */
            mService = new Messenger(service);
            mBound = true;
        }

        public void onServiceDisconnected(ComponentName className) {
            // This is called when the connection with the service has been
            // unexpectedly disconnected -- that is, its process crashed.
            mService = null;
            mBound = false;
        }
    };

    public void sayHello(View v) {
        if (!mBound) return;
        // 创建与服务交互的消息实体Message
        Message msg = Message.obtain(null, MessengerService.MSG_SAY_HELLO, 0, 0);
        try {
            //发送消息
            mService.send(msg);
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_messenager);
        Button bindService= (Button) findViewById(R.id.bindService);
        Button unbindService= (Button) findViewById(R.id.unbindService);
        Button sendMsg= (Button) findViewById(R.id.sendMsgToService);

        bindService.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("zj","onClick-->bindService");
                //当前Activity绑定服务端
                bindService(new Intent(ActivityMessenger.this, MessengerService.class), mConnection,
                        Context.BIND_AUTO_CREATE);
            }
        });

        //发送消息给服务端
        sendMsg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sayHello(v);
            }
        });


        unbindService.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Unbind from the service
                if (mBound) {
                    Log.d("zj","onClick-->unbindService");
                    unbindService(mConnection);
                    mBound = false;
                }
            }
        });
    }
}
```

在客户端进程中，我们需要创建一个ServiceConnection对象，该对象代表与服务端的链接，当调用bindService方法将当前Activity绑定到MessengerService时，onServiceConnected方法被调用，利用服务端传递给来的底层Binder对象构造出与服务端交互的Messenger对象，接着创建与服务交互的消息实体Message，将要发生的信息封装在Message中并通过Messenger实例对象发送给服务端。关于ServiceConnection、bindService方法、unbindService方法，前面已分析过，这里就不重复了，最后我们需要在清单文件声明Service和Activity，由于要测试不同进程的交互，则需要<u>将Service放在单独的进程中</u>，因此Service声明如下：

```xml
<service android:name=".messenger.MessengerService"
         android:process=":remote"/>
```

接着多次点击绑定服务，然后发送信息给服务端，最后解除绑定，Log打印如下：

![这里写图片描述](Service-绑定方法_imgs\20161003162626563.png)

通过上述例子可知Service服务端确实收到了客户端发送的信息，而且在Messenger中进行数据传递必须将数据封装到Message中，因为Message和Messenger都实现了Parcelable接口，可以轻松跨进程传递数据，而Message可以传递的信息载体有，what,arg1,arg2,Bundle以及replyTo，至于object字段，对于同一进程中的数据传递确实很实用，但对于进程间的通信，则显得相当尴尬，在android2.2前，object不支持跨进程传输，但即便是android2.2之后也只能传递android系统提供的实现了Parcelable接口的对象，也就是说我们通过自定义实现Parcelable接口的对象无法通过object字段来传递，因此object字段的实用性在跨进程中也变得相当低了。不过所幸我们还有Bundle对象，Bundle可以支持大量的数据类型。接着从Log我们也看出无论是使用拓展Binder类的实现方式还是使用Messenger的实现方式，它们的生命周期方法的调用顺序基本是一样的，即onCreate()、onBind、onUnBind、onDestroy，而且多次绑定中也只有第一次时才调用onBind()。

简单服务端与客户端双向消息传递的简单例子：

先来看看服务端的修改，在服务端，我们只需修改IncomingHandler，收到消息后，给客户端回复一条信息。

```java
  /**
     * 用于接收从客户端传递过来的数据
     */
    class IncomingHandler extends Handler {
        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                case MSG_SAY_HELLO:
                    Log.i(TAG, "thanks,Service had receiver message from client!");
                    //回复客户端信息,该对象由客户端传递过来
                    Messenger client=msg.replyTo;
                    //获取回复信息的消息实体
                    Message replyMsg=Message.obtain(null,MessengerService.MSG_SAY_HELLO);
                    Bundle bundle=new Bundle();
                    bundle.putString("reply","ok~,I had receiver message from you! ");
                    replyMsg.setData(bundle);
                    //向客户端发送消息
                    try {
                        client.send(replyMsg);
                    } catch (RemoteException e) {
                        e.printStackTrace();
                    }

                    break;
                default:
                    super.handleMessage(msg);
            }
        }
    }
```

接着修改客户端，为了接收服务端的回复，客户端也需要一个接收消息的Messenger和Handler，其实现如下：

```java
  /**
     * 用于接收服务器返回的信息
     */
    private Messenger mRecevierReplyMsg= new Messenger(new ReceiverReplyMsgHandler());

    private static class ReceiverReplyMsgHandler extends Handler{
        private static final String TAG = "zj";

        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                //接收服务端回复
                case MessengerService.MSG_SAY_HELLO:
                    Log.i(TAG, "receiver message from service:"+msg.getData().getString("reply"));
                    break;
                default:
                    super.handleMessage(msg);
            }
        }
    }
```

除了添加以上代码，还需要在发送信息时把接收服务器端的回复的Messenger通过Message的replyTo参数传递给服务端，以便作为同学桥梁，代码如下：

```java
 public void sayHello(View v) {
        if (!mBound) return;
        // 创建与服务交互的消息实体Message
        Message msg = Message.obtain(null, MessengerService.MSG_SAY_HELLO, 0, 0);
        // 把接收服务器端的回复的Messenger通过Message的replyTo参数传递给服务端
        msg.replyTo = mRecevierReplyMsg;
        try {
            //发送消息
            mService.send(msg);
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }
```

![这里写图片描述](Service-绑定方法_imgs\20161003173153947.png)

原理图：

![这里写图片描述](Service-绑定方法_imgs\20161004221152656.png)

## 使用AIDL

Code&Step：https://blog.csdn.net/weixin_37749732/article/details/124271111

要点：

1. Server中创建并使用AIDL：

   1.创建AIDL文件

   ![image-20220524160206554](Service-绑定方法_imgs\image-20220524160206554.png)

   2.自动生成对应的Java文件

   ![image-20220524161459959](Service-绑定方法_imgs\image-20220524161459959.png)

   ![image-20220524210518733](Service-绑定方法_imgs\image-20220524210518733.png)

2. Server中创建一个继承自IAidl.Stub的类，并于onBind()时return

```
public class MyRemoteService extends Service {
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        Log.e("MyRemoteSerivce", "onBind ");
        return new StudentService();
    }

    private class StudentService extends IStudentService.Stub {
        @Override
        public Student getStudentById(int id) throws RemoteException {
            Log.e("MyRemoteSerivce", "getStudentById:" + id);
            return new Student(id, "wang", 10000);
        }
    }
}
```

2. Client中的aidl文件放置层级应完全复制自Server

![在这里插入图片描述](Service-绑定方法_imgs\watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAN3p3YW5n,size_20,color_FFFFFF,t_70,g_se,x_16.png)

3. 绑定到Service时应使用IAidl.Stub.asInterface(iBinder)得到Server的Binder

```
conn = new ServiceConnection() {
            	//下面这个方法是bind绑定成功后的回调方法，在server服务端的 onBind返回的studentService
            	//可以在这里通过iBinder进行获取
                @Override
                public void onServiceConnected(ComponentName componentName, IBinder iBinder) {
                    Log.e(TAG, "onServiceConnected: ");
                    studentService = IStudentService.Stub.asInterface(iBinder);
                }

                @Override
                public void onServiceDisconnected(ComponentName componentName) {

                }
            };
```



## 关于绑定服务的注意点

1. 多个客户端可同时连接到一个服务。不过，只有在<u>第一个客户端绑定时，系统才会调用服务的 onBind() 方法来检索 IBinder</u>。<u>系统随后无需再次调用 onBind()，便可将同一 IBinder 传递至任何其他绑定的客户端</u>。当最后一个客户端取消与服务的绑定时，系统会将服务销毁（除非 startService() 也启动了该服务）。

2. 通常情况下我们应该在客户端生命周期（如Activity的生命周期）的引入 (bring-up) 和退出 (tear-down) 时刻设置绑定和取消绑定操作，以便控制绑定状态下的Service，一般有以下两种情况：
   - 如果只需要在 Activity 可见时与服务交互，则应在 onStart() 期间绑定，在 onStop() 期间取消绑定。
   - 如果希望 Activity 在后台停止运行状态下仍可接收响应，则可在 onCreate() 期间绑定，在 onDestroy() 期间取消绑定。需要注意的是，这意味着 Activity 在其整个运行过程中（甚至包括后台运行期间）都需要使用服务，因此如果服务位于其他进程内，那么当提高该进程的权重时，系统很可能会终止服务进程。

3. 通常情况下(注意)，<u>切勿在 Activity 的 onResume() 和 onPause() 期间绑定和取消绑定</u>，因为每一次生命周期转换都会发生这些回调，这样反复绑定与解绑是不合理的。此外，如果应用内的多个 Activity 绑定到同一服务，并且其中两个 Activity 之间发生了转换，则如果当前 Activity 在下一次绑定（恢复期间）之前取消绑定（暂停期间），系统可能会销毁服务并重建服务，因此服务的绑定不应该发生在 Activity 的 onResume() 和 onPause()中。
4. 我们应该始终<u>捕获 DeadObjectException DeadObjectException 异常</u>，该异常是在连接中断时引发的，表示调用的对象已死亡，也就是Service对象已销毁，这是远程方法引发的唯一异常，DeadObjectException继承自RemoteException，因此我们也可以捕获RemoteException异常。
   - 如何始终捕获某一异常？
5. 应用组件（客户端）可通过调用 bindService() 绑定到服务,Android 系统随后调用服务的 onBind() 方法，该方法返回用于与服务交互的 IBinder，<u>而该绑定是异步执行的</u>。