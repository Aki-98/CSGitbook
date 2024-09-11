![img](Android项目构建流程_imgs\Android项目构建流程_1.png)

整体流程：

- 首先aapt工具会将资源文件进行转化，生成对应资源ID的R文件和资源文件。
- aidl工具会将其中的aidl接口转化成Java的接口
- 至此，Java Compiler开始进行Java文件向class文件的转化，将R文件，Java源代码，由aidl转化来的Java接口，统一转化成.class文件。
- 通过dx工具将class文件转化为dex文件。
- 此时我们得到了经过处理后的资源文件和一个dex文件，当然，还会存在一些其它的资源文件，这个时候，就是将其打包成一个类似apk的文件。但还并不是直接可以安装在Android系统上的APK文件。
- 通过签名工具对其进行签名。
- 通过Zipalign进行优化，提升运行速度（原理后文会提及）。
- 最终，一个可以安装在我们手机上的APK了。

# 第1步：aapt打包资源文件，生成R.java和编译后的资源（二进制文件）

讲到资源文件的处理，我们先来看一下Android中的资源文件有那些呢?Android应用程序资源可以分为两大类，分别是assets和res：

1. assets类资源放在工程根目录的assets子目录下，它里面保存的是一些原始的文件，可以以任何方式来进行组织。这些文件最终会被原装不动地打包在apk文件中。如果我们要在程序中访问这些文件，那么就需要指定文件名来访问。例如，假设在assets目录下有一个名称为filename的文件，那么就可以使用以下代码来访问它：

```
AssetManager am = getAssets();    
InputStream is = assset.open("filename");  
```

2. res类资源放在工程根目录的res子目录下，它里面保存的文件大多数都会被编译，并且都会被赋予资源ID。这样我们就可以在程序中通过ID来访问res类的资源。res类资源按照不同的用途可以进一步划分为以下10种子类型：layout(布局文件)，drawable，xml，value，menu，raw，color，anim，animator，mipmap。

为了使得一个应用程序能够在运行时同时支持不同的大小和密度的屏幕，以及支持国际化，即支持不同的国家地区和语言，Android应用程序资源的组织方式有18个维度，每一个维度都代表一个配置信息，从而可以使得应用程序能够根据设备的当前配置信息来找到最匹配的资源来展现在UI上，从而提高用户体验。由于Android应用程序资源的组织方式可以达到18个维度，因此就要求Android资源管理框架能够快速定位最匹配设备当前配置信息的资源来展现在UI上，否则的话，就会影响用户体验。为了支持Android资源管理框架快速定位最匹配资源，Android资源打包工具aapt在编译和打包资源的过程中，会执行以下两个额外的操作：

- 赋予每一个非assets资源一个ID值，这些ID值以常量的形式定义在一个R.java文件中。
- 生成一个resources.arsc文件，用来描述那些具有ID值的资源的配置信息，它的内容就相当于是一个资源索引表。包含了所有的id值的数据集合。在该文件中，如果某个id对应的是string，那么该文件会直接包含该值，如果id对应的资源是某个layout或者drawable资源，那么该文件会存入对应资源的路径。

**为什么要转化为二进制文件？**

- 二进制格式的XML文件占用空间更小。这是由于所有XML元素的标签、属性名称、属性值和内容所涉及到的字符串都会被统一收集到一个字符串资源池中去，并且会去重。有了这个字符串资源池，原来使用字符串的地方就会被替换成一个索引到字符串资源池的整数值，从而可以减少文件的大小。
- 二进制格式的XML文件解析速度更快。这是由于二进制格式的XML元素里面不再包含有字符串值，因此就避免了进行字符串解析，从而提高速度。
  有了资源ID以及资源索引表之后，Android资源管理框架就可以迅速将根据设备当前配置信息来定位最匹配的资源了。

# 第2步：aidl

aidl，全名Android Interface Definition Language，即Android接口定义语言。是我们在编写进程间通信的代码的时候，定义的接口。

输入：aidl后缀的文件。输出：可用于进程通信的C/S端java代码，位于build/generated/source/aidl。

# 第3步：Java源码编译

我们有了R.java和aidl生成的Java文件，再加上工程的源代码，现在可以使用javac进行正常的java编译生成class文件了。

输入：java source的文件夹（另外还包括了build/generated下的：R.java, aidl生成的java文件，以及BuildConfig.java）。输出：对于gradle编译，可以在build/intermediates/classes里，看到输出的class文件。

# 第4步：代码混淆（proguard）

源码编译之后，我们可能还会对其进行代码的混淆，混淆的作用是增加反编译的难度，同时也将一些代码的命名进行了缩短，减少代码占用的空间。混淆完成之后，会生成一个混淆前后的映射表，这个是用来在反应我们的应用执行的时候的一些堆栈信息，可以将混淆后的信息转化为我们混淆前实际代码中的内容。

而这个过程使用的工具就是ProGuard，是一个开源的Java代码混淆器（obfuscation）。ADT r8开始它被默认集成到了Android SDK中。 其具备三个主要功能。

- 压缩 - 移除无效的类、属性、方法等

- 优化 - 优化bytecode移除没用的结构

- 混淆 - 把类名、属性名、方法名替换为晦涩难懂的1到2个字母的名字

  当然它也只能混淆Java代码，Android工程中Native代码，资源文件（图片、xml），它是无法混淆的。而且对于Java的常量值也是无法混淆的，所以不要使用常量定义平文的密码等重要信息。同时对于混淆，我们可以通过代码制定去混淆那些，不去混淆那些。

```
-keep public class com.rensanning.example.Test
```

# 第5步：转化为dex

调用dx.bat将所有的class文件转化为classes.dex文件，dx会将class转换为Dalvik字节码，生成常量池，消除冗余数据等。由于dalvik是一种针对嵌入式设备而特殊设计的java虚拟机，所以dex文件与标准的class文件在结构设计上有着本质的区别,当java程序编译成class后，使用dx工具将所有的class文件整合到一个dex文件，目的是其中各个类能够共享数据，在一定程度上降低了冗余，同时也是文件结构更加经凑，实验表明，dex文件是传统jar文件大小的50%左右。class文件结构和dex文件结构比对。

![img](Android项目构建流程_imgs\Android项目构建流程_2.png)

# 第6步：apkbuilder

打包生成APK文件。旧的apkbuilder脚本已经废弃，现在都已经通过sdklib.jar的ApkBuilder类进行打包了。输入为我们之前生成的包含resources.arcs的.ap_文件，上一步生成的dex文件，以及其他资源如jni、.so文件。_
大致步骤为：以包含resources.arcs的.ap_文件为基础，new一个ApkBuilder，设置debugMode

```
apkBuilder.addZipFile(f);
apkBuilder.addSourceFolder(f);
apkBuilder.addResourcesFromJar(f);
apkBuilder.addNativeLibraries(nativeFileList);
apkBuilder.sealApk(); // 关闭apk文件
generateDependencyFile(depFile, inputPaths, outputFile.getAbsolutePath());
```

# 第7步：对APK签名

对APK文件进行签名。Android系统在安装APK的时候，首先会检验APK的签名，如果发现签名文件不存在或者校验签名失败，则会拒绝安装，所以应用程序在发布之前一定要进行签名。签名信息中包含有开发者信息，在一定程度上可以防止应用被伪造。对一个APK文件签名之后，APK文件根目录下会增加META-INF目录，该目录下增加三个文件：

- MANIFEST.MF
- [CERT].RSA
- [CERT]

Android系统就是根据这三个文件的内容对APK文件进行签名检验的。签名过程主要利用apksign.jar或者jarsinger.jar两个工具。将根据我们提供的Debug和Release两个版本的Keystore进行相应的签名。

MANIFEST.MF中包含对apk中除了/META-INF文件夹外所有文件的签名值，签名方法是先SHA1()(或其他hash方法)在base64()。存储形式是：Name加[SHA1]-Digest。

[CERT].SF是对MANIFEST.MF文件整体签名以及其中各个条目的签名。一般地，如果是使用工具签名，还多包括一项。就是对MANIFEST.MF头部信息的签名。

[CERT].RSA包含用私钥对[CERT].SF的签名以及包含公钥信息的数字证书。

# 第8步：zipalign优化

Zipalign是一个Android平台上整理APK文件的工具，它首次被引入是在Android 1.6版本的SDK软件开发工具包中。它能够对打包的Android应用程序进行优化， 以使Android操作系统与应用程序之间的交互作用更有效率，这能够让应用程序和整个系统运行得更快。用Zipalign处理过的应用程序执行时间达到最低限度，当设备运行APK应用程序时占更少的RAM。

**Zipalign如何进行优化的呢？**

调用buildtoolszipalign，对签名后的APK文件进行对齐处理，使APK中所有资源文件距离文件起始偏移为4字节的整数倍，从而在通过内存映射访问APK文件时会更快。同时也减少了在设备上运行时的内存消耗。如果对于为何提速不理解，那么可以看下内存对齐的规则以及作用该篇文章，对于内存对齐的好处有比较生动详细的解释。最终这样我们的APK就生成完毕了。

**典型的APK中内容**

- AndroidManifest.xml 程序全局配置文件
- classes.dex Dalvik字节码
- resources.arsc 资源索引表
- META-INF该目录下存放的是签名信息
- res 该目录存放资源文件
- assets该目录可以存放一些配置或资源文件