# Android架构

![img](Android架构_imgs\14.png)

## **LINUX KERNEL**

Linux core, the Android system is modified based on the Linux system. The bottom layer of Android is Linux, and most of them are some drivers for operating hardware, such as Display Driver, Audio Drivers, and so on.

## HAL(硬件抽象层)

提供标准界面，向更高级别的Java API框架显示设备硬件功能。 HAL包含多个库模块，其中每个模块都为特定类型的硬件组件实现一个界面，例如相机或蓝牙模块。当框架API要求访问设备硬件时，Android系统将为该硬件组件加载库模块。

## ANDROID RUNTIME

Core Libraries: core library. Dalvik Virtual Machine: Android bottom layer is a Linux system, written in C and C ++ language, so Android program (written in Java language) needs a virtual machine to run on Linux, that is, DVM.

对于运行Android5.0(API 21)或更高版本的设备，每个应用都在其自己的进程中运行，并且有其自己的AndroidRuntime（ART）实例。ART编写为通过执行DEX文件在低内存设备上运行多个虚拟机，DEX未见时一种专为Android设计的字节码格式，经过优化，使用的内存很少。编译工具链（例如Jack）将Java源代码编译为DEX字节码，使其可在Android平台上运行。

ART的部分主要功能包括：

- 预先（AOT）和即时（JIT）
- 编译优化的垃圾回收（GC）
- 在Android 9 （API 28）及更高版本的系统中，支持将应用软件包中的Dalvik Executable格式（DEX）文件转换为更紧凑的机器代码
- 在Android 5.0 （API 21）之前，Dalvik是AndroidRuntime。如果您的应用在ART上运行效果很少，那么它应该也可以在Dalvik上运行，但反过来不一定。

> Dalvik 是 Android 操作系统中用于执行应用程序的一个虚拟机（VM）。Dalvik 虚拟机是为了在资源受限的移动设备上运行效率更高的 Java 程序而设计的。
>
> 主要特点和作用包括：
>
> 1. **优化内存和性能：** Dalvik 虚拟机被设计为在移动设备上更高效地使用内存和处理器资源。它使用基于寄存器的指令集，与传统的 Java 虚拟机（如 Java SE 中的 JVM）不同。
> 2. **DEX 文件格式：** Android 应用程序的 Java 代码经过编译后会生成 Dalvik 可执行文件，通常以 .dex 扩展名结尾。这个文件格式是为了在 Dalvik VM 上执行而优化过的。
> 3. **运行在沙盒环境中：** Dalvik 虚拟机使得每个 Android 应用程序运行在其独立的进程中，并在沙盒环境中，这有助于提高系统的安全性和稳定性。
> 4. **支持多任务处理：** Android 设备通常需要同时运行多个应用程序。Dalvik 虚拟机能够有效地管理多个应用程序的同时运行，通过使用不同的进程和线程来实现。
> 5. **预编译和即时编译：** Dalvik 虚拟机支持预编译和即时编译技术，以提高应用程序的启动速度和运行效率。
>
> 需要注意的是，从 Android 5.0（Lollipop）版本开始，Android 引入了新的运行时环境，称为 ART（Android Runtime），取代了 Dalvik。ART 在性能和优化方面带来了更多的改进，包括提供了更快的应用启动速度和更低的内存占用。因此，Dalvik 在较新的 Android 版本中逐渐被淘汰。



## Native C/C++ Libraries

Some libraries written in C language to complete the core functions of Android, such as OpenGL | ES (Simplified Graphic Image Engine), WebKit (browser kernel), SQLite (lightweight database), Surface Manager ), Media Framework (Multimedia Framework), FreeType (font library), SGL (another graphics and image engine), SSL (TCP-based security protocol), libc (fragmented library).

可提供Java API框架所使用的Java编程语言中的大部分功能，包括一些Java8语言功能，

许多核心Android系统组件和服务（例如ART和HAL）构建自原生代码，需要以C和C++编写的原生库。Android平台提供Java框架API以向应用显示其中部分原生库的功能。例如，您也可以通过Android框架的Java OpenGL API访问 OpenGL ES，以支持在应用中绘制和操作2D和3D图形。

如果开发的是需要C或C++代码的应用，可以使用Android NDK直接从原生代码访问某型原生平台库。

> 什么情况下开发Android应用会需要C、C++代码？
>
> 在Android应用开发中，通常使用Java或Kotlin等高级编程语言来编写应用程序的逻辑和用户界面。然而，有些情况下，可能会需要使用C或C++等底层语言编写一部分代码。以下是一些情况下可能需要使用C、C++代码的情况：
>
> 1. **性能优化：** 如果你的应用对性能要求极高，特别是需要进行大量计算或处理大量数据的情况下，使用C或C++可以更好地控制底层资源，以提高执行效率。
> 2. **现有库或代码：** 如果你要使用已有的C/C++库或代码，可以通过JNI（Java Native Interface）来调用这些库。这是一种使用Java代码调用本地（C/C++）代码的机制，使得你可以在Android应用中使用现有的本地库。
> 3. **跨平台开发：** 如果你计划在多个平台上共享代码，尤其是在Android和iOS之间，可以考虑使用C++开发核心逻辑，然后在Android和iOS上通过相应的桥接层进行调用。
> 4. **硬件相关操作：** 有些应用可能需要直接访问设备硬件或执行底层操作，这时候使用C或C++可能更为合适。例如，游戏引擎通常会使用C++来实现性能关键的游戏逻辑。
> 5. **系统级开发：** 在一些特殊的应用场景，比如系统级应用或者需要操作底层系统资源的应用，可能需要使用C或C++。
> 6. **图像处理、信号处理：** 对于需要高效处理图像、音频或其他信号的应用，C/C++的性能通常比Java更好，因此可能选择使用底层语言来实现这些部分。
>
> 请注意，尽管使用C或C++可以提供更高的性能和更多的底层控制权，但也增加了开发的复杂性。在选择使用底层语言之前，建议评估应用的性能需求，并确保确实需要使用底层语言来解决问题。



## **APPLICATION FRAMEWORK**

Application framework layer, all written in Java language for developers to call.

## **APPLICATIONS**

 Application layer, all the applications we install belong to this layer, such as WeChat, Plants vs. Zombies.

# Framework 层级

## 1. Framework function

Framework可以被简单地理解成API的仓库，这些API由Java写成，包含JNI方法。JNI会根据 core library 调用C/C++方法，最终访问到Linux Kernel。

Framework层有两个角色：

1. Write some standardized modules in Java and encapsulate them into a framework for APP layer developers to call and develop mobile applications with special services.

2. Use the Java Native Interface to call the native method of the core lib layer. The JNI library is loaded when the Dalvik virtual machine is started. Dalvik will directly address this JNI method and then call it.

一些重要的Framework层服务：

**Activity Manager**: Used to manage the application life cycle and provide commonly used navigation and rollback functions.

**Window Manager**: Provides some methods for us to access the mobile phone screen. Screen transparency, brightness, background.

**Content Providers**: Allows applications to access the data of another application (such as a contact database), or share their own data.

**View System**: Can be used to build applications. It includes Lists, Grids, Textboxes, Buttons, and even an embedded web browser.

**Notification Manager**: Allows the application to display customized prompt information in the status bar.

**Package Manager**: Provides access to system installation packages. Including installing and uninstalling applications, querying permission-related information, and querying Application-related information.

**Resource Manager**: Provides access to non-code resources, such as local strings, graphics, and layout files (Layout files).

**Location Manager**: Provides a way to obtain the address and location of the device. Obviously, GPS navigation can definitely use location services.

其他：

> **Telephony Manager**: It mainly provides a series of methods for accessing the status and information related to mobile phone communication, querying telecommunications network status information, sim card information, etc.
>
> **XMPP**: Extensible communication and presentation protocol. Formerly known as Jabber, it provides instant messaging services. For example, push function, Google Talk.

## 2. Activity Framework structure and running framework

1. Activity creation will create **PhoneWindow**, PhoneWindow will create **DocerView**, and DocerView will create View and **ViewGroup**.

2. The application adds and deletes windows in the Activity by calling the **addView** and **RemoveView** functions of the **WindowManager** class. The specific implementation is achieved by the **WindowManagerImpl** implemented in the bridge mode. Then turn to call **setView** and **removeViewLocked** of **ViewRoot** class, and then call **addWindow** and **removeWindow** in **WMS** (WindowManagerService) through **IPC** mechanism to complete.

3. When **AMS** (ActivityManagerService) informs ActivityThread to destroy an Activity, **ActivityThread** will directly call **WindowManager**’s **removeView** method to delete the window, implemented in **WindowManagerImpl** class.

4. **AMS** calls **WMS** (WindowManagerService), the general situation is to tell WMS some messages, such as <u>a new Activity to start</u> so that WMS will save a reference to the Activity record, and sometimes will also directly call the WMS interface, such as <u>switching windows</u> When the switch window is started, the **setAppStartingWindow** of WMS is called directly.

5.  **WMS** internally takes over the processing of <u>input messages</u> and <u>drawing of the screen</u>. 
   - The processing of input messages is completed with the help of the **InputManager** class. 
   - The **InputManger** class generates two threads, **InputReaderThread** and **InputDispatcherThread**. 
   - **InuptReaderThread** reads input messages from **EventHub** cyclically. 
   - <u>Non - big data</u> is distributed through the channel (**InputChannel** will generate **ServerChannel** and **ClientChannel**), and the corresponding big data is distributed through the shared cache **ShareMemory**; 
   - **InputDispatcherThread** will get the message from the **Channel** or **ShareMemory** and distribute, the distribution is through **InputPublisher**, application-layer client Through the **InputConsumer**, it continuously obtains the distributed messages from **Channel** or **ShareMemory**, and then passes them to **ViewRoot** for processing. 
   - **InputPublisher**, **InputPublisher**, and **InputConsumer** are generated by **InputMoniter**.
   - So **InputReaderThread** and **EventHub** are producers, **InputDispatcherThread** is a consumer, **InputMoniter** is a consumption channel, **ViewRoot** is a bridge between consumers and producers, and WMS and AMS are family butlers.

## 3. FrameWork startup process

**The Android startup process includes the entire process of loading from the Linux kernel to starting the Home application. The overall process is as follows:**

Android is a system platform based on the Linux kernel. When booting, first load the **Linux kernel** through the **bootloader** (system loader). When Linux is loaded and started, it is the same as the ordinary Linux startup process. Initialize the kernel first, and then call the init process.

Init process starts **zygote**: parsing configuration files: **init.rc** (system configuration file) and **initXXX.rc** (hardware platform-related files) content to execute a series of commands, including <u>creating mount directory,</u> <u>installing file system</u>, <u>setting properties</u>, <u>starting Attribute server</u>, <u>start Socket service</u> <u>port</u><u>-”Load preload-classes and preload-resources (Most of the Framework’s classes and resources)-” Fork start a new process Zygote (actually created by fork and execv).

**Zygote** incubates the first process, **SystemServer**, which starts various system service threads. The SystemServer process plays the role of a “nerve center” in the Android operating environment. Most of the system services that can be directly interacted with in the APK application are running in this process. Common systems such as **WMS**, **AMS**, **PackageManagerServer** (PmS), etc. **Services** exist in the SystemServer process as a thread. The main () function of SystemServer first calls the **init1 ()** function, which is a <u>native</u> function, and some initialization work related to the **Dalvik** virtual machine will be carried out internally. After the function is executed, it will call the **init2 ()** function on the <u>Java</u> side. The function first creates a **ServerThread** object, which is a thread, and then directly runs the thread. So, from the run () method of ServerThread, the real Start various service threads.

Basically, each service has a corresponding Java class. From the perspective of coding standards, the modes for starting these services can be categorized into three types: 

- Mode one refers to the use of a <u>constructor</u> to construct a service because most services correspond A thread, therefore, a thread will be created and run automatically inside the constructor. 
- Mode two refers to the service class that will provide a getInstance () method, through which to obtain the service object, this advantage is to ensure that the system contains <u>only one service object</u>. 
- Mode three refers to the <u>execution from the main () function</u> of the service class. 

Regardless of the above mode, after the service object is created, sometimes it may be necessary to call the <u>init ()</u> or <u>systemReady ()</u> function of the service class to complete the startup of the object

After the above service threads are started, **AMS** calls **systemReady** to complete the final start, **mMainStack.resumeTopActivityLocked (null)-”mService.startHomeActivityLocked** starts the first Activity. At this point, the framework started to complete.

# Framework 概述

## Server

- 主要是**ActivityManagerService**（AMS）、**WindowManagerService**（WMS），**PackageManagerService**（PMS）

  - AMS：用于管理所有应用程序的Activity
  - WMS：管理各个窗口、隐藏、显示等
  - PMS：用来管理跟踪所有应用APK的安装、解析、控制权限等


还有用来处理触摸消息的两个类**KeyInputQueue**和**InputDispatchThread**，一个用来读消息，一个用来分发消息。

## Client

The client contains the following classes:

- **ActivityThread**: is the main thread class of Android applications, that is, the UI thread or the main thread. All the work of processing user messages and drawing pages are completed in this thread.
- **Activity**: ActivityThread will choose which Activity object to put on its boat according to the user’s operation.
- **PhoneWindow**: Rich second-generation, inherited from the bullish Window class, owns a **DecorView** object in his house like his father likes to make rules to provide some general window operation API.
- **Window**: The rich generation, which looks more abstract, likes to make rules, and provides some general window operation APIs. It doesn’t like being managed. So, note: <u>the window managed by WindowManagerService is not the Window class, but it is actually View and ViewGroup</u>.
- **DecorView**: A very capable guy, the family property comes from **FrameLayout**, and pays more attention to external dressing. DecorView is a modification of FrameLayout, which can be seen from the name.
- **ViewRoot**: Little housekeeper. Inherited from **Handler**, the main function is to <u>convert WMS IPC call to a local asynchronous call.</u>
- **Class W**: ViewRoot assistant, inherited from the binder, is an internal class of ViewRoot. It mainly helps ViewRoot to convert the WMS IPC call into a local asynchronous call.
- **WindowManager**: If the client wants to create a window, it must first tell WindowManager, and then it communicates with WindowManagerService to see if it can be created, and the client cannot directly interact with WMS.

## Linux driver

主要是SurfaceFlingger（SF）和Binder驱动

- SurfaceFlingger(The painter)：每一个窗口都对应一个Surface，SF驱动的作用就是把每个Surface显示到同一个屏幕上。
- Binder(The courier)：为上面的服务端和客户端提供IPC通讯

From the running process of the apk program to see when the above components are doing.

- ActivityThread starts moving from the main () function and then calls prepareMainLooper () to create a message express channel, **MessageQueue**, for the UI thread.

- Then create **ActivityThread** object, the creation process will create a message handler **Handler** object and a courier **Binder** object, in which Binder is responsible for receiving the remote Ams IPC call, after receiving the call, let Handler load the message to the message express queue, the UI thread is busy It is asynchronous to take messages from the message express queue and perform corresponding operations, such as start, stop, pause.

- Then the UI thread allows the queue to call the **Looper.loop ()** method to enter the message loop body. After entering, it will continuously read and process messages from the message queue.

- When ActivityThread receives the express delivery of an Activity sent by Ams, it will create the specified **Activity** object. Activity will first press the window and then press the glass and window grille, so first create <u>PhoneWindow-> DecorView-> create the corresponding View or ViewGroup</u>. After the creation is complete, you can enjoy it, call **WindowManager** to display the interface on the screen, then create **ViewRoot**, and then call the remote interface provided by Wms to add a window and display it on the screen.

- The next step is the user’s operation. The event thread continuously sends the message to the event queue, and then the secretary of the event distribution thread takes out the messages one by one and then calls the corresponding function in Wms to process the message.

# Difference between custom thread and UI thread

The UI thread is run from ActivityThread. In the main () method of this class, **Looper.prepareMainLooper ()** has been used to add a Looper object to this thread. A message queue has been created for this thread, which comes with a secretary halo. Therefore, we can define the Handler object in the Activity, because the thread must have created the message queue when the Handler object is created, and the loading and unloading work must be equipped with the transport belt or the work will not work. 

The ordinary Thread does not create a message queue by default, so you cannot directly define the Handler directly in the Thread. This is the confusion caused by the fact that we do not understand the principle of program operation.

I have been listening to the user’s voice, and all the work of processing user messages and drawing pages is completed in the UI thread.

The client buddy contains at least <u>three thread</u> brothers. After the Activity starts, it creates a **ViewRoot.W** object, and ActivityThread creates an **ApplicationThread** object. These two objects inherit the message manager Binder. Each Binder corresponds to a thread and is responsible for receiving the Linux Binder IPC call sent by the driver. The other is the **UI thread.**

# SystemServer

zygote孵化出的第一个Dalvik进程叫做SystemServer，SystemServer仅仅是该进程的别名，而该进程具体对应的程序依然是app_process，因为SystemServer是从app_process中孵化出来的。

SystemServer中创建了一个Socket客户端，并用AMS负责管理该客户端，之后所有的Dalvik进程都将通过该Socket客户端间接被启动。当需要启动新的APK进程时，AMS中会通过该Socket客户端向Zygote进程的Socket服务端发送一个启动命令，然后Zygote会孵化出新的进程。

上面提到的服务端、AMS、PMS、WMS等都是在SystemServer中启动的。

# Android Framework 源头

操作系统的一般启动流程，分为三个步骤：

- 开机通电后，加载BootLoader程序
- 操作系统内核初始化
- 执行第一个应用程序

# Jetpack

## Jetpack介绍

**什么是Jetpack？**

Jetpack 是一个由多个库组成的套件，可帮助开发者遵循最佳做法，减少样板代码并编写可在各种 Android 版本和设备中一致运行的代码，让开发者精力集中编写重要的代码。

Jetpack 是 Google 为解决 Android 开发碎片化，打造成熟健康生态圈提出的战略规划，是 Google 对 Android 未来提出的发展方向，同时它也是众多优秀 Android 组件的集合。

**为何使用Jetpack**

- 遵循最佳做法：Android Jetpack 组件采用最新的设计方法构建，具有向后兼容性，可以减少崩溃和内存泄露。
- 消除样板代码：Android Jetpack 可以管理各种繁琐的 Activity（如后台任务、导航和生命周期管理），以便您可以专注于打造出色的应用。
- 减少不一致：这些库可在各种 Android 版本和设备中以一致的方式运作，助您降低复杂性。

**Jetpack的优势**

- Jetpack 拥有基于生命周期感知的能力，可以减少 NPE(空指针异常) 崩溃、内存泄漏，为开发出健壮且流畅的程序提供强力保障；
- Jetpack 可以消除大量重复样板式的代码，可以加速 Android 的开发进程，组件可搭配工作，也可单独使用，同时配合 Kotlin 语言特性能够显著提高工作效率；
- 统一开发模式，抛弃传统的 MVC, MVP；

## **Jetpack构成**

![img](Android架构_imgs\15.png)

如上图：Jetpack 主要包括 4 个部分，分别是【Architecture：架构】、【UI：界面】、【Behavior：行为】和【Foundation：基础】。

### **Architecture：架构组件**

目的：帮助开发者设计稳健、可测试且易维护的应用；

- **Lifecycle**：具备宿主生命周期感知能力的组件。特性：持有组件(如 Activity 或 Fragment)生命周期状态的信息，并且允许其他对象观察此状态；

- **LiveData**：新一代具备生命周期感知能力的数据订阅、分发的组件。特性：支持共享资源、支持黏性事件的分发、不再需要手动处理生命周期、确保界面符合数据状态；

- **ViewModel**：具备生命周期感知能力的数据存储组件。特性：页面因配置变更导致的重启，此时数据不丢失；可以实现跨页面(跨 Activity)的数据共享；

- **SavedState**：架构组件原理解析。特性：因内存不足，电量不足导致页面被回收时可以搭配 ViewModel 实现数据存储与恢复；

- **Room**：轻量级 orm 数据库，本质上是一个 SQLite 抽象层。特性：使用简单(类似于 Retrofit 库)，通过注解的方式实现相关功能，编译时自动生成相关实现类

- **DataBinding**：只是一种工具，解决的是 View 和数据之间的双向绑定。特性：支持数据与视图双向绑定、数据绑定空安全、减少模板代码、释放 Activity/Fragment 压力；

- **Paging**: 列表分页组件，可以轻松完成分页预加载以达到无限滑动的效果。特性：巧妙融合 LiveData、提供多种数据源加载方式；不足之处：不支持列表数据增删改，列表添加 HeaderView，FooterView 定位不准确；

- **Navigation**：端内统一路由组件。特性：能够为 Activity，Fragment，Dialog，FloatWindow 提供统一的路由导航服务，可以传递参数，指定导航动画，还支持深度链接等主要能力；不足：十分依赖 xml 配置文件不利于组件化，模块化

- **WorkManager**：新一代后台任务管理组件，service 能做的事情它都能做。特性：支持周期性任务调度、链式任务调度、丰富的任务约束条件、程序即便退出，依旧能保证任务的执行；

### Foundationy：基础组件

目的：提供横向功能，例如向后兼容性、测试、安全、Kotlin 语言支持，并包括多个平台开发的组件；

- **Android KTX**：优化了供 Kotlin 使用的 Jetpack 和 Android 平台 API，帮助开发者以更简洁、更愉悦、更惯用的方式使用 Kotlin 进行 Android 开发；

- **AppCompat**：帮助较低版本的 Android 系统进行兼容；

- **Auto**：开发 Android Auto 应用的组件，提供了适用于所有车辆的标准化界面和用户交互；

- **检测**：从 AndroidStudio 中快速检测基于 Kotlin 或 Java 的代码；

- **多 Dex 处理**：为具有多个 Dex 文件应用提供支持；

- **安全**：安全的读写加密文件和共享偏好设置；

- **测试**：用于单元和运行时界面测试的 Android 测试框架；

- **TV**：构建可让用户在大屏幕上体验沉浸式内容的应用；

- **Wear OS**：开发 Wear 应用的组件；

### Behavior：行为组件

目的：帮助开发者的应用与标准 Android 服务(如通知、权限、分享)相集成；

- **CameraX**：帮助开发简化相机应用的开发工作，提供一致且易于使用的界面，适用于大多数 Android 设备，并可向后兼容至 Android 5.0(API 21)；

- **DownloadManager**：处理长时间运行的 HTP 下载的系统服务；

- **媒体和播放**：用于媒体播放和路由(包括 Google Cast)的向后兼容 API；

- **通知**：提供向后兼容的通知 API，支持 Wear 和 Auto；

- **权限**：用于检查和请求应用权限的兼容性 API；

- **设置**：创建交互式设置，建议使用 AndroidX Preference Library 库将用户可配置设置集成到应用中；

- **分享操作**：可以更轻松地实现友好的用户分享操作；

- **切片**：切片是一种 UI 模板，创建可在应用外部显示应用数据的灵活界面元素；

### UI：界面组件

- **Animation and Transition**：该框架包含用于常见效果的内置动画，并允许开发者创建自定义动画和生命周期回调；

- **Emoji Compatibility**：即便用户没有更新 Android 系统也可以获取最新的表情符号；

- **Fragment**：组件化界面的基本单位；

- **布局**：用 XML 中声明 UI 元素或者在代码中实例化 UI 元素；

- **调色板**：从调色板中提取出有用的信息；

## Jetpack应用架构

![img](Android架构_imgs\16.png)

ViewModel 类旨在以注重生命周期的方式存储和管理界面相关的数据。ViewModel 类让数据可在发生屏幕旋转等配置更改后继续留存。

LiveData 是一种可观察的数据存储器类。与常规的可观察类不同，LiveData 具有生命周期感知能力，意指它遵循其他应用组件（如 Activity、Fragment 或 Service）的生命周期。这种感知能力可确保 LiveData 仅更新处于活跃生命周期状态的应用组件观察者。