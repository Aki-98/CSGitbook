参考：https://www.jianshu.com/p/0d7c44c84b9e

# 介绍

自定义屏保，当充电的设备空闲或者插入底座时显示的互动屏保。

# 使用

需要在Service中定义权限android.permission.BIND_DREAM_SERVICE

定义intent-filter\<action android:name="android.service.dreams.DreamService" />

指定的图标和标题都在这里设置

```xml
 <service
     android:name=".MyDream"
     android:exported="true"
     android:icon="@drawable/my_icon"
     android:label="@string/my_dream_label" 
     android:permission="android.permission.BIND_DREAM_SERVICE">
     <intent-filter>
         <action android:name="android.service.dreams.DreamService" />
         <category android:name="android.intent.category.DEFAULT" />
     </intent-filter>
     <!-- Point to additional information for this dream (optional) -->
     <meta-data
         android:name="android.service.dream"
         android:resource="@xml/my_dream" />
 </service>
```

如果填写了 `<meta-data>` 元素，dream的附加信息就被指定在XML文件的 `<dream>` 元素中。

通常提供的附加信息是对互动屏保的自定义设置，指向一个自己写的Activity

比如：res/xml/my_dream.xml

```xml
 <dream xmlns:android="http://schemas.android.com/apk/res/android"
     android:settingsActivity="com.example.app/.MyDreamSettingsActivity" />
```

.MyDream需要继承自DreamService，在onAttachedToWindow中设置布局

```java
package com.rust.service;

import android.service.dreams.DreamService;

import com.rust.aboutview.R;

public class MyDayDream extends DreamService {
    
    @Override
    public void onAttachedToWindow() {
        super.onAttachedToWindow();
        // Exit dream upon user touch
        setInteractive(false);
        // Hide system UI
        setFullscreen(true);
        // Set the dream layout
        setContentView(R.layout.my_day_dream);
    }

}
```

生命周期：

- onAttachedToWindow()
   初始化设置，在这里可以调用 setContentView()

- onDreamingStarted()
   互动屏保已经启动，这里可以开始播放动画或者其他操作

- onDreamingStopped()
   在停止 onDreamingStarted() 里启动的东西
- onDetachedFromWindow()
   在这里回收前面调用的资源（比如 handlers 和 listeners）

另外，onCreate 和 onDestroy 也会被调用。但要复写上面的几个方法来执行初始化和销毁操作。



在Settings-Display-Daydream中可以找到新增的选项