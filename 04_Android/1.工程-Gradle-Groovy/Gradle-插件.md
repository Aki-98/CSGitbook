# Gradle插件

## 插件介绍

Gradle的设计非常好，**本身提供一些基本的概念和整体核心的框架**，其他用于描述真实使用场景逻辑的都以插件扩展的方式来实现，比如构建Java应用，就通过Java插件来实现，那么自然构建Android应用，就通过Android Gradle插件来实现。

Gradle 提供了很多官方插件，**用于支持Java、Groovy等工程的构建和打包**。同时也提供了**自定义插件**机制，让每个人都可以通过插件来实现特定的构建逻辑，并可以把这些逻辑打包起来，分享给其他人。

Android Gradle插件是基于内置的Java插件实现的。Gradle插件的作用如下：

1. 可以添加任务到项目，比如**测试、编译、打包**等
2. 可以**添加依赖配置到项目**，帮助配置项目构建过程中需要的依赖，比如第三方库等
3. 可以向项目中现有的对象类型添加新的扩展属性和方法等，**帮助配置和优化构建**
4. 可以对项目进行一些约定，比如**约定源代码存放位置**等

# ?Gradle插件

通过使用插件可以扩展项目的功能，帮助我们做很多任务，比如编译、打包，Gradle 插件可以分为两类：

- 二进制插件：继承 org.gradle.api.Plugin 接口实现的插件
- 脚本插件：直接在 build.gradle 配置文件

##  二进制插件

**二进制插件**：实现了**org.gradle.api.Plugin**接口的插件，拥有**plugin id**，这个 id 是插件全局唯一的标识或名称

常见的二进制插件 com.android.application，这里的 ‘com.android.application’ 就是插件的 plugin id，二进制插件的使用形式:

```objectivec
apply plugin： plugin id
```

```groovy
apply plugin : 'java'
```

id式：apply plugin:'plugin id'

类型式：apply plugin:org.gradle.api.plugins.JavaPlugin

简写式：apply plugin:JavaPlugin

## 脚本插件

**脚本插件**：严格上只是一个脚本，即**自定义的以 .gradle 为后缀的脚本文件**，可以来自本地或网络

通常脚本插件用于本地的配置存储，使用格式：

```csharp
apply from： ‘fileName’
```

```groovy
// config.gradle
rootProject.ext {
    android = [
        compileSdkVersion : 28,
        buildToolsVersion : "28.0.0",
        applicationId : "sw.andoter.com.gradleplugindemo",
        minSdkVersion : 18,
        targetSdkVersion : 28,
        versionCode : 1,
        versionName : "1.0"
    ]

    sdkVersion = 13

    apkPath = [
       apkPath : "/Users/dengshiwei/Desktop/*.apk"
    ]
}

apply from: "../config.gradle"
```

## 第三方发布插件

**第三方发布插件**：**apply plugin:'com.android.application'**

# ?Gradle 自定义插件

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle](Gradle-插件_imgs\48.png)

##  **方式一：Build script脚本方式**

```groovy
apply plugin: MyPlugin
class MyPlugin implements Plugin<Project>{
    @Override
    void apply(Project project) {
        println "this is my plugin"
    }
}
```

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_02](Gradle-插件_imgs\49.png)


运行结果：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_02](Gradle-插件_imgs\50.png)

### 详细介绍？

1. 创建一个 module，什么样的都可以，不管是 Phone&Tablet Module 或 Android Librarty 都可以，然后只留下 src/main 和  build.gradle，其他的文件全部删除。

2. 在main 目录下创建  groovy 文件夹，然后在 groovy 目录下就可以创建我们的包名和 groovy 文件了,记得后缀要以 .groovy 结尾。在这个文件中引入创建的包名，然后写一个 Class 继承于 Plugin< Project > 并重写 apply 方法。

   ```groovy
   class MyPlugin implements Plugin<Project> {
   
       @Override
       void apply(Project project) {
           System.out.println("-----------插件开始-----------")
           System.out.println("---这是我们的自定义插件---")
           System.out.println("-----------插件结束-----------")
       }
   }
   ```

3. 在 main 目录下创建 resources文件夹，继续在 resources 下创建 META-INF 文件夹，继续在 META-INF 文件夹下创建 gradle-plugins 文件夹，最后在 gradle-plugins 文件夹下创建一个 xxx.properties 文件，注意：这个 xxx 就是在 app 下的 build.gradle 中引入时的名字，例如：apply plugin: ‘xxx’。在文件中写 implementation-class=implementation-class=com.andoter.customplugin.MyPlugin。

   ```groovy
   implementation-class=com.andoter.customplugin.MyPlugin
   ```

4. 打开 build.gradle 删除里面所有的内容。然后格式按这个写，uploadArchives 是上传到 maven 库，然后执行 uploadArchives 这个  task，就将我们的这个插件打包上传到了本地 maven 中，可以去本地的 Maven 库中查看。

   ```groovy
   apply plugin: 'groovy'
   apply plugin: 'maven'
   
   dependencies {
       compile gradleApi()
       compile localGroovy()
   }
   
   repositories {
       mavenCentral()
   }
   
   group = 'com.andoter.customplugin'
   version = '1.0'
   uploadArchives {
       repositories {
           mavenDeployer {
               repository(url: uri('../repo'))
           }
       }
   }
   ```

   在上面的实现中，我们也可以把 group、version 字段配置在内部:

   ```groovy
   uploadArchives {
       repositories {
           mavenDeployer {
               repository(url: uri('../repo'))
               pom.groupId = "com.andoter.customplugin"
               pom.artifactId = "groovydemo"
               pom.version = "1.0"
           }
       }
   }
   ```

5. 应用 gradle 插件：在项目下的 build.gradle（也可以在 module 中）中的 repositories 模块中定义本地 maven 库地址。在  dependencies 模块中引入我们的插件的路径。

   ```groovy
   // 根目录 .gradle 文件配置插件的地址
   buildscript {
       
       repositories {
           google()
           jcenter()
           mavenCentral()
           maven {
               url './repo'
           }
       }
       //格式为-->group:module:version
       dependencies {
           classpath 'com.android.tools.build:gradle:3.1.2'
           classpath 'com.andoter.customplugin:groovydemo:1.0'
       }
   }
   
   // 子项目使用插件
   apply plugin: 'com.andoter.customplugin'
   ```

这样就完成一个自定义插件的使用步骤，自定义插件的核心开发一个什么样的插件，比如结合 Transform 开发一个编译时框架。

## **方式二：buildSrc目录**

1、新建一个 buildSrc 文件夹

2、新建一个 build.gradle 文件，里面添加如下代码，然后点击 sync now，你就会发现 buildSrc 文件夹多了一个绿标

![Android Gradle三种自定义插件方式详解（含报错解决方案）_解决方法_04](Gradle-插件_imgs\51.png)

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

![Android Gradle三种自定义插件方式详解（含报错解决方案）_java_05](Gradle-插件_imgs\52.png)

运行结果展示：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_06](Gradle-插件_imgs\53.png)

## 方式三：独立项目

1、新建一个独立的module，不要选错了！！！，

![Android Gradle三种自定义插件方式详解（含报错解决方案）_解决方法_07](Gradle-插件_imgs\54.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_ide_08](Gradle-插件_imgs\55.png)

2、在该模块下的build.gradle里添加依赖

```groovy
dependencies {
    implementation gradleApi()
}
```


可能出现的报错 Build was configured to prefer settings repositories over project repositories but repository 'Gradle Libs' was added by unknown code

解决方法：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle_10](Gradle-插件_imgs\56.png)

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

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_11](Gradle-插件_imgs\57.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_java_12](Gradle-插件_imgs\58.png)

5、发布插件任务代码的编写

groupId、artifactId、version根据自己实际情况来写

![Android Gradle三种自定义插件方式详解（含报错解决方案）_ide_13](Gradle-自定义插件_imgs\59.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_14](Gradle-自定义插件_imgs\60.png)

如果有小伙伴没找到task视图，解决方法如下：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_ide_15](Gradle-自定义插件_imgs\61.png)

6、点击如下按钮，发布到本地仓库

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle_16](Gradle-插件_imgs\62.png)

7、使用

![Android Gradle三种自定义插件方式详解（含报错解决方案）_gradle_17](Gradle-插件_imgs\63.png)

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_18](Gradle-插件_imgs\64.png)

运行效果：

![Android Gradle三种自定义插件方式详解（含报错解决方案）_android_19](Gradle-插件_imgs\65.png)

 
