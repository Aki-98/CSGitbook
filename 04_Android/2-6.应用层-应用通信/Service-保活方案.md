# 前台服务

## 前台服务的创建及通知

前台服务被认为是用户主动意识到的一种服务，因此在内存不足时，系统也不会考虑将其终止<u>。 前台服务必须为状态栏提供通知</u>，状态栏位于“正在进行”标题下方，这意味着除非服务停止或从前台删除，否则不能清除通知。例如将从服务播放音乐的音乐播放器设置为在前台运行，这是因为用户明确意识到其操作。 状态栏中的通知可能表示正在播放的歌曲，并允许用户启动 Activity 来与音乐播放器进行交互。

设置服务运行于前台的方法：

- startForeground(int id, Notification notification)

该方法的作用是把当前服务设置为前台服务，其中id参数代表唯一标识通知的整型数，需要注意的是提供给 startForeground() 的整型 ID <u>不得为 0</u>，而notification是一个状态栏的通知。

- stopForeground(boolean removeNotification)

该方法是用来从前台删除服务，此方法传入一个布尔值，<u>指示是否也删除状态栏通知，true为删除</u>。 注意该方法<u>并不会停止服务</u>。 但是，<u>如果在服务正在前台运行时将其停止，则通知也会被删除</u>。

下面我们结合一个简单案例来使用以上两个方法，ForegroundService代码如下：

```java
package com.zejian.ipctest.foregroundService;

import android.app.Notification;
import android.app.Service;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.support.v4.app.NotificationCompat;

import com.zejian.ipctest.R;

/**
 * Created by zejian
 * Time 2016/10/4.
 * Description:启动前台服务Demo
 */
public class ForegroundService extends Service {

    /**
     * id不可设置为0,否则不能设置为前台service
     */
    private static final int NOTIFICATION_DOWNLOAD_PROGRESS_ID = 0x0001;

    private boolean isRemove=false;//是否需要移除

    /**
     * Notification
     */
    public void createNotification(){
        //使用兼容版本
        NotificationCompat.Builder builder=new NotificationCompat.Builder(this);
        //设置状态栏的通知图标
        builder.setSmallIcon(R.mipmap.ic_launcher);
        //设置通知栏横条的图标
        builder.setLargeIcon(BitmapFactory.decodeResource(getResources(),R.drawable.screenflash_logo));
        //禁止用户点击删除按钮删除
        builder.setAutoCancel(false);
        //禁止滑动删除
        builder.setOngoing(true);
        //右上角的时间显示
        builder.setShowWhen(true);
        //设置通知栏的标题内容
        builder.setContentTitle("I am Foreground Service!!!");
        //创建通知
        Notification notification = builder.build();
        //设置为前台服务
        startForeground(NOTIFICATION_DOWNLOAD_PROGRESS_ID,notification);
    }


    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        int i=intent.getExtras().getInt("cmd");
        if(i==0){
            if(!isRemove) {
                createNotification();
            }
            isRemove=true;
        }else {
            //移除前台服务
            if (isRemove) {
                stopForeground(true);
            }
            isRemove=false;
        }

        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onDestroy() {
        //移除前台服务
        if (isRemove) {
            stopForeground(true);
        }
        isRemove=false;
        super.onDestroy();
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
```

在ForegroundService类中，创建了一个notification的通知，并通过启动Service时传递过来的参数判断是启动前台服务还是关闭前台服务，最后在onDestroy方法被调用时，也应该移除前台服务。以下是ForegroundActivity的实现：

```java
package com.zejian.ipctest.foregroundService;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.zejian.ipctest.R;

/**
 * Created by zejian
 * Time 2016/10/4.
 * Description:
 */
public class ForegroundActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_foreground);
        Button btnStart= (Button) findViewById(R.id.startForeground);
        Button btnStop= (Button) findViewById(R.id.stopForeground);
        final Intent intent = new Intent(this,ForegroundService.class);


        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                intent.putExtra("cmd",0);//0,开启前台服务,1,关闭前台服务
                startService(intent);
            }
        });


        btnStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                intent.putExtra("cmd",1);//0,开启前台服务,1,关闭前台服务
                startService(intent);
            }
        });
    }
}
```

## Service保活

### 【情况1】因内存资源不足而杀死Service

这种情况比较容易处理，可将onStartCommand() 方法的返回值设为 START_STICKY或START_REDELIVER_INTENT ，该值表示服务在内存资源紧张时被杀死后，在内存资源足够时再恢复。也可将Service设置为前台服务，这样就有比较高的优先级，在内存资源紧张时也不会被杀掉。这两点的实现，我们在前面已分析过和实现过这里就不重复。简单代码如下：

```java
/**
     * 返回 START_STICKY或START_REDELIVER_INTENT
     * @param intent
     * @param flags
     * @param startId
     * @return
     */
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
//        return super.onStartCommand(intent, flags, startId);
        return START_STICKY;
    }
```

### 【情况2】用户通过 settings -> Apps -> Running -> Stop 方式杀死Service

这种情况是用户手动干预的，不过幸运的是这个过程会执行Service的生命周期，也就是onDestory方法会被调用，这时便可以在 onDestory() 中发送广播重新启动。这样杀死服务后会立即启动。这种方案是行得通的，但为程序更健全，我们可开启两个服务，相互监听，相互启动。服务A监听B的广播来启动B，服务B监听A的广播来启动A。这里给出第一种方式的代码实现如下：

```java
package com.zejian.ipctest.neverKilledService;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.IBinder;
import android.support.annotation.Nullable;

/**
 * Created by zejian
 * Time 2016/10/4.
 * Description:用户通过 settings -> Apps -> Running -> Stop 方式杀死Service
 */
public class ServiceKilledByAppStop extends Service{

    private BroadcastReceiver mReceiver;
    private IntentFilter mIF;

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        mReceiver = new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                Intent a = new Intent(ServiceKilledByAppStop.this, ServiceKilledByAppStop.class);
                startService(a);
            }
        };
        mIF = new IntentFilter();
        //自定义action
        mIF.addAction("com.restart.service");
        //注册广播接者
        registerReceiver(mReceiver, mIF);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();

        Intent intent = new Intent();
        intent.setAction("com.restart.service");
        //发送广播
        sendBroadcast(intent);

        unregisterReceiver(mReceiver);
    }
}
```

### 【情况3】用户通过 settings -> Apps -> Downloaded -> Force Stop 方式强制性杀死Service

这种方式就比较悲剧了，因为是直接kill运行程序的，不会走生命周期的过程,前面两种情况只要是执行Force Stop ，也就废了。也就是说这种情况下无法让服务重启，或者只能去设置Force Stop 无法操作了，不过也就没必要了，太流氓了。。。。
