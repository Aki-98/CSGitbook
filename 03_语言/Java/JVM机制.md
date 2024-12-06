## **JVM的生命周期**

JVM在Java程序开始运行的时候，它才运行，程序结束的时它就停止。

一个Java程序会开启一个JVM进程，如果一台机器上运行3个Java程序，那么就会有3个运行中的JVM进程。

JVM中的线程分为两种：守护线程和普通线程

守护线程是JVM自己使用的线程，比如垃圾回收（GC）就是一个守护线程。

普通线程一般是Java程序的线程，只要JVM中有普通线程在执行，那么JVM就不会停止。



**结束生命周期**

在如下几种情况下，Java虚拟机将结束生命周期

1、执行了System.exit()方法

2、程序正常执行结束

3、程序在执行过程中遇到了异常或错误而终止进程

4、由于操作系统出现错误而导致Java虚拟机进程终止



## JDK和JRE的区别

JDK是面向开发人员使用的SDK，它提供了Java的开发环境和运行环境，JDK中包含了JRE。

JRE是Java的运行环境，是面向所有Java程序的使用者，包括开发者。

JVM是包含在JRE里面的。

![img](JVM机制_imgs\QX8XBdfxAJy.png)



## **JVM的结构体系**

![img](JVM机制_imgs\ZG3iesDxQFC.png)

### **Class文件**

Class文件由Java编译器生成，我们创建的.Java文件在经过编译器后，会变成.Class的文件，这样才能被JVM所识别并运行。

Class文件的核心设计思想是 **平台无关性**，它存储的不是操作系统可以直接识别的二进制本地机器码，而是根据Java虚拟机规范所自定义的指令集、符号表和一些其他信息，所以只要任何一个操作系统下开发有对应的Java虚拟机，开发者的Java程序就能跑起来。

### **类加载子系统（**类加载器**）**

类加载子系统也可以称之为类加载器，JVM默认提供三个类加载器：

**1、Bootstrap ClassLoader** ：称之为启动类加载器，是最顶层的类加载器，**负责加载JDK中的核心类库，如 rt.jar、resources.jar、charsets.jar等**。

**2、Extension ClassLoader**：称之为扩展类加载器，负责加载Java的扩展类库，默认加载$JAVA_HOME中jre/lib/*.jar 或 -Djava.ext.dirs指定目录下的jar包。

**3、App ClassLoader**：称之为系统类加载器，负责加载应用程序classpath目录下所有jar和class文件。

除了Java默认提供的三个加载器之外，我们还可以根据自身需求自定义ClassLoader，自定义的类加载器必须继承自 java.lang.ClassLoader 类。

**除了 BootStrap ClassLoader 之外**的两个默认加载器都是继承自 java.lang.ClassLoader ，BootStrap ClassLoader 不是一个普通的Java类，它底层由C++编写，已嵌入到了JVM的内核当中，当JVM启动后，BootStrap ClassLoader 也随之启动，负责加载完核心类库，并构造Extension ClassLoader 和App ClassLoader 类加载器。

类加载器子系统不仅仅负责定位并加载类文件，它还严格按照以下步骤做了很多事情：

```text
1、加载：寻找并导入Class文件的二进制信息
2、连接：进行验证、准备和解析
     1）验证：确保导入类型的正确性
     2）准备：为类型分配内存并初始化为默认值
     3）解析：将字符引用解析为直接引用
3、初始化：调用Java代码，初始化类变量为指定初始值
```

详细请参考另一篇文章：[Java类加载机制 - 知乎专栏](https://zhuanlan.zhihu.com/p/25228545)



### **方法区（Method Area）**

方法区用于存储JVM加载完成的类型信息、常量、静态变量、即时编译器编译后的代码缓存，方法区和 Java 堆区一样，都是线程共享的内存区域。

在JDK8以前，使用永久代的方式来实现方法区，JDK8以后，永久代的概念被废弃了，方法区改用和 JRockit、J9一样的在本地内存中实现的元空间（Meta Space）来代替，好处是元空间会在运行时根据需要动态调整，只要没有超过当前进程可用的内存上限（32位和64位系统各不相同），就不会出现溢出的问题。

方法区也可以被垃圾回收，但条件非常严苛，必须在该类没有任何引用的情况下，详情可以参考另一篇文章：[Java性能优化之JVM GC（垃圾回收机制） - 知乎专栏](https://zhuanlan.zhihu.com/p/25539690)

当需要扩展时空间不足，会分别 OutOfMemoryError 异常。


**类型信息包括什么？**

```text
1、类型的全名（The fully qualified name of the type）

2、类型的父类型全名（除非没有父类型，或者父类型是java.lang.Object）（The fully qualified name of the typeís direct superclass）

3、该类型是一个类还是接口（class or an interface）（Whether or not the type is a class ）

4、类型的修饰符（public，private，protected，static，final，volatile，transient等）（The typeís modifiers）

5、所有父接口全名的列表（An ordered list of the fully qualified names of any direct superinterfaces）

6、类型的字段信息（Field information）

7、类型的方法信息（Method information）

8、所有静态类变量（非常量）信息（All class (static) variables declared in the type, except constants）

9、一个指向类加载器的引用（A reference to class ClassLoader）

10、一个指向Class类的引用（A reference to class Class）

11、常量池（The constant pool for the type）
```

### **Java堆（JVM堆**、Java **heap）**

堆区负责存放对象实例，当Java**创建一个类的实例对象或者数组时，都会在堆中为新的对象分配内存**。

虚拟机中只有一个堆，程序中所有的线程都共享它。

通常情况下，堆占用的内存空间是最多的。

堆的存取方式为管道类型，先进先出。

在程序运行中，可以动态的分配堆的内存大小。

堆的内存资源回收是交给JVM GC进行管理的，详情请参考：[Java性能优化之JVM GC（垃圾回收机制） - 知乎专栏](https://zhuanlan.zhihu.com/p/25539690)

当需要扩展时空间不足，会分别 OutOfMemoryError 异常。



### **虚拟机栈（JVM栈、VM Stack）**

在Java栈中**只保存基础数据类型**（**参考：**[Java 基本数据类型 - 四类八种 - 知乎专栏](https://zhuanlan.zhihu.com/p/25439066)）和对象的**引用**，**注意只是对象的引用而不是对象本身哦**，对象是保存在堆区中的。

**拓展知识：像String、Integer、Byte、Short、Long、Boolean等等包装类型，它们是存放于堆中的。**

栈的存取类型为类似于水杯，先进后出。

栈内创建的基本类型数据在超出其作用域后，会被自动释放掉，**它不由JVM GC管理**。而在栈内创建的引用类型实例，则还是由JVM GC管理。

当一个线程创建运行的时候，与之对应的栈就创建了，每个栈中的数据都是私有的，其他线程不能访问。

每个线程都会建立一个栈，每个栈又包含了若干个栈帧，每个栈帧对应着每个方法的每次调用，栈帧包含了三个部分：

局部变量区（方法内基本类型变量、对象实例的引用）

操作数栈区（存放方法执行过程中产生的中间结果）

运行环境区（动态连接、正确的方法返回相关信息、异常捕捉）

虚拟机栈在深度溢出或扩展失败的时候，会分别抛出StackOverflowError 和 OutOfMemoryError 异常。



### **本地方法栈（Native Method Stack）**

本地方法栈的功能和JVM栈非常类似，区别在于虚拟机栈执行的是Java方法，本地方法栈执行的是本地（Native）方法服务，存储的也是本地方法的局部变量表，本地方法的操作数栈等信息。

栈的存取类型为类似于水杯，先进后出。

栈内的数据在超出其作用域后，会被自动释放掉，**它不由JVM GC管理。**

每一个线程都包含一个栈区，每个栈中的数据都是私有的，其他栈不能访问。

本地方法栈是在 程序调用 或 JVM调用 **本地方法接口（Native）**时候启用。

本地方法都不是使用Java语言编写的，它们可能由C或其他语言编写，本地方法也不由JVM去运行，所以本地方法的运行不受JVM管理。

HotSpot VM将本地方法栈和JVM栈合并了。

本地方法栈也会在深度溢出或扩展失败的时候，分别抛出StackOverflowError 和 OutOfMemoryError 异常。

### **程序计数器**

在JVM的概念模型里，字节码解释器工作时就是通过改变这个计数器的值来选取下一条需要执行的字节码指令。分支、循环、跳转、异常处理、线程恢复等基础功能都需要依赖这个计数器来完成。

JVM的多线程是通过线程轮流切换并分配处理器执行时间的方式来实现的，为了各条线程之间的切换后计数器能恢复到正确的执行位置，所以**每条线程都会有一个独立的程序计数器**。

程序计数器仅占很小的一块内存空间。

当线程正在执行一个Java方法，程序计数器记录的是正在执行的JVM字节码指令的地址。如果正在执行的是一个Natvie（本地方法），那么这个计数器的值则为空（Underfined）。

程序计数器不会抛出 OutOfMemoryError（内存不足错误）。

### **JVM执行引擎**

Java虚拟机相当于一台虚拟的“物理机”，这两种机器都有代码执行能力，区别主要是物理机的执行引擎是直接建立在处理器、硬件、指令集和操作系统层面上的，而JVM的执行引擎是自己实现的，因此程序员可以自行制定指令集和执行引擎的结构体系。

执行引擎的主要职责，就是把这些自行制定的指令集翻译成硬件所支持的指令集格式，然后执行。

在JVM规范中制定了虚拟机字节码执行引擎的概念模型，这个模型称之为JVM执行引擎的统一外观，各个Java 虚拟机的发行厂商都需要按照这个规范来实现。

在不同的虚拟机实现中，可能会有两种的执行方式：解释执行（通过解释器执行）和编译执行（通过即时编译器产生本地代码）。虚拟机可以按自身的需求，采用一种或同时采用多种组合的方式来实现执行引擎。但无论内部怎么实现，都要遵循**输入的是字节码文件、处理过程是等效字节码解析过程、输出的是执行结果**这个JVM规范要求。



### **本地方法接口（JNI）**

JNI是Java Native interface的缩写，它提供了若干的API实现了Java和其他语言的通信（主要是C和C++）。

**JNI的适用场景**

当我们有一些旧的库，已经使用C语言编写好了，如果要移植到Java上来，非常浪费时间，而JNI可以支持Java程序与C语言编写的库进行交互，这样就不必要进行移植了。或者是与硬件、操作系统进行交互、提高程序的性能等，都可以使用JNI。需要注意的一点是需要保证本地代码能工作在任何Java虚拟机环境。

**JNI的副作用**

一旦使用JNI，Java程序将丢失了Java平台的两个优点：

1、程序不再跨平台，要想跨平台，必须在不同的系统环境下程序编译配置本地语言部分。

2、程序不再是绝对安全的，本地代码的使用不当可能会导致整个程序崩溃。一个通用规则是，调用本地方法应该集中在少数的几个类当中，这样就降低了Java和其他语言之间的耦合。



### **JVM GC（垃圾回收机制）**

详情请参考我的另外一篇文章：[Java性能优化之JVM GC（垃圾回收机制） - 知乎专栏](https://zhuanlan.zhihu.com/p/25539690)



## 常量池

要理解常量池，首先要知道，常量池是分3种类型的

1、Class文件内容里的常量池

2、运行时常量池（Runtime Constant Pool）

3、各个包装类型里实现的常量池，例如String类里面的字符串常量池（String Pool）



### Class 常量池

Java代码在经过编译器后，会生成一个Class文件，这个常量池就是Class文件里的一大段内容（通常是最大的一段内容），它主要存放着 字面量、符号引用 等信息，在JVM把Class文件加载完成后，Class 常量池里的数据会存放到**运行时常量池**中。



### 运行时常量池（Runtime Constant Pool）

运行时常量池是方法区（Method Area）的一部分，运行时常量池中存储的，是基本类型的数据和对象的引用，注意**是对象的引用而不是对象实例本身**哦。

Java虚拟机在加载Class文件时，Class文件内容里常量池的数据会放入运行时常量池。每一个加载好的Class对象里都会有一个运行时常量池。



### 字符串常量池（String Constant Pool） & 其他包装类型里实现的常量池

字符串由一个char[]构成，当我们的Java程序里频繁出现相同字面量的代码时，重复的创建和销毁对象是一件很浪费资源的事情，所以Java实现了一个字符串常量池。

JDK7之后，字符串常量池从方法区迁移到了堆区，它的底层实现可以理解为是一个HashTable。Java虚拟机中只会存在一份字符串常量池。字符串常量池里，存放的数据可以是引用也可以是对象实例本身。

字符串常量池 也具备 运行时常量池 动态性的特征，它支持运行期间将新的常量放入池中，这种特性被开发人员利用比较多的就是 String.intern() 方法。

**基本类型的包装类和常量池**

Byte、Short、Integer、Long、Character、Boolean、String 这 7 种包装类都各自实现了自己的常量池。

Float 和Double 这两个浮点类型没有实现常量池。

```java
//例子：
Integer i1 = 20;
Integer i2 = 20;
System.out.println(i1==i2);//输出TRUE
```

Byte、Short、Integer、Long、Character这5种包装类都默认创建了数值[-128 , 127]的缓存数据。**当这5个类型的数据不在这个区间内的时候，将会去创建新的对象，并且不会将这些新的对象放入常量池中。**

```java
//IntegerCache.low = -128
//IntegerCache.high = 127
public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);
    }
//例子
Integer i1 = 200;
Integer i2 = 200;
System.out.println(i1==i2);//返回FALSE
```



**字符串常量池（String pool）的实例**

```java
String str1 = "aaa";
```

当以上代码运行时，JVM会到字符串常量池查找 "aaa" 这个字面量对象是否存在：

**存在**：则返回该对象的引用给变量 **str1** 。

**不存在**：则创建一个对象，同时将引用返回给变量 **str1 。**（JDK8之后，对象实例直接存储在字符串常量池里）

```java
String str1 = "aaa";
String str2 = "aaa";
System.out.println(str1 == str2);//返回TRUE
```

因为变量**str1** 和**str2** 都指向同一个对象，所以返回true。

```text
String str3 = new String("aaa");
System.out.println(str1 == str3);//返回FALSE
```

当我们使用了**new**来构造字符串对象的时候，不管字符串常量池中是否有相同内容的对象的引用，新的字符串对象都会创建。因为两个指向的是不同的对象，所以返回FALSE 。



**String.intern()方法**

对于使用了new 创建的字符串对象，如果想要将这个对象添加到字符串常量池，可以使用intern() 方法。

```java
String str1 = "aaa";
String str2 = "aaa";
String str3 = new String("aaa");
String interns = str3.intern();
System.out.println(interns == str1);//返回TRUE
```

intern() 方法会检查字符串常量池中是否有与之匹配的对象，并做如下操作：

存在：直接返回对象引用给interns变量。

不存在：将这个对象引用加入到常量池，再返回对象引用给interns变量。



**以下创建了多少个对象呢？**

```java
String str4 = "abc"+"efg";
String str5 = "abcefg";
System.out.println(str4 == str5);//返回TRUE
```

答案是三个。第一个："abc" ，第一个："efg"，第三个："abc"+"efg"（"abcefg"）

String str5 = "abcefg"; 这句代码并没有创建对象，它从常量池中找到了"abcefg" 的引用，所以str4 == str5 返回TRUE，因为它们都指向一个相同的对象。



**什么情况下会将字符串对象引用自动加入字符串常量池？**

```text
//只有在这两种情况下会将对象引用自动加入到常量池：
String str1 = "aaa";
String str2 = "aa"+"a";

//以下都不会将对象引用自动加入到常量池：
String str3 = new String("aaa");
String str4 = New StringBuilder("aa").append("a").toString();
StringBuilder sb = New StringBuilder();
sb.append("aa");
sb.append("a");
String str5 = sb.toString();
```




**双等号（==）的含义**

基本数据类型之间使用双等号，比较的是值。

引用类型（Class类）之间使用双等号，比较的是对象的引用地址是否相等。