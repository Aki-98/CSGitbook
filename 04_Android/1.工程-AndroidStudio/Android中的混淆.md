refs:：https://blog.csdn.net/weixin_42602900/article/details/127671586



### 混淆的机制：

1. **代码压缩（Shrinking）**：删除未被引用的类、字段、方法和属性，减少 APK 文件大小。
2. **优化（Optimization）**：对字节码进行优化，以减少运行时的开销。
3. **混淆（Obfuscation）**：重命名类、方法和字段名称为无意义的名称，增加反编译的难度。

### 主要作用：

1. **提高安全性**：通过混淆代码，可以减少因反编译而泄露代码逻辑和关键信息的风险。
2. **减小 APK 大小**：通过代码压缩，可以减少未被使用的代码和资源，从而减小应用程序的体积。
3. **优化执行速度**：通过优化字节码，可以提高应用程序的执行速度。

### 混淆的配置：

要在 Android 项目中使用混淆，通常需要在 `build.gradle` 文件中进行配置。以下是一个基本的混淆配置示例：

```groovy
groovyCopy codeandroid {
    ...
    buildTypes {
        release {
            minifyEnabled true   //开启混淆
            zipAlignEnabled true  //压缩优化
            shrinkResources true  //移除无用资源
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro' //默认的混淆文件以及我们指定的混淆文件
        }
    }
}
```

在上述配置中：

- `minifyEnabled true`：启用代码压缩和混淆。
- `proguardFiles`：指定 ProGuard 配置文件。`'proguard-android-optimize.txt'` 是一个 Android 提供的默认配置文件，而 `'proguard-rules.pro'` 是自定义的 ProGuard 配置文件，用于指定特定的混淆规则。

### 混淆规则（proguard-rules.pro）：

在 `proguard-rules.pro` 文件中，您可以自定义混淆规则，如下所示：

```
proCopy code# 保留特定的类或方法不被混淆
-keep class com.example.MyClass { *; }

# 保留特定的类中的方法不被混淆
-keepclassmembers class com.example.MyClass {
    public <init>(...);
    public void myMethod(...);
}

# 保留特定的类或方法不被删除
-keep class com.example.MyClass
-keepclassmembers class com.example.MyClass {
    *;
}
```

编写语法：

- -keep    防止类和成员被移除或者被重命名
- -keepnames    防止类和成员被重命名
- -keepclassmembers    防止成员被移除或者被重命名
- -keepclasseswithmembers    防止拥有该成员的类和成员被移除或者被重命名
- -keepclasseswithmembernames    防止拥有该成员的类和成员被重命名

### 注意事项：

1. **保留入口点（Main Entry Points）**：确保应用程序的主要入口点（如 `Activity`、`Service`、`BroadcastReceiver` 和 `ContentProvider`）不被混淆。
2. **避免不必要的混淆**：避免对与 Android 框架相关的类进行混淆，以免影响应用程序的正常运行。
3. **调试**：在进行混淆后，建议在真实设备上进行充分的测试，以确保应用程序的功能和性能没有受到影响。

通过合理配置和使用混淆，可以有效提高 Android 应用程序的安全性和性能。

