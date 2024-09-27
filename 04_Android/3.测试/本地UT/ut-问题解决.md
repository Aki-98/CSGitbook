# 【如何获得静态内部类中定义的变量值】

```java
// 先拿到静态内部类
Class<?> screenParaClass = Class.forName("com.sony.dtv.search.commandprocessor.MediaControlWorker$ScreenPara");
// 然后用Whitebox.getInternalState获得静态内部类的成员值
assertEquals(Whitebox.getInternalState(screenParaClass, "ACTION_SCREEN"), action);
```

