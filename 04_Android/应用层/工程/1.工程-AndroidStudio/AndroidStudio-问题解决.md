# 没有配置ndk的项目找不到ndk路径

This is a Gradle bug that is documented here:
https://code.google.com/p/android/issues/detail?id=228424

 

The problem is that Gradle is computing the location of an NDK folder by just tacking on the string "/ndk-bundle" to the SDK folder location, even if you have never installed the NDK.

After establishing this false expectation of an NDK folder existing in a particular location, each time you build, Gradle gives you a warning that you're "missing" that folder. 

 

The solution was the following:

    1. Open project in Android Studio
    2. Wait for sync to finish
    3. Click on File -> Project structure -> SDK Location
    4. At Android NDK Location, if you don't have any NDK, install one
    5. Select an existing NDK location.

That should fix it.



# Entry name 'assets/agent_channel.ini' collided



更改apk生成的路径，举个栗子，Android studio 打包默认路径是这样的：

![img](AndroidStudio-问题解决_imgs\4VyUOE6PC1L.png)

等待你的就是`Entry name 'res/layout/test_toolbar.xml' collided`

解决办法，更改生成apk的路径，如

![img](AndroidStudio-问题解决_imgs\eeRB8A4i6bp.png)

# Entry name *.xml collided 解决

https://blog.csdn.net/luo_boke/article/details/106113266

总结：更改打包生成路径

# Current JDK version 1.8.0_341-b10 has a bug

 (https://bugs.openjdk.java.net/browse/JDK-8007720) that prevents Room from being incremental. 

https://stackoverflow.com/questions/58822538/current-jdk-version-1-8-has-a-bug-that-prevents-room-from-being-incremental

# The specified Gradle installation directory does not exist error...

https://stackoverflow.com/questions/71452170/the-specified-gradle-installation-directory-does-not-exist-error-after-android-s

![image-20230403145156197](AndroidStudio-问题解决_imgs\tQ7aI5Xxs7z.png)

选择'gradle-wrapper.properties' file

# output中文乱码问题

https://blog.csdn.net/jankingmeaning/article/details/104772104

# 自定义Todo

https://www.cnblogs.com/bellkosmos/p/AndroidStudio_custom_TODO.html#:~:text=AndroidStudio%E8%87%AA%E5%AE%9A%E4%B9%89TODO%20-%20%E8%B5%9B%E8%89%87%E9%98%9F%E9%95%BF%20-%20%E5%8D%9A%E5%AE%A2%E5%9B%AD%201.%E5%A2%9E%E5%8A%A0%E8%87%AA%E5%AE%9A%E4%B9%89TODO%E6%A0%87%E8%AE%B0%20Preferences,-%3E%20Editor%20-%3E%20TODO%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%8A%A0%E5%8F%B7%EF%BC%8C%E8%BE%93%E5%85%A5%E6%83%B3%E8%A6%81%E8%87%AA%E5%AE%9A%E4%B9%89%E7%9A%84TODO%E7%9A%84%E6%AD%A3%E5%88%99%20%E8%BE%93%E5%85%A5%20bXb.%2A%20%EF%BC%88X%E4%B8%BATODO%E6%A0%87%E7%AD%BE%E7%9A%84%E5%90%8D%E5%AD%97%EF%BC%89%EF%BC%8C%E8%BF%99%E9%87%8C%E4%BB%A5to_complete%E4%B8%BA%E4%BE%8B%EF%BC%8C%E8%BE%93%E5%85%A5%20bto_completeb.%2A

# Cmd下启动使用模拟器

cmd下启动使用模拟器

![image-20220227205156214](AndroidStudio-问题解决_imgs\gCMtxWtkUNI.png)

# 先运行一次程序才能找到R文件

![image-20220227205228484](AndroidStudio-问题解决_imgs\aMYdGBTLjeJ.png)

![image-20220227205241703](AndroidStudio-问题解决_imgs\0de8hTTcn4G.png)

# **修改工程名称及修改包名**

https://blog.csdn.net/u012693479/article/details/107233954

# **查找库**

File > Project Structure

![image-20220301163145537](AndroidStudio-问题解决_imgs\x253FHchZ2S.png)

然后就可以搜索了

![image-20220301163227009](AndroidStudio-问题解决_imgs\5tIMJ8EFGmF.png)

# **将本机文件导入到手机**

![image-20220307112518415](AndroidStudio-问题解决_imgs\iV08dwuJ8Bi.png)

# **打开模块设置**

![image-20220321101803316](AndroidStudio-问题解决_imgs\0zo6aXwUrR9.png)

![image-20220321102422691](AndroidStudio-问题解决_imgs\L6voYx9nDcX.png)

# **Gradle SDK Java AndroidStudio的历史版本查看下载**

https://www.jianshu.com/p/f7eca878b8d7

# **Rebuild Project命令包含Clean Project命令**

# 查看apk签名

进入SDK/build_tools/<sdk_version>/目录下使用apksigner

```shell
apksigner verify -v <apk-file>
```

![image-20230327161548042](AndroidStudio-问题解决_imgs\2HBred7gCDI.png)

