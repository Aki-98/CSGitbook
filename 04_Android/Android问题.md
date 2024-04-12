

# ContentProvider实现原理

# 介绍Binder机制

# 匿名共享内存，使用场景

# 如何自定义View，如果要实现一个转盘圆形的View，需要重写View中的哪些方法？(onLayout,onMeasure,onDraw)



# Socket和LocalSocket



# Android里跨进程传递数据的几种方案。

1.Bundle，在安卓中不同的应用运行在不同的进程中。通过Intent启动其他应用的组件Activity、Service、Receiver时，可以将数据存储在Bundle中，然后设置在Intent中。

2.系统文件，如SP。

3.ContentProvidert提供数据分享的接口：ContentResolver

4.跨进程Messenger

6.AIDL

# TextView怎么改变局部颜色

SpannableString、HTML

# Android中Handler声明非静态对象会发出警告，为什么，非得是静态的？(Memory Leak)

# 广播注册后不解除注册会有什么问题？(内存泄露)

# 属性动画(Property Animation)和补间动画(Tween Animation)的区别，为什么在3.0之后引入属性动画([官方解释：调用简单](http://android-developers.blogspot.com/2011/05/introducing-viewpropertyanimator.html))

# Android里的LRU算法原理

# BrocastReceive里面可不可以执行耗时操作?

# Service onBindService 和startService 启动的区别