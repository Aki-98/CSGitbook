Java反射机制是Java语言被视为准动态语言的关键性质。Java反射机制的核心就是允许在运行时通过Java Reflection APIs来取得已知名字的class类的相关信息，动态地生成此类，并调用其方法或修改其域（甚至是本身声明为private的域或方法）。

# Class类

调用Object对象的getClass方法可以获得一个对象的类型，此函数返回的就是一个Class类

# 得到Class类对象的方法

| Class object 诞生管道                          | 示例                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| 运用getClass()注：每个class 都有此函数         | String str = "abc";Class c1 = str.getClass();                |
| 运用Class.getSuperclass()                      | Button b = new Button();Class c1 = b.getClass();Class c2 = c1.getSuperclass(); |
| 运用static methodClass.forName()（最常被使用） | Class c1 = Class.forName ("java.lang.String");Class c2 = Class.forName ("java.awt.Button");Class c3 = Class.forName ("java.util.LinkedList$Entry");Class c4 = Class.forName ("I");Class c5 = Class.forName ("[I"); |
| 运用.<br />class 语法                          | Class c1 = String.class;Class c2 = java.awt.Button.class;Class c3 = Main.InnerClass.class;Class c4 = int.class;Class c5 = int[].class; |
| 运用primitive wrapper classes的TYPE 语法       | Class c1 = Boolean.TYPE;Class c2 = Byte.TYPE;Class c3 = Character.TYPE;Class c4 = Short.TYPE;Class c5 = Integer.TYPE;Class c6 = Long.TYPE;Class c7 = Float.TYPE;Class c8 = Double.TYPE;Class c9 = Void.TYPE; |

# 获得Class类对象的基本信息

| Java class 内部模块          | Java class 内部模块说明                                      | 相应之Reflection API，多半为Class methods。                  | 返回值类型(return type) |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------- |
| package                      | class隶属哪个package                                         | getPackage()                                                 | Package                 |
| import                       | class导入哪些classes                                         | 无直接对应之API。可间接获取。                                |                         |
| modifier                     | class（或methods, fields）的属性                             | int getModifiers()Modifier.toString(int)Modifier.isInterface(int) | intStringbool           |
| class name or interface name | class/interface                                              | 名称getName()                                                | String                  |
| type parameters              | 参数化类型的名称                                             | getTypeParameters()                                          | TypeVariable <Class>[]  |
| base class                   | base class（只可能一个）                                     | getSuperClass()                                              | Class                   |
| implemented interfaces       | 实现有哪些interfaces                                         | getInterfaces()                                              | Class[]                 |
| inner classes                | 内部classes                                                  | getDeclaredClasses()                                         | Class[]                 |
| outer class                  | 如果我们观察的class 本身是inner classes，那么相对它就会有个outer class。 | getDeclaringClass()                                          | Class                   |

# 类中最重要的三个信息

构造函数 > 成员函数 > 成员变量

之前提到的信息都是只读的，这三个信息可以在运行时被调用（构造函数和成员函数）或者被修改（成员变量）。

## 构造函数

获取构造函数的方法有以下几个：

- Constructor getConstructor(Class[] params) 

- Constructor[] getConstructors()

- Constructor getDeclaredConstructor(Class[] params) 

- Constructor[] getDeclaredConstructors()

当知道构造函数的参数时，可以利用getConstructor(Class[] params) 和getDeclaredConstructor(Class[] params)获得唯一确定的构造函数；

当不知道构造函数的参数时，可以利用getConstructors()和getDeclaredConstructors()获得所有的构造函数。

getConstructor(Class[] params) 和getConstructors()仅仅可以获取到public的构造函数；

而getDeclaredConstructor(Class[] params) 和getDeclaredConstructors()则能获取所有（包括public和非public）的构造函数。

## 成员函数

获取成员函数的方法有以下一些：

- Method getMethod(String name, Class[] params)

- Method[] getMethods()

- Method getDeclaredMethod(String name, Class[] params) 

- Method[] getDeclaredMethods() 

其中需要注意，String name参数，需要写入方法名。关于访问权限和确定性的问题，和构造函数基本一致。

## 成员变量

成员变量，我们经常叫做一个对象的域。从内存的角度来说，构造函数和成员函数都仅仅是Java对象的行为或过程，而成员变量则是真正构成对象本身的细胞和血肉。简单的说，就是成员变量占用的空间之和几乎就是对象占用的所有内存空间。

获取成员变量的方法与上面两种方法类似，具体如下：

- Field getField(String name)

- Field[] getFields()

- Field getDeclaredField(String name)

- Field[] getDeclaredFields()

其中，String name参数，需要写入变量名。关于访问权限和确定性的问题，与前面两例基本一致。

# 让动态真正动起来

动态语言是指在程序运行时可以改变其结构：新的函数可以被引进，已有的函数可以被删除等在结构上的变化。

Java不能算作动态语言，但是和C、C++等纯静态语言相比，java语言允许使用者在运行时加载、探知、使用编译期间完全位置的classes，所以说算是“准动态语言”。

反射机制如何让Java动起来？

## 创生

获取构造函数的方法返回Constructor类

Constructor支持泛型，也就是它本身应该是Constructor<T>。这个类有一个public成员函数，T newInstance(Object... args)，其中args为对应的参数。

## 行为

利用Object invoke(Object receiver, Object... args) 可以调用对象的成员函数。

object.method()这种调用方式是为了表明具体method()的调用对象。而invoke(Object receiver, Object... args)的第一个参数正是指明调用对象。在C++中，object.method()其实是有隐含参数的，那就是object对象的指针，method原型的第一个参数其实是this指针，于是原型为method(void* this)

如果某个方法是Java类的静态方法，那么Object receiver参数可以传入null，因为静态方法不从属于对象。

## 属性

java传输一个对象时可以利用Java对象序列化接口。记录对象的属性然后再远程恢复。

Field类有两个public方法，分别对应对象属性的读与写，它们是：

- Object get(Object object)

- void set(Object object, Object value)

# 关于反射的一些高级话题

Java反射中对数组做过单独的优化处理，具体可查看java.lang.reflect.Array类；还有关于泛型的支持，可查看java.lang.reflect.ParameterizedType及相关资料。

## Android编译期问题

Android的安全权限问题我把它简单的划分成三个层次，最不严格的一层就是仅仅骗过编译器的“@hide”标记。对于一款开源的操作系统而言，并不具备安全上的限制，方便硬件厂商做闭源的二次开发。

## 软件的解耦合

配置文件 + ClassLoader + 反射机制结合形成的这种软件解耦和方式

## 反射安全

作为Java的安全模型，它包括了：字节码验证器、类加载器、安全管理器、访问控制器等一系列的组件。之前文中提到过，我把Android安全权限划分为三个等级：第一级是针对编译期的“@hide”标记；第二级是针对访问权限的private等修饰；第三级则是以安全管理器为托管的Permission机制。

Java反射确实可以访问private的方法和属性，这是绕过第二级安全机制的方法（之一）。它其实是Java本身为了某种目的而留下的类似于“后门”的东西，或者说是为了方便调试？不管如何，它的原理其实是关闭访问安全检查。

Field、Method和Constructor类，它们都有一个共同的父类AccessibleObject 。AccessibleObject 有一个公共方法：void setAccessible(boolean flag)。正是这个方法，让我们可以改变动态的打开或者关闭访问安全检查，从而访问到原本是private的方法或域。另外，访问安全检查是一件比较耗时的操作，关闭它反射的性能也会有较大提升。

不要认为我们绕过了前两级安全机制就沾沾自喜了，因为这两级安全并不是真正为了安全而设置的。它们的作用更多的是为了更好的完善规则。而第三级安全才是真正为了防止恶意攻击而出现的。在这一级的防护下，可能都无法完成反射（ReflectPermission），其他的一切自然无从说起。

