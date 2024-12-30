# Android studio中的Gradle文件

## 版本配置

1. 项目的build.gradle（这里配置Gradle的Android插件的版本）

```gradle
dependencies {
	classpath 'com.android.tools.build:gradle:3.0.1'
}
```

2. gradle-wrapper.properties(在项目\gradlelwrapperl)（这里配置Gradle的版本）

```java
distributionUrl=https\://services.gradle.org/distributions/gradle-4.1-allzip
```

## 相关文件目录

![img](Gradle-AndroidStudio文件解析_imgs\nbkLBw6HIpw.jpg)

我们先来看看Android Gradle项目中那些涉及到gradle的文件分别是什么意思。

## Gradle wrapper（gradle包装）

上图中涉及到Gradle wrapper的部分如下所示，具体有上图中的gradle文件夹，gradlew文件和gradlew.bat批处理文件。

```
|--gradle
|   |--wrapper
|        |--gradle-wrapper.jar
|        |--gradle-wrapper.properties
|--gradlew
|--gradlew.bat
```


gradle文件夹中包含wrapper，wrapper顾名思义是对Gradle的一层包装，便于在团队开发过程中统一Gradle构建的版本。

上面目录中gradlew和gradlew.bat分别是Linux和Windows下的可执行脚本，gradle-wrapper.jar是具体业务逻辑实现的jar包，gradlew可执行脚本最终还是使用这个jar包来执行相关Gradle操作，gradle-wrapper.properties是配置文件，用于配置使用哪个版本的Gradle，配置文件中的具体内容如下所示：

```
#Wed Jun 19 10:09:08 GMT+08:00 2019
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-5.1.1-all.zip
```

## Settings.gradle （多工程配置）

此文件用于初始化以及工程树的配置，大多数用于配置子工程，在Gradle中多个工程是通过工程树来表示的，相当于我们在Android Studio看到的Project和Module概念一样，根工程相当于Project，子工程相当于Module，一个Project可以有很多Module，一个子工程只有在Setting.gradle中配置了才会生效。 配置举例：

```
// 添加:app和:common这两个module参与构建
include ':app' 
project(':app').projectDir = new File('存放目录')
include':common'
project(':common').projectDir = new File('存放目录')
```


如果不指定上述存放目录，则默认为是Settings.gradle其同级目录。

## **build.gradle文件（版本文件）**

每个工程都会有**build.gradle**文件，该文件是该工程的构建入口，在此文件中可以对该工程进行配置，如配置版本，插件，依赖库等。 既然每个工程都有一个build文件，那么根工程也不例外，在根工程中可以对子Module进行统一配置，**全局管理版本号或依赖库**。 build文件分为Project和Module两种，如下图所示：

![img](Gradle-AndroidStudio文件解析_imgs\MBeQPp0WAjb.jpg)

1. **Project的build.gradle**：整个Project的共有属性，包括配置版本、插件、依赖库等信息
2. **Module的build.gradle**：各个module私有的配置文件

```
//Ali的maven源
//        maven { url 'https://plugins.gradle.org/m2/' }
//        maven { url 'https://maven.aliyun.com/nexus/content/repositories/google' }
//        maven { url 'https://maven.aliyun.com/nexus/content/groups/public' }
//        maven { url 'https://maven.aliyun.com/nexus/content/repositories/jcenter'}
```

###  Project中build.gradle文件（顶层版本文件）

```text
buildscript {
    // gradle脚本执行所需依赖仓库
    repositories {
        google()
        jcenter()
        
    }
    // gradle脚本执行所需依赖
    dependencies {
        classpath 'com.android.tools.build:gradle:3.4.1'
    }
}

allprojects {
    // 项目本身需要的依赖仓库
    repositories {
        google()
        jcenter()
        
    }
}
```

那么buildscript中的repositories和allprojects的repositories的作用和区别是什么呢？

1. buildscript里是gradle脚本执行所需依赖，分别是对应的maven库和插件；
2. allprojects里是项目本身需要的依赖，比如我现在要依赖maven库的xx库，那么我应该将maven {url '库链接'}写在这里，而不是buildscript中，否则找不到所需要的库。

### Module中build.gradle文件（模块级版本文件）

此部分内容参考下文中3.3.2节。

## gradle.properties（属性文件）

此文件主要在其中配置**项目全局 Gradle 设置，如 Gradle 守护进程的最大堆大小**。如需了解详情，请参阅**[构建环境](https://link.zhihu.com/?target=https%3A//docs.gradle.org/current/userguide/build_environment.html)**
