gradle 入门指南 https://www.jianshu.com/p/4fbf352ffc56



**属性**

- minSdkVersion：APP支持的最低系统版本
- compileSdkVersion：编译的SDK版本。建议使用最新版本的api进行编译，避免废弃的api。不能影响运行时使用的sdk，这是由系统决定的。
- targetSdkVersion：APP所使用这个所设定的版本及该版本前的所有特性。

  - 例如：

    需求：app要支持Android SDK 4，并且能够使用手势。

    这个时候，就需要将minSdkVersion 设置为4，targetSdkVersion设置为7。因为手势实在Android SDK 7才引入的功能


- dependencies：依赖配置，依赖的库

**几个重要的配置文件**

1. 项目的build.gradle

```gradle
dependencies {
	classpath 'com.android.tools.build:gradle:3.0.1'
}
```

2. gradle-wrapper.properties(在项目\gradlelwrapperl)

```java
distributionUrl=https\://services.gradle.org/distributions/gradle-4.1-allzip
```

3. module中的build.gradle文件

# Gradle原理解释

我们都知道利用Android Studio编写APP时，会使用Gradle这个工具，那么Gradle到底是什么呢？它在APP编写中起到什么作用呢？

Gradle是一个<u>项目自动化建构工具</u>。构建就是根据输入信息执行一系列操作，最后得到几个产出物（APK包）。

传统的构建工具有<u>Ant</u>和<u>Maven</u>，但他们有一些缺点，例如Maven使用XML来制定构建规则。XML虽然通俗易懂，但是很难在xml中描述if{某条件成立，编译某文件}/else{编译其他文件}这样有不同条件的任务。针对这类问题自然需要编程来解决，所以，Gradle选择了Groovy语言。

Gradle的另一个特点是它是一种<u>DSL(Domain-Specific-Language)</u>，即特定领域语言，就是针对某一领域而产生的语言。DSL的好处是一句话可以包含很多意思，因为只针对特定领域解决问题。

Gradle当前其支持的语言限于Java、Groovy和Scala，计划未来将支持更多的语言。Gradle可以帮你管理项目中的差异，依赖，编译，打包，部署...，你可以定义满足自己需要的构建逻辑，写入到build.gradle中供日后复用，通俗的说：gradle是打包用的。

# Groovy基础

Groovy是个灵活的动态脚本语言，基于JVM虚拟机，语法和Java很相似，又兼容Java，且在此基础上增加了很多动态类型和灵活的特性，如支持闭包和DSL。Groovy的开发环境配置可以参考Groovy 环境配置，具体语言特性教程可以参考-Groovy教程。

Groovy基于Java，又扩展了Java，运行过程中首先会先将其编译成Java类字节码，然后通过JVM来执行这个Java类。

## 数据类型

Groovy是弱化类型语言，但是实现上还是强类型相关，如果类型不对，还是会报错。Groovy 中的基本数据类型有

- byte -这是用来表示字节值。例如2。

- short -这是用来表示一个短整型。例如10。

- int -这是用来表示整数。例如1234。

- long -这是用来表示一个长整型。例如10000090。

- float -这是用来表示32位浮点数。例如12.34。

- double -这是用来表示64位浮点数，这些数字是有时可能需要的更长的十进制数表示。例如12.3456565。

- char -这定义了单个字符文字。例如“A”。

- Boolean -这表示一个布尔值，可以是true或false。

- String -这些是以字符串的形式表示的文本。例如，“Hello World”的。

```groovy
int a = 4;
float b = 1.0;
double c = 2.1;
byte  te = 4;
char ch = 'c';
String str = "abcd";
```

## 变量和方法的声明

在 Groovy 中通过 def 关键字进行变量和方法的声明。

```groovy
def a = 1
def b = 1.0
def str = "Hello World"

def output() {
    print 'Hello World'
}
```

Groovy 类似脚本，所以有很多都可以省略：

- 语句后的分号;可以省略
- 变量的类型可以省略
- 方法返回值 return 语句可以省略

方法的声明：

Groovy 也是一门 JVM 语言，所以在语法上与 Java 有很多相通的地方，这样在方法的声明时候格式也比较随意，所以作为 Android 程序员，我们可以选择靠拢 Java 语法格式的风格。

```groovy
def methodName() {
    print("HelloWorld")
}

def int sum2Number(a, b) {
    return a + b
}

def sum(a, b) {
    return a+b
}

int add(a ,b) {
    return a + b
}
```

## 循环

Groovy 中循环控制语句与 Java 中的类似，有以下三种：

- for 语句
- while 语句
- for-in 语句

```groovy
for(int i = 0 ;i < 9; i++) {
    println(i)
}

int i = 0
while(i++ < 9) {
    println(i)
}

for(int j in 1..9) {
    println(j)
}
```

同样，针对循环也有循环控制语句：

break：break语句用于结束循环和switch语句内的控制流。

continue：结束本次循环，进行下次循环，仅限于while和for循环。

```groovy
for(int i = 0 ;i < 9; i++) {
    println(i)
    continue
}

for(int j in 1..9) {
    println(j)
    break
}
```

## 条件判断语句

Groovy 中的条件判断语句与 Java 中的类似，有：

- if
- if...else
- if...else if...else
- switch

例子就不演示了，语法跟 Java 相同。

在上面的 Groovy 基础介绍中，形式上跟 Java 语言非常相似，没有太大的变化，针对 Java 、Android 程序员来说应该非常容易上手。

## List列表

基本语法：List 列表使用[ ] 进行声明，并通过索引进行区分。

```groovy
def listEmpty = []    //空列表
def list = [1,2,3,4,5] //整数值列表
def listInt = [1,[2,3],4,5] //列表嵌套列表
def listString = ["andoter","note"] //字符串列表
def listNone = ["andoter",1,4]  //异构对象列表
```

列表中的方法：

- boolean add(E e)
- void add(int index, E element)
- boolean addAll(Collection<? extends E> c)
- void clear()
- boolean contains(Object o)
- Iterator<E> iterator()
- Object[] toArray()
- int lastIndexOf(Object o)
- E set(int index, E element)

这些方法都跟 Java 中的类似，打开对应的类型查看后，发现通过 def 声明的列表竟然是 java.util.List 下面的。

```groovy
def listEmpty = []    //空列表
def list = [1,2,3,4,5] //整数值列表
def listInt = [1,[2,3],4,5] //列表嵌套列表
def listString = ["andoter","note"] //字符串列表
def listNone = ["andoter",1,4]  //异构对象列表

listEmpty.add(1)
listEmpty << 6
println(listEmpty.size())
list.clear()
println(listInt.contains([2,3]))
println(listString.lastIndexOf("note"))
println(listNone.indexOf(1))
```

> 需要注意，在 groovyjarjarantlr.collections.List 包下同样存在 List，所以使用的时候需要注意。

关于列表 List 的遍历，我们可以参照 Java 中的 Iterator 接口去遍历，或者使用 Groovy 系统提供的 each 方法进行遍历。在 Groovy 中提供 DefaultGroovyMethods 类，该类定义很多快捷使用方法：

- abs：取绝对值计算
- addAll(Collection)
- each：遍历
- eachWithIndex：带 index 的遍历
- grep：符合条件的element会被提取出来，形成一个list
- every：所有的element都满足条件才返回true，否则返回false
- any：只要存在一个满足条件的element就返回true，否则返回false
- join：用指定的字符连接collection中的element
- sort：根据指定条件进行排序
- find：查找collection中满足条件的‘第一个’element
- findAll：查找collection中满足条件的‘所有’element

很多使用的方法，可参照源码查看。

```groovy
def listString = ["andoter","note"]

listString.each {
    println(it)
}

listString.each {
    value -> println(value)
}
```

## Map 映射

Map集合中的元素由键值访问。 Map中使用的键可以是任何类。当我们插入到Map集合中时，需要两个值：键和值。

```groovy
def mapEmpty = [ : ]
def mapString = ["name":"andoter","email" : "andoter0504@gmail.com"]
def mapInt = ["name" : 123, "age" : 26]
```

映射中的方法：

- void clear()
- boolean containsValue(Object value)
- Map.Entry<K, V> eldest()
- Set<Map.Entry<K,V>> entrySet()
- void forEach(BiConsumer<? super K, ? super V> action)
- V get(Object key)
- Set<K> keySet()
- Collection<V> values()

总体上方法与 Java 中的 Map 相同。

```groovy
def mapEmpty = [ : ]
def mapString = ["name":"andoter", "email" : "andoter0504@gmail.com"]
def mapInt = ["name" : 123, "age" : 26]

mapEmpty.put("name","andoter")
mapEmpty.values()
mapString.get("name")
mapInt.containsValue("123")
mapString.each {key, value ->
    if(key == null || key.length() == 0) {
        println("Null Object")
    }

    if(key.equals("name")){
        println(key + "=" + value)
    }else{
        println(key + ":" + value)
    }
}
```

## IO操作

Java 提供了 java.io.* 一系列方法用于文件的操作，这些方法在 Groovy 中也适用。Groovy 针对 Java 提供的方法做了增强处理，更方便使用。

```groovy
def file = new File("/Users/dengshiwei/WorkProject/GradlePlugin/groovydemo/src/main/groovy/TestGroovy.groovy")
if (file.exists()) {
   file.eachLine {
       line ->
           println(line)
   }
} else {
    print("File not exist")
}
```

这里简单的示例下，更多的内容请参照官方 API 接口。

## 闭包

闭包作为 Groovy 中非常重要的特性，它使得 Groovy 语言更加灵活，在 Gradle 项目构建中，更是在 DSL 中大量被使用，所以掌握闭包的使用对掌握 Android 项目构建有非常重要的作用。

# Gradle介绍

Gradle是一个工具，也是一个编程框架。要弄清楚Gradle，则必须知道其组成的基本组件，Gradle中每个待被编译的工程叫Project，每个Project在构建时都包含一系列Task，如Android Studio构建过程中包括Java代码编译Task，资源编译Task，Lint规则检查Task，签名Task等等。

**[深入理解Android之Gradle](https://link.zhihu.com/?target=https%3A//blog.csdn.net/innost/article/details/48228651)**

配置Gradle环境前，确保已经安装配置好Java环境，下载Gradle后解压并配置环境变量，具体可以参考-**[配置Gradle](https://link.zhihu.com/?target=https%3A//blog.csdn.net/u010316188/article/details/84257383)**

下面是一个Gradle语言版的Hello word例子：

```text
// Gradle版Hello word
// 新建build.gradle文件：
task hello{ // 定义一个任务Task名为hello
    doLast{ // 添加一个动作Action，表示在Task执行完毕后回调doLast闭包中的代码
        println'Hello World'//输出字符串，单双号均可
    }
}
// 命令行：
gradle hello // 执行build.gradle中名为Hello的任务
// 输出：
Hello World
```

总而言之，学习Gradle我们需要掌握**Groovy**语言，以及Gradle在Android Studio中的工作方式，工作流程，工作原理。

## Android studio中的Gradle文件

Android Studio 会使用高级构建工具包 Gradle 来**自动执行和管理构建流程**，同时也允许开发者定义灵活的自定义版本配置。每个版本配置均可定义自己的一组代码和资源，同时重复利用应用各个版本的共用部分。

Gradle提供了一种**编译、构建和打包 Android 应用或库**的灵活方式。 一个Android Studio和Gradle的项目目录如下：

![img](Gradle_imgs\v2-3793ac4a94fa116585701a8da301b48c_720w.jpg)

我们先来看看Android Gradle项目中那些涉及到gradle的文件分别是什么意思。

> 一个Android项目中所有文件的具体含义可参考**[Android开发者指南](https://link.zhihu.com/?target=https%3A//developer.android.com/studio/projects%3Fhl%3Dzh-cn)**

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

![img](Gradle_imgs\v2-f1162bda6d75478b4c2e8205444508e0_720w.jpg)

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

# Gradle插件

## 插件介绍

Gradle的设计非常好，**本身提供一些基本的概念和整体核心的框架**，其他用于描述真实使用场景逻辑的都以插件扩展的方式来实现，比如构建Java应用，就通过Java插件来实现，那么自然构建Android应用，就通过Android Gradle插件来实现。

Gradle 提供了很多官方插件，**用于支持Java、Groovy等工程的构建和打包**。同时也提供了**自定义插件**机制，让每个人都可以通过插件来实现特定的构建逻辑，并可以把这些逻辑打包起来，分享给其他人。

Android Gradle插件是基于内置的Java插件实现的。Gradle插件的作用如下：

1. 可以添加任务到项目，比如**测试、编译、打包**等
2. 可以**添加依赖配置到项目**，帮助配置项目构建过程中需要的依赖，比如第三方库等
3. 可以向项目中现有的对象类型添加新的扩展属性和方法等，**帮助配置和优化构建**
4. 可以对项目进行一些约定，比如**约定源代码存放位置**等

## 插件种类及用法

### **插件种类**

- **二进制插件**：实现了**org.gradle.api.Plugin**接口的插件，拥有**plugin id**，这个 id 是插件全局唯一的标识或名称
- **脚本插件**：严格上只是一个脚本，即**自定义的以 .gradle 为后缀的脚本文件**，可以来自本地或网络

### **插件用法**

下面分别说下二进制插件和脚本插件的使用方法，

- **二进制插件**：

> id式：apply plugin:'plugin id'
>
> 类型式：apply plugin:org.gradle.api.plugins.JavaPlugin
>
> 简写式：apply plugin:JavaPlugin

- **脚本插件**：**apply from:'version.gradle'**
- **第三方发布插件**：**apply plugin:'com.android.application'**

## **Android Gradle插件**

从Gradle的角度看，Android其实就是Gradle的一个第三方插件，它是由Google的Android团队开发的，Android 开发 IDE Android Studio 就采用 Gradle 构建项目。

### **Android Gradle插件分类**

1. **App应用工程**：生成可运行apk应用；插件id: **com.android.application**
2. **Library库工程**：生成AAR包给其他的App工程公用，其使用方式和jar包一样，里面有相关的 Android 资源文件；插件id: **com.android.library**
3. **Test测试工程**：对App应用工程或Library库工程进行单元测试；插件id: **com.android.test**

### **Android Gradle插件的应用**

主要来看下Android Gradle的build.gradle配置文件：

```text
// 插件id
apply plugin:'com.android.application'
// 自定义配置入口，后续详解
android{
    compileSdkVersion 23 // 编译Android工程的SDK版本
    buildToolsVersion "23.0.1" // 构建Android工程所用的构建工具版本
 
    defaultConfig{
        applicationId "com.example.myapplication" // 配置包名
        minSdkVersion 14 // 最低支持的Android系统的Level
        targetSdkVersion 23 // 表示基本哪个Android版本开发
        versionCode 1 // APP应用内部版本名称
        versionName "1.0" // APP应用的版本名称
    }
    buildTypes{
        release{ // 构建类型
            minifyEnabled false // 是否启用混淆
            proguardFiles getDefaultPraguardFile('proguard-andrcid.txt'), 'proguard-rules.pro' // 配置混淆文件
        }
    }
}
// 配置第三方依赖
dependencies{
   implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'androidx.appcompat:appcompat:1.0.2'
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'androidx.test:runner:1.2.0'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'
}
```

**android{}是Android Gradle插件提供的一个扩展类型**，可以让我们自定义Android Gradle工程。**defaultConfig{}是默认的配置，是一个ProductFlavor**(**构建渠道**)，**ProductFlavor**允许我们根据不同的情况同时生成不同的APK包。**buildTypes{}是一个NamedDomainObjectContainer**类型，是一个域对象，可以在buildTypes{}里新增任意多个我们需要构建的类型，比如debug类型。

> NamedDomainObjectContainer具体可以参考-**[NamedDomainObjectContainer详解](https://link.zhihu.com/?target=https%3A//www.jianshu.com/p/167cd4b82653)**

### 多渠道构建

由于发布或者推广APP的渠道不同，就造成了Android APP可能会有很多个，所以需要针对不同的渠道做不同的处理。 在Android Gradle中，定义了一个叫**Build Variant**(**构建变体/构建产物**)的概念，一个构建变体（**Build Variant**）=构建类型（**Build Type**）+构建渠道（**Product Flavor**），下面举个例子：

- Build Type有**release、debug**两种构建类型
- Product Flavor有baidu、google两种构建渠道
- Build Variant有baiduRelease、baiduDebug、googleRelease、googleDebug四种构件产物

配置好发布渠道后，Android Gradle插件就会生成很多task，比如**assembleBaidu，assembleRelease，assembleBaiduRelease**等

> Gradle中一个原子性的操作叫做task，简单理解为task是Gradle脚本中的最小可执行单元。

- **assemble开头的Task负责生成构件产物(Apk)**

1. assembleBaidu：运行后会生成baidu渠道的release和debug包
2. assembleRelease：运行后会生成所有渠道的release包
3. assembleBaiduRelease：运行后只会生成baidu的release包

# Android Studio Gradle插件构建流程

## Gradle生命周期

![img](Gradle_imgs\v2-8b3c702d268b20f71a90afde7271f605_720w.jpg)

1. **Initialization（初始化阶段）**：Gradle支持单项目和多项目构建。在初始化阶段，Gradle确定将要参与构建的项目，并为每个项目创建一个Project对象。通俗的说就是执行上述**settings.gradle**文件。
2. **Configuration（配置阶段）**：在此阶段，解析每个Project中的**build.gradle**文件，并生成将要执行的task。
3. **Execution（执行阶段）**：执行 task，进行主要的构建工作

## APK构建流程

**构建流程涉及许多将项目转换成 Android 应用软件包 (APK)的工具和流程**，具体如下图所示：

![img](Gradle_imgs\v2-8294a02772391fb87af12be6965c5f37_720w.jpg)

Android 应用模块的构建流程通常按照以下步骤执行：

1. **编译器将您的源代码转换成 DEX 文件**（Dalvik 可执行文件，其中包括在 Android 设备上运行的字节码），**并将其他所有内容转换成编译后的资源**；
2. **APK 打包器将 DEX 文件和编译后的资源合并到一个 APK 中**。不过，在将应用安装并部署到 Android 设备之前，必须先为 APK 签名。
3. **APK 打包器使用调试或发布密钥库为 APK 签名**：

- a. 如果构建的是调试版应用（即专用于测试和分析的应用），则打包器会使用调试密钥库为应用签名。Android Studio 会自动使用调试密钥库配置新项目。
- b. 如果构建的是打算对外发布的发布版应用，则打包器会使用发布密钥库为应用签名

1. 在生成最终 APK 之前，**打包器会使用 zipalign 工具对应用进行优化**，以减少其在设备上运行时所占用的内存。

构建流程结束时，将获得应用的调试版 APK 或发布版 APK，以用于部署、测试或发布给外部用户。



# Android Gradle Plugin 与 Gradle

**Gradle** --> 构建项目的工具，能够简化编译、打包、测试过程。可以把Gradle类比成Maven --> 在gradle-wrapper.properties中修改

**Android Gradle** --> 一堆适合Android开发的Gradle插件的集合，主要由Google的Android团队开发，Gradle不是Android的专属构建系统；一边调用 Gradle本身的代码和批处理工具来构建项目，一边调用Android SDK的编译、打包功能，从而让我们能够顺畅地在AS上进行开发 --> 在proj的build.gradle中修改

详解：https://juejin.cn/post/6915214037697445896

详解2：https://zhuanlan.zhihu.com/p/32714369