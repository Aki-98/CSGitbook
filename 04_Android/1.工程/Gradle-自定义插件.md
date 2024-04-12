**Gradle是什么？**

- Gradle是一个自动化构建开源工具。
- Gradle运行在JVM中，执行Gradle就相当于开启了一个Java程序。

**创建Gradle的三种方式**

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle](Gradle-自定义插件_imgs\48.png)

#  **方式一：Build script脚本方式**

```groovy
apply plugin: MyPlugin
class MyPlugin implements Plugin<Project>{
    @Override
    void apply(Project project) {
        println "this is my plugin"
    }
}
```

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_02](Gradle-自定义插件_imgs\49.png)


运行结果：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_02](Gradle-自定义插件_imgs\50.png)

# **方式二：buildSrc目录**

1、新建一个 buildSrc 文件夹

2、新建一个 build.gradle 文件，里面添加如下代码，然后点击 sync now，你就会发现 buildSrc 文件夹多了一个绿标

![Android Gradle三种自定义插件方式详解（含报错解决方案）_解决方法_04](Gradle-自定义插件_imgs\51.png)

```groovy
apply plugin: "java"
apply plugin: 'java-gradle-plugin'
```


 3、新建子目录 src/main/java ,并编写一个插件类



```groovy
import org.gradle.api.Plugin;
import org.gradle.api.Project;

public class MyPlugin implements Plugin<Project> {
    @Override
    public void apply(Project project) {
	}
}
```

4、在app下的build.gradle里面应用

![Android Gradle三种自定义插件方式详解（含报错解决方案）_java_05](Gradle-自定义插件_imgs\52.png)

运行结果展示：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_06](Gradle-自定义插件_imgs\53.png)

# 方式三：独立项目

1、新建一个独立的module，不要选错了！！！，

![Android Gradle三种自定义插件方式详解（含报错解决方案）_解决方法_07](Gradle-自定义插件_imgs\54.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_ide_08](Gradle-自定义插件_imgs\55.png)

2、在该模块下的build.gradle里添加依赖

```groovy
dependencies {
    implementation gradleApi()
}
```


可能出现的报错 Build was configured to prefer settings repositories over project repositories but repository 'Gradle Libs' was added by unknown code

解决方法：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle_10](Gradle-自定义插件_imgs\56.png)

 3、编写插件类

```groovy
package com.example.secondplugin;

import org.gradle.api.Plugin;
import org.gradle.api.Project;

public class MyClass implements Plugin<Project> {
    @Override
    public void apply(Project project) {
        System.out.println("this is third plugin");
    }
}
```

4、 编写插件配置文件

层级结构不能错

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_11](Gradle-自定义插件_imgs\57.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_java_12](Gradle-自定义插件_imgs\58.png)

5、发布插件任务代码的编写

groupId、artifactId、version根据自己实际情况来写

![Android Gradle三种自定义插件方式详解（含报错解决方案）_ide_13](Gradle-自定义插件_imgs\59.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_14](Gradle-自定义插件_imgs\60.png)

如果有小伙伴没找到task视图，解决方法如下：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_ide_15](Gradle-自定义插件_imgs\61.png)

6、点击如下按钮，发布到本地仓库

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle_16](Gradle-自定义插件_imgs\62.png)

7、使用

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle_17](Gradle-自定义插件_imgs\63.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_18](Gradle-自定义插件_imgs\64.png)

运行效果：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_19](Gradle-自定义插件_imgs\65.png)

 
