# JobService

JobService是Android L时候官方加入的组件。适用于需要特定条件下才执行后台任务的场景。 由系统统一管理和调度，在特定场景下使用JobService更加灵活和省心，相当于是Service的加强或者优化。

**JobService 与Service的对比**

| 对比角度   | Service                                                      | JobService                                                   | 补充                                                         |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 实现原理   | 由APP侧发出请求，ActivityManagerService接收请求后进行调度，通知APP侧进行创建，开始(绑定)，停止(解绑)和销毁Service。 | 由APP侧发出请求，JobSchedulerService接收请求后，通过ActivityManagerService去调度JobService的创建，绑定和解绑。并由JobSchedulerService自己进行JobService的开始，取消和停止等操作。 | 从原理上看，JobService的开始，取消和停止是由JobSchedulerService维护的，而不是由ActivityManagerService维护的。这是他们在实现原理上的明显区别。即JobService是由系统负责调用和维护 |
| 启动条件   | Service的启动并没有什么特定的条件设置。如果说非要有什么具体的执行条件的话，就是APP侧自己根据业务逻辑在适当的时候调用startService()或者bindService()。 | JobService的执行需要至少一个条件。没有条件的JobService是无法启动的，在创建JobInfo的时候会抛出异常。 |                                                              |
| 运行时间   | onStartCommand()的回调在UI线程，不可执行耗时逻辑，否则可能造成ANR。 | onStartJob()的回调在UI线程，不可执行耗时逻辑，否则可能造成ANR或者Job被强制销毁(超过8s)。并且，JobService里即便新起了线程，处理的时间也不能超过10min，否则Job将被强制销毁。 |                                                              |
| 启动角度   | onStartCommand()里返回START_STICKY可以告诉AMS在被停止后自动启动。 | onStopJob()里返回true，即可在被强制停止后再度启动起来。      |                                                              |
| 扩展性     | APP侧可以通过Binder创建远程Service进行IPC。                  | JobService的绑定实际上是由JobSchedulerService自己去做的。绑定后产生的Binder用于和JobSchedulerService进行IPC，APP侧无法通过JobService扩展去实现别的IPC功能。 | Google本来的初衷也不是让JobService实现远程Service的功能。    |
| 实际应用上 | 适合需要常驻后台，立即执行，进行数据获取，功能维持的场景。比如 音乐播放，定位，邮件收发等。 | 适合不需要常驻后台，不需要立即执行，在某种条件下触发，执行简单任务的场景。比如 联系人信息变化后的快捷方式的更新，定期的更新电话程序的联系人信息，壁纸更改后去从壁纸提取颜色的后台任务。 |                                                              |

简单来讲，Service适合一些优先级较高，执行任务复杂耗时的任务。JobService适合轻量级的灵活的任务。

**JobService API**

| 方法名                                                     | 参数                                                         | 描述                                                         | 补充                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| onStartJob(JobParameters params)                           | params：包含用于配置/识别作业的参数，系统传递给我们的        | 定义：Job开始的时候的回调，实现实际的工作逻辑。执行该方法时需要返回一个Boolean值，True表示需要执行，返回True时，作业将保持活动状态，直到系统调用jobFinished或者直到该作业所需的条件不再满了 | 注意：如果返回false的话，系统会自动结束本job；只要Job工作正在执行，系统就会代表应用程序保留一个唤醒锁。 在调用此方法之前获取此唤醒锁，并且直到您调用jobFinished（JobParameters，boolean）或系统调用onStopJob（JobParameters）以通知正在执行的作业它过早关闭之后才会释放。 |
| jobFinished(JobParameters params, boolean wantsReschedule) | wantsReschedule：若希望系统再次执行该Job，则设置为true后返回 | 调用此方法通知JobScheduler该作业已完成其工作。当系统收到此消息时，它会释放为该作业保留的唤醒锁。该操作在Job的任务执行完毕后，APP端自己的调用通知JobScheduler已经完成了任务。 | 注意:该方法执行完后不会回调onStopJob(),但是会回调onDestroy() |
| onStopJob(JobParameters params)                            | 同上                                                         | 定义：停止该Job。当JobScheduler发觉该Job条件不满足的时候，或者job被抢占被取消的时候的强制回调。即如果系统确定你必须在有机会调用jobFinished（JobParameters，boolean）之前必须停止执行作业，则调用此方法。 | 注意:如果想在这种意外的情况下让Job重新开始，返回值应该设置为true。 |
| onCreate()                                                 | 父类Service的基础方法，可以覆写来实现一些辅助作用。Service被初始化后的回调。 | 作用：可以在这里设置BroadcastReceiver或者ContentObserver     |                                                              |
| onDestroy()                                                | 定义：Service被销毁前的回调。                                | 作用：可以在这里注销BroadcastReceiver或者ContentObserver     |                                                              |

上面可以看出，JobService只是实际的执行和停止任务的回调入口。 那如何将这个入口告诉系统，就需要用到JobScheduler了。