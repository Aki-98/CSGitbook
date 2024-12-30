# 第一章 Android的性能指标

## 1.1 性能很重要

- 电商APP购物流程的卡顿冗长将降低交易率和用户满意度。
- APP频繁的网络请求会让服务器、网络的性能变差。
- 最恶劣的影响——网站宕机。而低性能就像持续的宕机。

## 1.2 电池寿命

移动设备上最耗电的就是**屏幕**、**蜂窝式网络**和**Wi-Fi**，以及其他的信号发射器（如**蓝牙**或**GPS**）。

# 第二章 构建Android设备实验室

## 2.1 了解用户都在使用什么设备

- 专门网站
- 在APP中植入？，通过数据分析出用户使用设备的分布。

## 2.2 了解用户设备的特性分布

有些设备没有摄像头，有些只有后置摄像头，有些前后置都有。还有些设备附带了NFC、温度传感器、加速度传感器……

### 2.2.1 屏幕

- 分辨率
- 像素密度

### 2.2.2 SDK版本

### 2.2.3 CPU/内存和存储

## 2.3 用户使用的网络

## 2.4 设备差异

- root设备 --> 用户查看敏感文件导致的安全问题
- 工程版本
- 开发者版本

## 2.5 创建设备实验室

需要用不同的设备来覆盖下面这些参数：

- 屏幕尺寸
  - 小（4.4%）
  - 中（82.9%）
  - “巨屏手机”（8.6%）
  - 平板电脑（4.1%）
  - 特殊情况（穿戴设备、电视、汽车等）
- 屏幕分辨率
  - 低（4.8%）
  - 中（16.1%）
  - 高（40.2%）
  - 超高（36.6%）
- 处理器
  - 双核
  - 四核
  - 多核
- 内存
  - RAM
  - 存储（例如，对比容量可用很少和大量空闲的设备）
- 网络速度
  - 3G
  - LTE
  - Wi-Fi
- SDK版本（陈旧了）
  - Gingerbread（2.3、2.3.3、2.3.7）
  - Ice Cream Sandwich
  - Jelly Bean（4.1、4.3）
  - KitKat
  - Lollipop
  - Marshmallow（或更高）
- 其他考虑
  - root设备
  - 安全测试
  - 原始设备制造商（OEM）差别

### 2.5.1 购买建议

- 选择了与从??年起历年高端的、特性相近的手机（之前流行的）
- 使用设备分析来推断现在流行的设备，并从这个列表中采购设备（目前流行的）
- Nexus设备会率先更新操作系统，这样一来就可以早于主流设备提前在最新的操作系统上测试App（以后流行的）

### 2.5.2 除了手机的设备

**Android Wear**

- APP在手表和手机上应该配有不同的界面。
- Google将手表上的交互划分为下面两种：
  - 建议：即时信息列表（消息、位置相关的数据等）
  - 要求：允许语音命令控制Wear设备发出请求数据

### 2.5.3 AOSP设备

这些设备缺少以下组件：

- 分发App的Google Play Store
- Google Cloud Messenger推送消息
- Google Play服务
- Google产品，几乎所有Google定制的其他工具类App

常见的AOSP设备：

- Amazon电子阅读器
- 其他的Android手机/平板电脑（小米、华为）

### 2.5.4 其他选择

#### 远程设备测试

有些在线服务提供了通过网络接口访问实际设备的API。但这些服务不太可能节省你的测试成本（事实上，它可能更贵）。这样做还有另一个缺点，没有实际的物理设备，你无法看到运行缓慢的情况或性能问题。这样你只是得到了测试结果，而不能真正看到App在这些设备上的运行状况。

#### Google云测试实验室

针对每一个品牌、每一个型号、每一个版本的物理设备，世界上的每一种语言、方向和网络状况下构建一种虚拟设备（网络物理设备）。

#### 开放设备实验室

志愿构建，存放旧设备，与同行分享测试机（中国没有）。

### 2.5.5 注意事项

- 获得USB集线器以确保你的所有设备都能供上电
- 为你的移动设备建立一个专用Wi-Fi网络（以确保有足够的Wi-Fi吞吐量）
- 确保所有的设备在每次使用后都会擦除数据，而且不会意外升级系统
- 为每种设备准备合适的电缆和充电器

# 第三章 硬件性能和电池寿命

## 3.1 耗电原因

免费的、有广告的安卓游戏会在背后下载大量广告。

### 3.1.1 Android能耗统计文件

在Android操作系统内部，有一个XML文件描述了系统中主要硬件组件的电量消耗情况。

在/System/Frameworks/目录下，复制一份frameworks-res.apk到你的工作电脑中，然后反编译就可以导出/res/xml/power_profile.xml文件了。

### 3.1.2 屏幕

屏幕是耗电量最大的硬件之一。

1. LCD：每一个像素消耗的能量是相同的，和它们呈现的颜色无关。
2. LED：黑色不使用任何颜色，所以不消耗能量，而与此相对的白色，使用了所有颜色和最高亮度的光，所以会消耗更多的能量。

### 3.1.3 无线设备

蜂窝无线和Wi-Fi使用的电量相近。

蜂窝无线和Wi-Fi最大的不同点在于，蜂窝无线的持续时间要比Wi-Fi长很多，使用蜂窝无线的会话时间也会变长，结果便是比Wi-Fi消耗更多的电能。从根本上讲，若App要使用无线传输，最好的性能提升方式是一次下载尽可能多的数据，然后关闭无线设备。减少请求次数是一个一举两得的办法，不仅可以提升屏幕的加载速度，也可以节省电量。

避免使用GPS可以加快App的响应速度（设备的位置服务依然可用），同时节省电能。

GPS失效备援：当用户处于地下室时，设备可能接收不到GPS信号。如果在一段时间内你都接收不到GPS信号，那么请确保关闭GPS。

### 3.1.4 CPU

CPU的占用率越高，电量消耗得就越快。

### 3.1.5 其他传感器

确保在调用完传感器之后将其注销。如果回调监听者保持活跃，传感器将继续报告数据，这势必会造成不必要的处理器负载、内存占用和电量消耗。

海森堡的测不准原理：观察世界必然干扰世界。监测设备在监测电量使用情况的同时也在消耗电量，从而对监测结果产生干扰。

### 3.1.6 休眠

App不工作的时候让其休眠是很重要的。释放传感器和信号发射器并允许屏幕休眠，会节省很多电量。让App休眠至关重要，算准时机激活App同样很重要。合适的唤醒频率可能会极大地延长电池的使用时间。

### 3.1.7 WakeLock和Alarm

**WakeLock**

WakeLock可以唤醒（保持唤醒状态）移动设备的部分组件。屏幕WakeLock就是电影流媒体App在播放电影期间保持屏幕点亮，或者是音乐流媒体App在播放期间保证音频频道正常运行。

WakeLock是电源管理API的一部分。这个API的使用会影响设备的电源寿命。除非真的需要，否则不要获取PowerManager.WakeLocks，要尽量少用WakeLock并确保使用之后尽快释放，只要屏幕休眠就要确保WakeLock被释放。

WakeLock 检测 API：

```
adb shell dumpsys batterystats
```

**Alarm**

Alarm允许开发者设置时间执行特定的操作，特别是App在后台运行或者是设备处于休眠状态的时候。

有时间精确性要求的提醒应该设置一个准确的Alarm（例如，创建一个闹钟App）。其他的情况下可以使用不精确的Alarm，操作系统会自动协调、合并Alarm来节省电量。

### 3.1.8 Doze模式

Doze模式用来限制设备被唤醒的次数。（Marshmallow之后）

- 激活状态：屏幕点亮。
- 休眠状态：屏幕休眠，但是设备处于唤醒状态。
- 待闲置状态：准备进入闲置状态。
- 闲置状态：设备休眠。
- 闲置维护状态：队列中Alarm和更新任务的短暂的执行机会。

强制设备进入Marshmallow的这几种不同的状态的命令如下：

```
adb shell dumpsys battery unplug //设备停止充电的命令
adb shell dumpsys deviceidle step //重复该命令，遍历各种状态
```

实际上，设备在灭屏的状态下从休眠状态到待闲置状态需要30分钟，并且需要再经过30分钟才会进入闲置模式。一旦进入了闲置模式，设备将推迟所有的Alarm直到下一个闲置维护期（60分钟后）。闲置维护期之间的延时是不断增加的（1小时、2小时、4小时、6小时），最大的间隔是6小时。 所有的Alarm和WakeLock都会被暂停直到维护期的到来，对于那些长期处于闲置状态的设备（像平板电脑），这无疑会节省大量的电量。

## 3.2 基本的电量消耗分析

### 3.2.1 电能统计

开启报告全部WakeLock的功能（这个功能只支持Lollipop及以上的系统）

```
adb shell dumpsys batterystats --reset 
adb shell dumpsys batterystats --enable full-wake-history
```

开启电能统计转储（在这里，下载上次完全充电后的所有电能数据）：

```
adb shell dumpsys batterystats --charged
```

### 3.2.2 Battery Historian

atterystats可以在很大程度上帮助我们确定App消耗电量的原因。它有大量的、有用的、可深入研究的细节，可以用来了解App的表现以及潜在的问题。为了简化分析，Google开发出了Battery  Historian（http://github.com/google/battery-historian），它将原始的batterystats输出文件以图形化的方式生成为一份HTML文档。

运行下面的命令，就可以根据batterystats创建一个可视化的网页：

```
adb bugreport > bugreport.txt  //download the output to your computer ./historian.py  bugreport.txt > out.html //create the html file
```

- battery_level（剩余电量）：鼠标悬停在battery_level变化处，显示剩余电量，以及距上次battery_level变化的间隔
- top（上栏）：列举了当前屏幕上显示的进程。
- Battery info（电池信息）
  - status（状态）：正在放电（与充电状态相对应）。
  - health（健康）：电池健康状态，来自电池管理器API。
  - plug（连接状态）：设备是否接通电源。
- phone_signal_strength（无线网络信息）：显示信号变化（有差、中、好三种）。

- wifi_suppl（Wi-Fi状态）
- wifi_signal_strength（Wi-Fi信号强度）
- phone_scanning（电话扫描）：如果没有信号，手机就会扫描信号（这样会导致更多的电量消耗）。
- screen（屏幕）：屏幕开启的时长。
- plugged（连接）：电量来源（类似于上面的电量信息）。
- data_conn（数据连接）
- phone_state（手机状态）：可以看到蜂窝网络覆盖变化，或者你是否打了一个电话。
- fg：这里指的是前台应用。前台程序很少被销毁来释放内存。
- sync（同步）：处理与服务器的同步。
- wake_lock：
- gps（全球定位系统）
- running（运行）
- wake_reason（唤醒原因）
  - qcom, smd-modem：高通共享内存驱动，与调制解调器内存交互。
  - qcom, smd-rpm：高通共享内存驱动-电源管理器。
  - qcom，mpm：高通MSM电源休眠管理；关闭时钟，将设备置为休眠状态。
  - qcom, spmi高通系统电源管理接口；让设备从工作状态回到休眠状态。
- wake_lock_in（唤醒锁）

- mobile_radio（手机无线网络）：蜂窝无线网络的连接时间（指连接到网络，不一定传输数据），手机切换网络时会有空挡。
- user（使用者）：可能会有多个使用者的情况。
- userfg（前台使用者）：测试时，处于前台的使用者。

## 3.3 JobScheduler

JobScheduler可以替代WakeLock和Alarm运行App的任务。可以将它看作“互相协作的WakeLock/Alarm”API。如果5个App每30分钟唤醒设备一次，则它们的唤醒几乎不可能同步，最终设备每小时会被唤醒10次。但由于JobScheduler是在系统层级，系统可以更有效地执行所有的调度工作。每小时唤醒设备的次数也会减少。

# 第四章 屏幕和UI性能

## 4.1 UI性能基准

研究显示，0~100毫秒的延迟会让用户感知到瞬时的卡顿；100~300毫秒的延迟会让用户感觉迟缓；300~1000毫秒的延迟让用户感觉“手机卡死了”；1000毫秒以上的延迟会让用户想去干别的事情。

**卡顿**

大部分Android设备一秒刷新屏幕60次（也有例外，比如早期的Android设备的刷新频率是50fps，甚至更低）。由于屏幕每16毫秒刷新一次（1s/60fps=16ms/f），所以保证每帧的渲染时间少于16毫秒是非常重要的。如果有一帧跳过了，用户就会感知到动画的跳跃，这样的体验是非常不好的。

## 4.2 Android上的UI和渲染性能改进

- 在使用Gingerbread或更早的Android系统版本的设备上，屏幕绘制是完全在软件上完成的（没有GPU的需求）。然而，随着Android设备的屏幕越来越大，像素精度越来越高，为了能及时渲染屏幕，对软件的要求也越来越高。
- Android的Honeycomb版本新增了平板电脑版，进一步扩大了屏幕的尺寸。考虑到这一点，这个版本增加了GPU芯片，App可以选择完全使用GPU硬件加速来运行渲染的程序。
- 对于运行在Ice Cream Sandwich或者更高版本系统上的App，GPU硬件加速是默认打开的，App会将大部分渲染工作交给特定的硬件，这显著地提高了渲染的速度。
- Jelly Bean  4.1和4.2版本上，为了让App运行起来更加流畅，“黄油计划”为避免卡顿和抖动做了进一步的改进。通过改善VSYNC的时序（更好地调度帧的创建），增加额外的帧缓冲，Jelly Bean设备改善了卡顿丢帧的情况。Android团队在做这些改进的同时，也提供了一系列的工具来测量屏幕绘制、VSYNC缓冲和卡顿的情况，并对开发者开放了这些工具。       

## 4.3 工具

要通过减少布局的层级来加快屏幕的绘制，尽可能地保持视图层级的扁平化并删除所有不必要渲染的视图。

**Hierarchy Viewer**

Hierarchy  Viewer（层次结构查看器）能够很便捷地以可视化方式查看各种视图嵌套关系，可用于研究XML视图结构。

**Systrace**

记录整个Android系统的数据。Systrace Screen Painting可以用来观察屏幕绘制的步骤。

# 第五章 内存性能

# 5.1 内存

**共有内存**：所有的App都会利用这些公共的框架类、资源以及本地类库。为了节省内存，Android使用共享内存来保存这些资源。当分配内存给App时，这些共享内存将被平均分配给所有正在运行的进程。

**私有内存**：私有内存是指只被你的App使用，而其他App不能使用的内存。因为只有你的进程可以使用这些数据，所以这些私有内存将会完全地分配给你的这个进程。

**Zygote**：在Android中，Zygote是一个包含所有框架类、公共资源以及本地库（预装在Zygote内部）的进程。当App启动时，在加载任何你编写的代码之前，它会分支（fork）出一个Zygote进程（App在系统中存活需要的一切由此开始）。这样App初始化就比从零开始快多了。

**脏内存**：脏内存是指仅存在于RAM中的内存，如果数据从RAM中清除掉，App需要重新运行才能将这些数据取回。

**干净内存**：而干净内存是指这些存储在RAM中的单元同样也会存储在磁盘上，如果这些数据被清理掉了，只需从设备中重新加载就可以了。

**ART**：在运行ART的设备上，程序代码已经在安装的时候编译过了，并且在磁盘上也做好准备了，所以当前内存中的程序代码是干净的。

### 5.1.1 内存清理

一般来说，一旦<u>某个对象在App中没有一个活动的引用</u>，就可以作为垃圾被回收了。垃圾回收器会先从根部的对象开始（它知道这些对象是活动的并且正被进程所使用），并且沿着每个引用去查找它们的关联。

#### 5.1.1.1 垃圾回收在操作系统上的改变

**< Gingerbread**

设备内存很小，所以App的堆往往较小。垃圾回收器会遍历整个堆来寻找垃圾，会使所有的CPU进程和线程停止。对于使用内存少的App，垃圾回收非常迅速：可能是2~5毫秒。然而，随着设备变得越来越强大（读取更多内存），并且App也变得越来越大，垃圾回收花费的时间也越来越长。这些中断开始阻碍UI。

**Gingerbread**

使用了一个并发的垃圾回收器来做局部的回收工作，尽管不能清理所有未被引用的对象，但速度更快。并发垃圾回收器会和APP一起运行，而不是阻止APP运行。

**<= KitKat**

垃圾回收器只做简单的“标记清理”，从一整条的内存中一块块地移除未被引用的对象，就会导致内存的碎片化。当设备显示有20MB的自由内存时，最大块的自由内存事实上可能只有1MB，如果用户尝试创建一个4MB的图片，将会遇到内存溢出问题。

**Lollipop**

在这个版本中，Android运行时由Dalvik转变成ART，垃圾回收的效率进一步提高。

在ART中有许多新的垃圾回收算法，其中一个：当一个App不在前台时，它将是一个半空间垃圾回收器，没有被引用的对象被移除之后，被用过的控件将被复制到内存的一块自由空间内，这样内存将会没有碎片。

![image-20221028171019487](【高性能Android应用开发】读书笔记_imgs\aU2HNIfYvKL.png)

> 15年AOSP有一个压缩垃圾回收器项目，可以实现对象在内存中移动位置从而消除碎片。

#### 5.1.1.2 垃圾回收的执行时机

- 在App被分配了新对象（这增加了App所需要的内存空间）时；
- 新视图被创建，而旧视图无效（释放了内存中的引用）时；
- App发生内存泄露，并且在内存中保存了无用的引用（阻塞了垃圾回收，同时导致了其他的内存问题）时。

### 5.1.2 确定APP使用的内存大小

返回App可以使用的堆的最大值：

```
ActivityManager.getMemoryClass()
```

可以获得更多内存。但是大的内存堆将会降低App的速度（因为此架构不得不通过查找更多的数据捕获无用的对象）：

```
getLargeMemoryClass()
```

在log中输出信息：

```
adb  shell  dumpsys  meminfo
```

app使用的全部内存包括私有内存和一定比例的共享内存。

**procstats**

设置→开发者选项→进程统计中，可以看到一个可视的设备内存使用量的界面（默认统计时间是最近的3小时，但是可以改为6、12或者24小时）。

### 5.1.3 Android内存警告

如果App正在运行，并存在内存问题，onTrimMemory会发出以下警告：

- **TRIM_MEMORY_RUNNING_MODERATE**

  首先发出TRIM_MEMORY_RUNNING_MODERATE警告。

- **TRIM_MEMORY_RUNNING_LOW**

  如果继续执行，将会发出TRIM_MEMORY_RUNNING_LOW警告，就像是黄灯警示。这时系统会开始释放资源来提高系统性能。

- **TRIM_MEMORY_RUNNING_CRITICAL**

  如果仍然继续执行并且没有释放资源，将会发出红灯警告：TRIM_MEMORY_RUNNING_CRITICAL。此时，系统会结束后台进程以获取更多的内存。同时，这将降低App的性能。

- **TRIM_MEMORY_UI_HIDDEN**

  当回调TRIM_MEMORY_UI_HIDDEN时，App刚从前台转为后台，这是释放大量UI资源的大好时机。此时App在缓存的App列表中。如果有问题，此App的进程将会被结束。作为一个后台程序，尽可能多地释放资源，这样的恢复会比纯粹的重启更加快速。其中有3个级别：

  - TRIM_MEMORY_BACKGROUND

    App处于列表中，但是是接近尾部的位置。

  - TRIM_MEMORY_MODERATE

    App处于列表的中部。

  - TRIM_MEMORY_COMPLETE

    这是“下一个被结束的就是此App”的警告。

## 5.3 追踪内存泄露的工具

### 5.3.1 Heap Dump

### 5.3.2 Allocation Tracker

### 5.3.3 更加深层次的堆解析：MAT和LeakCanary

hprof是已保存的堆转储文件。转换工具hprof-conv存储于AndroidSDK 工具目录下。

MAT是Eclipse的内存分析工具，可以独立下载使用。

# 第六章 CPU与CPU性能

## 6.1 检测CPU占用率

查看设备的CPU占用率

```
adb shell top -n 1 -m 10 -d 1
```

运行1次命令（-n  1），可以获取1秒内（-d  1）10个CPU占用率最高的App（-m  10）

报告如下：

```
User 58%, System 14%, IOW 0%, IRQ 0% 
User 157 + Nice 6 + Sys 41 + Idle 75 + IOW 1 + IRQ 0 + SIRQ 0 = 280
PID		PR	CPU%	S	#THR	VSS			RSS		PCY	UID		Name 
15252  	1  	32%		S	16		1581536K	93324K	fg 	u0_a109	com.example.isitagoat
1952  	0  	20% 	S	97		1708552		136668K	fg	system	system_server
15987	2	2%		R	1		4464K		1108K	shell		top  	
2413	2   2%		S	32		1650148K	76044K	fg	u0_a11	com.google.process.gapps
3010	1   2%		S	41		1810248K	179400K	fg	u0_a28	com.google.android.googlequicksearchbox
3384	1   2%		S	47		1621432K	83928K  fg	u0_a11	com.google.process.location
2586	1   2%		S	26		1566872K	93088K  fg	u0_a91	com.elvison.batterywidget
2125	0   1% 		S	32		1698300K	166068K	fg	u0_a24	com.android.systemui
267		1   1%		R	15		227172K		17060K  fg	system	/system/bin/surfaceflinger  
6256  	1   0% 		S	49		1603916K	83816K	fg	u0_a28	com.google.android.googlequicksearchbox
```

第一行：用户占用了58%的CPU，内核空间占用了14%

第二行：调度器在状态间切换花费的时间（几十毫秒）。最大数值可能是CPU数的100倍。活跃的进程一共有280个，由于测试运行在Nexus 6（四核CPU）上，最大值是400。

表格：“Is  it  a  goat?”App占用了32%的CPU，系统占用了20%，top命令占用了2%，后台和Google App也占用了一部分。

查看更详细的CPU信息

```
dumpsys cpuinfo
```

看到log

```
Load: 12.28 / 11.64 / 11.56
CPU usage from 11368ms to 4528ms ago with 99% awake:   
	0.3% 1531/mediaserver: 0% user + 0.3% kernel / faults: 1093 minor 1 major   
	130% 15754/com.coffeestainstudios.goatsimulator: 111% user + 19% kernel /      
		faults: 130 minor   
	10% 306/mdss_fb0: 0% user + 10% kernel   
	9.8% 267/surfaceflinger: 4.5% user + 5.2% kernel 
	4.5% 1952/system_server: 1.4% user + 3% kernel / faults: 65 minor   
	0.8% 19261/kworker/0:1: 0% user + 0.8% kernel   
	0.7% 2982/com.android.phone: 0.2% user + 0.4% kernel / faults: 181 minor   
	0.5% 158/cfinteractive: 0% user + 0.5% kernel   
	0.5% 18754/kworker/u8:4: 0% user + 0.5% kernel   
	0.4% 205/boost_sync/0: 0% user + 0.4% kernel   
	0.4% 211/ueventd: 0.2% user + 0.1% kernel   
	0.4% 2586/com.elvison.batterywidget: 0.2% user + 0.1% kernel /   
	faults: 121 minor 
<snip>
```

第一行：CPU在过去的1、5、15分钟的平均负载

后面的：近7秒内所有App的CPU占用率（由于空间原因被截断了）。你可以看到每个App占用CPU的百分比（如果不止运行在一个核心上，它可以超过100%），以及用户态和内核态的比例。

## 6.2 使用Systrace分析CPU

## 6.3 Traceview（遗留的监视器DDMS工具）

## 6.4 Traceview（Android Studio）

## 6.5 其他优化工具

高通提供了一款免费App——Trepn。通过这款软件，你可以查看内存、CPU、电量、网络和其他特性。

# 第七章 网络性能

## 7.1 Wi-Fi与蜂窝无线电

### 7.1.1 Wi-Fi

高吞吐量、低延迟、没有数据收费、建立连接和关闭连接时会有延迟。

### 7.1.2 蜂窝

当手机处于数据连接的低覆盖区域，必须开启天线功率才能维持连接。

活跃的蜂窝无线信号（处于125毫安）比Wi-Fi信号（处于240毫安）耗电量低，但是鉴于蜂窝连接在网络中的实现方式，蜂窝连接的功耗通常会更高一些。

### 7.1.3 RRC状态机

为了提高蜂窝网络的服务质量，所有运营商都采用了一种无线资源控制（Radio Resource Control，RRC）的状态机来控制数据连接的建立与中断。

当手机启动数据连接后，在创建TCP连接之前，会有几种初始无线信号被发送到信号塔。这些信号会使无线连接的创建时间增加500~1000毫秒。

延迟是移动连接质量的关键之一，状态机可以在一定程度上抵消这种延迟。

每一种移动网络都有一个RRC状态机，用于确保在最后一个数据包发出之后无线电信号仍然开启，以补偿建立连接时产生的延迟并平衡电量消耗。（看了好久，终于看懂了，意思是手机中的网络连接因为建立连接时的延迟会和信号塔发送的数据包存在一定的错位，补偿延迟的意思就是保证手机接收到最后一个数据包时信号塔才会关闭连接。平衡电量消耗就看不懂了。）

1. 4G（LTE）状态机

如果没有上面提到的延迟，如果接下来仍有数据快速地发送过来，又需要经历建立连接时产生地延迟。

采用状态机时，当最后的高功率延续时间段没有数据包时，无线连接将会关闭以节省电量。

一般情况下，LTE无线连接比3G无线连接耗费更多的电量。

但如果正在传输的文件很大，LTE的下载速度可能要更快，结束无线连接的时间也会相应缩短，因此使用的电量更少。

但是，绝大多数的移动数据传输并不是大型文件，而是由数百个小型文件构成，因此使用的数据块也相对较小。这些小小的文件无法充分利用LTE的带宽能力（因为它们太小了），因此通过LTE下载内容所耗费的电量比使用3G网络要稍多一些。

**无线电连接和数据连接**

无线电连接指的是Wi-Fi，数据连接指的是蜂窝网络。

蜂窝网络的连接数量有限，一段时间后，网络会自动清理孤立的连接。

蜂窝网络只有在需要进行数据传输时才会建立连接。

而Wi-Fi的连接一直存在。

**手机通话时使用数据**

手机通话时数据网络会降到3G，除非开启了VOLTE

## 7.2 测试工具

### 7.2.1 Wireshark

### 7.2.2 Fiddler

### 7.2.3 MITMProxy

### 7.2.4 AT&T ARO

### 7.2.5 混合型App和WebPageTest.org

## 7.3 Android网络优化

14条标志性性能优化原则：

- 减少HTTPS请求
- 使用内容发布网络
- 添加Expires头
- 压缩组件
- 将样式表放在顶部
- 将脚本放在底部
- 避免CSS表达式

- 使用外部JavaScript和CSS
- 减少DNS查找
- 精简JavaScript
- 避免重定向
- 移除重复脚本
- 配置Etags
- 使AJAX可缓存

### 7.3.1 文件优化

#### 压缩文本文件

常用的压缩算法 --> **Gzip** --> 增设排除小文件的功能，把不足859字节的文件放到一个不用压缩就能发送的数据包里

更进一步的压缩算法，提高5%的压缩率，但是压缩执行时间多出100倍，注意只用它处理已经预压缩过的文件 --> **Zopfli**

### 7.3.2 精简文本文件

（Souders：精简JavaScript）

精简过程就是去掉文本文件中所有只具有方便阅读作用的格式（比如空格、制表符和注释），进而使文件变小。

根据页面大小和复杂度，精简可以将文件缩小20%~50%。很多构建工具（如grunt）自带精简库，在你做改动的时候就可以自动精简文件（帮你节省了很多工作）。

精简虽然可以把文件缩小10%~15%，但是精简过和未精简过的文件进行Gzip压缩后，所节省的文件大小差异只有1%~2%（因为空格的压缩效果好）。

可是，即便只能节省1%~2%的网络传输量，你也应该养成精简的习惯，因为这样能为用户节约设备存储空间。另外，文件越小，读入内存的速度就越快（而且导致内存有限的设备崩溃的可能性越小）。

### 7.3.3 图片

1.**尺寸超大化**

为图片创造图片bucket，App向服务器提供屏幕尺寸以确保得到尺寸正确的图片。

如果缩略图和原图在APP上展示效果一致，可以考虑下载缩略图而不是原图。

2.**元数据**

当用数码相机拍摄照片时，文件里很可能有与相片相关的元数据（设备名称、设备设置、拍摄地点）。图片编辑软件也会给图片添加一些元数据。如果不需要这些元数据的话可以考虑删除。

3.**压缩**

WebP格式图片通常比类似的JPEG格式图片小20%。

### 7.3.4 文件缓存

1.**应用内缓存**

Android缓存功能默认是关闭的，所以你需要将它打开。对于Android  4.0及更新版本，在onCreate中调用以下代码就可以启用HTTP响应缓存：

```java
private void enableHttpResponseCache() {   
    try {     
        long httpCacheSize = 10 * 1024 * 1024; // 10 MiB     
        File httpCacheDir = new File(getCacheDir(), "http");     
        Class.forName("android.net.http.HttpResponseCache")          
            .getMethod("install", File.class, long.class)          
            .invoke(null, httpCacheDir, httpCacheSize);   
    } catch (Exception httpResponseCacheNotAvailable) {     
        Log.d(TAG, "HTTP response cache is unavailable.");   
    } 
}
```

2.**服务器端缓存**

服务器向设备传输的报头设定了设备里存储的每个文件的缓存时间。缓存定时器的长度实际取决于缓存内容及其改动的频率。

3.**Cache Control**（添加Expires报头）

缓存最常用的报头是Cache-Control报头，它有几个可以指定的常用值。

- Private/Public

  网络中CDN缓存使用的代表性指令。它可以向CDN表明文件是公共的（任何人都可以使用）还是用户私有的。

- no-store如果文件

  使用该指令，那么该文件无法缓存，必须在每次使用时下载。

- no-cache

  no-cache报头的名称可能令人误解。带有no-cache报头的文件实际上是可以缓存的，但是再次使用前必须重新验证。

- max age=X

  max-age表示文件可以缓存的最大时间（单位：秒）。常用值为0（与no-cache相同）、60、300、600、3600（1小时）、86 400（1天）、3 153 600（1年）。

4.**ETag**

ETag是一种响应报头，包含由随机字符组成的唯一字符串。每次从缓存中使用文件时，ETag必须先在服务器端验证。如果本地字符串与服务器端一致，服务器发回“304  not modified”，那么使用本地文件。如果ETag不一致，则下载新文件并保存在缓存内。

对于经常过期的文件，ETag是验证本地缓存文件是否依旧与服务器同步的好方法。但对于很少改动的文件，ETag则是昂贵（从性能方面来看）的缓存机制。这是因为尽管并未下载文件（这样节省了带宽），但是依旧建立了连接，连接时间延长了文件处理过程。

**5.Expires**

给出文件未来过期和应当重新验证的具体日期。这是网络上最早使用的缓存报头，一些老式的浏览器可能还在使用它。

**第一次启动APP**

第一次启动几乎决定了用户满意度，关乎成败。如果App第一次启动花费了很长时间进行配置（下载图片和文件），那么用户可能就不会再用你的App了。把图片和文件放入App的资源文件，虽然需要下载的App会变大，但是可以加快第一次启动的速度。此外，如果你改动了标志、图标等，你需要做的是发布一个App更新。

HTTP缓存规范规定，如果文件不含内容，那么会被缓存24小时。如果你不想缓存文件，必须明确说明，以避免出现按照规范进行缓存的情况！

### 7.3.5 分组连接

利用JobScheduler API 进行定期连接，减少APP进行网络连接的数量，

### 7.3.6 检测应用的无线电使用情况

检查用户连接的是wifi还是蜂窝网络：

```java
public static String getNetworkClass(Context context) {     	
    ConnectivityManager cm = (ConnectivityManager)context.getSystemService(Context.CONNECTIVITY_SERVICE);    
    NetworkInfo info = cm.getActiveNetworkInfo(); 
    if(info==null || !info.isConnected())  
        return "-"; 
    //未连接
    if(info.getType() == ConnectivityManager.TYPE_WIFI) 
        return "wifi";     
    if(info.getType() == ConnectivityManager.TYPE_MOBILE) {
        return "cellular";          
    }      
    return "unknown";  
}
```

确认蜂窝网络连接是否存在，使用TelephonyManager（Tel）数据行为API确定无线电是否打开。

```java
if (Tel.getDataActivity() >0){
	if (Tel.getDataActivity() <4){           
        //1, 2, 3响应代表蜂窝网络正在传输!           
        //用image getter下载图片           
        imagegetter(counter, numberofimages);            
        //并显示广告           
        AdRequest adRequest = new AdRequest();            
        adRequest.addTestDevice(AdRequest.TEST_EMULATOR);            	adView.loadAd(adRequest);            
        //发起通用请求以便随广告加载           
        adView.loadAd(new AdRequest()); 
    }
}
```

在Android 5.0中，ConncetivityManager中加入了新API，现在可以利用ConnectivityManager.OnNetworkActiveListener将这个仅适用蜂窝网络的方法推广应用到所有无线连接，从而找出无线网络何时处于高功率状态（并准备传输数据）。可以使用ConnectivityManager.isDefaultNetworkActive()查看网络是否已经处于活动状态。使用已经建立的无线连接是共享资源和节省用户电量的好方法。

**GCM Network Manager**

GCM  Network Manager可以在Gingerbread（2.3）版本之后的所有Google  Android设备上运行。

用这个API设置的任务可以只在Wi-Fi开启状态或设备连通电源的时候运行。你也可以设置任务使其在后台定期运行或自动退出。利用此API进行非紧急性更新与连接，可以为用户直接节省大量的设备电池用量。

### 7.3.7 适时关闭连接

当需要下载很多的数据包时，可能会只对服务器开启TCP连接，这样就可以减少一些连接设置延迟。对相对快速、连续发送的文件确实如此。但如果文件发送的间隔时间达到或超过了15秒，可能还是得开启无线电（其实连接设置所需时间极少）。

如果一段时间内没有产生数据流量而连接还在开启，设备和服务器都有个关闭连接的清理进程。这也不是件坏事（后续的章节会讲述原由）。但缺点就是关闭连接的一方会告诉对方：“喂，我现在要关闭连接了。”这可能会造成无线电连接的继续开启，继续在设备上运行10~15秒的RRC状态机，给用户造成额外的电量损耗。

图片下载完成后，服务器和设备就会立即关闭连接的代码：

```java
HttpURLConnection connectionCloseProperly = (HttpURLConnection)ulrn.openConnection(); 
//这禁用了“保持链接”
connectionCloseProperly.setRequestProperty("connection", "close");          
connectionCloseProperly.setUseCaches(true); 
connectionCloseProperly.connect();
Object response = connectionCloseProperly.getContent(); 
InputStream isclose = connectionCloseProperly.getInputStream();         //...download and render bitmap image 
connectionCloseProperly.disconnect();
```

### 7.3.8  定期执行重复的ping命令

完美风暴：重复连接和关闭连接

想象一下，当几个人在某区域移动，他们手机上的App每隔五秒和服务器交换一次实时数据以更新位置信息。再想象一下，收到最后一个数据包后（在服务器上保留IP地址），服务器上的连接仍然保持90秒。通常而言，如果每个用户每次会话只要占用一个连接，这就应该没什么问题了。但是如果你更改了代码中的配置，使每一次ping都与服务器建立一个新的TCP连接，而App在发布前没有测试到这个问题，最后会发生什么事？

那么你就引发了一场完美的数据流量风暴！现在每个Android用户每5秒ping一次，将18个之多的IP地址连入服务器。连入的用户越来越多，可能就会发生IP冲突现象，从而导致用户无法连接！恭喜，你的App向服务器成功地完成了一次DDoS攻击。

因此，要特别注意服务器重复执行ping操作，并且应当在App发布前进行测试。

### 7.3.9 网络安全技术的应用（HTTP和HTTPS）

在用网络传输数据时，必须保证用户的个人数据安全。

用户可能会连接到任何类型的网络，包括服务场所不安全的Wi-Fi热点。如果你传输的数据通过HTTP发送，窥探者能毫不费力地获取该数据——因为你是用明文发送的！你应该通过HTTPS发送，使用密钥加密数据，然后再将密钥告知接收方。

## 7.4 全球移动网络覆盖范围

![【高性能Android应用开发】-2](【高性能Android应用开发】读书笔记_imgs\BvjDOa3yAPi.png)

全球数据仅供参考

### 7.4.1 CDN服务器

CDN服务器（大体上来说）是用来在网络前沿或者接近最后一英里处存储数据的服务器。它依赖于数据存储的分布式系统，主系统不会因为请求次数太多而不堪重负。将这些CDN服务器放置在用户附近，数据就更靠近用户了，这样就减少了请求和传送文件的往返时间。

### 7.4.2 仿真慢速网络

1.**Wi-Fi网络节流**

如果你正在使用无线路由器进行测试，并且可以在路由器上安装OpenWRT （一个开源路由器），那么会有一个wshaper插件（http://wiki.openwrt.org/doc/recipes/guest-wlan），让你可以对上行和下行链路连接进行节制，这至少可以让你模拟较慢的网络速度（但不是延迟）。

2.**模拟器**

Android模拟器可以控制网络条件。打开模拟器后，你可以登录到模拟器以模拟不同的吞吐量和延迟：

```
telnet localhost 5554 
network speed edge  //gprs, umts hsdpa和全面的附加选项
network delay edge
```

3.**自制法拉第笼**

法拉第笼是由金属丝构成的笼子，它将内部空间同外部的电磁辐射完全隔离开来。制作局部法拉第笼能够减少到达手机的信号量。有报道称，一些开发人员成功使用旧的（不插电！）微波炉屏蔽掉了部分无线电。由于实验的不确定性，这些测试的结果很难重现，但这也许已足以用于定性测试了。

4.**网络弱化器**

AT&T发布了一款名为AT&T网络弱化器（http://developer.att.com/attenuator）的工具，如图7-16所示。这款网络弱化器在Samsung S3  ICS内核上运行（需要root和一个由AT&T提供的自制ROM闪光）。安装后，这个App可以像一个刻度盘一样减慢移动网络、降低吞吐量（很抱歉，如果你连接的是3G网络，它并不能使你的连接变得和4G网络一样快）。当滑动滑块将网速从UMTS变为EDGE时，上行链路、下行链路和往返时间定时器都会相应地作出调整，让你在较慢速的网络条件下对App进行一些简单的测试。你也可以从左到右滑动滑块以调整网络拥塞程度，增加每个连接的往返时间。

### 7.4.3 构建网络感知APP

感知网络，并且根据所测得的网络条件，调整用户的体验。

要为连接快速、中速和慢速网络的设备提供不一样的移动体验，只需要简单地去除内嵌视频或者减少图像的数量（或者至少改变图像的大小）。

确定移动网络速度的代码：

```java
TelephonyManager teleMan = (TelephonyManager)getSystemService(Context.TELEPHONY_SERVICE); 
int networkType = teleMan.getNetworkType(); 
switch (networkType) {
    case 1:
        netType = "GPRS";                         
        networkSpeed = "slow"; 
        break;  
    case 2:     
        netType = "EDGE";                 
        networkSpeed = "slow";  
        break; 
    case 3:     
        netType = "UMTS";                         
        networkSpeed = "medium"; 
        break; 
        // 我们会略过一些网络类型，但你应该明白我的意思了
        // 你可以在GitHub中查看完整代码
    case 13:    
        netType = "LTE";                         
        networkSpeed = "fast"; 
        break;
}
```

手机向服务器发起下载图片的请求后获得200回复的时间 与 图片下载完成的时间 的差值可以用作估算网络延迟

确定实时的往返时间和吞吐量的代码：

```java
private Bitmap downloadBitmap(String url) {    
    //下载开始时间
	Long start = System.currentTimeMillis();                
    
    final DefaultHttpClient client = new DefaultHttpClient();
    final HttpGet getRequest = new HttpGet(url); 
    try {
        HttpResponse response = client.execute(getRequest);
        //检查成功返回码200 
        final int statusCode = response.getStatusLine().getStatusCode();
        //收到200成功码回复的时间           
        Long gotresponse = System.currentTimeMillis();
    } final HttpEntity entity = response.getEntity();
    //获得文件的ContentLength
    contentlength = entity.getContentLength();
    if (entity != null) {
        InputStream inputStream = null;
        try {
            inputStream = entity.getContent();
            final Bitmap bitmap = BitmapFactory.decodeStream(inputStream);
            Long gotimage = System.currentTimeMillis();
            //图片下载完成的时间
            responsetime = gotresponse - start;
            //200回复完成的时间
            imagetime = gotimage - start;
            //下载时间
            throughput = ((double)contentlength/1024)/((double)imagetime/1000);//KB/s
            return bitmap;
        }
    }
}
```

### 7.4.4 计算延迟

如果处于高延迟环境中，考虑预加载。

### 7.4.5 最后一英里的延迟

延迟通常在数据传输的最后一英里发生，在移动网络中尤其如此。这些技巧可以帮助你应对延迟，缓解问题，但不能从根本上解决问题。正如在7.4.2节中描述的那样，Facebook发现，在印度尼西亚的慢网连接中，84％的流量来自于南美和欧洲的CDN服务器。

### 7.4.6 其他无线电

Wi-Fi和蜂窝无线网都是最常用的传输数据的网络，也是最容易优化的。但是其他的无线电网络也会导致设备的能耗，因此它们的行为也应该被关注、讨论。

### 7.4.7 GPS

Android提供了模糊定位，使用附近蜂窝基站和Wi-Fi网点的信息即可生成粗略的位置信息，并不需要开启GPS。然而，很多App需要更精准的定位，它们会打开GPS设备，从GPS卫星接收信号。定位需要从手机到卫星之间的一条信号线。为了优化定位设备的使用性能，可能必须调整GPS打开的时间（保持GPS接收器打开多久），以及使用频率。打开的时间越长，使用的频率越高，你得到的位置信息就越精准。

### 7.4.8 蓝牙

目前，所有的Android旧设备都必须通过蓝牙才能连接到其他设备。如果你对蓝牙的数据传输感兴趣的话，可以在Wireshark的非集群中收集它的日志信息。对于使用KitKat和更新版本系统的设备，你可以在开发者选项设置中打开“Bluetooth  HCI  snoop  log”。当你选中了该选项时，Android设备将会收集所有通过蓝牙接口发送的数据包的日志信息，信息会被存放在/sdcard/btsnoop_hci.log中。在Wireshark中打开这个日志文件，你可以看到被传输数据包的信息。大部分数据是加密的，但是你可以观察到两个设备之间的通信模式（见图7-17）。

# 第八章 真实用户检测

真实用户检测即收集App的运行时数据，统计结果，生成报告，从这些数据中寻找可能出现的问题。

常用的RUM工具（境外）：

Crashlytics、Crittercism、Google  Analytics和New Relic  RUM
