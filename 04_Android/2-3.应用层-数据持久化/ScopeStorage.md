# 1.强制启用ScopedStorage

Android 11中，Scoped Storage被强制启用了。

Android 10中虽然也有Scoped Storage功能，但没有强制启用。

只要应用程序指定的targetSdkVersion低于29，或targetSdkVersion等于29，但在AndroidManifest.xml中加入了如下配置：

```xml
<manifest ... >
  <application android:requestLegacyExternalStorage="true" ...>
    ...
  </application>
</manifest>
```


那么Scoped Storage功能就不会被启用。

在Android 11中以上配置依然有效，但仅限于targetSdkVersion小于或等于29的情况。如果你的targetSdkVersion等于30，Scoped Storage就会被强制启用，requestLegacyExternalStorage标记将会被忽略。

# 2.管理设备上所有的文件

在Android 11中，如果你想要管理整个设备上的文件，也需要使用类似的技术。

首先，你必须在AndroidManifest.xml中声明MANAGE_EXTERNAL_STORAGE权限，如下所示：

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.example.scopedstoragedemo">

    <uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"
        tools:ignore="ScopedStorage" />

</manifest>
```

# 3.Batch operations

每个应用程序都有权限向MediaStore贡献数据，比如说插入一张图片到手机相册当中。也有权限读取其他应用程序所贡献的数据，比如说获取手机相册中的所有图片，但限制了写入其他应用程序所贡献数据的权限。

Batch operations，允许我们可以一次性对多个文件的操作权限进行申请。

- createWriteRequest() 用于请求对多个文件的写入权限。
- createFavoriteRequest() 用于请求将多个文件加入到Favorite（收藏）的权限。
- createTrashRequest() 用于请求将多个文件移至回收站的权限。
- createDeleteRequest() 用于请求将多个文件删除的权限。