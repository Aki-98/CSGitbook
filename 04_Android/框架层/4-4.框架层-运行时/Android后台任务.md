

**指导原则**：一般来说，运行时间<u>超过几毫秒</u>的所有任务都应委派给台线程。长时间运行的常见任务包括解码位图、访问存储空间、处理机器学习 (ML) 模型、执行网络请求等。

**后台任务的类别**：

- 即时任务：是否需要在用户与应用进行互动时完成？
- 精确任务：是否需要在精确的时间点运行？
- 延期任务：以上两者都不是，那么定义为延期任务

**解决方案**：

- **即时任务**
  - [Kotlin 协程](https://developer.android.com/kotlin/coroutines?hl=zh-cn)。许多 [Android KTX](https://developer.android.com/kotlin/ktx?hl=zh-cn) 库都包含适用于常见应用组件（如 [`ViewModel`](https://developer.android.com/topic/libraries/architecture/coroutines?hl=zh-cn#viewmodelscope)）和常见应用[生命周期](https://developer.android.com/topic/libraries/architecture/coroutines?hl=zh-cn#lifecyclescope)的现成可用的协程作用域。
  - 如果您是 Java 编程语言用户，请参阅 [Android 上的线程处理](https://developer.android.com/guide/background/threading?hl=zh-cn)。
  - 对于应立即执行并需要继续处理的任务，即使用户将应用放在后台运行或重启设备，我们也建议使用 [`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager?hl=zh-cn) 并利用其对[长时间运行的任务](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/long-running?hl=zh-cn)的支持。
  - 在特定情况下（例如使用媒体播放或主动导航功能时），您可能希望直接使用[前台服务](https://developer.android.com/guide/components/services?hl=zh-cn#Foreground)。

- **延期任务**：如果您希望某些可延期异步任务即使在应用退出或设备重启后仍能正常运行，使用 `WorkManager` 可以轻松地调度这些任务。

- **精确任务**：需要在精确时间点执行的任务可以使用 [`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager?hl=zh-cn)。