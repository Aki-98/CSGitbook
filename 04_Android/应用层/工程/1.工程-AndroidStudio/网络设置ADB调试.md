## 1. 安卓的adb调试模式有两种：

- 使用usb线
- 使用网络

## 2. 使用网络adb模式：

- 安卓设备跟电脑需处于同一局域网内，可以使用有线网的方式
- 让电脑跟安卓设备连接在同一wifi路由下，亦可通过电脑创建wifi热点让安卓设备连接都可以

## 3. 设置网络adb的监听端口，设置的方法有以下几种：

- 方法一：先是使用usb线连接电脑跟安卓设备，打开电脑的cmd窗口，输入命令：adb tcpip 5555 ；该条命令是设置网络adb监听的端口，5555是默认，也可以设置成其它的。
- 方法二：该种方法是在系统有root权限下才能使用，依次输入命令：adb shell su -c setprop service.adb.tcp.port 5555
- 方法三：该种方法是在系统有root权限下才能使用，使用文件管理器按照以下路径打开文件：/system/build.prop，在该文件的最后添加以下内容：service.adb.tcp.port=5555

> 方法一在安卓设备重启后会失效，需重新设置才行 方法二、三在重启后依然有效，但是该两种方法需在系统有root权限下才能做修改 一、二需先使用usb模式连接电脑设置，三不需要连接电脑

## 4. 在设置好端口后就可输入命令连接：

| `1 ` | `adb connect 192.168.1.1:5555` |
| ---- | ------------------------------ |
|      |                                |

> 其中192.168.1.1是安卓设备的ip地址，如果设置的端口号是默认的5555，后面的：5555可以不用输入

## 5. 断开连接的命令：

| `1 ` | `adb disconnect 192.168.1.1` |
| ---- | ---------------------------- |
|      |                              |

## 6. 如图的第一个adb devices,是使用usb线连接设置调试端口号

![img](网络设置ADB调试_imgs\0oGolOB2yUt.png)

## 7. 在使用adb tcpip 5555设置好调试端口号，使用adb connect 192.168.1.5连接安卓屏，连接成功会显示下面的conenct to xxx.xxx.x.xxx:5555

> 注意：在connect成功后如果kill掉adb.exe后重新打开需要重新使用命令adb connect 192.168.1.1进行连接