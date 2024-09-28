# Service在清单文件中的声明

前面说过Service分为启动状态和绑定状态两种，但无论哪种具体的Service启动类型，都是通过继承Service基类自定义而来，也都需要在AndroidManifest.xml中声明，那么在分析这两种状态之前，我们先来了解一下Service在AndroidManifest.xml中的声明语法，其格式如下：

```xml
<service android:enabled=["true" | "false"]
    android:exported=["true" | "false"]
    android:icon="drawable resource"
    android:isolatedProcess=["true" | "false"]
    android:label="string resource"
    android:name="string"
    android:permission="string"
    android:process="string" >
    . . .
</service>
```

- android:exported：代表是否能被其他应用隐式调用，其默认值是由service中有无intent-filter决定的，如果有intent-filter，默认值为true，否则为false。为false的情况下，即使有intent-filter匹配，也无法打开，即无法被其他应用隐式调用。
- android:name：对应Service类名
- android:permission：是权限声明
- android:process：是否需要在单独的进程中运行,当设置
  - android:process=”:remote”时，代表Service在单独的进程中运行。注意“：”很重要，它的意思是指要在当前进程名称前面附加上当前的包名，所以“remote”和”:remote”不是同一个意思，前者的进程名称为：remote，而后者的进程名称为：App-packageName:remote。

- android:isolatedProcess ：设置 true 意味着，服务会在一个特殊的进程下运行，这个进程与系统其他进程分开且没有自己的权限。与其通信的唯一途径是通过服务的API(bind and start)。
- android:enabled：是否可以被系统实例化，默认为 true因为父标签 也有 enable 属性，所以必须两个都为默认值 true 的情况下服务才会被激活，否则不会激活。