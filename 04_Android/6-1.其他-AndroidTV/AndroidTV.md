# 开发入门

## UI设计

- TV的观看距离较远，建议限制TV屏幕上的文字和阅读量
- 确保界面具有清晰的两轴导航路径以供上下左右四个方向的移动操作使用
- 应用必须清楚地指明聚焦的对象，这样用户就很容易看出他们可以执行的操作。使用缩放、阴影亮度 、不透明度、动画来帮助用户看出聚焦的对象。

## 声明 TV Activity

目标平台为 TV 设备的应用必须在其清单中声明 TV 启动器 Activity。它使用 CATEGORY_LEANBACK_LAUNCHER intent 过滤器来执行此操作。此过滤器可将您的应用标识为支持 TV 平台，并让 Google Play 将其识别为 TV 应用。

```java
    <application
      android:banner="@drawable/banner" >
      ...
      <activity
        android:name="com.example.android.MainActivity"
        android:label="@string/app_name" >

        <intent-filter>
          <action android:name="android.intent.action.MAIN" />
          <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
      </activity>

      <activity
        android:name="com.example.android.TvActivity"
        android:label="@string/app_name"
        android:theme="@style/Theme.Leanback">

        <intent-filter>
          <action android:name="android.intent.action.MAIN" />
          <category android:name="android.intent.category.LEANBACK_LAUNCHER" />
        </intent-filter>

      </activity>
    </application>
```

注意：如果您不在应用中包含 CATEGORY_LEANBACK_LAUNCHER intent 过滤器，那么用户在 TV 设备上运行 Google Play 时将看不到您的应用。此外，如果您的应用没有此过滤器，那么当您使用开发者工具将其加载到 TV 设备上时，该应用不会出现在 TV 界面中。

## 声明Leanback支持

声明您的应用使用 Android TV 所要求的 Leanback 界面。如果您要开发一款在移动设备（手机、穿戴式设备、平板电脑等）以及 Android TV 上都可运行的应用，请将 required 属性值设为 false。如果您将 required 属性值设为 true，您的应用将只能在使用 Leanback 界面的设备上运行。

```java
    <manifest>
        <uses-feature android:name="android.software.leanback"
            android:required="false" />
        ...
    </manifest>
```

## 将触摸屏声明为非必备条件

目标平台为 TV 设备的应用不依赖于触摸屏进行输入。为明确这一点，您的 TV 应用的清单必须声明 android.hardware.touchscreen 功能为非必备功能。此设置会将您的应用标识为能够在 TV 设备上工作，这也是您的应用在 Google Play 中被视为 TV 应用的必要条件。以下代码示例展示了如何添加此清单声明：

```java
 <manifest>
        <uses-feature android:name="android.hardware.touchscreen"
                  android:required="false" />
        ...
</manifest>
```

注意：您必须在应用清单中声明触摸屏并非必要条件（如本示例代码中所示），否则您的应用将不会出现在 TV 设备上的 Google Play 中。

## 提供主屏幕横幅

如果应用包含 Leanback 启动器 intent 过滤器，那么它必须针对每种本地化语言提供一张主屏幕横幅图片。横幅是显示在主屏幕的应用和游戏行中的应用启动点。如需向您的应用添加横幅，请在清单中描述横幅，如下所示：

```java
    <application
        ...
        android:banner="@drawable/banner" >

        ...
    </application>
    
```

您可以将 android:banner 属性与 <application> 标记一起使用，为所有应用 Activity 提供默认横幅，也可以将其与 <activity> 标记一起使用，为特定 Activity 提供横幅。

横幅应该是 xhdpi 资源，尺寸为 320 x 180 像素。文本必须包含在图片中。如果您的应用支持多种语言，对于带文本的横幅，您必须针对支持的每种语言提供单独的版本。

*大概类似于logo吧。。。

## 更改启动器颜色

当 TV 应用启动时，系统会显示动画，就像一个不断膨胀的实心圆。要自定义此动画的颜色，请将 TV 应用或 Activity 的 android:colorPrimary 属性设为特定颜色。此外，还应将另外两个过渡重叠属性设为 true，如主题背景资源 XML 文件中的以下代码段所示：

```java
    <resources>
        <style ... >
          <item name="android:colorPrimary">@color/primary</item>
          <item name="android:windowAllowReturnTransitionOverlap">true</item>
          <item name="android:windowAllowEnterTransitionOverlap">true</item>
        </style>
    </resources>
    
```

# 添加 TV 库

Jetpack 包含用于 TV 应用的 androidx 软件包库。这些库为 TV 设备提供了 API 和界面微件。

- androidx.leanback.app
- androidx.leanback.database
- androidx.leanback.graphics
- androidx.leanback.media
- androidx.leanback.preference
- androidx.leanback.system
- androidx.leanback.widget
- androidx.leanback.widget.picker

# 代理设置

C:\Users\5109U25854\.gradle的gradle.properties文件下

systemProp.http.proxyHost=137.153.66.14

systemProp.http.proxyPort=10080

systemProp.https.proxyHost=137.153.66.14

systemProp.https.proxyPort=10080

# 确认App是否运行在TV设备下

UiModeManager.getCurrentModeType()

```java
public static final String TAG = "DeviceTypeRuntimeCheck";
UiModeManager uiModeManager = (UiModeManager)getSystemService(UI_MODE_SERVICE);
if(uiModeManager.getCurrentModeType()==Configuration.UI_MODE_TYPE_TELEVISION){
    Log.d(TAG,"Running on a TV Device")
}else{
    Log.d(TAG,"Running on a non-TV Device")
}
```

# 连接

TV开发不像手机开发， 通过USB线连接进行调试。 可以在电视的网络设置中找到电视的IP地址，通过以下adb命令进行连接， 连接成功后即可在AS中操作电视设备。

```arduino
// 连接电视
adb connect 170.2.10.20  

// 断开连接
adb disconnect 170.2.10.20
```

开发版的系统可以直接连接

# 键盘输入

和手机的输入方式相比，可以说复杂了很多。电视不是触屏的，每一个字符度需要操作遥控器，通过上下左右找到字符，点击确认输入。

如果发现之前的某个字符输错， 又要返回去删除， 简直是噩梦。

部分遥控器已经有了红外操作装置， 输入字符类似于鼠标点击键盘， 但是相比手机触屏，依旧复杂.......

通过下面的adb命令可以快速将字符串输入到电视的输入框中

```arduino
adb shell input text "hello,world"
```

# 焦点控制

电视的按钮状态，相比手机要稍微复杂一些。

用户使用手机APP是可以随处点击，没有限制。 有点击事件的，没有点击事件的，都想点点试试。

电视用户的话，需要限制用户那块可以点击，那块不可以，这就需要用遥控器的上下左右跳转来限制View能否或得焦点。并需要时时刻刻需要告诉用户目前的焦点处于什么位置，方便进行接下来的操作。

## 1.设置可获取焦点

布局文件中

```ini
android:focusable="true"
```

代码中

```arduino
view.setFocusable(true);
```

## 2.设置触摸获取焦点

布局文件中

```ini
android:focusableInTouchMode="true"
```

代码中

```arduino
view.setFocusableInTouchMode(true);
```

## 3.View焦点监听

```typescript
view.setOnFocusChangeListener(new View.OnFocusChangeListener() {
    @Override
    public void onFocusChange(View v, boolean hasFocus) {
        if (hasFocus) {
            // 获取焦点时操作，常见的有放大、加边框等
        } else {
            // 失去焦点时操作，恢复默认状态
        }
    }
});
```

## 4.View获取焦点时， 设置下一个获取焦点的View

布局文件中：

```ini
 android:nextFocusDown="@id/button1"
 android:nextFocusUp="@id/button2"
 android:nextFocusLeft="@id/button3"
 android:nextFocusRight="@id/button4"
```

代码中：

```ini
 view.setNextFocusDownId(R.id.button1);
 view.setNextFocusUpId(R.id.button2);
 view.setNextFocusLeftId(R.id.button3);
 view.setNextFocusRightId(R.id.button4);
```

## 5.确定焦点的位置

TV开发过程中，最头疼的就是遥控器按着按着就不知道焦点去哪了。 明明所有的的View都限制了能否获取焦点，以及获取焦点的状态。 还是会出现按着按着就不知道焦点去哪了。这个在复杂的自定义View中容易出现。

这个时候就要相办法定位到焦点躲到哪里去了......

```java
        ViewTreeObserver observer = getWindow().getDecorView().getViewTreeObserver();
        observer.addOnGlobalFocusChangeListener(new ViewTreeObserver.OnGlobalFocusChangeListener() {
            @Override
            public void onGlobalFocusChanged(View oldFocus, View newFocus) {
                VLog.d(TAG, "oldFocus:    " + oldFocus + "/n" + "newFocus:    " + newFocus);
            }
        });
复制代码
```

设置Window的全局焦点监听，将失去焦点和获得焦点的View打印出来。

## 6.descendantFocusability属性

在复杂的自定义View中， 只有外层的父View能获取到焦点， 子View无论如何也获取不到焦点。
 如何让子View也能获取到焦点那？descendantFocusability属性可以帮忙搞定

官方的定义是这样子的：

```xml
<!-- Defines the relationship between the ViewGroup and its descendants when looking for a View to take focus. -->
<attr name="descendantFocusability">
	<!-- The ViewGroup will get focus before any of its descendants. -->
	<enum name="beforeDescendants" value="0" />
	<!-- The ViewGroup will get focus only if none of its descendants want it. -->
	<enum name="afterDescendants" value="1" />
	<!-- The ViewGroup will block its descendants from receiving focus. -->
	<enum name="blocksDescendants" value="2" />
</attr>
```

descendantFocusability是View的一个属性。通过这个属性可以指定viewGroup和其子View到底谁获取焦点， 直接在viewGroup的 xml的布局上使用就行。

```ini
android:descendantFocusability="afterDescendants"
```

三种属性值分别为：

- beforeDescendants ：viewGroup会优先其子类控件而获取到焦点
- afterDescendants ：viewGroup只有当其子类控件不需要获取焦点时才获取焦点
- blocksDescendants ：viewGroup会覆盖子类控件而直接获得焦点

# 按键监听

UI可能天马行空的想给某个View的按下操作加个动画， 这个时候就要监听遥控器的按下操作，并开启动画了。

如何监听那？

```csharp
view.setOnKeyListener(new View.OnKeyListener() {
        @Override
        public boolean onKey(View v, int keyCode, KeyEvent event) {
            if (keyCode == KeyEvent.KEYCODE_BACK && event.getAction() == KeyEvent.ACTION_DOWN) {
                // 这种情况就是当按下遥控器返回键时
                return true;
            }
            return false;
        }
    });
复制代码
```

常用的遥控器按键：

```arduino
KeyEvent.KEYCODE_BACK // 返回键
KeyEvent.KEYCODE_DPAD_DOWN // 下键
KeyEvent.KEYCODE_DPAD_UP // 上键
KeyEvent.KEYCODE_DPAD_LEFT // 左键
KeyEvent.KEYCODE_DPAD_RIGHT // 右键
KeyEvent.KEYCODE_MENU // 菜单键
KeyEvent.KEYCODE_SETTINGS // 设置键
```

跟手机开发一样，HOME键监听不到

# UI状态

为了方便用户的操作，更好的提示用户。按钮有焦点态， 按下态，点击态等多种状态，这些可能度需要处理。类似于下图这种

像这种其实也是比较简单的，用一个SelectDrawable就可以解决

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@drawable/bg_focus" android:state_focused="true" />
    <item android:drawable="@drawable/bg_press" android:state_pressed="true" />
    <item android:drawable="@drawable/bg_select" android:state_selected="true" />
    <item android:drawable="@drawable/bg_normal" />
</selector>
复制代码
```

# 模拟器模拟电视分辨率

如果电视的屏幕特别大的话， 对UI的开发也是一种挑战。
 现在的电视动辄就五十多英寸起步，太大了。 看个UI效果都要退后离电视三五米。这样开发谁受得了。
 这个时候就需要模拟器来帮你了， 用模拟器模拟电视的分辨率， 可以在本地的模拟器上直接看效果。 不用再离电视三五米的距离了......

我用的MuMu模拟器设置分辨率， 其他第三方模拟器应该也是支持的

# Chrome插件模拟遥控器点击

既然使用模拟器来模拟TV， 那就还缺一样东西。 PC的模拟器虽然不是触控的， 需要用鼠标操作。 和电视的遥控器有一定区别。

那有没有一种工具， 像遥控器一样操作模拟器来模拟上下左右的按键嘛？答案是有的。

Chrome插件，ChromeADB可以模拟遥控器对设备的操作

下载地址：[chrome.google.com/webstore/de…](https://link.juejin.cn?target=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fchromeadb%2Ffhdoijgfljahinnpbolfdimpcfoicmnm%3Fhl%3Dzh-cn)

不能科学上网的同学，可以去GitHub下载进行离线安装：[github.com/importre/ch…](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fimportre%2Fchromeadb)

安装完成后， 连接模拟器。右边的Keyboard就可以当做遥控器来操作设备了。

# 实战之RecyclerView的焦点问题处理

在开发Android TV应用时， 使用遥控器控制RecyclerView的焦点，向用户展示当前选中的是那个item。会遇到几个头疼的问题：

- 设置Item获得焦点时的效果
- RecyclerView第一次获得焦点，默认选中第一项
- RecyclerView重新获得焦点后，选中上次的item
- RecyclerView失去焦点后，继续保持item的选中效果

## 1.设置Item获得焦点时的效果

和单个View一样， 给Item设置SelectDrawable即可。

## 2.RecyclerView第一次获得焦点，默认选中第一项

由于Android系统的焦点跳转规则是就近跳转，可能某个离RecyclerView比较近的View，在跳转时， 跳转到了离它比较近的，RecyclerView内部的某个ItemView，而不是RecyclerView内部的第一个ItemView。这显然不符合我们的要求。

那么如何才能让我们在RecyclerView第一次获得焦点时，选中第一项那？

答案是使用： HorizontalGridView或者VerticalGridView。这两个View是leanback仓库里面的两个类，  都是继承自BaseGridView，而BaseGridView继承自RecyclerView。HorizontalGridView是处理横向RecyclerView的焦点问题， VerticalGridView是处理竖向的。

添加依赖：

```arduino
implementation "androidx.leanback:leanback:1.0.0"
```

使用

```ini
 <androidx.leanback.widget.HorizontalGridView
        android:id="@+id/rvHead"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:nextFocusLeft="@id/rvHead"
        android:nextFocusRight="@id/rvHead"/>
```

因为HorizontalGridView extends BaseGridView extends RecyclerView，所以之前使用RecyclerView的代码基本不用改变，并且不用调用setLayoutManager。（千万不调用setLayoutManager，调用的话会不生效。BaseGridView的焦点控制完全是由内部设置的LayoutManager来生效的）

## 3.RecyclerView重新获得焦点后，选中上次的item

在不做任何处理的情况下，RecyclerView重新获得焦点也是按照最近原则来获得焦点的，而不是上次选中的View获得焦点。
要想让RecyclerView重新获得焦点后，选中上次的item。 使用HorizontalGridView或者VerticalGridView即可。

## 4.RecyclerView失去焦点后，继续保持item的选中效果

(1)同一时刻，有且只能有一个View保持选中状态。当一个View选中时， 之前选中的View取消选中。 那就保存上一次选中的View，当有新的View选中时， 上一次选中的View取消选中，新的View失去焦点时， 将其更新为上次选中的View。

```typescript
            mRootView.setOnFocusChangeListener(new View.OnFocusChangeListener() {
                @Override
                public void onFocusChange(View v, boolean hasFocus) {
                    if (hasFocus) {
                        v.setSelected(true);
                        if (mLastFocusView!= null) {
                            mLastFocusView.setSelected(false);
                        }
                    } else {
                        mLastFocusView = v;
                    }
                }
            });
复制代码
```

(2)既然每次只能有一个ItemView处于选中状态，那就拿到被选中ItemView 的positon, 遍历RecyclerView的所有ItemView, 只要不是被选中的positon, 均不让其处于选中状态。

第二种方法比较暴力，推荐使用第一种方法。

# LeanBack项目

仓库地址：  [github.com/android/tv-…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fandroid%2Ftv-samples%2Ftree%2Fmain%2FLeanback)

This sample is a Videos By Google app, designed to run on an Android TV device, which demonstrates how to use the Leanback Support library which enables you to easily develop beautiful Android TV apps with a user-friendly UI that complies with the UX guidelines of Android TV.

这个项目是Google官方提供，面向TV设备的一个视频APP。主要目的是教你使用Leanback库，轻松的上手开发对用户友好，规范的Android TV APP。

这个库通过一些界面的实现方式， 帮助开发者快速实现TV的开发。下面是这个库一些界面的截图。

感兴趣的同学可以下载到本地，体验一下。

## 推荐

Google TV开发指南： [developer.android.com/training/tv…](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.android.com%2Ftraining%2Ftv%3Fhl%3Dzh-cn)

Android TV--RecyclerView中item焦点实战：[juejin.cn/post/687811…](https://juejin.cn/post/6878114450478628877#comment)

LeanbackShowcase：[github.com/android/tv-…](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fandroid%2Ftv-samples%2Ftree%2Fmain%2FLeanbackShowcase)

tv-samples： [github.com/android/tv-…](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fandroid%2Ftv-samples)
