# 搭建

1.安装nodejs

2.安装android的sdk包

3.安装java的jdk

4.安装appium-desktop

5.安装python client

```
pip install Appium-Python-Client
```

# 介绍

## 测试对象

- Native apps（本地应用）：使用iOS、Android、Windows SDKs开发的APP
- Mobile web apps（网络移动应用）：使用手机浏览器（iOS上的Safari、安卓上的Chrome或者内置浏览器）访问的web app
- Hybrid apps（混合模式移动应用）：使用WebView访问网页内容的APP

## 测试平台

iOS、Android、Windows

因为Appium的跨平台特性，使得在不同平台上的测试代码可以重复利用。

## Appium的理念

### CS架构

Appium本质上是一个暴露了REST API的服务器，这种C/S架构可以让测试脚本以任何语言写成，也可以将测试脚本与搭载Appium的服务器分离到两个不同的主机

### 会话Session

自动化测试需要在会话中进行，客户端初始化会话需要首先构建一个叫做'Desired Capabilities'的JSON对象，然后将这个json对象发送到appium服务器，服务器会返回一个session id用于发送测试命令。

### Desired Capabilities

定义会话的一套键值对属性，可以区分会话的平台（安卓/苹果）

Appium 和 Appium-Desktop的区别：

Appium-Desktop比Appium多了GUI，可以看到设备界面和视图层级，Appium使用命令行启动。

Desired Capabilities常用属性：

- platformName："Android"	//Andorid/iOS/Windows
- platformVersion："12"    //代表S
- deviceName："BRAVIA_AE_M6L"    //设备名称，查看设备配置文件可以看到
- app："/path/to/the/downloaded/ApiDemos-debug.apk"    //可以指定希望进行自动化测试的app路径
- appPackage："com.qing.testapp"    //指定需要自动化的app包名
- appActivity：".MainActivity"    //指定需要启动的Activity    
- automationName: "UiAutomator2"    //指定自动化测试驱动，有UiAutomator和UiAutomator2

### Appium 的技术架构

- iOS: Apple’s UIAutomation
- Android 4.2+: Google’s UiAutomator
- Android 2.3+: Google’s Instrumentation. (Instrumentation support is provided by bundling a separate project, Selendroid)

Android 4.2 于2012年发布，TestAutomation源码中AndroidUIAutomationService > src 部分应该是4.2以前用于插桩的代码，现在有了UiAutomator不再需要插桩，UiAutomator应该是由Appium Server安装的。

# 命令

## Status

获取远程终端状态确认是否可以连接

## Execute Mobile Command

Execute a native mobile command

可用命令：https://github.com/appium/appium-uiautomator2-driver#platform-specific-extensions

## Session

### 创建会话

### 结束会话

### 获取Session的Desired Capabilities

### 回退到上一步网页（只能用于Web上下文）

### 截屏

### 获取页面源

Web上下文中得到当前窗口的HTML源文件，本地应用上下文中获取视图层次的XML文件

是由Appium遍历App的层次然后创建一个XML文件，所以会花费很长时间。

### Timeouts

- 设置超时
  - 为某项操作设置可以执行的最长时间，超时则中止。
- 设置隐藏等待时间
  - 当驱动在页面上寻找元素时，会拉取页面直到找到元素或者超过隐藏等待时间，如果不设置隐藏等待时间，则其默认为0ms。
- 设置脚本超时
  - 设置Execute Async命令执行的异步脚本的超时时间

### Orientation

- 获取方向
  - 获取当前设备/浏览器的方向
- 设置方向
  - 设置当前设备/浏览器的方向

### Geolocation

- 获取当前的地理位置
- 设置当前的地理位置

### Logs

- Get available log types
  - 获取可用的log类型
- Get Logs
  - 获取给定日志类型的日志。每次请求后都会重置日志缓冲区

### Events

- Log event
  - 在Appium服务器内存储自定义事件
- Get event
  - 获取Appium服务器内存储的自定义事件

### Settings

- Update Device Settings
  - 更新当前设备的设置
- Retrieve Device Settings
  - 获取当前设备的设置

### Execute Driver Script

- 在当前会话中执行WebdriverIO脚本

## Device

### Activity

- Start Activity
  - 开启一个Activity
- Get Current Activity
  - 获取当前Activity
- Get Current Package
  - 获得当前的安卓包名

### APP

- Install App
  - 安装App
- Is App Installed
  - 某个App是否已安装
- Launch App
  - 运行Session中定义的需要进行测试的App
  - 如果待测应用（AUT）已关闭或后台运行，它将启动它；如果AUT已经打开，它将让其在后台运行之后再重新启动它。
- Background App
  - 将当前正在运行的app设置为在后台运行
  - 需传入希望app在后台运行的时间
  - 经过上面传入的时间后，app会重新启动
- Close App
  - 关闭Session中定义的需要进行测试的App
- Reset App
  - 关闭Session中定义的需要进行测试的App后重新启动
- Remove App
  - 从当前设备中卸载一个APP
- Active App
  - 打开某个应用程序
- Terminate App
  - 对应ActiveApp，关闭某个应用程序
  - Close App只能关闭Session指定的App，Terminate App可以关闭用Active App打开的应用
- Get App State
  - 获取设备上给定应用的状态

```
driver.query_app_state('com.apple.Preferences')
```

| 状态码 | 含义                                |
| ------ | ----------------------------------- |
| 0      | not installed.                      |
| 1      | not running.                        |
| 2      | running in background or suspended. |
| 3      | running in background.              |
| 4      | running in foreground.              |

- Get App Strings
  - ？？？实在看不懂
- End Test Coverage
  - 获取测试覆盖率数据

### Clipboard（剪切板）

- Get Clipboard
  - 获取系统剪切板的内容
- Set Clipboard
  - 设置系统剪切板的内容

### Emulator

- Emulate power state
  - 模拟连接的模拟器上的电源状态更改（只能用于模拟器，关闭或打开电源）
- Emulate power capacity
  - 在连接的模拟器上模拟电源容量变化。

### Files

- Push File
- Pop File
- Push Folder

### Interaction

#### Shake

- 摇晃手机

#### Lock

- 锁屏

#### Unlock

- 启屏

#### Is Locked

- 确认是否已经锁屏

#### Rotate

- 旋转屏幕

### Keys

#### Press keycode

- 按下keycode

#### Long press keycode

- 长按keycode

#### Hide Keyboard

- 隐藏键盘

#### Is Keyboard Shown

- 确认键盘是否已经打开

### Network

#### Toggle Airplane Mode

- 打开或关闭飞行模式

#### Toggle Data

- 打开或关闭数据服务？？
- 不可用于安卓API21及以上，因为需要系统级或特权权限

#### Toggle WiFi

- 打开或关闭wifi
- 不可用于Android Q及以上

#### Toggle Location Services

- 打开或关闭地理位置服务

#### Send SMS

- 发送短信
- 只能用于模拟器

#### GSM Call

- 打电话
- 只能用于模拟器

#### GSM Signal

- 设置GMS信号强度
- 只能用于模拟器

#### GSM Voice

- 设置GMS语音状态？
- 只能用于模拟器

#### Network speed

- 设置网速
- 只能用于模拟器

### Performance Data

- Get Performance Data
  - 返回支持读取的系统状态信息，如 CPU、内存、网络流量和电池
  - 需要自己指定获取哪一项
- Performance Data Types
  - 返回支持读取的系统状态的信息类型，如 CPU、内存、网络流量和电池

### Screen Recording

- 开始屏幕录制
- 停止屏幕录制

### Perform Touch ID

- 仅限于IOS应用

### System

#### Open Notifications

- 打开安卓通知栏，仅限模拟器

#### Get System Bars

- 检索状态和导航栏的可见性和边界信息

#### Get System Time

- 获得设备上的系统时间

#### Get Display Density

- 获得当前安卓设备的dpi

### Authentication

- Finger Print
  - 通过在受支持的模拟器上使用指纹扫描对用户进行身份验证。


## Element

### Find Element

- 在页面上寻找一个元素

### Find Elements

- 在页面上寻找多个元素

> Appium定位控件的方式：
>
> 1.id定位：通过uiautomatorviewer.bat工具看到的对象id
>
> 2.name定位：指控件的text属性
>
> 3.class name定位：指控件的类，比如Button的class属性是android.widget.Button
>
> 4.XPath定位：(WebDriver提供)
>
> ```
> driver.findElement(By.xpath("//android.view.ViewGroup/android.widget.Button"))  
> 
> driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click()
> 
> driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'times')]")).click()
> 
> driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click()
> 
> driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'equals')]")).click()
> ```
>
> 5.Accessibility ID定位：（Appium拓展的方法）找到元素的contentDescription属性
>
> ```
> driver.findElementByAccessibilityId("plus").click();
> ```
>
> 6.android uiautomator定位：（Appium拓展的方法）
>
> 一个元素的任意属性都可以通过android uiautomator方法来进行定位，但要保证这种定位方式的唯一性。
>
> ```java
> driver.findElementByAndroidUIAutomator("new UiSelector().text(\"clr\")").click();
> driver.findElementByAndroidUIAutomator("new UiSelector().text(\"8\")").click();
> driver.findElementByAndroidUIAutomator("new UiSelector().description(\"plus\")").click();
> driver.findElementByAndroidUIAutomator("new UiSelector().text(\"5\")").click();
> driver.findElementByAndroidUIAutomator("new UiSelector().description(\"equals\")").click();
> ```

定位元素：

```
el ` `=` `driver.findElementByXPath(` `"//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[contains(@index,0)]"` `);
    ` `assertThat(el.getText(),equalTo(` `"note2"` `));
```

### Actions

#### Click

- 点击控件

#### Send Keys

- 向元素发送一系列击键，比如向EditText发送一个字符串作为输入

#### Clear

- Clear an element's value，？是不是也是清空EditText？？

### Attributes

#### Text

- 获取控件可见的文本

#### Name

- 指tag名称

#### Attribute

- 获得控件的某项属性
- 需指定属性名称

```
[checkable, checked, {class,className}, clickable, {content-desc,contentDescription}, enabled, focusable, focused, {long-clickable,longClickable}, package, password, {resource-id,resourceId}, scrollable, selection-start, selection-end, selected, {text,name}, bounds, displayed, contentSize]
```

#### Selected

- 确定一个表单或者类表单控件是否已被选中8

#### Enabled

- 确定元素当前是否已启用

#### Displayed

- 确定一个元素是否正在展示

#### Location

- 确定一个元素在屏幕或页面中的坐标

#### Size

- 确定一个元素的像素大小

#### Rect

- 获取元素的维度和坐标

#### CSS Property

- 查询 Web 元素的经过计算的 CSS 属性的值

#### Location in View

- 在元素滚动到视图中后确定元素在屏幕上的位置（主要是内部命令，并非所有客户端都支持）

### Other

#### Submit

- 提交表单元素

#### Active Element

- 激活当前会话中的一个元素

#### Equals Element

- 比较两个元素的id是否相同

## Context

- ### Get Context

  - 获得Appium正在运行的上下文

- ### Get All Contexts

  - 获取所有可用于自动化的上下文

- ### Set Context

  - 设置要自动化的上下文

## Interactions

### Mouse

#### Move To

将鼠标移动特定元素的偏移量

```
actions = ActionChains(driver)
actions.move_to(element, 10, 10)
actions.perform()
```

#### Click

在当前鼠标坐标处点击鼠标的任意按钮

```
actions = ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()
```

#### Double Click

双击当前鼠标坐标（moveTo设置的）

```
actions = ActionChains(driver)
actions.move_to_element(element)
actions.double_click()
actions.perform()
```

#### Button Down

在当前鼠标坐标处单击并按住鼠标左键

#### Button Up

释放先前按住的鼠标按钮

### Touch

#### Single Tap

在支持触摸的设备上单击一下

#### Double Tap

使用手指运动事件双击触摸屏

#### Move

手指在屏幕上移动

```
from appium.webdriver.common.touch_action import TouchAction
# ...
actions = TouchAction(driver)
actions.tap_and_hold(element)
actions.move_to(element, 50, 50)
actions.perform()
```

#### Touch Down

手指在屏幕上下滑

```
from appium.webdriver.common.touch_action import TouchAction
# ...
actions = TouchAction(driver)
actions.tap_and_hold(element)
actions.move(50, 50)
actions.perform()
```

#### Touch Up

手指在屏幕上上滑

```
from appium.webdriver.common.touch_action import TouchAction
# ...
actions = TouchAction(driver)
actions.tap_and_hold(20, 20)
actions.release(50, 50)
actions.perform()
```

#### Long Press

使用手指运动事件长按触摸屏

```
from appium.webdriver.common.touch_action import TouchAction
# ...
actions = TouchAction(driver)
actions.long_press(element)
actions.perform()
```

#### Scroll

使用基于手指的运动事件在触摸屏上滚动

```
from appium.webdriver.common.touch_action import TouchAction
# ...
actions = TouchAction(driver)
actions.scroll_from_element(element, 10, 100)
actions.scroll(10, 100)
actions.perform()
```

#### Flick

使用手指运动事件在触摸屏上轻拂

```
from appium.webdriver.common.touch_action import TouchAction
# ...
actions = TouchAction(driver)
actions.flick_element(element, 1, 10, 10)
actions.perform()
```

#### Multi Touch Perform

执行多点触控操作序列

```
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
# ...
a1 = TouchAction()
a1.press(10, 20)
a1.move_to(10, 200)
a1.release()

a2 = TouchAction()
a2.press(10, 10)
a2.move_to(10, 100)
a2.release()

ma = MultiAction(self.driver)
ma.add(a1, a2)
ma.perform()
```

#### Touch Perform

执行触摸操作序列

```
from appium.webdriver.common.touch_action import TouchAction
// ...
actions = TouchAction(driver)
actions.tap_and_hold(20, 20)
actions.move_to(10, 100)
actions.release()
actions.perform()
```

### W3C Actions

执行一个或多个键盘和指针（触摸、鼠标、触笔）操作链

```
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element_by_accessibility_id("elId")
actions = ActionChains(driver)
actions.move_to_element(element)
actions.click(hidden_submenu)
actions.perform()
```

## Web

网络应用才会用到的功能