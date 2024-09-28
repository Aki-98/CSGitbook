

![这里写图片描述](Service-生命周期_imgs\20161004164521384.png)

![image-20220310093313926](Service-生命周期_imgs\image-20220310093313926.png)

## 1. 生命周期常用方法

在Service的生命周期里，常用的有：

- 4个手动调用的方法

| 手动调用方法    | 作用     |
| :-------------- | :------- |
| startService()  | 启动服务 |
| stopService()   | 关闭服务 |
| bindService()   | 绑定服务 |
| unbindService() | 解绑服务 |

- 5个内部自动调用的方法

| 内部自动调用的方法 | 作用     |
| :----------------- | :------- |
| onCreat()          | 创建服务 |
| onStartCommand()   | 开始服务 |
| onDestroy()        | 销毁服务 |
| onBind()           | 绑定服务 |
| onUnbind()         | 解绑服务 |

------

## 2. 生命周期方法具体介绍

  主要介绍内部调用方法和外部调用方法的关系。            

### 2.1 startService()

- 作用：启动Service服务
- 手动调用startService()后，自动调用内部方法：onCreate()、onStartCommand()
- 调用逻辑如下：  

![调用逻辑](Service-生命周期_imgs\1.png)

调用逻辑

### 2.2 stopService()

- 作用：关闭Service服务
- 手动调用stopService()后，自动调用内部方法：onDestory()
- 调用的逻辑：

![调用逻辑](Service-生命周期_imgs\2.png)

调用逻辑

### 2.3 bindService()

- 作用：绑定Service服务
- 手动调用bindService()后，自动调用内部方法：onCreate()、onBind()
- 调用的逻辑：

![调用的逻辑](Service-生命周期_imgs\3.png)

调用的逻辑

### 2.4 unbindService()

- 作用：解绑Service服务
- 手动调用unbindService()后，自动调用内部方法：onCreate()、onBind()、onDestory()
- 调用的逻辑：  

![调用的逻辑](Service-生命周期_imgs\4.png)

调用的逻辑

------

## 3. 常见的生命周期使用

#### 3.1 只使用startService启动服务的生命周期

![startService启动服务的生命周期](Service-生命周期_imgs\5.png)

startService启动服务的生命周期

#### 3.2 只使用BindService绑定服务的生命周期

![BindService绑定服务的生命周期](Service-生命周期_imgs\6.png)

BindService绑定服务的生命周期

#### 3.3 同时使用startService()启动服务、BindService()绑定服务的生命周期

![Paste_Image.png](Service-生命周期_imgs\7.png)

Paste_Image.png

## 4. 特别注意

### Service在系统中永远为单一实例

Android系统仅会为一个Service创建一个实例对象，所以不管是启动服务还是绑定服务，<u>操作的是同一个Service实例</u>

### 4.1 **startService() **

#### **服务可以在后台无限期运行**

当应用组件（如 `Activity` 或 `Fragment`）通过调用 `startService()` 启动一个服务时，该服务进入了“启动”状态。即：

- 这个服务将继续运行，即使启动它的 `Activity` 已经被销毁。这意味着服务和启动它的组件之间没有直接的生命周期联系。组件销毁不会影响服务的运行。

#### 必须显式停止

服务一旦通过 `startService()` 启动后，需要**显式地停止**。有两种方式可以停止服务：

- **调用 `stopService()`**：由启动服务的组件或其他组件调用 `stopService()` 停止服务。
- **调用 `stopSelf()`**：服务内部通过调用 `stopSelf()` 来决定自己停止。常用于任务完成后服务自动结束。

如果不手动调用这两个方法，服务会一直运行下去，占用系统资源。

#### 通常执行单一操作，不返回结果

通过 `startService()` 启动的服务往往被设计为**执行特定的任务**（如文件上传、下载、播放音乐），并且这些任务通常不需要返回结果给调用方。

- 例如，假设 `Activity` 启动了一个服务来下载文件，`Activity` 不会直接从服务中获取下载状态或结果。这种服务不会像 `bindService()` 那样通过客户端-服务端交互，来实时返回信息。

#### 无法调用Service的方法

- startService()和stopService()只能开启和关闭Service，无法操作Service



### 4.2 bindService()

#### 当不存在绑定方时，服务自动销毁

startService开启的Service，调用者退出后Service仍然存在；    BindService开启的Service，调用者退出后，Service随着调用者销毁。

#### **可以需要处理回调或通知**

- 当组件需要接收服务中的回调或通知时，通过 `bindService()` 绑定服务可以实现此功能。例如，服务可以通过 `Binder` 返回一个接口，客户端可以实现这个接口以接收回调。



## 5. 方法详解

### onStartCommand（Intent intent, int flags, int startId）

**intent** ：启动时，启动组件传递过来的Intent，如Activity可利用Intent封装所需要的参数并传递给Service

**flags**：表示启动请求时是否有额外数据，可选值有 0，START_FLAG_REDELIVERY，START_FLAG_RETRY，0代表没有：

- **START_FLAG_REDELIVERY**：这个值代表了onStartCommand方法的返回值为
  START_REDELIVER_INTENT，而且在上一次服务被杀死前会去调用stopSelf方法停止服务。其中START_REDELIVER_INTENT意味着<u>当Service因内存不足而被系统kill后，则会重建服务，并通过传递给服务的最后一个 Intent 调用 onStartCommand()</u>，此时Intent时有值的。
- **START_FLAG_RETRY**：该flag代表<u>当onStartCommand调用后一直没有返回值时，会尝试重新去调用onStartCommand()</u>。

**startId** ： 指明当前服务的唯一ID，与stopSelfResult (int startId)配合使用，stopSelfResult 可以更安全地根据ID停止服务。

**onStartCommand的返回值int类型**，有三种可选值， START_STICKY，START_NOT_STICKY，START_REDELIVER_INTENT，它们具体含义如下：

- **START_STICKY**：<u>当Service因内存不足而被系统kill后，一段时间后内存再次空闲时，系统将会尝试重新创建此Service，一旦创建成功后将回调onStartCommand方法，但其中的Intent将是null，除非有挂起的Intent，如pendingintent</u>，这个状态下比较适用于<u>不执行命令、但无限期运行</u>并等待作业的媒体播放器或类似服务。
- **START_NOT_STICKY**：当Service因内存不足而被系统kill后，即使系统内存再次空闲时，系统也不会尝试重新创建此Service。除非程序中再次调用startService启动此Service，这是最安全的选项，可以避免在不必要时以及应用能够轻松重启所有未完成的作业时运行服务。
- **START_REDELIVER_INTENT**：当Service因内存不足而被系统kill后，则会重建服务，并通过传递给服务的最后一个 Intent 调用 onStartCommand()，任何挂起 Intent均依次传递。与START_STICKY不同的是，<u>其中的传递的Intent将是非空，是最后一次调用startService中的intent</u>。这个值适用于主动执行<u>应该立即恢复</u>的作业（例如下载文件）的服务。

由于每次启动服务（调用startService）时，onStartCommand方法都会被调用，因此我们可以通过该方法使用Intent给Service传递所需要的参数，然后在onStartCommand方法中处理的事件，最后根据需求选择不同的Flag返回值，以达到对程序更友好的控制。
