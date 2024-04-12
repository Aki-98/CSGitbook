# 介绍

**xUnit**：一套基于测试驱动开发的测试框架，包括了 PythonUint、CppUnit、Junit，分别是 Python、C++、Java的测试框架

**Junit**：Java的面向程序员的测试框架，基于xUnit实现

**wiki**：https://junit.org/junit4

# 使用

## 导入依赖

app/build 下导包

```
dependencies {
	// JUnit 4 framework
	testImplementation 'junit:junit:4.13.2'
	// AndroidJUnitRunner
	testImplementation 'androidx.test:runner:1.2.0'
	// some rules for example ActivityTestRule
	testImplementation 'androidx.test:rules:1.2.0'
	// ext class for junit
	testImplementation 'androidx.test.ext:junit:1.1.1'
	testImplementation 'androidx.test.ext:truth:1.2.0'
}
```

 //前面是 testImplementation

使用Junit5：https://blog.csdn.net/yihanss/article/details/125809714



## 基本使用，断言方法

- 先准备好 原类（被测试类）

  - 注意，被测试的方法是要用 public 修饰，不然调用不到

  - 如下，下面就是几个简单的计算方法

```java
public class Calculator {
    public int add(int a,int b) {
        return a + b;
    }

    public int subtract(int a,int b) {
        return a - b;
    }

    public int multiply(int a,int b) {
        return a * b;
    }

    public int divide(int a,int b) {
        return a / b;
    }
}
```
- <u>鼠标光标移至 **被测试类名** 处，快捷键：Alt + Enter -> 选择 create Test （或者 右击 -> go to -> Test）</u>，然后进行选择一些类的方法、存放路径等信息，完成即可生成 测试类。测试类名是以 Test 作为后缀的，接下来就可以进行一些测试操作了。
  - 关于 测试类 存放的位置
    - AS已经自动帮我们创建好了，如下：

```
app/src
     ├── androidTestjava (仪器化单元测试、UI测试)
     ├── main/java (业务代码)
     └── test/java  (本地单元测试)
```

- 然后编写测试方法，使用 @Test 进行注解，都是 <u>public void 且 无参数</u> 的方法，这里编写测试方法有快捷键：<u>Alt + Insert 即可选择自动生成测试方法等</u>

  - 方法名与原类中的方法名一致，或以 test 为前缀进行命名

  - 使用 Assert 类中的静态方法 assertXxx() 进行测试，又称为断言方法
    - 下面代码中使用的是 assertEquals() 方法，比较实际值（调用 被测试方法的结果）与 期望值（你认为的值）是否相同。相同，Run 通过；不同，控制台提示错误信息（很明显的提示你）

  - 跑程序的时候可以选择是跑一个类（即全部的测试方法），还是指定的方法

```java
public class CalculatorTest {
    private static final String TAG = "TAG";
    private Calculator calculator = new Calculator();

    @Before
    public void setUp() throws Exception {
//        Log.d(TAG,"执行：setUp()");
    }
    
    @After
	public void tearDown() throws Exception {
//        Log.d(TAG,"执行：tearDown()");
}

	@Test
	public void add() {
    	assertEquals(6,calculator.add(3,3));
	}

	···

	@Test
	public void divide() {
   		assertEquals(3,calculator.divide(9,3));
	}
}
```


## 测试套件

测试套件就是<u>组织测试类一起运行</u>

- 写一个空类作为测试套件的入口类

- 使用 @RunWith 注解入口类，指明测试运行器为 Suite 类

  - Suite 是一个标准运行程序，允许您手动构建包含来自多个类的测试的套件

  - 作用就是改变测试运行器

- 使用 @Suite.SuiteClasses 注解入口类，并以数组的形式指明测试类
  - 这里，数组的先后顺序会影响进行测试的先后顺序
    - 按顺序依次执行方法，一个测试类的方法执行完之后才会执行下一个测试类的方法

```java
//测试套件：入口类
@RunWith(Suite.class)
@Suite.SuiteClasses({Test1Test.class,Test2Test.class})
public class Test {

}

//测试套件：测试类一
public class Test1Test {
    @Test
    public void add() {
        assertEquals(5,new Test1().add(2,3));
        System.out.println("测试类Test1Test执行add()方法");
    }

    @Test
    public void subtract() {
        assertEquals(5,new Test1().subtract(5,0));
        System.out.println("测试类Test1Test执行subtract()方法");
    }
}

//测试套件：测试类二
public class Test2Test {
    @Test
    public void add() {
        assertEquals(5,new Test2().add(2,3));
        System.out.println("测试类Test2Test执行add()方法");
    }

    @Test
    public void subtract() {
        assertEquals(5,new Test2().subtract(6,1));
        System.out.println("测试类Test2Test执行subtract()方法");
    }
}
```


## 参数化测试

- 参数化测试允许开发人员使用 不同的值 反复运行 同一个测试

  - 和方法传值类似，一个方法可以调用多次，每次传递不同的值

  - 但是测试方法并没有参数，所以提供了这样一个参数化测试来实现

  - 使用如下

- 使用 @RunWith 注解测试类，并指定属性值为 Parameterized.class
  - Parameterized是实现参数化测试的标准运行程序。运行参数化的测试类时，将为测试方法和测试数据元素的叉积创建实例。

- 然后就是定义你的测试方法所需要的参数值，（期望值 + 断言方法里调用的方法所需的参数值）
- 再编写一个构造方法，使用 @Parameterized.Parameters 进行注解，在构造方法中对定义的变量进行赋值
- 再定义一个 public static 修饰的方法，返回值为 Collection<>，可以指定类型参数（推荐），也可以不指定
  - 在这个方法中定义一个二维数组（一维数组不够），然后使用 Arrays.asList() 方法将数组转换为 List集合，然后返回即可
    - 这里二维数组的元素就是你要进行测试的值
- 至此，就可以正常的进行测试了

```java
@RunWith(Parameterized.class)
public class ParamTestTest {

    private int expected = 0;
    private int input1 = 0;
    private int input2 = 0;

    @Parameterized.Parameters
    public static Collection<Object[]> t() {
        return Arrays.asList(new Object[][]{
                {5,2,3},
                {11,5,6}
        });
    }

    public ParamTestTest(int expected, int input1, int input2) {
        this.expected = expected;
        this.input1 = input1;
        this.input2 = input2;
    }

    @Test
    public void add() {
        assertEquals(expected,new ParamTest().add(input1,input2));
    }
}
```


## 分类测试

- 所谓分类测试，就是将测试代码中的方法进行分类，然后根据类别来选择该跑什么类别的方法，当然，这个时候同一类别的方法肯定是都会执行的
- 主要是 @Category 注解的使用，还包含：@RunWith、@SuiteClasses、@IncludeCategory 这几个注解一起使用
- 一共需要的类数量：原类 + 测试类 + 作标识符的类 + 最后运行的类
  - 原类：提供方法进行测试
  - 测试类：方法使用 @Category 注解，指明属性值（为类别的标识符），别忘了 @Test
  - 作标识符的类：就是几个空类
  - 最后运行的类：空类 + 注解
    - 使用 @RunWith 注解，并指定属性值为 Categories 类
    - 使用 @Categories.IncludeCategory 注解，并指明属性值为你要进行测试的 标识符的类
    - 使用 @Suite.SuiteClasses 注解，并指明属性值为测试类
  - 最后就可以运行了
- 如下：

```java
//原类
public class CategoryTest {
    public int add(int a,int b) {
        return a + b;
    }

    public int subtract(int a,int b) {
        return a - b;
    }

    public int secondPower(int a) {
        return a * a;
    }

    public int theThirdPower(int a) {
        return a * a * a;
    }
}

//测试类
public class CategoryTestTest {

    @Category(BaseOperations.class)
    @Test
    public void add() {
        assertEquals(5,new CategoryTest().add(2,3));
    }

    @Category(BaseOperations.class)
    @Test
    public void subtract() {
        assertEquals(5,new CategoryTest().subtract(6,1));
    }

    @Category(PowerOperations.class)
    @Test
    public void secondPower() {
        assertEquals(4,new CategoryTest().secondPower(2));
    }

    @Category(PowerOperations.class)
    @Test
    public void theThirdPower() {
        assertEquals(8,new CategoryTest().theThirdPower(2));
    }
}

//作标识符进行判断种类的类（这里就是两种，幂运算，基本运算）
public class PowerOperations {
    //这个代表幂运算类的方法标识符
}

public class BaseOperations {
    //这个代表基本运算的方法标识符
}

//最后运行的类
@RunWith(Categories.class)
@Categories.IncludeCategory(BaseOperations.class)
@Suite.SuiteClasses(CategoryTestTest.class)
public class Operations {
}
```


## 假设测试

- 使用 assumeXxx（假设方法）进行判断，假设的条件是否成立，不成立则终止测试
- Assume类中有很多的假设方法，可以自行查看，都有注释的

```java
@Test
public void testAssumptions() {
    //假设进入testAssumptions时，变量i的值为10，如果该假设不满足，程序不会执行assumeThat后面的语句
    assumeThat( i, is(10) );
    //如果之前的假设成立，会打印"assumption is true!"到控制台，否则直接调出，执行下一个测试用例函数
    System.out.println( "assumption is true!" );    
}
```



## 断言方法

- 断言方法都有很多的重载形式，这里讲讲含义就行了，具体可以自行查看
- 断言方法都来自 Assert 类，都是 static public 的
- 不满足断言方法，则会抛出：AssertionError

**assertArrayEquals**

断言两个对象数组相等

**assertEquals**

断言两个对象相等

**assertNotEquals()**

断言两个对象不相等

**assertNull()**

断言一个对象为空

**assertNotNull()**

断言一个对象不为空

**assertSame()**

断言两个对象引用相同的对象

**assertNotSame()**

断言两个对象没有引用同一对象

**assertThat()**

断言实际值是否满足指定的条件，与 Matcher 一起使用，Matcher 指定条件

- 详细看后面的讲解

**assumeThat**

假设满足指定的条件，如果不满足，测试停止

Assume类中有很多的假设方法

**assertTrue()**

断言条件为真

**assertFalse()**

断言条件为假

**assertThat与CoreMatchers**

断言实际值是否满足指定的条件，与 Matcher 一起使用
这种断言方法一共两种重载形式：

```java
//第一个参数：reason 为断言失败时的输出信息
//第二个参数：actual 为断言的值或对象
//第三个参数：matcher 为断言的匹配器，里面的逻辑决定了 给定的 actual对象满不满足断言
public static <T> void assertThat(String reason, T actual, Matcher<? super T> matcher) {
        MatcherAssert.assertThat(reason, actual, matcher);
}
    
public static <T> void assertThat(T actual, Matcher<? super T> matcher) {
        assertThat("", actual, matcher);
}
```

在 CoreMatchers类中组织了所有JUnit内置的Matcher（匹配的方法），调用其任意一个方法都会创建一个与方法名字相关的Matcher

下面的匹配并没有全部讲解完，具体请自行进入 org.hamcrest.CoreMatchers 类中查看

### assertThat

上面我们所用到的一些基本的断言，如果我们没有设置失败时的输出信息，那么在断言失败时只会抛出AssertionError，无法知道到底是哪一部分出错。而assertThat就帮我们解决了这一点。它的可读性更好。

```
assertThat(T actual, Matcher<? super T> matcher);
assertThat(String reason, T actual, Matcher<? super T> matcher); 
```


其中reason为断言失败时的输出信息，actual为断言的值，matcher为断言的匹配器。

常用的匹配器整理：

| 匹配器               | **说明**                           | **例子**                                          |
| -------------------- | ---------------------------------- | ------------------------------------------------- |
| is                   | 断言参数等于后面给出的匹配表达式   | assertThat(5, is (5));                            |
| not                  | 断言参数不等于后面给出的匹配表达式 | assertThat(5, not(6));                            |
| equalTo              | 断言参数相等                       | assertThat(30, equalTo(30));                      |
| equalToIgnoringCase  | 断言字符串相等忽略大小写           | assertThat(“Ab”, equalToIgnoringCase(“ab”));      |
| containsString       | 断言字符串包含某字符串             | assertThat(“abc”, containsString(“bc”));          |
| startsWith           | 断言字符串以某字符串开始           | assertThat(“abc”, startsWith(“a”));               |
| endsWith             | 断言字符串以某字符串结束           | assertThat(“abc”, endsWith(“c”));                 |
| nullValue            | 断言参数的值为null                 | assertThat(null, nullValue());                    |
| notNullValue         | 断言参数的值不为null               | assertThat(“abc”, notNullValue());                |
| greaterThan          | 断言参数大于                       | assertThat(4, greaterThan(3));                    |
| lessThan             | 断言参数小于                       | assertThat(4, lessThan(6));                       |
| greaterThanOrEqualTo | 断言参数大于等于                   | assertThat(4, greaterThanOrEqualTo(3));           |
| closeTo              | 断言浮点型数在某一范围内           | assertThat(4.0, closeTo(2.6, 4.3));               |
| allOf                | 断言符合所有条件，相当于&&         | assertThat(4,allOf(greaterThan(3), lessThan(6))); |
| anyOf                | 断言符合某一条件，相当于或         | assertThat(4,anyOf(greaterThan(9), lessThan(6))); |
| hasKey               | 断言Map集合含有此键                | assertThat(map, hasKey(“key”));                   |
| hasValue             | 断言Map集合含有此值                | assertThat(map, hasValue(value));                 |
| hasItem              | 断言迭代对象含有此元素             | assertThat(list, hasItem(element));               |

当然了匹配器也是可以自定义的。这里我自定义一个字符串是否是手机号码的匹配器来演示一下。

只需要继承BaseMatcher抽象类，实现matches与describeTo方法，代码如下：

```java
public class IsMobilePhoneMatcher extends BaseMatcher<String> {

    /**
     * 进行断言判定，返回true则断言成功，否则断言失败
     */

    @Override
    public boolean matches(Object item) {
        if (item == null) {
            return false;
        }

        Pattern pattern = Pattern.compile("(1|861)(3|5|7|8)\\d{9}$*");
        Matcher matcher = pattern.matcher((String) item);

        return matcher.find();
    }

    /**
     * 给期待断言成功的对象增加描述
     */
    @Override
    public void describeTo(Description description) {
        description.appendText("预计此字符串是手机号码！");
    }

    /**
     * 给断言失败的对象增加描述
     */
    @Override
    public void describeMismatch(Object item, Description description) {
        description.appendText(item.toString() + "不是手机号码！");
    }
}
```


## 字符串相关匹配符

**containsString** 

匹配符表明如果测试的字符串testedString包含子字符串"developerWorks"则测试通过

```java
assertThat(testedString, containsString("developerWorks"));
```

**endsWith** 

匹配符表明如果测试的字符串testedString以子字符串"developerWorks"结尾则测试通过

```java
assertThat(testedString, endsWith("developerWorks")); 
```

**startsWith** 

匹配符表明如果测试的字符串testedString以子字符串"developerWorks"开始则测试通过

```java
assertThat(testedString, startsWith("developerWorks")); 
```

**equalTo** 

匹配符表明如果测试的testedValue等于expectedValue则测试通过，equalTo可以测试数值之间，字符串之间和对象之间是否相等，相当于Object的equals方法

```java
assertThat(testedValue, equalTo(expectedValue)); 
```



## collection相关匹配符

**hasItem** 

匹配符表明如果测试的迭代对象 iterableObject 含有元素 “element” 项则测试通过

```java
assertThat(iterableObject, hasItem("element"));
```



## 自定义 Matcher

- 首先，大家要去看看 Matcher 这个接口与 BaseMatcher 这个实现类，就几个方法，比较简单，都写着有注释
- 看完就知道我们自定义的 Matcher 应该去继承的是 BaseMatcher 这个类，而不是 Matcher 这个类
- 使用：
  - 创建一个类继承 BaseMatcher 类，然后重写两个方法：matche()、describeTo()，根据自己的需求去实现
  - 然后就可以在测试方法中使用了

```java
//IsRichardMatcher这个类是我实现的Matcher类
assertThat(user,new IsRichardMatcher());
```



## 注解

### @Test

- 将一个普通方法修饰为测试方法
  - 限时测试，异常捕获
- 指定异常，以使测试方法在 当且仅当方法抛出 指定类的异常 时才成功，没有抛异常则会失败

```java
//在 @Test 中指定了 断言异常，运行时不会出现错误
@Test(expected = AssertionError.class)
public void add() {
    assertEquals(6,calculator.add(3,1));
    System.out.println("测试方法：add() 执行");
}
```

- 以毫秒为单位 指定超时时间，超时则失败
  - 超过指定的时间会中断方法，并抛出异常

```java
@Test(timeout = 3000)
public void subtract() {
    assertEquals(20,calculator.subtract(30,10));
    System.out.println("测试方法：subtract() 执行");
    try {
        Thread.sleep(2000);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}
```

### @Ignore

- 在测试中测试运行器会忽略被 @Ignore 注解的方法，可以指定属性值（比如说为什么被忽略）
- 一般用于测试方法还没有准备好，或者方法太耗时之类

```java
@Ignore("暂时不需要测试这个方法，所以进行忽略")
@Test
public void multiply() {
    assertEquals(10,calculator.multiply(2,5));
    System.out.println("测试方法：multiply() 执行");
}
```

### @RunWith

- 可以更改运行测试器
- 如果一个类使用了@RunWith，或者一个类的父类使用了@RunWith，JUnit将调用其引用的类，以在该类中运行测试，而不是使用JUnit内置的运行器。
  - JUnit 4中的套件是使用RunWith和一个名为Suite的自定义运行程序构建的
- 一般在测试套件的时候使用

### @BeforeClass

- 在所有测试开始之前执行一次，必须为 static 修饰
- 用于做一些耗时的初始化工作(如: 连接数据库)

```java
@BeforeClass
public static void setUpBeforeClass() throws Exception {
    System.out.println("BeforeClass执行");
}
```

### @AfterClass

- 在所有测试结束之后执行一次，必须为 static 修饰
- 用于清理数据(如: 断开数据连接)

```java
@AfterClass
public static void tearDownAfterClass() throws Exception {
    System.out.println("AfterClass执行");
}
```

### @Before

- 在每个测试方法运行前执行一次
- 用于准备测试环境(如: 初始化类，读输入流等)，在一个测试类中，每个@Test方法的执行都会触发一次调用

```java
@Before
public void setUp() throws Exception {
    System.out.println("Before执行");
}
```

### @After

- 在每个测试方法运行结束后执行一次
- 这个方法在每个测试之后执行，用于清理测试环境数据，在一个测试类中，每个@Test方法的执行都会触发一次调用

```java
@After
public void tearDown() throws Exception {
    System.out.println("After执行");
}
```

### @Run

还记得一开始我们在@Before与@After注解的方法中加入”测试开始”的提示信息吗？假如我们一直需要这样的提示，那是不是需要每次在测试类中去实现它。这样就会比较麻烦。这时你就可以使用@Rule来解决这个问题，它甚至比@Before与@After还要强大。

自定义@Rule很简单，就是实现TestRule 接口，实现apply方法。代码如下：

public class MyRule implements TestRule {

```java
public class MyRule implements TestRule {

    @Override
    public Statement apply(final Statement base, final Description description) {

        return new Statement() {
            @Override
            public void evaluate() throws Throwable {
                // evaluate前执行方法相当于@Before
                String methodName = description.getMethodName(); // 获取测试方法的名字
                System.out.println(methodName + "测试开始！");

                base.evaluate();  // 运行的测试方法

                // evaluate后执行方法相当于@After
                System.out.println(methodName + "测试结束！");
            }
        };
    }
}
```

我们使用一下我们自定义的MyRule，效果如图：

![这里写图片描述](Junit_imgs\SouthEast.png)



### @FixMethodOrder

- 修饰类，使得该测试类中的所有测试方法都按照方法名的字母顺序执行，属性值有三个
- 指定形式：@FixMethodOrder(MethodSorters.NAME_ASCENDING)，MethodSorters是一个枚举类，下面的三个值都是它的枚举常量
  - DEFAULT
    - 以确定但不可预测的顺序对测试方法进行排序，默认值
  - JVM
    - 将测试方法按JVM返回的顺序保留，请注意，JVM的运行顺序可能会有所不同
  - NAME_ASCENDING
    - 根据 方法名称 按字典名称 对测试方法进行排序，升序

```java
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class CalculatorTest {

	···
  
    @Test
    public void divide() {
        assertEquals(3,calculator.divide(9,3));
        System.out.println("测试方法：divide() 执行");
    }
}
```
## 13.Junit 运行流程

- 下面是打印出来的信息，代码很简单就贴出来了
  - 在开发中，BeforeClass、AfterClass注解的方法是 static 的

```java
BeforeClass执行（类加载）
Before执行
测试方法：subtract() 执行
After执行
Before执行
测试方法：divide() 执行
After执行
Before执行
测试方法：add() 执行
After执行
Before执行
测试方法：multiply() 执行
After执行
AfterClass执行
```

- 可以很明显的看出执行顺序：

  BeforeClass -> Before -> 测试方法 -> After -> AfterClass，如果有多个测试方法，那么重复： Before -> 测试方法 -> After 这段流程

## 14.使用中可能出现的 Bug

在测试方法中打 Log，出现错误：java.lang.RuntimeException: Method d in android.util.Log not mocked.

a. 先仔细想一想，文章的一开始说了什么呀

b. 就是 Junit 可以隔离 Android 框架呀

```java
    @Before
    public void setUp() throws Exception {
       Log.d(TAG,"执行：setUp()");  //在此使用 Log
    }
```

原因：

Log类是android sdk的api,用Junit做单元测试，只能用纯java API，否则会报错

这里就如果要使用 Log 就得自己创建一个 Log 类了，然后编写方法，如下：

```java
public class Log {
    
    public static int d(String tag, String msg) {
        System.out.println("DEBUG: " + tag + ": " + msg);
        return 0;
    }
    public static int i(String tag, String msg) {
        System.out.println("INFO: " + tag + ": " + msg);
        return 0;
    }

    public static int w(String tag, String msg) {
        System.out.println("WARN: " + tag + ": " + msg);
        return 0;
    }

    public static int e(String tag, String msg) {
        System.out.println("ERROR: " + tag + ": " + msg);
        return 0;
    }

	// add other methods if required...
}
```
