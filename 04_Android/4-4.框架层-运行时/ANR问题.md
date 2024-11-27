## 触发ANR的条件

- 在 5 秒内对输入事件（例如按键或屏幕轻触事件）没有响应。
- `BroadcastReceiver` 在 10 秒内尚未执行完毕。

## 避免ANR的策略

1.使用AsyncTask

只需扩展 `AsyncTask` 并实现 `doInBackground()` 方法即可执行相应操作。如需向用户发布进度变化，您可以调用 `publishProgress()`，它会调用 `onProgressUpdate()` 回调方法。通过 `onProgressUpdate()`（在界面线程中运行）的实现，您可以向用户发送通知。

2.使用Thread或HandlerThread类

果是这样，您应该调用 `Process.setThreadPriority()` 并传递 `THREAD_PRIORITY_BACKGROUND`，从而将线程优先级设为“后台”优先。如果您不通过这种方式将线程设置为较低的优先级，则此线程仍可能会让应用变慢，因为默认情况下，此线程会按照与界面线程相同的优先级操作。

如果您实现了 `Thread` 或 `HandlerThread`，请确保在等待工作线程完成操作期间，界面线程不会阻塞；请勿调用 `Thread.wait()` 或 `Thread.sleep()`。非但不应在等待工作线程完成操作期间阻塞，主线程在完成操作时还应提供 `Handler` 以供其他线程向回发送。以这种方式设计应用，即可让应用的界面线程对输入保持响应，从而避免因 5 秒的输入事件超时而导致系统显示 ANR 对话框。

3.如果 `BroadcastReceiver` 接收到广播后要执行耗时操作，应该启动IntentService

对 `BroadcastReceiver` 执行时间的特定约束强调了广播接收器的功能：在后台执行少量离散工作，例如保存设置或注册 `Notification`。因此，与在界面线程中调用的其他方法一样，应用应避免在广播接收器中执行可能会长时间运行的操作或计算。但如果需要执行可能需要长时间运行的操作以响应 intent 广播，则应用应启动 `IntentService`，而不是通过工作线程执行密集型操作。

## 加强响应能力

通常，100 到 200 毫秒是一个阈值，一旦超出此阈值，用户便能够感受到应用速度缓慢。因此，除了采取措施以避免显示 ANR 之外，还有一些提示可以让用户感觉您的应用响应迅速：

- 如果应用在后台执行操作以响应用户输入，则显示正在进行该操作（例如在界面中使用 `ProgressBar`）。
- 特别是游戏，在工作线程中计算走法。
- 如果应用具有耗时较长的初始设置阶段，考虑显示启动画面或尽快呈现主视图，表明正在加载，并异步填充信息。在任何一种情况下，您都应以某种方式表明操作正在进行，以免用户认为应用已卡住。
- 使用 [Systrace](https://developer.android.com/tools/help/systrace?hl=zh-cn) 和 [Traceview](https://developer.android.com/tools/help/traceview?hl=zh-cn) 等性能工具确定应用响应能力方面的瓶颈。



# 什么是ANR，如何避免

ANR是指应用程序未响应，安卓系统对于一些事件需要在一定的时间范围内完成，如果超过预定时间仍未能得到有效响应或者响应时间过长，都会造成ANR。

出现的原因有三种：

（1）KeyDispatchTimeout（5 seconds）主要类型按键或触摸事件在特定时间内无响应

（2）BroadcastTimeout（10 seconds）BoradcastReceiver在特定的时间内无法处理

（3）ServiceTimeout（20 seconds）小概率类型Service在特定的时间内无法处理完成

3：避免ANR最核心的一点就是在主线程减少耗时操作。通常需要从那个以下几个方案下手：

（1）使用子线程处理耗时IO操作

（2）降低子线程优先级，使用Thread或者HandlerThread时，调用Process.setThreadPriority（Process.THREAD_PRIORITY_BACKGROUND）设置优先级，否则仍然会降低程序响应，因为默认Thread的优先级和主线程相同

（3）使用Handler处理子线程结果，而不是使用Thread.wait()或者Thread.sleep()来阻塞主线程

（4）Activity的onCreate和onResume回调中尽量避免耗时的代码

（5）BroadcastReceiver中onReceiver代码也要尽量减少耗时操作，建议使用intentService处理。intentService是一个异步的，会自动停止的服务，很好解决了传统的Service中处理完耗时操作忘记停止并销毁Service的问题