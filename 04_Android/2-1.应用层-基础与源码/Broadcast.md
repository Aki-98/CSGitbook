阅读：

https://blog.csdn.net/qq_43667625/article/details/109704482



广播分类：

- 标准广播：会被所有接收器同时接收到。
- 有序广播：先被优先级高的接收器接收到，响应完成后再传递给之后的广播，如果中途被接收器截断，后续的接收器就无法接收到广播。



广播接收器的注册：

- 静态注册：在AndroidManifest中注册，消耗更多资源，开机广播需要使用静态注册。
  - 有些比较消耗资源的广播是无法静态注册的
    - //屏幕亮起
      android.intent.action.SCREEN_ON
      //屏幕熄灭
      android.intent.action.SCREEN_OFF
      //电量变化
      android.intent.action.BATTERY_CHANGED
      //屏幕方向，设备信息发生改变
      android.intent.action.CONFIGURATION_CHANGED
      //时间改变（每分钟发送一次）
      android.intent.action.TIME_TICK

```xml
//加在application标签中间
<receiver
          android:name=".broadcastreceiver.aReceiver"
          android:enabled="true"
          android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>	
```

- 动态注册：在代码中注册，更加灵活。
  - 自定义广播接收器 --> 创建广播接收器并addAction --> 注册广播接收器 --> ... --> 注销广播接收器



发送广播：

- 动态注册：
  - 标准广播：直接用sendBroadcast发送intent
  - 有序广播：
    - 为接收器的intentFilter调用setPriority设置优先级
    - 使用sendOrderedBroadcast方法发送广播
    - 接收器调用abortBroadcast()可以截断广播
- 静态注册：发送广播之前需要为intent调用setPackageName指定接收的应用，使其变成显式广播（Android8.0之后，静态注册的接收器无法接收到隐式广播）



本地广播：

- 获取本地广播其实例localBroadcastManager = LocalBroadcastManager.getInstance(this);
- 注册/注销接收器



