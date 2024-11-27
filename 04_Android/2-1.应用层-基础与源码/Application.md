# Application

**作用**

Application对象全局可访问，且全程陪同应用进程。所以特别适合完成以下任务:

共享全局状态

初始化全应用所需的服务

**回调函数**

Application对象由Android系统管理，它的回调函数都运行于U线程。

onCreate

onConfigurationChanged

比如语言变更和屏幕方向改变

onLowMemory

Application对象vs.静态单例

静态单例模块化程度更好

Application就是一个context，所以有访问资源的能力>静态单例可以接受context参数

Application对象能接收系统回调，自动知悉系统环境变化> Application对象的生命周期由系统控制

如果单例能实现需求就用单例