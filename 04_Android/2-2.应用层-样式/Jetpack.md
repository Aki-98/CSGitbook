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

![img](E:\.personal\CSGitbook\04_Android\4-1.框架层-基础与源码\Android架构_imgs\15.png)

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

![img](E:\.personal\CSGitbook\04_Android\4-1.框架层-基础与源码\Android架构_imgs\16.png)

ViewModel 类旨在以注重生命周期的方式存储和管理界面相关的数据。ViewModel 类让数据可在发生屏幕旋转等配置更改后继续留存。

LiveData 是一种可观察的数据存储器类。与常规的可观察类不同，LiveData 具有生命周期感知能力，意指它遵循其他应用组件（如 Activity、Fragment 或 Service）的生命周期。这种感知能力可确保 LiveData 仅更新处于活跃生命周期状态的应用组件观察者。