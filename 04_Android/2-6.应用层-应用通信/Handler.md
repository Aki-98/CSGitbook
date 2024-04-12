# Handler

**应用场景**

1. To schedule messages and runnables to be executed as some point in the future(实现定时任务)
2. To enqueue an action to be performed on a different thread than your own.(不同进程间通信)

**相关概念**

![c1113313-ae24-4f80-9dcc-73c9eabb35e5.jpg](Handler_imgs\c1113313-ae24-4f80-9dcc-73c9eabb35e5.jpg)

UI线程:就是我们的主线程,系统在创建UI线程的时候会初始化一个Looper对象,同时也会创建一个与其关联的MessageQueue;

Handler:作用就是发送与处理信息,如果希望Handler正常工作,在当前线程中要有一个Looper对象

Message:Handler接收与处理的消息对象

MessageQueue:消息队列,先进先出管理Message,在初始化Looper对象时会创建一个与之关联的MessageQueue;

Looper:每个线程只能够有一个Looper,管理MessageQueue,不断地从中取出Message分发给对应的Handler处理！

在使用android的消息的处理机制的时候：一般是有两种手段，

1. 该message自己绑定到目标handler后，自行进入messageQueue,等待handler接受处理。Message方法：public static Message obtain(Handler h, int what, int arg1, int arg2, Object obj) ,通过该方法可以获得一个消息：Message message = Message.obtain(handler, 33, 2, 3, "hello");发送消息的方式，有一点将自己绑定好了被发射的感觉，message.sendToTarget(); ---被动（意会）

2. handler主动设置要发送的消息的各个属性值：arg1，arg2，obj，what。方法：public final Message obtainMessage(int what, int arg1, int arg2, Object obj) 通过该方法也可以获得一个消息：比如Message message = handler.obtainMessage(3, 1, 2, "java");然后将设置好的消息，由handler发送出去：handler.sendMessage(message);----主动（自己意会的）。下面十几个常用方法：

**为什么handler中带有上下文会导致内存泄露**

handler接收到的消息可能是异步的,需要处理的时候上下文已经被销毁了,这种情况下会导致传入的上下文无法被垃圾回放器GC回收,所以会造成内存泄露。

所以~要实现静态的handler

**handler引入包**

## Thread，Looper和Handler的关系

与Windows系统一样，Android也是消息驱动型的系统。引用一下消息驱动机制的四要素：

接收消息的“消息队列”
阻塞式地从消息队列中接收消息并进行处理的“线程”
可发送的“消息的格式”
“消息发送函数”
与之对应，Android中的实现对应了

接收消息的“消息队列” ——【MessageQueue】
阻塞式地从消息队列中接收消息并进行处理的“线程” ——【Thread+Looper】
可发送的“消息的格式” ——【Message】
“消息发送函数”——【Handler的post和sendMessage】
一个Looper类似一个消息泵。它本身是一个死循环，不断地从MessageQueue中提取Message或者Runnable。而Handler可以看做是一个Looper的暴露接口，向外部暴露一些事件，并暴露sendMessage()和post()函数。

在安卓中，除了UI线程/主线程以外，普通的线程(先不提HandlerThread)是不自带Looper的。想要通过UI线程与子线程通信需要在子线程内自己实现一个Looper。开启Looper分三步走：

判定是否已有Looper并Looper.prepare()
做一些准备工作(如暴露handler等)
调用Looper.loop()，线程进入阻塞态
由于每一个线程内最多只可以有一个Looper，所以一定要在Looper.prepare()之前做好判定，否则会抛出java.lang.RuntimeException: Only one Looper may be created per thread。为了获取Looper的信息可以使用两个方法：

Looper.myLooper()
Looper.getMainLooper()
Looper.myLooper()获取当前线程绑定的Looper，如果没有返回null。Looper.getMainLooper()返回主线程的Looper,这样就可以方便的与主线程通信。注意：在Thread的构造函数中调用Looper.myLooper只会得到主线程的Looper，因为此时新线程还未构造好

下面给一段代码，通过Thread，Looper和Handler实现线程通信：

MainActivity.java

    public class MainActivity extends Activity {
        public static final String TAG = "Main Acticity";
        Button btn = null;
        Button btn2 = null;
        Handler handler = null;
        MyHandlerThread mHandlerThread = null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn = (Button)findViewById(R.id.button);
        btn2 = (Button)findViewById(R.id.button2);
        Log.d("MainActivity.myLooper()", Looper.myLooper().toString());
        Log.d("MainActivity.MainLooper", Looper.getMainLooper().toString());


        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mHandlerThread = new MyHandlerThread("onStartHandlerThread");
                Log.d(TAG, "创建myHandlerThread对象");
                mHandlerThread.start();
                Log.d(TAG, "start一个Thread");
            }
        });
    
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(mHandlerThread.mHandler != null){
                    Message msg = new Message();
                    msg.what = 1;
                    mHandlerThread.mHandler.sendMessage(msg);
                }
    
            }
        });
    }

}
MyHandlerThread.java
public class MyHandlerThread extends Thread {
    public static final String TAG = "MyHT";

    public Handler mHandler = null;
    
    @Override
    public void run() {
        Log.d(TAG, "进入Thread的run");
        Looper.prepare();
        Looper.prepare();
        mHandler = new Handler(Looper.myLooper()){
            @Override
            public void handleMessage(Message msg){
                Log.d(TAG, "获得了message");
                super.handleMessage(msg);
            }
        };
        Looper.loop();
    }}


# 