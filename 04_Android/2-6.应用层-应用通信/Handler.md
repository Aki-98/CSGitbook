# Handler

## **应用场景**

1. To schedule messages and runnables to be executed as some point in the future(实现定时任务)
2. To enqueue an action to be performed on a different thread than your own.(不同进程间通信)

## **相关概念**

![c1113313-ae24-4f80-9dcc-73c9eabb35e5.jpg](Handler_imgs\c1113313-ae24-4f80-9dcc-73c9eabb35e5.jpg)

- **UI线程**:就是我们的主线程,系统在创建UI线程的时候会初始化一个Looper对象,同时也会创建一个与其关联的MessageQueue;
- **Handler**:作用就是发送与处理信息,如果希望Handler正常工作,在当前线程中要有一个Looper对象
- **Message**:Handler接收与处理的消息对象
- **MessageQueue**:消息队列,先进先出管理Message,在初始化Looper对象时会创建一个与之关联的MessageQueue;
- **Looper**:每个线程只能够有一个Looper,管理MessageQueue,不断地从中取出Message分发给对应的Handler处理！

## 创建和发送Message的方法

### 1. Message 自己绑定到目标 Handler 后发送 (被动)

这种方式强调的是 `Message` 自己“知道”它将由哪个 `Handler` 来处理，消息在创建时已经被绑定到特定的 `Handler` 上：

```
javaCopy codeMessage message = Message.obtain(handler, 33, 2, 3, "hello");
message.sendToTarget();
```

- **获取 `Message` 对象**：`Message.obtain(handler, 33, 2, 3, "hello")` 方法不仅初始化了 `Message` 的内容（`what`, `arg1`, `arg2`, `obj`），还将这个 `Message` 绑定到指定的 `Handler` 上。
- **发送消息**：调用 `message.sendToTarget()` 会将 `Message` 发送给绑定的 `Handler`，`Handler` 接着会将消息放入它的 `MessageQueue` 中等待处理。

在这种方式中，`Message` 创建时就已经“知道”要发送到哪个 `Handler`，可以看作是一种被动的行为，`Message` 被创建后再调用 `sendToTarget()`，就会自动发送给指定的 `Handler`。

### 2. Handler 主动创建并发送消息 (主动)

在这种方式中，`Handler` 主动地创建 `Message`，并在适当的时候发送它：

```
javaCopy codeMessage message = handler.obtainMessage(3, 1, 2, "java");
handler.sendMessage(message);
```

- **获取 `Message` 对象**：`handler.obtainMessage(3, 1, 2, "java")` 方法从 `Handler` 中获取一个新的 `Message` 对象，并设置它的内容（`what`, `arg1`, `arg2`, `obj`）。
- **发送消息**：`handler.sendMessage(message)` 方法将这个 `Message` 发送出去，由 `Handler` 自己将消息放入 `MessageQueue` 中。

在这种方式中，`Handler` 是“主动”的，`Handler` 自己创建 `Message`，并决定何时发送。

### 主动与被动的区别（意会）

- **被动**：`Message` 创建时已经决定好由哪个 `Handler` 来处理，只需调用 `sendToTarget()`，它会自动被发送给目标 `Handler`。`Message` 是被动的，因为它自己“知道”要去哪。
- **主动**：`Handler` 主动决定要创建并发送 `Message`，`Message` 本身并不知道它会被发送给哪个 `Handler`。`Handler` 是主动的，因为它控制着消息的整个生命周期。

### 常用方法

`Handler` 和 `Message` 提供了一些常用的方法来简化消息处理：

- **Handler 的常用方法**：
  - `obtainMessage(int what)`：获取一个 `what` 值的 `Message`。
  - `obtainMessage(int what, Object obj)`：获取一个 `what` 和 `obj` 值的 `Message`。
  - `obtainMessage(int what, int arg1, int arg2)`：获取一个 `what`, `arg1`, `arg2` 值的 `Message`。
  - `sendMessage(Message msg)`：发送一个 `Message`。
  - `sendEmptyMessage(int what)`：发送一个仅包含 `what` 值的 `Message`。
  - `post(Runnable r)`：将一个 `Runnable` 放入消息队列，`Handler` 处理时会执行此 `Runnable`。
- **Message 的常用方法**：
  - `obtain()`：获取一个空的 `Message`。
  - `obtain(Handler h)`：获取一个绑定了特定 `Handler` 的 `Message`。
  - `sendToTarget()`：将 `Message` 发送给已经绑定的 `Handler`。
  - `setTarget(Handler target)`：设置消息的目标 `Handler`。
  - `recycle()`：回收 `Message`，以便重复使用。

## Handler的使用

### 1.最好显式地声明使用的Looper

Handler handler = new Handler() -> 会默认用当前线程的looper

如果在代码中Handler的定位是用来刷新操作UI，需要在主线程中操作。

### 2.最好使用static的Handler

> 内存泄漏：当我们在使用完某个对象时，如果这个对象所占据的内存不及时的别释放，这就可能发生了内存越来越少的情况，最后可能就没了。
>
> 内存溢出：溢出就是太多了，很显然不是可用内存太多了，而是我们在执行某个操作的时候需要的内存，超过了应用的分配内存，这就是内存溢出。

Handler作为一个内部类被声明时，这个handler就会持有外部类的引用，如果在我们的handler关联的MessageQueue还有消息没有处理，或者有一个延时很长的消息，那么垃圾回收器就无法回收这个使用handler的Activity，就会导致内存泄漏问题。因为和Activity有关，换句话说，只有<u>在主线程中</u>才可能发生内存泄漏的情况

#### 解决方式1：声明称一个static 的内部类，持有外部类的weakReference，在内部类中使用外部类传递过来的weakReference的成员。

```java
public class MainActivity extends Activity {

    private TextView mTextView;
    private Handler mHandler;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mTextView = (TextView)findViewById(R.id.textview);
        mHandler = new MyHandler(this);

    }

    /**
    *测试方法
    */  
    public void executeTest(View v){
        mHandler.sendEmptyMessage(0x110);
    }

    static class MyHandler extends Handler{
        WeakReference<MainActivity> mActivity;
        public MyHandler(MainActivity activity) {
            mActivity = new WeakReference<MainActivity>(activity);
        }
        @Override
        public void handleMessage(Message msg) {
            MainActivity mainActivity = mActivity.get();
            if(msg.what==1){
                mainActivity.mTextView.setText("执行正确");
            }

        }

    }

}
```

#### 解决方式2：简单版

```java
    private Handler mHandler = new Handler(new Handler.Callback() {

        @Override
        public boolean handleMessage(Message msg) {
            // TODO Auto-generated method stub
            return false;
        }
    });
```

