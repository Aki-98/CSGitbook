## **Android Gradle插件**

从Gradle的角度看，Android其实就是Gradle的一个第三方插件，它是由Google的Android团队开发的，Android 开发 IDE Android Studio 就采用 Gradle 构建项目。

### **Android Gradle插件分类**

1. **App应用工程**：生成可运行apk应用；插件id: **com.android.application**
2. **Library库工程**：生成AAR包给其他的App工程公用，其使用方式和jar包一样，里面有相关的 Android 资源文件；插件id: **com.android.library**
3. **Test测试工程**：对App应用工程或Library库工程进行单元测试；插件id: **com.android.test**