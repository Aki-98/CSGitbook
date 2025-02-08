# Framework

**检查 SystemServer 是否有异常**

观察 `SystemServer` 是否有异常日志

```
adb logcat -b system
```



# Wifi

**检查 Wi-Fi 状态**

查看当前 Wi-Fi 连接的频率是否正常

```
adb shell dumpsys wifi | grep 'frequency'
```

进一步观察 `WifiScoringParams` 相关的日志。

```
adb logcat -b main -s WifiScoringParams`
```



**查看 Wi-Fi 驱动日志**

查看是否有 Wi-Fi 适配器初始化失败的日志。

```
adb logcat | grep wifi
adb logcat -b radio
```



# Memory

**检查 `lowmemorykiller` 是否触发**

如果 `lowmemorykiller` 触发，说明系统内存紧张，可能导致进程被杀掉。

```
adb shell dmesg | grep -i "lowmemorykiller"
adb shell logcat -d | grep "lowmemorykiller"
```



**检查 `oom_score` 及内存使用**

如果某个进程的 `oom_score` 很高，说明它是内存紧张时的优先清理目标。

```
adb shell cat /proc/meminfo
adb shell cat /proc/<pid>/oom_score
adb shell dumpsys meminfo
```



**检查 GPU 显存分配情况**

可以看到 `gralloc` (显存分配器) 的使用情况，是否有异常增长。

```
adb shell dumpsys meminfo | grep -i "gralloc"
adb shell dumpsys SurfaceFlinger
```



**检查是否有 OOM 事件**

```shell
adb shell dmesg | grep -i "oom"
adb logcat -d | grep "lowmemorykiller"
```



**检查 GPU 负载情况**

```shell
adb shell dumpsys gfxinfo
```



# Others

**检查温度相关日志**

如果设备因为温度过高进入保护模式，也可能触发 **安全关闭**。

```shell
adb shell dmesg | grep -i "thermal"
```