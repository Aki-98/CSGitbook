# Power按键如何分发给PhoneWindowManager

1.系统的核心进程SystemServer在run()方法中启动InputManagerService和WindowManagerService。创建WindowManagerService前，先创建InputManager，将其作为参数，且创建了PhoneWindowManager实例：

源码路径：frameworks/base/services/java/com/android/server/SystemServer.java

```java
private void startOtherServices() {
       ......
       inputManager = new InputManagerService(context);   //输入系统服务   【step_SystemServer_1】
       
       ......
　　　　//【step_SystemServer_2】
       wm = WindowManagerService.main(context, inputManager,
                 mFactoryTestMode != FactoryTest.FACTORY_TEST_LOW_LEVEL,
                 !mFirstBoot, mOnlyCore, new PhoneWindowManager());   //PhoneWindowManager实例
       ServiceManager.addService(Context.WINDOW_SERVICE, wm);
       ServiceManager.addService(Context.INPUT_SERVICE, inputManager);

}　　　
```

源码路径：frameworks/base/services/core/java/com/android/server/wm/WindowManagerService.java

```java


private WindowManagerService(Context context, InputManagerService inputManager,
            boolean haveInputMethods, boolean showBootMsgs, boolean onlyCore,
            WindowManagerPolicy policy) {
            ......

             mPolicy = policy;    //实例： PhoneWindowManager对象      【step_InputMonitor_2】　　　　　　　......}
```

2、启动inputManager之前，设置了一个回调接口：

```java
　　　　　　//消息分发之前回调--->查看InputManagerService
　　　　　　inputManager.setWindowManagerCallbacks(wm.getInputMonitor());   
　　　　　　inputManager.start();
```

3、InputMonitor.java：

底层收到按键会回调InputManagerService的dispatchUnhandledKey()--->InputMonitor的函数dispatchUnhandledKey()。具体由底层InputDispatcher.cpp调用。

源码路径： frameworks/base/services/core/java/com/android/server/wm/InputMonitor.java

```java
//【Power键属于系统级按键，因此处理方法是dispatchUnhandledKey】
    /* Provides an opportunity for the window manager policy to process a key that
     * the application did not handle. */
    @Override
    public KeyEvent dispatchUnhandledKey(
            InputWindowHandle focus, KeyEvent event, int policyFlags) {
        WindowState windowState = focus != null ? (WindowState) focus.windowState : null;
        
        //此处 mservice: WindowManagerService    【step_InputMonitor_0】
        return mService.mPolicy.dispatchUnhandledKey(windowState, event, policyFlags);
    }
```

由这三步可知，最终由PhoneWindowManager处理。将上述整理成时序图：

![img](PhoneWindowManager-Power键的处理_imgs\2.png)



# PhoneWindowManager处理Power键的基本流程

**1.拦截按键事件**

`PhoneWindowManager` 使用 `interceptKeyBeforeQueueing()` 和 `interceptKeyBeforeDispatching()` 方法来拦截和处理按键事件。其中，电源键的事件会被系统识别为 `KeyEvent.KEYCODE_POWER`。

- **`interceptKeyBeforeQueueing`**： 这个方法是在按键事件加入事件队列之前调用的，主要用于决定事件是否应该被进一步处理，或者应该被丢弃。
- **`interceptKeyBeforeDispatching`**： 这个方法是在事件派发给窗口之前调用的，在这里可以处理具体的按键逻辑。对于电源键，系统在这个阶段会根据按键状态（按下或松开）进行特定操作。

**2.按下电源键**

当电源键被按下时，`PhoneWindowManager` 首先会捕获到 `KeyEvent.ACTION_DOWN` 事件。根据系统当前的状态，可能会触发以下几种不同的操作：

- **屏幕关闭（锁屏）**：如果电源键按下时间较短，系统会触发屏幕熄灭和锁屏操作，调用 `goToSleep()`。
- **唤醒屏幕**：如果屏幕处于关闭状态，按下电源键会唤醒屏幕并点亮显示器。
- **长按电源键**：如果用户长按电源键，系统会启动电源菜单（Power Menu），用于显示重启、关机等选项。

**3.松开电源键**

当电源键被松开时，系统会捕获到 `KeyEvent.ACTION_UP` 事件。如果之前的按键被识别为短按，则不会触发长按逻辑；相反，如果长按时会弹出电源菜单。

**4.电源键的特殊处理**

在某些特定情况下，电源键还会触发其他行为，如：

- **快速双击电源键**：启动相机或某些快捷操作。
- **电源键+音量键组合**：用于截屏等功能。

这些行为通常由 `PhoneWinterceptKeyBeforeQueueingindowManager` 结合系统设置来进行配置和处理。

# interceptKeyBeforeQueueing中对于Power键的处理

按键动作切割：

- 按下： interceptPowerKeyDown(KeyEvent event, boolean interactive)
- 释放： interceptPowerKeyUp(KeyEvent event, boolean interactive, boolean canceled)

参数含义：

- interactive：是否亮屏
- KeyEvent.FLAG_FALLBACK：不被应用处理的按键事件或一些在 键值映射中不被处理的事件(例：轨迹球事件等)。

涉及到的配置信息的相关源码路径：

(下述代码的执行过程中有对一些变量的判断，而这些值都是系统配置的，在config.xml中，因此具体执行哪个流程以当前平台配置为准)

```
frameworks/base/core/java/android/view/ViewConfiguration.java
frameworks/base/core/res/res/values/config.xml
```

## interceptPowerKeyDown

```java
  1  private void interceptPowerKeyDown(KeyEvent event, boolean interactive) {
      		// ???
  2         //FACE_UNLOCK_SUPPORT start
  3         Slog.i("FaceUnlockUtil", "interceptPowerKeyDown interactive = " + interactive);
  4         Settings.System.putInt(mContext.getContentResolver(), "faceunlock_start", 1);
  5         //FACE_UNLOCK_SUPPORT end
      
      		// 获得唤醒锁
  6         // Hold a wake lock until the power key is released.
  7         if (!mPowerKeyWakeLock.isHeld()) {
  8             mPowerKeyWakeLock.acquire();          
  9         }
 10 
     		// 取消连按超时检测
 11         // Cancel multi-press detection timeout.
 12         if (mPowerKeyPressCounter != 0) {
 13             mHandler.removeMessages(MSG_POWER_DELAYED_PRESS);
 14         }
 15 
     		
 16         // Detect user pressing the power button in panic when an application has
 17         // taken over the whole screen.
 18         boolean panic = mImmersiveModeConfirmation.onPowerKeyDown(
                    // 屏幕是否点亮
                    interactive,
                    // 用来获取当前的系统时间，可能用于判断按键按下的时间或按下的频率。
 19                 SystemClock.elapsedRealtime(), 
                    // 检查当前是否处于沉浸模式。沉浸模式会隐藏系统导航栏和状态栏，允许应用程序完全占据屏幕。
                    isImmersiveMode(mLastSystemUiFlags),
                    // 检查导航栏是否为空，意味着是否有应用占据整个屏幕。
 20                 isNavBarEmpty(mLastSystemUiFlags));
            // panic = true意味着用户可能是在全屏的应用中无法退出的紧急情况下按下电源键。例如，某些全屏应用可能让用户感觉到被"锁定"而不能正常退出，导致用户按下电源键寻求帮助。
 21         if (panic) {
                // 一旦进入恐慌模式，代码会将 mHiddenNavPanic 事件通过 mHandler.post 提交到主线程去执行。这通常是为了确保导航栏或系统界面（如状态栏）恢复显示，以便用户可以退出当前全屏应用，避免陷入无法操作的情况。
 22             mHandler.post(mHiddenNavPanic);
 23         }
 24 
 25         // Latch power key state to detect screenshot chord.
                // 条件1：亮屏
 26         if (interactive && 
                // 条件2：截屏组合键中Power键Trigger位未被设置
                !mScreenshotChordPowerKeyTriggered && 
                // 条件3：不为Fallback按键事件
                (event.getFlags() & KeyEvent.FLAG_FALLBACK) == 0) { 
     			// 标记按下power key，用于组合键截屏，具体参考下述3
 28             mScreenshotChordPowerKeyTriggered = true;                
 29             mScreenshotChordPowerKeyTime = event.getDownTime();
 30             interceptScreenshotChord();
 31         }
 32 
 33         // Stop ringing or end call if configured to do so when power is pressed.
 34         TelecomManager telecomManager = getTelecommService();
 35         boolean hungUp = false;
 36         if (telecomManager != null) {
 37             if (telecomManager.isRinging()) {
 38                 // Pressing Power while there's a ringing incoming
 39                 // call should silence the ringer.
 40                 telecomManager.silenceRinger();
 41             } else if ((mIncallPowerBehavior
 42                     & Settings.Secure.INCALL_POWER_BUTTON_BEHAVIOR_HANGUP) != 0
 43                     && telecomManager.isInCall() && interactive) {
 44                 // Otherwise, if "Power button ends call" is enabled,
 45                 // the Power button will hang up any current active call.
 46                 hungUp = telecomManager.endCall();
 47             }
 48         }
 49 
 50         GestureLauncherService gestureService = LocalServices.getService(
 51                 GestureLauncherService.class);
 52         boolean gesturedServiceIntercepted = false;
 53         if (gestureService != null) {
                // gesturedServiceIntercepted 是一个标志变量，用来指示手势服务是否拦截了电源键的按下事件。默认值设为 false，表示事件尚未被拦截。
 54             gesturedServiceIntercepted = gestureService.interceptPowerKeyDown(event, interactive,
 55                     mTmpBoolean);
                // 在设备即将进入睡眠状态时，用户的手势（如快速双击电源键启动相机）触发了相机启动操作。
 56             if (mTmpBoolean.value && mRequestedOrGoingToSleep) {
 57                 mCameraGestureTriggeredDuringGoingToSleep = true;
 58             }
 59         }
 60 
 61         // Inform the StatusBar; but do not allow it to consume the event.
 62         sendSystemKeyToStatusBarAsync(event.getKeyCode());     //
 63 
 64         // If the power key has still not yet been handled, then detect short
 65         // press, long press, or multi press and decide what to do.
 66         mPowerKeyHandled = hungUp || mScreenshotChordVolumeDownKeyTriggered
 67                 || mA11yShortcutChordVolumeUpKeyTriggered || gesturedServiceIntercepted;
 68         if (!mPowerKeyHandled) {
 69             if (interactive) {   // 亮屏
 70                 // When interactive, we're already awake.
 71                 // Wait for a long press or for the button to be released to decide what to do.
 72                 if (hasLongPressOnPowerBehavior()) { //长按----判断是否为弹出操作界面的逻辑
 73                     Message msg = mHandler.obtainMessage(MSG_POWER_LONG_PRESS);
 74                     msg.setAsynchronous(true);
 75                     mHandler.sendMessageDelayed(msg,
 76                             ViewConfiguration.get(mContext).getDeviceGlobalActionKeyTimeout());  //500ms
 77                 }
 78             } else {
 79                 wakeUpFromPowerKey(event.getDownTime());     //唤醒屏幕---......
 80 
 81                 if (mSupportLongPressPowerWhenNonInteractive && hasLongPressOnPowerBehavior()) { //当前配置mSupportLongPressPowerWhenNonInteractive=false
 82                     Message msg = mHandler.obtainMessage(MSG_POWER_LONG_PRESS);
 83                     msg.setAsynchronous(true);
 84                     mHandler.sendMessageDelayed(msg,
 85                             ViewConfiguration.get(mContext).getDeviceGlobalActionKeyTimeout());
 86                     mBeganFromNonInteractive = true;
 87                 } else {
 88                     final int maxCount = getMaxMultiPressPowerCount();   //当前配置不支持config.xml
 89 
 90                     if (maxCount <= 1) {
 91                         mPowerKeyHandled = true;      //执行此处#
 92                     } else {
 93                         mBeganFromNonInteractive = true;
 94                     }
 95                 }
 96             }
 97         }
 98     }
 99 
100 ......
101 
102     private int getResolvedLongPressOnPowerBehavior() {
103         if (FactoryTest.isLongPressOnPowerOffEnabled()) { //默认false,
104             return LONG_PRESS_POWER_SHUT_OFF_NO_CONFIRM;    //长按Power,直接关机；对应属性：factory.long_press_power_off
105         }
106         return mLongPressOnPowerBehavior;
107     }
108 
109     private boolean hasLongPressOnPowerBehavior() {
110         return getResolvedLongPressOnPowerBehavior() != LONG_PRESS_POWER_NOTHING;
111     }
```

### (1) 亮屏

hasLongPressOnPowerBehavior()---mHandler发送消息(500ms)--powerLongPress() ------>getResolvedLongPressOnPowerBehavior()根据获取的值来 执行相应的流程：　　　　

- LONG_PRESS_POWER_GLOBAL_ACTIONS：弹出操作界面---->showGlobalActionsInternal()--->sendCloseSystemWindows(String reason) /mGlobalActions.showDialog()---->PhoneWindow.sendCloseSystemWindows(mContext, reason)....
- LONG_PRESS_POWER_SHUT_OFF/LONG_PRESS_POWER_SHUT_OFF_NO_CONFIRM：直接关机，相当于点击上述弹框中的关机操作。此处可结合源码查看： 对应属性：factory.long_press_power_off 使用命令：adb shell getprop/setprop...即可测试效果。

### (2) 灭屏

wakeUpFromPowerKey()---->wakeUp()---- >mPowerManager.wakeUp()....调用PowerManagerService唤醒屏幕.

```java
 1     private void wakeUpFromPowerKey(long eventTime) {
 2         wakeUp(eventTime, mAllowTheaterModeWakeFromPowerKey, "android.policy:POWER");
 3     }
 4 
 5     private boolean wakeUp(long wakeTime, boolean wakeInTheaterMode, String reason) {
 6         ......
10         final boolean theaterModeEnabled = isTheaterModeEnabled();
11         if (!wakeInTheaterMode && theaterModeEnabled) {
12             return false;
13         }
14 
15         // Settings.Global.THEATER_MODE_ON：
16         if (theaterModeEnabled) {
17             Settings.Global.putInt(mContext.getContentResolver(),
18                     Settings.Global.THEATER_MODE_ON, 0);
19         }
20 
21         mPowerManager.wakeUp(wakeTime, reason);
22         return true;
23     }
```

## interceptPowerKeyUp

```java
 1 private void interceptPowerKeyUp(KeyEvent event, boolean interactive, boolean canceled) {
 2         final boolean handled = canceled || mPowerKeyHandled;  
 3         mScreenshotChordPowerKeyTriggered = false;
 4         cancelPendingScreenshotChordAction();
 5         cancelPendingPowerKeyAction();   //取消长按事件---即500ms内未监听到释放，才执行长按事件
 6 
 7         if (!handled) { //亮屏 短按Power释放时执行此处##  因mPowerKeyHandled=false
 8             // Figure out how to handle the key now that it has been released.
 9             mPowerKeyPressCounter += 1;
10 
11             final int maxCount = getMaxMultiPressPowerCount();  //maxCount=1
12             final long eventTime = event.getDownTime();
13             if (mPowerKeyPressCounter < maxCount) {  //不成立
14                 // This could be a multi-press.  Wait a little bit longer to confirm.
15                 // Continue holding the wake lock.
16                 Message msg = mHandler.obtainMessage(MSG_POWER_DELAYED_PRESS,
17                         interactive ? 1 : 0, mPowerKeyPressCounter, eventTime);
18                 msg.setAsynchronous(true);
19                 mHandler.sendMessageDelayed(msg, ViewConfiguration.getMultiPressTimeout());
20                 return;
21             }
22 
23             // No other actions.  Handle it immediately.
24             powerPress(eventTime, interactive, mPowerKeyPressCounter);    //mPowerKeyPressCounter=1
25         }
26 
27         // Done.  Reset our state.
28         finishPowerKeyPress();   
29     }
30 
31     private void finishPowerKeyPress() {
32         mBeganFromNonInteractive = false;
33         mPowerKeyPressCounter = 0;
34         if (mPowerKeyWakeLock.isHeld()) {
35             mPowerKeyWakeLock.release();    //释放down事件时获得的锁
36         }
37     }
38 ......
39 
40     private void powerPress(long eventTime, boolean interactive, int count) {
41         if (mScreenOnEarly && !mScreenOnFully) {
42             Slog.i(TAG, "Suppressed redundant power key press while "
43                     + "already in the process of turning the screen on.");
44             return;
45         }
46 
47         if (count == 2) {
48             powerMultiPressAction(eventTime, interactive, mDoublePressOnPowerBehavior);
49         } else if (count == 3) {
50             powerMultiPressAction(eventTime, interactive, mTriplePressOnPowerBehavior);
51         } else if (interactive && !mBeganFromNonInteractive) {   //  mBeganFromNonInteractive=false
52             switch (mShortPressOnPowerBehavior) {  //mShortPressOnPowerBehavior : 配置为1
53                 case SHORT_PRESS_POWER_NOTHING:
54                     break;
55                 case SHORT_PRESS_POWER_GO_TO_SLEEP: //执行#
56                     goToSleep(eventTime, PowerManager.GO_TO_SLEEP_REASON_POWER_BUTTON, 0);
57                     break;
58       　　　　.......
59       }
60 } 65  
```

### (1) 亮屏

powerPress()--->goToSleep()--- >mPowerManager.goToSleep()...调用PowerManagerService 使系统睡眠。

### (2) 灭屏

finishPowerKeyPress()...

## 组合键（Power + 音量减）：功能就是我们常用的**屏幕截图**的快捷方式。

```java
  1     @Override
  2     public int interceptKeyBeforeQueueing(KeyEvent event, int policyFlags) {
  3         if (!mSystemBooted) {
  4             // If we have not yet booted, don't let key events do anything.
  5             return 0;
  6         }
  7         
  8         ......//代码略
  9         final int keyCode = event.getKeyCode();
 10         // Basic policy based on interactive state.
 11         int result;
 12         
 13         // Handle special keys.
 14         switch (keyCode) {
 15             ......
 16             case KeyEvent.KEYCODE_VOLUME_MUTE: {
 17                 if (keyCode == KeyEvent.KEYCODE_VOLUME_DOWN) {   //音量键减-     【Power + VOLUME_DOWN】截屏操作
 18                     if (down) {
 19                         if (interactive && !mScreenshotChordVolumeDownKeyTriggered
 20                                 && (event.getFlags() & KeyEvent.FLAG_FALLBACK) == 0) {
 21                             mScreenshotChordVolumeDownKeyTriggered = true;
 22                             mScreenshotChordVolumeDownKeyTime = event.getDownTime();
 23                             mScreenshotChordVolumeDownKeyConsumed = false;
 24                             cancelPendingPowerKeyAction();
 25                             interceptScreenshotChord();
 26                             interceptAccessibilityShortcutChord();
 27                         }
 28                     } else {
 29                         mScreenshotChordVolumeDownKeyTriggered = false;
 30                         cancelPendingScreenshotChordAction();
 31                         cancelPendingAccessibilityShortcutAction();
 32                     }
 33                 } else if(...){
 34                     ......
 35                 }
 36                 ......
 37                 break;    
 38             }
 39             case KeyEvent.KEYCODE_POWER: {      //POWER 键
 40                 if(SystemProperties.getBoolean("sys.requireKey", false)) break;
 41                 // Any activity on the power button stops the accessibility shortcut
 42                 cancelPendingAccessibilityShortcutAction();
 43                 result &= ~ACTION_PASS_TO_USER;        //不分发按键至应用
 44                 isWakeKey = false; // wake-up will be handled separately
 45                 if (down) {
 46                     interceptPowerKeyDown(event, interactive);   //在上述1中interceptPowerKeyDown()的第28行可见标记mScreenshotChordPowerKeyTriggered = true;
 47                 } else {
 48                     interceptPowerKeyUp(event, interactive, canceled);
 49                 }
 50                 break;
 51             }
 52             ......
 53         }
 54         
 55         ......
 56         return result;    
 57     }
 58     
 59     // 截屏
 60     private void interceptScreenshotChord() {
 61         if (mScreenshotChordEnabled
 62                 && mScreenshotChordVolumeDownKeyTriggered && mScreenshotChordPowerKeyTriggered    //同时按下Volum_down + Power, 后执行的该方法
 63                 && !mA11yShortcutChordVolumeUpKeyTriggered) {
 64             final long now = SystemClock.uptimeMillis();
 65             if (now <= mScreenshotChordVolumeDownKeyTime + SCREENSHOT_CHORD_DEBOUNCE_DELAY_MILLIS
 66                     && now <= mScreenshotChordPowerKeyTime
 67                             + SCREENSHOT_CHORD_DEBOUNCE_DELAY_MILLIS) {   //150ms
 68                 mScreenshotChordVolumeDownKeyConsumed = true;
 69                 cancelPendingPowerKeyAction();
 70                 mScreenshotRunnable.setScreenshotType(TAKE_SCREENSHOT_FULLSCREEN);
                    // 根据是否在锁屏界面设置不同的延迟时间，了解即可
 71                 mHandler.postDelayed(mScreenshotRunnable, getScreenshotChordLongPressDelay());   
 72             }
 73         }
 74     }
 75     
 76     private class ScreenshotRunnable implements Runnable {
 77         private int mScreenshotType = TAKE_SCREENSHOT_FULLSCREEN;
 78 
 79         public void setScreenshotType(int screenshotType) {
 80             mScreenshotType = screenshotType;
 81         }
 82 
 83         @Override
 84         public void run() {
 85             takeScreenshot(mScreenshotType); //#
 86         }
 87     }
 88     
 89     private static final String SYSUI_PACKAGE = "com.android.systemui";
 90     private static final String SYSUI_SCREENSHOT_SERVICE =
 91             "com.android.systemui.screenshot.TakeScreenshotService";
 92     
 93     private void takeScreenshot(final int screenshotType) {
 94         synchronized (mScreenshotLock) {
 95             if (mScreenshotConnection != null) {
 96                 return;
 97             }
 98             final ComponentName serviceComponent = new ComponentName(SYSUI_PACKAGE,
 99                     SYSUI_SCREENSHOT_SERVICE);  //SystemUI中的截屏服务
100             final Intent serviceIntent = new Intent();
101             serviceIntent.setComponent(serviceComponent);
102             ServiceConnection conn = new ServiceConnection() {
103                 @Override
104                 public void onServiceConnected(ComponentName name, IBinder service) {
105                     synchronized (mScreenshotLock) {
106                         if (mScreenshotConnection != this) {
107                             return;
108                         }
109                         Messenger messenger = new Messenger(service);
110                         Message msg = Message.obtain(null, screenshotType);
111                         final ServiceConnection myConn = this;
112                         Handler h = new Handler(mHandler.getLooper()) {
113                             @Override
114                             public void handleMessage(Message msg) {
115                                 synchronized (mScreenshotLock) {
116                                     if (mScreenshotConnection == myConn) {
117                                         mContext.unbindService(mScreenshotConnection);
118                                         mScreenshotConnection = null;
119                                         mHandler.removeCallbacks(mScreenshotTimeout);
120                                     }
121                                 }
122                             }
123                         };
124                         msg.replyTo = new Messenger(h);
125                         msg.arg1 = msg.arg2 = 0;
126                         if (mStatusBar != null && mStatusBar.isVisibleLw())
127                             msg.arg1 = 1;
128                         if (mNavigationBar != null && mNavigationBar.isVisibleLw())
129                             msg.arg2 = 1;
130                         try {
131                             messenger.send(msg);
132                         } catch (RemoteException e) {
133                         }
134                     }
135                 }
136 
137                 @Override
138                 public void onServiceDisconnected(ComponentName name) {
139                     synchronized (mScreenshotLock) {
140                         if (mScreenshotConnection != null) {
141                             mContext.unbindService(mScreenshotConnection);
142                             mScreenshotConnection = null;
143                             mHandler.removeCallbacks(mScreenshotTimeout);
144                             notifyScreenshotError();
145                         }
146                     }
147                 }
148             };
149             if (mContext.bindServiceAsUser(serviceIntent, conn,
150                     Context.BIND_AUTO_CREATE | Context.BIND_FOREGROUND_SERVICE_WHILE_AWAKE,
151                     UserHandle.CURRENT)) {
152                 mScreenshotConnection = conn;
153                 mHandler.postDelayed(mScreenshotTimeout, 10000);
154             }
155         }
156     }     
```

结合上述代码，可概括流程为：

interceptScreenshotChord()：----->启动线程ScreenshotRunnable---->takeScreenshot()----可看出真正的截图操作是在SystemUI中。
