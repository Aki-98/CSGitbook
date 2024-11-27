# Java 调用 C++ 函数

要从Java调用C++函数，你需要进行以下操作:

1. **在Java类中创建一个native方法，此方法被本类其他方法调用**

```
private native void functionName(parameters)
```

2. **创建一个头文件，可以利用javah命令生成**

在头文件中定义它的签名，如下所示：

```
extern "C" {
	JNIEXPORT void JNICALL Java_package_MyClass_functionName(JNIEnv *, jclass);
}
```

接口规范：

```
JNIEXPORT <返回类型> JNICALL Java_<包名>_<类名>_<方法名>(JNIEnv*, <原对象引用>，<参数1>..<参数n>)
```

- extern "C" 只被C++编译器识别，标明此方法利用C的函数命名协议来编译。
- JNIEXPORT 是JNI必要的修饰符。
- 数据类型带有"j"前缀的：jdouble,jobject..等是Java对象或类型在C++中的映射
- JNIEnv* 指向JNI 环境，可以利用其调用所有JNI函数
- jobject 引用当前Java对象

3. **创建一个源文件，实现头文件中定义的接口。实现内容就是Java代码调用的C/C++代码**

4. **编译头文件和源文件生成C/C++动态链接库 .so/.dll 文件**

5. **此native方法所在类，加载动态链接库。因为加载链接库要在执行native方法之前，所以此加载过程一般放在静态初始化块内执行**

```
static {
	System.loadLibrary("libraryName");//库名即可（从java.library.path对应路径下搜索对应名称的库文件并加载）
}
```

或

```
static {
	System.load("libraryFile");//绝对地址 包含路径、库名、后缀
}
```

**总结一下，从Java代码中调用C/C++代码的流程：**

（1）创建一个有native标识的方法，并且从其他Java方法调用它

（2）Java编译器生成字节码

（3）C/C++ 编译器生成动态库  .so文件（Linux）或 .dll文件（Windows）

（4）运行程序，执行字节码

（5）执行到loadLibary或load调用的时候，添加一个 .so文件到这个进程中

（6）执行到native方法的时候，通过方法签名，在已打开的.so文件中进行搜索。

（7）如果链接库内有对应方法，就会被执行，否则程序崩溃

# C代码访问Java对象的实例变量

获取对象的实例变量的步骤：

1. 通过GetObjectClass()方法获得此对象的类引用

2. 通过类引用的GetFieldID()方法获得实例变量的Field ID.

   - 需要提供变量名，字段类型描述符
   - 对于Java 类， 字段描述符格式为 "**L<类全称>;**" 类全称中，点"."用 "/"代替。例如，String 的描述符为"Ljava/lang/String;"    注意：这里不要漏了分号"**;**"
   - 对于基本类型，则有固定标识。注：这里不需要分号。int => "I" ，byte => "B"，short => "S"，long => "J"，float => "F"，double => "D"，char => "C"，boolean => "Z"
   - 对于数组，则结合以上类型描述符，加上前缀"**[**"，

   　　　　　　如Object数组，用"**[**L/java/lang/Object;"表示

   　　　　　　int数组，用"**[**I"表示

3. 基于FieldID，通过GetObjectField()方法或Get<基本类型>Field()方法获取实例变量
4. 如果需要更新实例变量，可以使用SetObjectField()或Set<基本类型>Field()函数进行

jni.h

```
//returns the class of an object
jclass GetObjectClass(JNIEnv *env, jobject obj);

//returns the field ID for an instance variable of a class
jfieldID GetFieldID(JNIEnv *env, jclass cls, const char *name, const char *sig);

//Get/Set the value of an instance variable of an object
//<type> includes each of the eight primitive types plus Object.
NativeType Get<type>Field(JNIEnv *env, jobject obj, jfieldID fieldID);
void Set<type>Field(JNIEnv *env, jobject obj, jfieldID fieldID, NativeType value);
```

# Java调用C语言代码回调Java方法

要想调用实例对象的方法，需要进行以下步骤：

1. 通过对象实例，获取到对象类的引用 => GetObjectClass()
2. 通过类引用，获取到方法ID => GetMethodID() 
   - 需要提供方法名，和方法签名。也就是需要这两个信息来标识确定一个方法
   - 方法签名格式：（参数列表）返回值类型
   - 你可以通过javap命令工具，查看方法的签名

```
private TestCallbackMethods();
descriptor:()V

private native void nativeMethod();
descriptor:()V

private void callback();
descriptor:()V

private void callback(java.lang.String);
descriptor:(Ljava/lang/String;)V

private static java.lang.String callbackStatic();
descriptor:()Ljava/lang/String

public static void main(java.lang.String[]);
descriptor:([Ljava/lang/String;)V

static{};
descriptor:()V
```

3. 基于方法ID，你可以根据返回值类型，调用Call<基本类型>Method()或者CallVoidMethod()或CallObjectMethod()，来调用对应的方法。