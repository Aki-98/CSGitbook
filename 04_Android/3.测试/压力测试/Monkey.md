# 简介

- Android SDK 中附带的一个工具
- 原理：利用socket通讯（Android客户端和服务端以TCP/UDP方法）来模拟用户的按键输入、触摸屏输入、手势输入等，并把它们发送给系统。同时，Monkey还对测试中的系统进行监测，对下列三种情况进行特殊处理（自动停止）。
  - 如果限定了Monkey运行在一个或几个特定的包上，那么它会检测试图转到其他包的操作，并对其进行阻止。
  - 如果应用程序崩溃或接收到任何失控异常，Monkey将停止并报错
  - 如果应用程序产生了应用程序不响应(anr)的错误，Monkey将会停止并报错
- 相关位置
  - Monkey程序由Android系统自带，使用Java语言写成，在Android文件系统中的存放路径是：/system/framework/monkey.jar；
  - Monkey.jar程序是由一个名为“monkey”的Shell脚本来启动执行，shell脚本在Android文件系统中的存放路径是：/system/bin/monkey；

# 参数

![22](Monkey_imgs\baNP6uGFObW.jpg)

## 帮助

**-help**

```
adb shell monkey -help
```

## 基础参数

**-v**

指定日志级别，Level 0-2。

Level 0 级别最低，仅提供启动提示、测试完成和最终结果等少量信息。

Level 1 提供较为详细的测试信息，如逐个发送到Activity的事件。

Level 2 提供更加详细的测试信息，如测试中被选中或未被选中的Activity。

日志级别 Level 0 示例：

```
adb shell monkey -p com.htc.Weather -v 100 
```

日志级别 Level 1 示例：

```
adb shell monkey -p com.htc.Weather -v -v 100  
```

日志级别 Level 2 示例：

```
adb shell monkey -p com.htc.Weather -v -v -v 100 
```

-v要在事件数目前面

**-S \<seed\>**

伪随机数生成器的seed值，如果用相同的seed值再次运行monkey，它将生成相同的事件序列，对9个事件分配相同的百分比。

**-throttle <毫秒>**

用于指定用户操作（即事件）间的时延，单位是毫秒；如果不指定这个参数，monkey会尽可能快的生成和发送消息。

```
adb shell monkey -p com.sf.DarkCalculator –-throttle 1000 -v 100
```

**-p <包名>**

用此参数指定一个或多个包（即App）

如果不指定此参数，Monkey会允许系统启动所有页面上的Activities

eg.指定一个包：

```
adb shell monkey -p com.example.sellclientapp 100 
```

com.example.sellclientapp为包名，100是事件计数（即让monkey程序模拟100次随机用户事件）

eg.指定多个包：

```
adb shell monkey -p com.htc.Weather -p com.htc.pdfreader 100 
```

**-c \<category\>**

如果指定了一个或更多的category，Monkey会允许系统参观指定目录下列出的Activity。

如果不指定任何的目录，Monkey会选中在目录Intent.CATEGORY_LANUCHER或者Intent.CATEGORY_MONKEY列出的Activity

## 发送的事件类型

| 选项            | 含义                                                         |
| --------------- | ------------------------------------------------------------ |
| --pct-touch     | 点击事件（屏幕某点的一组down-up事件）                        |
| --pct-motion    | 滑动事件（由屏幕上某处的一鞥down事件，一系列的伪随机事件和一个up事件组成） |
| --pct-pinchzoom | 缩放事件                                                     |
| --pct-trackball | 轨迹球事件（由一个或几个随机的移动组成，有时还伴随有点击）   |
| --pct-rotation  | 屏幕旋转事件                                                 |
| --pct-nav       | 基本导航事件（由来自方向输入设备的up/down/left/right组成）   |
| --pct-majornav  | 主要导航事件（如5-way键盘的中间按键、回退按键、菜单按键，通常引发图形界面中的动作） |
| --pct-syskeys   | 系统按键事件百分比（Home、Back、Start、Call、StartCall、EndCall、音量控制键） |
| --pct-appswitch | Activity启动事件                                             |
| --pct-flip      | 键盘唤出隐藏事件                                             |
| --pct-anyevent  | 其他事件                                                     |

*各事件类型的百分比总数不能超过100%

```
adb shell monkey -p com.sf.DarkCalculator --pct-touch 50 --pct-motion 50 1000
```

触摸事件50%，滑动事件50%，事件总数1000

## 调试选项

| 选项                         | 含义                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| --hprof                      | 指定该项后在事件序列发送前后会立即生成分析报告 —— 一般建议指定该项 |
| --ignore-crashes             | 即使应用程序崩溃，Monkey依然会发送事件到系统，直到事件数目达到目标值 |
| --ignore-timeouts            | 即使应用程序发生ANR，Monkey依然继续发送事件到系统，直到事件数目达到目标值 |
| --ignore-security-exceptions | 即使应用程序发生安全异常，如要启动一个Activity但没有相应的权限时，Monkey依然继续发送事件到系统，直到事件数目达到目标值。 |
| --ignore-native-crashes      | 忽略本地方法崩溃                                             |
| --kill-process-after-error   | 发生错误后直接杀掉进程                                       |
| --monitor-native-crashes     | 跟踪本地方法的崩溃问题                                       |
| --dbg-no-events              | 初始化启动的activity，但是不产生任何事件                     |
| --wait-dbg                   | 直到连接了调试器才执行monkey测试                             |

## 其他

为测试分配一个专用的端口号，不过这个命令只能输出跳转的信息及有错误时输出信息；

```
adb shell monkey -p com.package --port 端口号 -v
```

输出到d:\monkeyScreenLog.log

```
adb shell monkey -p http://com.tencent.XXX(替换包名) --throttle 500 --ignore-crashes--ignore-timeouts --ignore-security-exceptions --ignore-native-crashes -v -v -v 1000000 > d:\monkeyScreenLog.log
```

# 日志定位问题

搜索关键字：Fatal、Crash、ANR、Exception





-c： activity必须至少包含一个指定的category，才能被启动，否则启动不了 

