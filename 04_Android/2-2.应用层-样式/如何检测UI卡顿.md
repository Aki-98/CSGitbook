# 如何检测UI卡顿

## 一、使用 GPU 渲染模式分析工具进行分析

[GPU 渲染模式分析](https://developer.android.google.cn/studio/profile/dev-options-rendering?hl=zh-cn)工具可以显示渲染流水线的每个阶段渲染前一帧所用的相对时间。这些信息有助于您确定流水线中的瓶颈所在，从而了解应该优化哪些方面来提高应用的渲染性能。

启用性能分析器

开始前，请确保您使用的是搭载 Android 4.1（API 级别 16）或更高版本的设备，并[启用开发者选项](https://developer.android.google.cn/studio/debug/dev-options?hl=zh-cn#enable)。如需在使用应用时开始分析设备 GPU 渲染，请执行以下操作：

1. 在您的设备上，转到**设置**并点按**开发者选项**。
2. 在**监控**部分，选择 **GPU** **渲染模式分析**或 **HWUI** **渲染模式分析**，具体取决于设备上搭载的 Android 版本。
3. 在“GPU 渲染模式分析”对话框中，选择**在屏幕上显示为条形图**，将图表以条形图的形式叠加在您设备的屏幕上。
4. 打开您要分析的应用。

GPU 渲染模式分析工具以图表（以颜色编码的直方图）的形式显示各个阶段及其相对时间。图 1 显示了此图表的一个示例。

![https://developer.android.google.cn/static/topic/performance/images/bars.png?hl=zh-cn](D:\.repo\CSGitbook\04_Android\2-2.应用层-样式\如何检测UI卡顿_imgs\clip_image002.png)

**图 1.** GPU 渲染模式分析图表

GPU 渲染模式分析图表中显示的每个竖条中的每个分段都表示流水线的一个阶段，并在条形图中使用特定的颜色突出显示。图 2 说明了显示的每种颜色所代表的含义。

![https://developer.android.google.cn/static/topic/performance/images/s-profiler-legend.png?hl=zh-cn](D:\.repo\CSGitbook\04_Android\2-2.应用层-样式\如何检测UI卡顿_imgs\clip_image004.png)

**图 2.** GPU 渲染模式分析图表的图例

基本规则：对于每个可见的应用程序，该工具都会显示一个图形。  

- 沿水平轴的每个柱状图都代表一帧，柱状图的高度代表该帧渲染所花费的时间（以毫秒为单位）。 
- 水平的绿线表示16毫秒。为了达到每秒60帧，每帧柱状图的高度必须保持在此线以下。当柱状图超过该线时，动画中可能会有卡顿。
- 超过16毫秒阈值的帧通过加宽图形宽度和减少透明度来突出显示。    
- 每个柱状图都有不同彩色组成，这些颜色表示不同的渲染阶段。颜色的数量取决于设备所使用的API level。 

| 颜色   | 渲染阶段                | 描述                                                         |
| ------ | ----------------------- | ------------------------------------------------------------ |
| 橙色   | Swap Buffers            | 表示CPU等待GPU完成工作的时间。如果此线条变高，则表示该应用在GPU上执行了太多工作。 |
| 红色   | Command Issue           | 表示Android的2D渲染器向OpenGL发送命令进行绘制及重新绘制显示列表所花费的时间。该条的高度与每个显示列表执行所花费的时间之和成正比，显示列表内容越多，红色条越高。 |
| 浅蓝色 | Sync & Upload           | 表示将位图信息上传到GPU中所需的时间。多数时候意味着该应用程序需要花费大量时间来加载大量图形。 |
| 蓝色   | Draw                    | 表示用于创建和更新视图的显示列表的时间。如果这一部分很高，则可能有很多自定义的视图，或者onDraw方法中有很多工作。 |
| 浅绿色 | Measure / Layout        | 表示在视图层次结构中的onLayout和onMeasure回调上花费的时间。意味着视图层次结构需要花费很长时间进行处理。 |
| 绿色   | Animation               | 表示运行该帧中全部动画所花费的时间。如果此线条很高，则您的应用可能使用的自定义动画效果不佳，或者由于更新了属性而发生了意外工作。 |
| 深绿色 | Input Handling          | 表示应用程序在输入事件回调中执行代码所花费的时间。如果此线条很高，则表明该应用花费了太多时间来处理用户输入。应该考虑将此类处理工作分配到另一个线程。 |
| 墨绿色 | Misc Time / VSync Delay | 表示应用在两个连续的帧之间花费执行时间的时间。如果此线条很高，可能是UI线程中发生了过多的处理，这些处理可以转移到其他线程。 |

 

## 二、利用loop()中打印的日志进行分析

```java
 public static void loop() {
     final Looper me = myLooper();
     final MessageQueue queue = me.mQueue;
     //...
     for (;;) {
       Message msg = queue.next(); // might block
       if (msg == null) {
         return;
       }

      final Printer logging = me.mLogging;
       if (logging != null) {
         logging.println(">>>>> Dispatching to " + msg.target + " " +msg.callback + ": " + msg.what);
       }

      final long traceTag = me.mTraceTag;
       if (traceTag != 0 && Trace.isTagEnabled(traceTag)) {
         Trace.traceBegin(traceTag,
           msg.target.getTraceName(msg));
       }
       try {
         msg.target.dispatchMessage(msg);
       } finally {
         if (traceTag != 0) {
           Trace.traceEnd(traceTag);
         }
       }
       if (logging != null) {
        logging.println("<<<<< Finished to "  + msg.target + " " + msg.callback);
       }
       //...
     }
  }
```

通过给Looper类的mLogging属性创建一个Printer对象，那么运行在主线程中的所有代码都能获取执行的时间，找出耗费时间长的，分析出干了什么，优化之，从而解决UI卡顿问题。

 

## 三、利用Choreographer

Android系统每隔16ms发出VSYNC信号，触发对UI进行渲染。SDK中包含了一个相关类，以及相关回调。理论上来说两次回调的时间周期应该在16ms，如果超过了16ms我们则认为发生了卡顿，我们主要就是利用两次回调间的时间周期来判断.

 

 

 