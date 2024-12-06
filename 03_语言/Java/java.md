# Java

# 简介

**JVM（Java Virtual Machine）:**

 Java虚拟机，Java平台无关性的关键

**Java程序的执行过程：**

.java源文件-->编译器compiler-->.class字节码文件-->解释器interpreter-->program（把字节码解释成具体平台上的机器语言后，实现一次编译、到处运行）

**JDK（Java Development Kit）:**

Java语言的软件开发工具包

两个主要组件：

-javac -编译器，将源程序转成字节码

-java -运行编译后的java程序（.class后缀的）

**JRE（Java Runtime Environment）：**

包括Java虚拟机（JVM），Java核心类库和支持文件

如果只需要运行Java程序，下载并安装JRE即可；如果要开发Java软件，需要下载JDK

在JDK中附带有JRE

**JDK、JRE、JVM三者的关系**

![img](java_imgs\4B43cogdCyy.gif)

JRE = JVM + JavaSE标准类库

 JDK = JRE + 开发者工具集（例如javac编译工具等）

**Java平台**

JavaSE Java标准版 桌面程序

JavaEE Java企业版 Web程序

 JavaME Java微型版 移动设备（现在用得少了）

# 常量与变量

## 标识符的命名规则：

标识符可以由字母、数字、下划线和美元符（$）组成，不能以数字开头

标识符不能有空格

标识符不能和关键字相同（eclipse中紫色）

标识符不能是Java保留字（如goto 现在不使用以后可能会使用）

标识符的命名最好能反映其作用

## 关键字表格

![img](java_imgs\3G6ZVGig6QK.gif)

## 数据类型

![img](java_imgs\EIDVjMqUAiJ.gif)

## 基本数据类型

![img](java_imgs\HYF8RIGJA4u.gif)

## 进制表示

八进制：以0开头，包括0-7的数字

十六进制：以0x或0X开头，包括0-9的数字，及字母a-f，A-F

## 基本数据类型变量的存储

数据类型分为基本数据类型和引用数据类型

引用数据类型包括数组和类等

类定义的变量又叫对象

## 变量按作用范围分为：

类级、对象实例级、方法级（局部变量 ）、块级

## Unicode

目标支持世界上所有的字符集，例：char c='\u005d'（四位的）

## 自动类型转换顺序

![img](java_imgs\yhr1I5PYfge.gif)

## 常量

定义变量最前头加上final

# 运算符

## 运算符优先级

 同一级别，从左到右进行运算。

![img](java_imgs\xrN5MgRlTcc.gif)

# 关键字

## 访问控制

**private 私有的**

private 关键字是访问控制修饰符，可以应用于类、方法或字段（在类中声明的变量）。 只能**在声明 private（内部）类、方法或字段的类**中引用这些类、方法或字段。在类的外部或者对于子类而言，它们是不可见的。

**protected 受保护的**

protected 关键字是可以应用于类、方法或字段（在类中声明的变量）的访问控制修饰符。可以在声明 protected 类、方法或字段的类、**同一个包中的其他任何类以及任何子类（无论子类是在哪个包中声明的）**中引用这些类、方法或字段。

**public 公共的**

public 关键字是可以应用于类、方法或字段（在类中声明的变量）的访问控制修饰符。 可能只会在其他任何类或包中引用 public 类、方法或字段。

那么我们总结一下，Java之中的权限访问修饰符（其实还有一种权限访问情况，就是默认情况，暂且称作default吧）：

| 访问权限 | 当前类 | 包   | 子类 | 其他包 |
| -------- | ------ | ---- | ---- | ------ |
| public   | ∨      | ∨    | ∨    | ∨      |
| protect  | ∨      | ∨    | ∨    | ×      |
| default  | ∨      | ∨    | ×    | ×      |
| private  | ∨      | ×    | ×    | ×      |

## 类、方法和变量修饰符

### abstract 声明抽象

abstract关键字可以修改类或方法。**abstract类可以扩展（增加子类），但不能直接实例化。abstract方法不在声明它的类中实现，但必须在某个子类中重写。采用 abstract方法的类本来就是抽象类，并且必须声明为abstract。**

### class类

class 关键字用来声明新的 Java 类，该类是相关变量和/或方法的集合。类是面向对象的程序设计方法的基本构造单位。类通常代表某种实际实体，如几何形状或人。类是对象的模板。每个对象都是类的一个实例。要使用类，通常使用 new 操作符将类的对象实例化，然后调用类的方法来访问类的功能。

### extends 继承、扩展

extends 关键字用在 class 或 interface 声明中，用于指示所声明的类或接口是其名称后跟有 extends 关键字的类或接口的子类。**子类继承父类的所有 public 和 protected 变量和方法（但是不包括构造函数）。 子类可以重写父类的任何非 final 方法。一个类只能扩展一个其他类。**

extends 关键字用在 class 或 interface 声明中，用于指示所声明的类或接口是其名称后跟有 extends 关键字的类或接口的子类。

### final 最终、不可改变

在Java中，final关键字可以用来修饰类、方法和变量（包括成员变量和局部变量）。final方法在编译阶段绑定，称为静态绑定(static binding)。下面就从这四个方面来了解一下final关键字的基本用法。

**①修饰类**

当用final修饰一个类时，表明这个类**不能被继承，不能有子类**。也就是说，如果一个类你永远不会让他被继承，就可以用final进行修饰。final类中的成员变量可以根据需要设为final，但是要注意final类中的所有成员方法都会被隐式地指定为final方法。

**②修饰方法**

使用final方法的原因有两个。第一个原因是把方法锁定，以防任何继承类修改它的含义；第二个原因是效率。在早期的Java实现版本中，会将final方法转为内嵌调用。但是如果方法过于庞大，可能看不到内嵌调用带来的任何性能提升。在最近的Java版本中，不需要使用final方法进行这些优化了。

因此，如果只有在想明确禁止 该方法在子类中被覆盖的情况下才将方法设置为final的。

还有就是，类的private方法会隐式地被指定为final方法。

**③修饰变量**

修饰变量是final用得最多的地方。

对于一个final变量，如果是**基本数据类型的变量，则其数值一旦在初始化之后便不能更改**；如果是**引用类型的变量，则在对其初始化之后便不能再让其指向另一个对象**。引用变量被final修饰之后，虽然不能再指向其他对象，但是它指向的对象的内容是可变的。

**④final参数**

**当函数参数为final类型时，你可以读取使用该参数，但是无法改变该参数的值或者引用指向。**道理同final变量。

概括起来就是：

●  在A类是声明为final类型的方法，那么不能在子类里被覆盖；

●  如果A类被声明为final类型的类，那么B类不能继承A类；

●  如果成员变量声明为final类型，那么成员变量不能被修改；

注意：

1. 一个类不能同时是 abstract 又是 final**。abstract 意味着必须扩展类，final 意味着不能扩展类。**一个方法不能同时是 abstract 又是 fina**l。abstract 意味着必须重写方法，final 意味着不能重写方法。两者是相互矛盾的。

2. 当用final作用于类的成员变量时，**成员变量（注意是类的成员变量，局部变量只需要保证在使用之前被初始化赋值即可）必须在定义时或者构造器中进行初始化赋值，而且final变量一旦被初始化赋值之后，就不能再被赋值了**。

3. final变量和普通变量的区别。当final变量是基本数据类型以及String类型时，如果在编译期间能知道它的确切值，则编译器会进行优化，会把它当做编译期常量使用。也就是说在用到该final变量的地方，相当于直接访问的这个常量，不需要在运行时确定。这种和C语言中的宏替换有点像。而普通变量在编译时，确定不了自身的值，需要在运行时才能知道。

4. 局部内部类和匿名内部类只能访问局部final变量。因为这里的局部变量，需要在编译阶段便需要确定下来的。也就是说，如果局部变量的值在编译期间就可以确定，则直接在匿名内部里面创建一个拷贝。如果局部变量的值无法在编译期间确定，则通过构造器传参的方式来对拷贝进行初始化赋值。（？？？？？？）

### implements实现

implements 关键字在 class 声明中使用，以指示所声明的类提供了在 implements 关键字后面的名称所指定的接口中所声明的所有方法的实现。类必须提供在接口中所声明的所有方法的实现。一个类可以实现多个接口。

### interface 接口

interface 关键字用来声明新的 Java 接口，接口是方法的集合。

接口是 Java 语言的一项强大功能。任何类都可声明它实现一个或多个接口，这意味着它实现了在这些接口中所定义的所有方法。

实现了接口的任何类都必须提供在该接口中的所有方法的实现。一个类可以实现多个接口。

### **native** 本地

native 关键字可以应用于方法，以指示该方法是用Java以外的语言实现的，方法对应的实现不是在当前文件，而是在用其他语言（如C和C++）实现的文件中。。

 Java不是完美的，Java的不足除了体现在运行速度上要比传统的C++慢许多之外，Java无法直接访问到操作系统底层（如系统硬件等)，为此Java使用native方法来扩展Java程序的功能。

可以将native方法比作Java程序同Ｃ程序的接口，其实现步骤：

1. 在Java中声明native()方法，然后编译；

2. 用javah产生一个.h文件；

3. 写一个.cpp文件实现native导出方法，其中需要包含第二步产生的.h文件（注意其中又包含了JDK带的jni.h文件）；

4. 将第三步的.cpp文件编译成动态链接库文件；

5. 在Java中用System.loadLibrary()方法加载第四步产生的动态链接库文件，这个native()方法就可以在Java中被访问了。

 JAVA本地方法适用的情况

1. 为了使用底层的主机平台的某个特性，而这个特性不能通过JAVA API访问

2. 为了访问一个老的系统或者使用一个已有的库，而这个系统或这个库不是用JAVA编写的

3. 为了加快程序的性能，而将一段时间敏感的代码作为本地方法实现。

### new 新,创建

new 关键字用于创建类的新实例。

new 关键字后面的参数必须是类名，并且类名的后面必须是一组构造方法参数（必须带括号）。 参数集合必须与类的构造方法的签名匹配。

= 赋值号左侧的变量的类型必须与要实例化的类或接口具有赋值兼容关系。

### static 静态

static可以用于修饰属性，可以修饰代码块，也可以用于修饰方法，还可以用于修饰类。

1. static修饰属性：

无论一个类生成了多少个对象，所有这些对象共同使用唯一一份静态的成员变量；一个对象对该静态成员变量进行了修改，其他对象的该静态成员变量的值也会随之发生变化。如果一个成员变量是static的，那么我们可以通过‘类名.成员变量名’的方式来使用它。

2. static修饰方法：

static修饰的方法叫做静态方法。对于静态方法来说，可以使用‘类名.方法名’的方式来访问。静态方法只能继承，不能重写（Override），因为重写是用于表现多态的，重写只能适用于实例方法，而静态方法是可以不生成实例直接用类名来调用，这就会与重写的定义所冲突，与多态所冲突，所以静态方法不能重写，只能是隐藏。

static方法与非static方法：不能在静态方法中访问非静态成员变量；可以在静态方法中访问静态的成员变量。可以在非静态方法中访问静态的成员变量：因为静态方法可以直接用类名来调用，而非静态成员变量是在创建对象实例时才为变量分配内存和初始化变量值。

不能在静态方法中使用this关键字：因为静态方法可以直接用类名来调用，而this实际上是创建实例时，实例对应的一个应用，所以不能在静态方法上使用this。

3. static修饰代码块：

静态代码块。静态代码块的作用也是完成一些初始化工作。首先执行静态代码块，然后执行构造方法。静态代码块在类被加载的时候执行，而构造方法是在生成对象的时候执行；要想调用某个类来生成对象，首先需要将类加载到Java虚拟机上（JVM），然后由JVM加载这个类来生成对象。

类的静态代码块只会执行一次，是在类被加载的时候执行的，因为每个类只会被加载一次，所以静态代码块也只会被执行一次；而构造方法则不然，每次生成一个对象的时候都会调用类的构造方法，所以new一次就会调用构造方法一次。如果继承体系中既有构造方法，又有静态代码块，那么首先执行最顶层的类的静态代码块，一直执行到最底层类的静态代码块，然后再去执行最顶层类的构造方法，一直执行到最底层类的构造方法。注意：静态代码块只会执行一次。

4. static修饰类：

这个有点特殊，首先，static是可以用来修饰类的，但是static是不允许用来修饰普通类，只能用来修饰内部类，被static所修饰的内部类可以用new关键字来直接创建一个实例，不需要先创建外部类实例。static内部类可以被其他类实例化和引用（即使它是顶级类）。

其实理解起来也简单。因为static主要是修饰类里面的成员，包括内部类、属性、方法这些。修饰这些变量的目的也很单纯，那就是暗示这个成员在该类之中是唯一的一份拷贝，即便是不断的实例化该类，所有的这个类的对象都会共享这些static成员。这样就好办了。因为是共享的、唯一的，所以，也就不需要在实例化这个类以后再通过这个类来调用这个成员了，显然有点麻烦，所以就简单一点，直接通过类名直接调用static成员，更加直接。然而这样设置之后，就出现了一个限制，就是，static方法之中不能访问非static属性，因为这个时候非static属性可能还没有给他分配内存，该类还没有实例化。

所以，通常，static 关键字意味着应用它的实体在声明该实体的类的任何特定实例外部可用。

可以从类的外部调用 static 方法，而不用首先实例化该类。这样的引用始终包括类名作为方法调用的限定符。

### strictfp 严格,精准

strictfp的意思是FP-strict，也就是说精确浮点的意思。在Java虚拟机进行浮点运算时，如果没有指定strictfp关键字时，Java的编译器以及运行环境在对浮点运算的表达式是采取一种近似于我行我素的行为来完成这些操作，以致于得到的结果往往无法令人满意。而一旦使用了strictfp来声明一个类、接口或者方法时，那么所声明的范围内Java的编译器以及运行环境会完全依照浮点规范IEEE-754来执行。因此如果想让浮点运算更加精确，而且不会因为不同的硬件平台所执行的结果不一致的话，那就请用关键字strictfp。

可以将一个类、接口以及方法声明为strictfp，但是不允许对接口中的方法以及构造函数声明strictfp关键字。

### synchronized线程、同步

synchronized 关键字可以应用于方法或语句块，并为一次只应由一个线程执行的关键代码段提供保护。

synchronized 关键字可防止代码的关键代码段一次被多个线程执行。

如果应用于静态方法，那么，当该方法一次由一个线程执行时，整个类将被锁定。

如果应用于实例方法，那么，当该方法一次由一个线程访问时，该实例将被锁定。

如果应用于对象或数组，当关联的代码块一次由一个线程执行时，对象或数组将被锁定。

一般的用法有：

**synchronized 方法控制对类成员变量的访问：每个类实例对应一把锁**

每个synchronized 方法都必须获得调用该方法的类实例的锁方能执行，否则所属线程阻塞，方法一旦执行，就独占该锁，直到从该方法返回时才将锁释放，此后被阻塞的线程方能获得该锁，重新进入可执行状态。这种机制确保了同一时刻对于每一个类实例，其所有声明为 synchronized 的成员函数中至多只有一个处于可执行状态（因为至多只有一个能够获得该类实例对应的锁），从而有效避免了类成员变量的访问冲突（只要所有可能访问类成员变量的方法均被声明为 synchronized）。

在Java中，不光是类实例，每一个类也对应一把锁，这样我们也可将类的静态成员函数声明为 synchronized ，以控制其对类的静态成员变量的访问。

synchronized 方法的缺陷：若将一个大的方法声明为synchronized 将会大大影响效率，典型地，若将线程类的方法 run() 声明为synchronized ，由于在线程的整个生命期内它一直在运行，因此将导致它对本类任何synchronized 方法的调用都永远不会成功。当然我们可以通过将访问类成员变量的代码放到专门的方法中，将其声明为 synchronized ，并在主方法中调用来解决这一问题，但是 Java 为我们提供了更好的解决办法，那就是 synchronized块。

**synchronized块**

当两个并发线程访问同一个对象object中的这个synchronized(this)同步代码块时，一个时间内只能有一个线程得到执行。另一个线程必须等待当前线程执行完这个代码块以后才能执行该代码块。

然而，当一个线程访问object的一个synchronized(this)同步代码块时，另一个线程仍然可以访问该object中的非synchronized(this)同步代码块。

尤其关键的是，当一个线程访问object的一个synchronized(this)同步代码块时，其他线程对object中所有其它synchronized(this)同步代码块的访问将被阻塞。同样适用其它同步代码块。也就是说，当一个线程访问object的一个synchronized(this)同步代码块时，它就获得了这个object的对象锁。结果，其它线程对该object对象所有同步代码部分的访问都被暂时阻塞。

这里的关键之处在于，这个object的对象锁只有一把，一把锁对应一个线程。

### transient **短暂（？？？？）**

transient 关键字可以应用于类的成员变量，以便指出该成员变量不应在包含它的类实例已序列化时被序列化。

当一个对象被串行化的时候，transient型变量的值不包括在串行化的表示中，然而非transient型的变量是被包括进去的。

Java的serialization提供了一种持久化对象实例的机制。当持久化对象时，可能有一个特殊的对象数据成员，我们不想用serialization机制来保存它。为了在一个特定对象的一个域上关闭serialization，可以在这个域前加上关键字transient。

transient是Java语言的关键字，用来表示一个域不是该对象串行化的一部分。当一个对象被串行化的时候，transient型变量的值不包括在串行化的表示中，然而非transient型的变量是被包括进去的。

### volatile易失

volatile 关键字用于表示可以被多个线程异步修改的成员变量。

注意：**volatile 关键字在许多 Java 虚拟机中都没有实现。 volatile 的目标用途是为了确保所有线程所看到的指定变量的值都是相同的。**

Volatile修饰的成员变量在每次被线程访问时，都强迫从主内存中重读该成员变量的值。而且，当成员变量发生变化时，强迫线程将变化值回写到主内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。**

**Java语言规范中指出：**

为了获得最佳速度，允许线程保存共享成员变量的私有拷贝，而且只当线程进入或者离开同步代码块时才与共享成员变量的原始值对比。

这样当多个线程同时与某个对象交互时，就必须要注意到要让线程及时的得到共享成员变量的变化。

而volatile关键字就是提示VM：对于这个成员变量不能保存它的私有拷贝,而应直接与共享成员变量交互。

使用建议：在两个或者更多的线程访问的成员变量上使用volatile。当要访问的变量已在synchronized代码块中，或者为常量时，不必使用。

由于使用volatile屏蔽掉了VM中必要的代码优化，所以在效率上比较低，因此一定在必要时才使用此关键字。

Java 语言中的 volatile 变量可以被看作是一种 “程度较轻的 synchronized”；与 synchronized 块相比，volatile 变量所需的编码较少，并且运行时开销也较少，但是它所能实现的功能也仅是 synchronized 的一部分。

# 数组

## 语法格式

数据类型[] 数组名; 数据类型 数组名[]

## 数组在内存中的存储

一段连续的内存空间，int数组默认值为0

## 增强型for循环

int[] arr = {1,2,3,4,5}

for(int n:arr)

System.out.println(n);

## 声明二维数组

列数可以省略，行数不能省略

![img](java_imgs\MnFkCfhFNRL.gif)

## 方法

1. 可变参数列表：

一个方法中，只能有一个可变参数列表作为参数；在方法的参数列表中，如果有两个以上的参数，可变参数列表一定是放在最后。

public void sum(int... n){}

2. 可以将数组传递给可变参数列表：

但数组作为参数时，不能将多个值传递给数组。

3. 可变参数列表所在的方法是最后被访问的。
4. 文档注释：

通过命令去执行，可以将注释中的内容提取出来，生成java的帮助文档

# 面向对象

## 单一功能原则：

一个类只有一个功能。

## 实例化对象的过程可以分为两部分

①声明对象：Cat one

在栈中开辟一片新的空间，空间内没有内容

![img](java_imgs\fRtRVKzjk9i.gif)

②实例化对象：new Cat()

在堆中开辟一片新的空间，完成了相关的初始化操作

![img](java_imgs\GeXG0sfU9fb.gif)

③Cat one = new Cat();

将声明的对象指向实例化的具体的空间

## 构造方法

构造方法是不能被对象单独调用的，必须配合new关键字。

当没有指定构造方法时，系统会自动添加无参的构造方法

当有指定构造方法，无论是有参、无参的构造方法，都不会自动添加无参的构造方法

一个类中可以有多个构造方法

构造方法在类内不能被普通方法调用，构造方法只能在构造方法之间被调用

通过this调用构造方法，必须放在方法体内第一行

# 继承

## 方法重载与方法重写的区别

**方法重载**

在同一个类中

方法名相同，参数列表不同（参数顺序、个数、类型）

方法返回值、访问修饰符任意

与方法的参数名无关

**方法重写：**

有继承关系的子类中

方法名相同，参数列表相同（参数顺序、个数、类型），方法返回值相同

访问修饰符，访问范围需要大于等于父类的访问范围

与方法的参数名无关

## 继承中的构造方法

- 父类的构造方法不允许被继承，不允许被重写
- 子类构造默认调用父类无参构造方法
- 调用父类构造方法的语句必须在子类构造方法的第一行

## **继承后初始化的顺序**

父类静态成员

子类静态成员

父类对象构造

子类对象构造

## 继承中的关键字

**private、public、protected**

- 访问修饰符不影响成员加载顺序，跟书写位置有关

 **super关键字**

- 访问父类成员方法 super.print();

- 访问父类属性 super.name;

- 访问父类构造方法 super();

**this**

- 不能在静态方法中调用。

**final**

- 编写过程中final和public是可以互换的，只要都写在class前面就可以
- final 关键字可以用于成员变量、本地变量、方法以及类
- final 类中的成员属性：一旦初始化不能修改，如果定义的同时没有初始化，则初始化位置只能在构造函数、构造代码块。
- 不能够对 final 变量再次赋值
- 本地变量必须在声明时赋值
- 在匿名类中所有变量都必须是 final 变量
- final 方法不能被重写
- final 类不能被继承
- 接口中声明的所有变量本身是 final 的
- final 和 abstract 这两个关键字是反相关的，final 类就不可能是 abstract 的
- 没有在声明时初始化 final 变量的称为空白 final 变量(blank final variable)，它们必须在构造器中初始化，或者调用 this() 初始化，不这么做的话，编译器会报错final变量(变量名)需要进行初始化
- 按照 Java 代码惯例，final 变量就是常量，而且通常常量名要大写
- 对于集合对象声明为 final 指的是引用不能被更改
- final方法：该方法不允许被子类重写，允许正常被子类继承使用
- final修饰的引用数据类型，不能修改它的引用，可以修改属性值。
- final不可以修饰构造方法
- final方法内的局部变量：只要在具体被使用之前进行赋值即可，一旦赋值不允许被修改
- 拓展：https://developer.aliyun.com/article/723832（没看懂）

# 多态

1. 多态分两种：

   - 编译时多态：设计时多态方法重载

   - 运行时多态：程序运行时动态决定调用哪个方法
     大多数是运行时多态

2. 多态的必要条件：

   - 满足继承关系

   - 父类引用指向子类对象


3. instanceof 判断左边对象是否为右边类 的实例
   返回true/false
   cat0 instanceof Cat

4. java中只支持单继承，即一个子类只有一个父类

5. 父类中的成员变量和接口中的常量重名时，子类无法自动解析
   父类中的函数与接口中的函数重名时，子类会使用父类的函数、

6. 接口可以同时继承自两个父类

7. 静态外部类对象可以不依赖于内部类，直接使用，静态方法之间才能够直接调用

# 封装

1. 建议采用"import 包名.类名的方式加载，提高效率"

加载类的顺序跟import导入语句的位置无关，会先找能够直接解析到的那个类

比如com.immoc.下有mechanics.Cat和animal.Cat 语句：      import com.imooc.mechanics.*     import com.imooc.animal.Cats 会先加载com.imooc.animal.Cats

2. static 为类对象共享，在类加载时产生，销毁时释放，生命周期长

可以有静态属性、静态方法，没有静态类，没有方法中的静态局部变量

在成员方法中可以直接访问静态成员

静态方法只能访问静态成员（属性、方法），只能通过对象实例化后，对象.成员方法的方式访问非静态成员

-static + 属性/方法/类/方法内局部变量/代码块

3. 静态块和构造块

静态块：用static申明，JVM加载类时执行，仅执行一次

构造块：类中直接用{}定义，每一次创建对象时执行

例子

```java
public class Study_static {
    //静态对象    
    public static char text = 'a';      
    //构造函数    
    public Study_static(){            
        System.out.println('c');    
    }     
    //构造块  
    {                     
        System.out.println('b');   
    }     
    //静态块  
    static{                   
        System.out.println(text);  
    }     
    //执行入口    
    public static void main(String[] args){      
        Study_static a = new Study_static();     
    } 
}
```

4. 不同代码块中可以使用同样命名的变量，采用就近原则。同一代码块结束后，数据被回收。

int temp=14; {     int .temp=12;     System.out.printlnC"我是普通代码块1，temp="+temp);}//普通代码块     System. out.println(name +"快跑,temp="+temp; {     int temp=13;     System.out.println("我是普通代码块2，temp="+temp);//普通代码块 }

代码块外的变量作用域是整个类/方法体

5. 定义包：package 包名;

必须放在Java源文件的第一行

一个Java源文件中只能有一个package语句

包名全部英文小写

命名方法：域名倒序+模块+功能

# 注解

注解，按照运行机制分：
源码注解：注解只在源码中存在，编译成.class文件就不存在了
编译时注解：注解在源码和.class文件中都存在
运行时注解：在运行阶段还起作用，甚至会影响运行逻辑的注解
按照来源分：
来自JDK的注解
来自第三方的注解
我们自己定义的注解
还有：
元注解

# 常用类

## Object类

Object类是所有类的父类

### 方法和方法的作用

Java面试中经常会被问到Object类的具有哪些方法以及每个方法的作用。这个题目很好的考察了面试者的Java基础，使得面试者都能有话说，但是想回答完全却还是很难的。 Object类中的方法如下图所示。 上图中的这些方法中除了registerNatives方法用于注册本地方法，不常考之外，其他都有可能详细考察，下面针对这些方法一一讲解。 

**getClass方法** 

可以返回这个实体的Class对象，可以用来获得这个类的元数据。在反射中经常使用。 

**clone方法** 被用来拷贝一个新对象。在Java中使用等号只是拷贝对象的引用并不是对象，需要拷贝对象的时候，可以借助clone方法。 要通过clone方法复制某一个对象，在该类中必须实现java.lang.Cloneable接口。 

下面的代码将演示浅拷贝。 

```java
public class Province {  
    private String name;  
    
    Province(String name){
        this.name = name;
    }  
                                      
	public String getName(){    
        return name;  
    } 
    
    public void setName(String name){    
        this.name = name;  
    }
}

public class Student implements Cloneable {  
    private String name;  
    private int age;  
    private Province province;  
    
    public Student(int age, String name, Province province){    
        this.age = age;    
        this.name = name;    
        this.province = province;  
    }  
    
    public int getAge() {    
        return age;  
    }  
    
    public void setAge(int age) {    
        this.age = age;  
    }  
    
    public String getName() {    
        return name;  
    }  
    
    public void setName(String name) {    
        this.name = name;  
    }  
    
    @Override  
    protected Object clone(){    
        try {      
            return super.clone();    
        } catch (CloneNotSupportedException e) {      
            e.printStackTrace();    
        }    
        return null;  
    }  
    
    public static void main(String[] args) {    
        Province teacher = new Province("Shannxi");    
        Student student1 = new Student(23, "mianjingxiangjie", teacher);    
        Student student2 = (Student) student1.clone();    
        student1.province.setName("Beijing");    
        System.out.println(student1.province.getName());    
        System.out.println(student2.province.getName());  
    }
} 
```

上面的代码输出如下： BeijingBeijing 

可见当实现Cloneable 接口的对象有其他对象的成员变量时，clone方法并不会复制一个新的成员变量。上面的student1和student2使用的是同一个province对象，当更改了student1的province名称，student2的province也相应的改变了。这就是浅拷贝。 那么怎么实现深拷贝呢？ 以上面的例子为例只需要改变clone方法如下：   

```java
@Override  
protected Object clone(){    
    try {      
        Student temp = (Student) super.clone();      
        temp.province
```

### equals与hashcode()的区别

obj1.equals(obj2)

根据《effective java》第七条之规定：在改写equals的时候遵守通用约定

当符合以下条件时不需要重写equals方法：

1. 一个类的每一个实例本质上都是唯一的

2. 不关心一个类是否提供了“逻辑相等”的测试功能

3. 超类已经改写了equals方法，并且从超类继承过来的行为对于子类也是合适的

4. 一个类时私有的或者是package私有的，并且可以确定它的equals方法永远不会被调用。（这种情况下最好将equals方法改写成以下方式：

```java
public boolean equals(Object obj){
	throws new UnsupportOperationException();
}
```

只有当一个类有自己特定的“逻辑相等”概念，而且超类也没有改写equals以实现期望的行为，我们需要改写equals方法。通常适用于“值类”。

在改写equals方法时，也要遵守他们的通用约定（equals方法实现了**等价关系**）：

1. 自反性：x.equals(x) = true;

2. 对称性：如果有x.equals(y) = true,那么一定有y.equals(x) = true;

3. 传递性：对任意的x,y,z。如果有x.equals(y) = y.equals(z) = true,那么一定有x.equals(z)= true;

4. 一致性：无论多少次调用，x.equals(y)总会返回相同的结果。

5. 非空性（暂定）：所有的对象都必须！=null;

上面的只是理论性的说法，更加具体的做法如下：

1. 使用==操作符检查“实参是否为指向对象的一个引用”，如果是则返回true；

2. 使用instanceof操作符检查“实参是否为正确的类型”，如果不是，则返回false;

3. 将实参装换为正确的类型；

4. 对于该类中的每一个关键域，检查实参中的域与当前对象中对应的域是否匹配。如果所有测试都成功，则返回true，否则返回false。

5. 方法完成之后，确定equals方法的对称性，传递性，一致性。

一些忠告：

1. 改写equals方法的时候，必须改写hashCode方法；

2. 不要把equals声明中的Object对象替换为其他类型；

改写的形式必须为:

public boolean equals（Object obj）{...code segment...}

根据《effective java》第八条：改写equals时总要改写hashCode

hashCode的通用约定如下：

1. 只要对象equals方法涉及到的关键域内容不改变，那么这个对象的hashCode总是返回相同的整数。（如果关键域内容改变，则hashCode返回的整数就可以改变）。

2. 如果两个对象的equals(Object obj)方法时相等的，那么调用这两个对象中的任意一个对象的hashCode方法必须产生相同的整数结果。如果两个对象equals方法不同，那么必定返回不同的hashCode整数结果。（简而言之：相等的对象必须有相等的散列码即hashCode）；

一个好的hashCode方法趋向于“为不相等的对象产生不相等的散列码”理想情况下的散列函数应该把一个集合中不相等的实例均匀分布到所有可能的散列值上。下面给出一种参考方法：

1. 把某个非零常数值保存在一个叫做result的int类型的变量中

2. 为该对象中的每一个关键域f计算int类型的散列码。

​		a)   为该域计算int类型的散列码c：

​			i.如果域是Boolean类型，计算：(f?0:1)

​			ii.如果是byte,char,short,int类型，计算：(int)f

​			iii.如果是long类型，计算：(int)(f^(f>>32))

​			iv.如果是float类型，计算：Float.floatToIntBits(f)

​			v.如果是double类型，计算Double.doubleToLongBits(f)得到long类型的值，在按照long值对待，继续进一步计算

​			vi.如果是对象引用，递归调用hashCode方法计算，如果遇到为null的关键域，则返回0

​			vii.如果是数组，将每一个元素都当做单独的域来计算，递归应用上述规则

​		b)   按照下面公式，将a得到的散列码c组合到result中

​			result = 37*result + c;

3. 返回result

4. 写完之后，检查hashCode方法是否相等的实例具有相等的散列码，并找出错误原因。

## 包装类

![image-20220311083703567](java_imgs\1OO9vltqlKl.png)

![image-20220311083714605](java_imgs\bmNvcSILh72.png)

包装类对象的初始值为null

# 字符串

## String

特点：

- **不可变性**：`String`对象是不可变的，一旦创建，其值就不能改变。如果需要对字符串进行修改，实际上会创建一个新的`String`对象。
- **线程安全**：由于不可变性，`String`是线程安全的，可以在多个线程中安全使用而无需同步。

![image-20220311084214891](java_imgs\Zzf0gscWg1b.png)

## String的常用方法

![image-20220311083814534](java_imgs\vmU17g7mm3g.png)



## StringBuffer

特点：

- **可变性**：`StringBuffer`对象是可变的，可以对其内容进行修改而不创建新的对象。
- **线程安全**：`StringBuffer`是同步的，所有方法都被` synchronized`修饰，所以它是线程安全的，但同步导致性能开销较大。

## StringBuilder

特点：

- **可变性**：`StringBuilder`与`StringBuffer`类似，都是可变的。
- **非线程安全**：`StringBuilder`不是同步的，所以在单线程环境下性能比`StringBuffer`高。
- **性能优越**：因为没有同步开销，`StringBuilder`在单线程操作字符串时比`StringBuffer`更快。

## StringBuffer和StringBuilder的常用方法

1. **append()**：添加字符串到末尾
2. **insert()**：在指定位置插入字符串
3. **replace()**：替换指定范围内的字符串
4. **delete()**：删除指定范围内的字符
5. **deleteCharAt()**：删除指定位置的字符
6. **reverse()**：反转字符串
7. **setCharAt()**：修改指定位置的字符
8. **substring()**：获取子字符串
9. **toString()**：转换为 `String`

# 集合

集合长度是动态改变的

集合的应用场景：
- 无法预测存储数据的数量
- 同时存储具有一对一关系的数据
- 需要进行数据的增删
- 数据重复问题

![image-20220311085230509](java_imgs\VTtSWvxrlOr.png)

![image-20220311085242080](java_imgs\EJeH07hpUIX.png)

## List

- List是元素有序并且可以重复的集合，称为序列

- List可以精确的控制每个元素的插入位置，或删除某个位置的元素

- List的两个主要实现类是ArrayList和LinkedList

###  ArrayList

- ArrayList底层是由数组实现的
- 动态增长，以满足应用程序的需求
- 在列表尾部插入或删除数据非常有效
- 更适合查找和更新元素
- ArrayList中的元素可以为null

List&ArrayList的区别https://www.geeksforgeeks.org/difference-between-list-and-arraylist-in-java/

| List                                                         | ArrayList                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| List is an interface                                         | ArrayList is a class                                         |
| List interface extends the Collection framework              | ArrayList extends AbstractList class and implements List interface |
| List cannot be instantiated.                                 | ArrayList can be instantiated.                               |
| List interface is used to create a list of elements(objects) that are associated with their index numbers. | ArrayList class is used to create a dynamic array that contains objects. |
| List interface creates a collection of elements that are stored in a sequence and they are identified and accessed using the index. | ArrayList creates an array of objects where the array can grow dynamically. |

##  set

- 元素无序且不可重复的集合

###  HashSet

-  一种set

- 只允许一个null元素

- 具有良好的存取和查找性能

##  Map

- Map中的数据是以键值对（key-value）的形式存储的

- key-value以Entry类型的对象实例存在

- 可以通过key值快速地查找value

- 一个映射不能包含重复的键

##  HashMap

- 允许使用null值和null键，null键只能有一个

- key值不允许重复

- Entry对象是无序排列的

## 迭代器Iterator

![image-20220311085629631](java_imgs\6AILi3CpjSQ.png)

![image-20220311085642158](java_imgs\bRPUIZ4wyYf.png)

![image-20220311085652195](java_imgs\ads2oV3PASp.png)

## 比较器Comparator

![image-20220311085712671](java_imgs\rXC2sw6KsoX.png)

![image-20220311085727337](java_imgs\ehqxq95Ps68.png)

![image-20220311085736171](java_imgs\JkkUgtiUdbQ.png)

![image-20220311085746893](java_imgs\EAUCiciiWUW.png)



#  文件读写

 

![clipboard.png](java_imgs\qWGBUmw8tQa.gif)

 

![clipboard.png](java_imgs\oNJS4uDMw8j.gif)

相对目录：..返回到上一级目录，默认在工程目录下

 

![clipboard.png](java_imgs\VGFGfR4oX8T.gif)

 

![clipboard.png](java_imgs\MYcP3awabNx.gif)

 

![clipboard.png](java_imgs\KLWF2yUHDzB.gif)

 

![clipboard.png](java_imgs\eqb2THuygpL.gif)

 

![clipboard.png](java_imgs\IsyY9vqJreO.gif)

 

![clipboard.png](java_imgs\ETzEhXWou2d.gif)

 

![clipboard.png](java_imgs\fxyjhgwnlAZ.gif)

 

时间戳转换为时间

https://www.runoob.com/java/date-timestamp2date.html