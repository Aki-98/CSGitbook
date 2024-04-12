# pm

【清空缓存】

```shell
adb shell pm clear <package_name>
```



【完全删除某一系统应用】

```shell
adb root
adb shell pm uninstall -k --user 0 <package_name>
```



【查询应用安装路径】

```shell
adb shell pm path <package name>
```



【查看所有已安装的app包名】

```
adb shell pm list packages
```



【查看自己安装的app包名】

```
adb shell pm list packages -3
```



# am

【强制停止】

```shell
adb shell am force-stop <package_name>
```



# dumpsys

【查看版本号】

```shell
adb shell dumpsys package <package_name> | grep "version"
```



【查看Activities信息】

```
adb shell dumpsys activity activities
```



# logcat

【输出日志】

 ```shell
 adb logcat -s com.sony.dtv.searchapp > 1.txt
 adb logcat -time > <file-location>
 ```



# screencap

【截屏】

```
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png
```



# mount/remount

【更改系统文件权限】

```shell
adb shell mount -rw -o remount /
adb shell mount -o rw,remount /
adb remount
```

【remount】

adb remount将 /system部分置于可写入的模式，默认情况下 /system 部分是只读模式的。这个命令只适用于已被 root 的设备。
在将文件 push 到 /system 文件夹之前，必须先输入命令 adb remount。
adb remount 的作用相当于 adb shell mount -o rw,remount,rw /system。

```bash
adb remount
```



# 其他

【根据包名查找应用路径/查看应用大小】

进入adb shell 之后 

1. 拿path

```shell
adb shell dumpsys package <package_name> | grep path
```

输出：

```
...
  path: /data/app/~~TEGS7xtZ4eH-bLK3sKfKwA==/com.sony.dtv.searchapp-xqyu1EsYldLgqQNvokbJ1A==/base.apk
```

2. du -h 粘贴path

```shell
adb shell du -h /data/app/~~TEGS7xtZ4eH-bLK3sKfKwA==/com.sony.dtv.searchapp-xqyu1EsYldLgqQNvokbJ1A==/base.apk
```

输出：

```shell
98M   /data/app/~~TEGS7xtZ4eH-bLK3sKfKwA==/com.sony.dtv.searchapp-xqyu1EsYldLgqQNvokbJ1A==/base.apk
```



【查看前5进程cpu占用%】

```
adb shell top -m 5 -d 1
```



【查看设备Android版本】

```
adb shell getprop ro.build.version.sdk
```



【注入按键】

```
adb shell input keyevent 219(219是语音键)
```



【查看设备的cpu架构】

```
adb shell getprop ro.product.cpu.abi
```



【查看platform版本号】

```
adb shell getprop ro.build.version.release
```



【查看api版本号】

```
adb shell getprop ro.build.version.sdk
```



【获取设备名称】

```
adb root
adb shell
cat /system/build.prop
```



【全局查找文件】

https://blog.csdn.net/chouzhou9701/article/details/119395831

```
> adb shell
# cd data/local/tmp
# ./busybox find 目录 -name "文件名"
# ./busybox find / -name "*.txt"
```



【查看KernelLog】

```shell
adb shell dmesg
```



