# Smail

## Smali语法

[Smali--Dalvik虚拟机指令语言-->【android_smali语法学习一】](https://blog.csdn.net/wdaming1986/article/details/8299996)

一个简单的Activity代码如下：

```java
public class SmaliActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_smail);

        initView();
    }

    private void initView() {
        int num = 2 + 3;
        String name = "zhangsan";
        Log.w("xfhy666", "initView: num = " + num + "  name = " + name);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
    }
}
```

它的smali代码如下：

```java
# 这里简单介绍了类的名称,父类是谁
.class public Lcom/xfhy/allinone/smali/SmaliActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "SmaliActivity.java"

# direct methods 从这里开始的都是在当前类定义的方法
# .method 表示这是一个方法
# 这里定义的是当前类的不带参数缺省的构造方法,末尾的V表示方法返回类型是void
.method public constructor <init>()V
    # .locals 表示当前方法需要申请多少个寄存器
    .locals 0

    .line 16
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method

.method private initView()V
    .locals 4

    .line 27
    const/4 v0, 0x5

    .line 28
    .local v0, "num":I
    const-string v1, "lisi"

    .line 29
    .local v1, "name":Ljava/lang/String;
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "initView: num = "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v3, "  name = "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const-string v3, "xfhy666"

    invoke-static {v3, v2}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    .line 30
    return-void
.end method


# virtual methods  从这里开始的都是覆写父类的方法
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .line 20
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 21
    const v0, 0x7f0b001f

    invoke-virtual {p0, v0}, Lcom/xfhy/allinone/smali/SmaliActivity;->setContentView(I)V

    .line 23
    invoke-direct {p0}, Lcom/xfhy/allinone/smali/SmaliActivity;->initView()V

    .line 24
    return-void
.end method

.method protected onDestroy()V
    .locals 0

    .line 35
    invoke-super {p0}, Landroidx/appcompat/app/AppCompatActivity;->onDestroy()V

    .line 36
    return-void
.end method
```

上面的这份smali代码就比Java代码多了一个缺省的构造方法.然后每个方法的开始是以`.method`开始的,以`.end method`结束.

[Smali官方文档](https://source.android.com/devices/tech/dalvik/dalvik-bytecode)

Davlik字节码中,寄存器是32位,一般的类型用一个寄存器就够存了.只有64位类型的需要2个寄存器来存储,Long和Double就是64位类型的.

**原始数据类型**

| 类型表示 | 原始类型      |
| -------- | ------------- |
| v        | void          |
| Z        | boolean       |
| B        | byte          |
| S        | short         |
| C        | char          |
| I        | int           |
| J        | long (64位)   |
| F        | float         |
| D        | double (64位) |

**对象类型**

| 类型表示            | Java中的类型 |
| ------------------- | ------------ |
| Ljava/lang/String;  | String       |
| Landroid/os/Bundle; | Bundle       |

- 对象类型的前面会加一个L
- 末尾会加一个`;`
- 包名全路径,中间以`/`分隔

**数组**

| 类型表示            | Java中的类型 |
| ------------------- | ------------ |
| [I                  | int[]        |
| `[[I`               | `int[][]`    |
| [Ljava/lang/String; | String[]     |

**方法定义**

| 类型表示                                              | Java中的表示                                   |
| ----------------------------------------------------- | ---------------------------------------------- |
| public getDouble()D                                   | public double getDouble()                      |
| public getNum(ILjava/lang/String;Z)Ljava/lang/String; | public String getNum(int a,String b,boolean c) |

```
.method public getDouble()D
    .locals 2

    .line 45
    const-wide/16 v0, 0x0

    return-wide v0
.end method
```

**字段定义**

| 类型表示                                        | Java中的表示            |
| ----------------------------------------------- | ----------------------- |
| .field private num:I                            | private int num         |
| .field public text:Ljava/lang/String;           | public String text      |
| .field private tvName:Landroid/widget/TextView; | private TextView tvName |

可以看到在字段定义的前面会加一个关键字`.field`,然后修饰符+名称+`:`+类型.

**指定方法寄存器个数**

一个方法中需要多少个寄存器是需要指定好的.有2种方式

- `.registers` 指定方法寄存器总数
- `.locals` 表名方法中非参寄存器的总数,一般在方法的第一行

```
.method public getNum(ILjava/lang/String;Z)Ljava/lang/String;
    .registers 6
    .param p1, "a"    # I
    .param p2, "b"    # Ljava/lang/String;
    .param p3, "c"    # Z

    .prologue
    .line 40
    const/4 v0, 0x2

    .line 41
    .local v0, "num":I
    const-string v1, ""

    return-object v1
.end method

.method public getNum(ILjava/lang/String;Z)Ljava/lang/String;
    .locals 2
    .param p1, "a"    # I
    .param p2, "b"    # Ljava/lang/String;
    .param p3, "c"    # Z

    .line 40
    const/4 v0, 0x2

    .line 41
    .local v0, "num":I
    const-string v1, ""

    return-object v1
.end method
```

**方法传参**

方法的形参也会被存储于寄存器中,形参一般被放置于该方法的最后N个寄存器中(eg:形参是2个,那么该方法的最后2个寄存器就是拿来存储形参的). 值得注意的是,非静态方法隐含有一个this参数.

**寄存器命名方式**

命名方式有2种,v命名法(v0,v1...)和p命名法(p0,p1...)

来看一段smali代码加深一下印象

```
.method public getNum(ILjava/lang/String;Z)Ljava/lang/String;
    .locals 2
    .param p1, "a"    # I
    .param p2, "b"    # Ljava/lang/String;
    .param p3, "c"    # Z

    .line 40
    const/4 v0, 0x2

    .line 41
    .local v0, "num":I
    const-string v1, ""

    return-object v1
.end method
```

- 首先通过`.locals 2`表明该方法内有2个v寄存器.
- 然后定义了p1,p2,p3这3个寄存器,其实还有一个p0寄存器,p0表示`this`(即本身的引用,this指针).
- 这个方法里面既有v命名的,也有p命名的
- 只有v命名的寄存器需要在`.locals`处声明个数,而p命名的不需要

**字段定义**

| 标记            | 含义           |
| --------------- | -------------- |
| static fields   | 定义静态变量   |
| instance fields | 定义实例变量   |
| direct methods  | 定义静态方法   |
| virtual methods | 定义非静态方法 |

**控制条件**

| 语句                     | 含义                             |
| ------------------------ | -------------------------------- |
| `if-eq vA, vB, :cond_**` | `如果vA等于vB则跳转到:cond_**`   |
| `if-nevA, vB, :cond_**`  | 如果vA不等于vB则跳转到:cond_**   |
| `if-ltvA, vB, :cond_**`  | 如果vA小于vB则跳转到:cond_**     |
| `if-gevA, vB, :cond_**`  | 如果vA大于等于vB则跳转到:cond_** |
| `if-gtvA, vB, :cond_**`  | 如果vA大于vB则跳转到:cond_**     |
| `if-levA, vB, :cond_**`  | 如果vA小于等于vB则跳转到:cond_** |
| `if-eqz vA, :cond_**`    | 如果vA等于0则跳转到:cond_**      |
| `if-nezvA, :cond_**`     | 如果vA不等于0则跳转到:cond_**    |
| `if-ltzvA, :cond_**`     | 如果vA小于0则跳转到:cond_**      |
| `if-gezvA, :cond_**`     | 如果vA大于等于0则跳转到:cond_**  |
| `if-gtzvA, :cond_**`     | 如果vA大于0则跳转到:cond_**      |
| `if-lezvA, :cond_**`     | 如果vA小于等于0则跳转到:cond_**  |

## Smali插桩（代码注入）

[关于smali插桩](https://www.cnblogs.com/wangaohui/p/5071647.html)

smali修改部分省略

smali代码改好之后保存,然后用apktool工具,打包成apk : `apktool b apkFileName`.

打包完成之后,是不能立即在Android手机上进行安装的,还需要签名.得去下载一个autosign,给这个apk签名,命令是`java -jar signapk.jar testkey.x509.pem testkey.pk8 update.apk update_signed.apk`. 打包好之后,运行到手机上,完美,toast输出的是Skip ad.插桩成功.

可以下载一个Android逆向助手,里面有autosign工具包. 下载地址如下:

链接:https://pan.baidu.com/s/1NW9PAyuar1dWeUfQBQEftg 密码:8nb7

# 工具

## apktool

[官方网站](https://ibotpeaches.github.io/Apktool/)

apktool主要用于逆向apk文件,可以将资源解码,并在修改之后可以重新构建它们.它还可以用来重新构建apk.

**功能**

- 将资源解码成近乎原始的形式(包括resources.arsc, classes.dex, 9.png. 和 XMLs)
- 将解码的资源重新打包成apk/jar
- 组织和处理依赖于框架资源的APK
- Smali调试
- 执行自动化任务

[安装教程](https://ibotpeaches.github.io/Apktool/install/)

**使用**

- 逆向apk文件: `apktool d xx.apk`,逆向之后只能看到代码的smali格式文件,需要学习smali语法才能看懂.
- 重新打包: `apktool b xx`,打包出来的是没有签名的apk,需要签名才能安装

## dex2jar

一个将dex转换成jar的工具,下载下来之后是一个压缩包,里面有很多工具.

使用方式也比较简单,随便举个例子,命令行进入解压之后的文件夹,将待转成jar的dex(假设为classes.dex,拷贝到当前文件夹)准备好.让这些文件全部有执行权限,`chmod +x *`(Windows不需要).然后执行`./d2j-dex2jar.sh classes.dex`即可将dex转成jar(转出来的jar包名字是classes-dex2jar.jar),然后用jd-gui工具即可查看该jar中的class对应的java源码(和原始的源码不太一样哈).

下载地址: https://sourceforge.net/projects/dex2jar/

## jd-gui

jd-gui是一款反编译软件,可以将查看jar中的class对应的java代码.使用方式: 直接将jar文件拖入jd-gui即可,查看里面的class对应的java代码.

jd-gui github : https://github.com/java-decompiler/jd-gui

## jadx

jadx github : https://github.com/skylot/jadx

需要下载jadx的直接到GitHub页面下载最新的Relase包.

jadx就更厉害了,直接将apk文件将其拖入.可得到如下信息:

- 签名的详细信息(类型,版本,主题,签名算法,MD5,SHA-1,SHA-256等等)
- 所有资源文件(比如layout布局文件都是反编译了的,可以直接查看)
- 所有class对应的java代码(未加壳的才行),java代码对应的smali代码也能看.
- so文件

据说,jadx是史上最好用的反编译软件,从使用上来看,确实是这样,操作简单.除了上面提到的功能点外,还有些你可能更喜欢的,比如:

- 导出Gradle工程
- 反混淆
- 代码跳转(Ctrl+鼠标左键)
- 全局搜索文本

## 脱壳

软件脱壳，顾名思义，就是对软件加壳的逆操作，把软件上存在的壳去掉。在一些计算机软件里也有一段专门负责保护软件不被非法修改或反编译的程序。它们一般都是先于程序运行，拿到控制权，然后完成它们保护软件的任务。

说到脱壳,这里简单介绍几个工具

- Xposed 框架
- VirtualXposed
- FDex2

如果手机已经root,则选择Xposed框架+FDex2. 如果手机没有root,则选择VirtualXposed+FDex2.

### Xposed 框架

首先我们得知道什么是Xposed框架?

维基百科: Xposed框架（Xposed framework）是一套开放源代码的、在Android高权限模式下运行的框架服务，可以在不修改APK文件的情况下修改程序的运行（修改系统），基于它可以制作出许多功能强大的模块，且在功能不冲突的情况下同时运作。这套框架需要设备解锁了Bootloader方可安装使用（root为解锁Bootloader的充分不必要条件，而xposed安装仅需通过TWRP等第三方Recovery卡刷安装包而不需要设备拥有完整的root权限）。

Xposed框架非常非常牛皮,可以安装各种插件(xposed插件,这里有很多 https://www.xda.im/),比如自动抢红包、防撤回、步数修改等等各种骚操作.就是Xpose框架的安装非常麻烦.安装教程这里就不说了,每个手机可能不太一样.我记得我的手机当时解锁BootLoader,刷机啥的,麻烦.

传统的Xposed框架只支持到Android N,后续的Android版本可以使用[EdXposed](https://github.com/ElderDrivers/EdXposed)替代.

### VirtualXposed

> 官网: https://vxposed.com/

VirtualXposed也非常牛逼,它看起来提供了一个虚拟的安卓环境,但它其实是一个app.它提供Xposed框架环境,而不需要将手机root,不需要解锁BootLoader,也不需要刷机.Xposed模块提供了超多应用、游戏的辅助,但是苦于Xposed框架安装的麻烦很多用户只能放弃,VirtualXposed最新版让用户可以非常方便地使用各种Xposed模块.

### FDex2

FDex2是Xposed的一个插件,用来从运行中的app中导出dex文件的工具.

使用:首先安装FDex2这个apk,然后在Xposed框架中勾选这个插件,然后手机重启.进入FDex2,点击需要脱壳的应用,然后FDex2会展示该app脱壳之后的dex输出目录.然后去运行那个需要脱壳的app,就可以获得该app对应的dex.然后导出dex到电脑上,用jadx查看反编译的代码.

当然,FDex2不一定能成功.

## 开发者助手

这个工具特别厉害,但是大部分功能是需要root权限才能使用的.主要功能如下:

- 实时查看任何应用数据库和SP
- 网络请求信息
- log输出
- 当前Activity或者Fragment
- 界面资源分析(可以查看那个控件是什么做的)

apk酷安下载地址: https://www.coolapk.com/apk/com.toshiba_dealin.developerhelper

从应用详情里面看到,开发者助手还有电脑版本,功能也不少

- 支持了大部分手机版开发者助手的功能
- 支持截图到电脑
- 支持全局debug开启 (动态调试用)
- 支持进程优先级查看
- 更稳定的当前包名/activity名/fragment名获取

开发者助手电脑版下载链接：https://pan.baidu.com/s/1MFagBWVbR1xNDMakWUlv5g 提取码：l4hv

## 其他

大概的工具就是上面这些了,勉强够用了.还有些其他的工具我也一并放入下面的下载链接里面了.

链接:https://pan.baidu.com/s/1kuoJ83vob13SM971mIwrmw 密码:lc6p

这里有一个库,里面关于安卓应用的安全和破解讲解的很全面,喜欢的可以去看看. https://github.com/crifan/android_app_security_crack

# 流程

（2020）

## 1. 反编译基操

### 1.1 借鉴code

一般来说,如果只是想借鉴一下友商的code,我们只需要拿到对方的apk,拖到jadx里面就行.jadx能查看apk的xml布局和java代码.jadx有时候会出现部分class反编译失败的情况,这时可以试试Bytecode-Viewer,它也能反编译, 而且还能反编译出jadx不能反编译的class.但是如果apk是已加固了的,那么jadx是不能查看代码的.这时需要脱壳,然后再进行反编译.

### 1.2 修改执行逻辑

如果是想修改程序的执行逻辑,则需要修改smali代码.

如何拿smali代码? 这时需要用到apktool,使用命令:`apktool d xx.apk`即可将apk逆向完成,拿到smali代码.这里如果反编译失败了且报错`org.jf.dexlib2.dexbacked.DexBackedDexFile$NotADexFile: Not a valid dex magic value: cf 77 4c c7 9b 21 01 cd`,则试试`apktool d xx.apk -o xx --only-main-classes`这条命令.

然后用VS Code打开,这里最好在VS Code里面装一个`Smali`插件,用于在VS Code里面支持smali语法,高亮之类的.完成之后大概是这个样子:

![img](Android反编译_imgs\20200909163611.png)

环境倒是OK了,回到正题,我们需要修改执行逻辑.在此之前,我们最好先简单学习一下smali的基本语法,详情见我之前写过的文章[反编译基础知识](https://blog.csdn.net/xfhy_/article/details/107026357).

修改好逻辑之后,我们需要将这些代码重新打包成apk,此时需要用到apktool,执行:`apktool b xx`.执行完成之后,输出的apk会在`xx/dist`目录下.它打包出来的是没有签名的apk,需要签名才能安装.

签名需要用到autosign这个工具包,使用命令`java -jar signapk.jar testkey.x509.pem testkey.pk8 debug.apk debug_signed.apk`

## 2. 加日志

有时候,你可能需要在修改原有执行逻辑之后,在代码里面加点日志,方便查看打出来的包逻辑是否正确.这里我摸索出一个简单的方式打日志,写一个日志打印工具类,然后将这个工具类转成smali文件,然后放入apk反编译出来的smali代码文件夹中, 之后就可以在这个项目的任何smali中使用这个工具类了.下面详细介绍一下:

### 2.1 写日志打印工具类LogUtil

这个日志打印工具类是为了外界方便调用的,所以需要让外界调用的时候尽量简单.下面是我简单实现的工具类,tag都是我定义好了的,免得外面再定义一次(麻烦).

```
public class LogUtil {

    public static void logNoTrace(String str) {
        Log.d("xfhy888", str);
    }

    public static void test() {
        logNoTrace("大撒大撒大撒");
    }

}
```

### 2.2 打印调用栈

上面的工具类目前只能打印普通的日志,但是有时我们想在打印日志的同时输出这个地方的调用栈,此时我们再加个方法扩展一下.

```
public static void log(String str) {
        Log.d("xfhy888", str);

        Throwable throwable = new Throwable();
        StackTraceElement[] stackElements = throwable.getStackTrace();
        StringBuilder stringBuilder = new StringBuilder();
        if (stackElements != null) {
            for (StackTraceElement stackElement : stackElements) {
                stringBuilder.append(stackElement.getClassName()).append(" ");
                stringBuilder.append(stackElement.getFileName()).append(" ");
                stringBuilder.append(stackElement.getMethodName()).append(" ");
                stringBuilder.append(stackElement.getLineNumber()).append("\n");
            }
        }
        Log.d("xfhy888", stringBuilder.toString());
    }
```

在log方法中我们手工构建了一个Throwable,然后通过其getStackTrace方法即可得到调用栈信息,通过Log打印出来.效果如下:

```
12817-12817/com.xfhy.demo D/xfhy888: com.xfhy.LogUtil LogUtil.java log 10
com.xfhy.startactivitydemo.MainActivity$1 MainActivity.java onClick 45
android.view.View View.java performClick 6724
android.view.View View.java performClickInternal 6682
android.view.View View.java access$3400 797
android.view.View$PerformClick View.java run 26472
android.os.Handler Handler.java handleCallback 873
android.os.Handler Handler.java dispatchMessage 99
android.os.Looper Looper.java loop 233
android.app.ActivityThread ActivityThread.java main 7210
java.lang.reflect.Method Method.java invoke -2
com.android.internal.os.RuntimeInit$MethodAndArgsCaller RuntimeInit.java run 499
com.android.internal.os.ZygoteInit ZygoteInit.java main 956
```

### 2.3 将工具类转smali

在Android Studio里面写好这个工具类之后,装一个`java2smali`插件.然后选中LogUtil文件,再依次点击`Build->Compile to Smali`,即可将LogUtil.java转成smali.下面是我转好的

```
.class public Lcom/xfhy/LogUtil;
.super Ljava/lang/Object;
.source "LogUtil.java"


# direct methods
.method public constructor <init>()V
    .registers 1

    .prologue
    .line 5
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static log(Ljava/lang/String;)V
    .registers 9
    .param p0, "str"    # Ljava/lang/String;

    .prologue
    .line 8
    const-string v4, "xfhy888"

    invoke-static {v4, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 10
    new-instance v3, Ljava/lang/Throwable;

    invoke-direct {v3}, Ljava/lang/Throwable;-><init>()V

    .line 11
    .local v3, "throwable":Ljava/lang/Throwable;
    invoke-virtual {v3}, Ljava/lang/Throwable;->getStackTrace()[Ljava/lang/StackTraceElement;

    move-result-object v1

    .line 12
    .local v1, "stackElements":[Ljava/lang/StackTraceElement;
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    .line 13
    .local v2, "stringBuilder":Ljava/lang/StringBuilder;
    if-eqz v1, :cond_52

    .line 14
    array-length v5, v1

    const/4 v4, 0x0

    :goto_17
    if-ge v4, v5, :cond_52

    aget-object v0, v1, v4

    .line 15
    .local v0, "stackElement":Ljava/lang/StackTraceElement;
    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getClassName()Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, " "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 16
    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getFileName()Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, " "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 17
    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getMethodName()Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, " "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 18
    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getLineNumber()I

    move-result v6

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, "\n"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 14
    add-int/lit8 v4, v4, 0x1

    goto :goto_17

    .line 21
    .end local v0    # "stackElement":Ljava/lang/StackTraceElement;
    :cond_52
    const-string v4, "xfhy888"

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 22
    return-void
.end method

.method public static logNoTrace(Ljava/lang/String;)V
    .registers 2
    .param p0, "str"    # Ljava/lang/String;

    .prologue
    .line 25
    const-string v0, "xfhy888"

    invoke-static {v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 26
    return-void
.end method
```

有了编译好的smali文件,还需要放到反编译项目的对应包名里面,我这里的是`com/xfhy/`,那我就得放到这个目录下.

### 2.4 使用工具类

这里我随便写个方法测试一下,java代码如下:

```
public void test() {
    for (int i = 0; i < 10; i++) {
        System.out.println(i);
    }
}
```

它所对应的smali代码如下:

```
.method public test()V
    .registers 3

    .prologue
    .line 29
    const/4 v0, 0x0

    .local v0, "i":I
    :goto_1
    const/16 v1, 0xa

    if-ge v0, v1, :cond_d

    .line 30
    sget-object v1, Ljava/lang/System;->out:Ljava/io/PrintStream;

    invoke-virtual {v1, v0}, Ljava/io/PrintStream;->println(I)V

    .line 29
    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    .line 32
    :cond_d
    return-void
.end method
```

我在方法的一开始就打印一句日志,首先加registers个数+1,因为需要新定义一个变量来存字符串,然后再调用LogUtil的静态方法打印这个字符串.

```
.method public test()V
    .registers 4

    const-string v2, "test method"

    invoke-static {v2}, Lcom/xfhy/LogUtil;->log(Ljava/lang/String;)V

    .prologue
    .line 29
    const/4 v0, 0x0

    .local v0, "i":I
    :goto_1
    const/16 v1, 0xa

    if-ge v0, v1, :cond_d

    .line 30
    sget-object v1, Ljava/lang/System;->out:Ljava/io/PrintStream;

    invoke-virtual {v1, v0}, Ljava/io/PrintStream;->println(I)V

    .line 29
    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    .line 32
    :cond_d
    return-void
.end method
```

## 3. 调试smali

我们不能直接调试反编译拿到的java代码,而是只能调试反编译拿到的smali代码.当然,调试的时候,需要懂一些smali的基本语法,这样的话,基本能看懂程序在干嘛.

### 3.1 让App可以调试

首先是让App可以调试

1. 可以修改AndroidManifest.xml中的debuggable改为true(具体操作:先用apktool反编译,再修改AndroidManifest,再打包签名,运行到手机上);
2. 也可以使用[XDebug](https://github.com/deskid/XDebug) 让所有进程处于可以被调试的状态;

### 3.2 如何调试?

首先是在Android Studio里装一个smalidea的插件,我上面分享的网盘地址里面有.我试了下,smalidea是不支持最新版的Android Studio的.我去查了下,smalidea最后一个版本是0.05, 最后更新时间是2017-03-31。确实有点老了,我看18年年末的时候有人在博客中提到了这个插件,于是我想了下,同时期的Android Studio肯定可以用这个插件. 在Android Studio官网一顿乱串之后发现, 官网提供了历史版本的[下载地址](https://developer.android.google.cn/studio/archive#android-studio-3-0?utm_source=androiddevtools&utm_medium=website). 最后下载了一个2018年10月11日的Android 3.2.1,装上插件试了下->可行->完美.

把apktool反编译好的文件夹导入Android Studio,把所有smali开头的文件夹都标记一下Sources Root(标记方法: 文件夹右键,Mark Directory as -> Sources Root).然后找到你需要调试的类,打好断点.

![img](Android反编译_imgs\smalidea打断点.png)

打开需要调试的App,然后打开Android Device Monitor(在`SDK\tools`里面).打开Monitor的时候需要关闭Android Studio.

![img](Android反编译_imgs\Monitor端口号.png)

查看该App对应的端口是多少,记录下来.重新打开Android Studio,编辑`Edit Configurations`,点击`Add New Configuration`,添加之后再修改一下端口号就行,这里的端口号填上面Monitor看到的那个端口号.

![img](Android反编译_imgs\ConfigurationPort.png)

Configuration添加好之后,点击Debug按钮即可进行调试.

![img](Android反编译_imgs\smalidea调试.png)

熟悉的界面,熟悉的调试方式,开始愉快的调试吧,起飞~

