# 框架选择

- 如果您的测试对 Android 框架有依赖性（特别是与框架建立复杂互动的测试），最好使用 Robolectric 添加框架依赖项。
- 如果您的测试对 Android 框架的依赖性极小，或者如果测试仅取决于您自己的对象，可以使用诸如 Mockito 之类的模拟框架添加模拟依赖项。

# 设置测试环境

本地单元测试的源文件存储在 `module-name/src/test/java/` 中。当您创建新项目时，此目录已存在。

您还需要为项目配置测试依赖项，以使用 JUnit 4 框架提供的标准 API。如果您的测试需要与 Android 依赖项互动，请添加 Robolectric 或 Mockito 库以简化您的本地单元测试。

导入依赖项：

```
dependencies {
	// Required -- JUnit 4 framework
	testImplementation 'junit:junit:4.13.2'
	// Optional -- Robolectric environment
	testImplementation 'androidx.text:core:1.2.0'
	testImplementation 'org.robolectric:robolectric:4.3.1'
	// Optional -- Mockito framework
	testImplementation 'org.mockito:mockito-core:2.28.2'
	// Optional -- PowerMock framework
	testImplementation 'org.powermock:powermock-module-junit4:2.0.5'
	testImplementation 'org.powermock:powermock-module-junit4-rule:2.0.5'
	testImplementation 'org.powermock:powermock-api-mockito2:2.0.5'
	testImplementation 'org.powermock:powermock-clasloading-xstream:2.0.5'
	// Optional -- AndroidJUnitRunner
	testImplementation 'androidx.test:runner:1.2.0'
	// Optional -- some rules for example ActivityTestRule
	testImplementation 'androidx.test:rules:1.2.0'
	// Optional -- ext class for junit
	testImplementation 'androidx.test.ext:junit:1.1.1'
	testImplementation 'androidx.test.ext:truth:1.2.0'
	// Optional google test assertions framework
	testImplementation 'com.google.truth:truth:0.42'
	// Optional espresso:ui test framework
	testImplementation 'androidx.test.espresso:espresso-core:3.2.0'
}
```

在build.gradle增加测试选项

```
android {
	...
	testOptions {
		unitTests.includeAndroidResources = true
	}
}
```

# 规则

TestName: makes the current test name available inside test methods.

ActivityScenarioRule: 在测试开始前启动Activity，测试结束后关闭Activity

PowerMockRule：apply power mock method proxy

# Mock与Stub

Stub，也即“桩”，即某个程序模块还未准备好时，编写的向外呈现模块主要特性的替代。

Mock，模拟对象的各种性质，返回值等的一个虚假的对象。



stub对象可以用来替代某些东西：比如外部的设备，需要交互的服务，尤其是这些可以替代的东西还未准备就绪，这个时候可以通过stub来模拟它们的存在，使得开发不被阻塞住。换句话说，stub是架构设计中的一个组件，用来隔离一些未就绪的东西（但同时这些未就绪的东西也可能是系统的一个变化点）

而mock对象的使用场景被限制在单元测试里，由于被测模块很可能还需要访问数据库，访问远程接口，或者调用其他模块的方法，很难满足被测对象的接口需求（或者精确的控制被测对象的行为）这个时候可以通过mock对象来模拟被测模块所依赖的一切东西，包括Stub。

是的，你没看错，mock可以用来模拟Stub。因为Stub不会写的太复杂，一般来说只能反映被替代对象的主要特性，这个时候可以在单元测试里构造mock对象所有可能的返回值，从而驱动被测模块控制流的走向，提高单元测试的语句覆盖率。

# FAQ

**1.How to write a ui test:**

please refer to the espresso and robolectric

https://developer.android.google.cn/training/testing/espresso?hl=en

http://robolectric.org/androidx_test/



**2.How to get application object**

 AlbumApplication albumApp= ApplicationProvider.getApplicationContext();

//launch a fragment in a empty activity

FragmentScenario.launchInContainer(AbstractAlbumFragmentSubClass.class, null,

​        R.style.Theme_AlbumLeanback, myFragmentFactory);



**3.How to launch a activity**

 @Rule public ActivityScenarioRule<HostActivity> hostActivityActivityScenarioRule = new ActivityScenarioRule<>(BrowseHostFragmentTest.HostActivity.class);



**4.How to declare a test only activity in a library module**

add a Manifest file in module

/src/test folder refer to the right



**5.How to declare a test only activity in a application module**

solution1://robolectric issue workaround

In order to use test-only activities, you can create a test support gradle project which 

contains the test activity and declares it in its manifest, then add a testImplementation

dependency to that project. For detail please refer to 

https://github.com/robolectric/robolectric/pull/4736



solution2://add the test activity into debug apk

you can create a test support library which contain the test activity and declares it in its manifest

and add it as debugImplementation dependency to the app module

for example, the following test code will lanch a EmptyFragmentActivity which is a test only 

activity.

 mScenario = FragmentScenario.launchInContainer(HeaderMenuFragment.class);

You should use the following dependence in build.gradle

 debugImplementation 'androidx.fragment:fragment-testing:1.2.3'

If you change debugImplementation into testImplementation, it will report the following



error:

java.lang.RuntimeException: Unable to resolve activity for Intent { act=android.intent.

action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.sony.dtv.

smartmediaapp/androidx.fragment.app.testing.FragmentScenario$EmptyFragmentActivity

(has extras) } -- see https://github.com/robolectric/robolectric/pull/4736 for details



**6.How to enable log in robolectric test?**

ShadowLog.stream = System.out;



# Issues

when run robolectric tests on Android API 29 now strictly requires a Java9 runtime or 

newer. If you are seeing errors about unsupported Java version when running tests on 

API 29 via Android Studio; you can use the 'JRE' field in the Run Configuration dialog to 

configure a newer Java runtime. 

See https://developer.android.com/studio/run/rundebugconfig for more background.

But we didn't know how to use java 8 to compile java code and use java 9 to run the unit 

test in gradle task'coverageInstrumentedTestsReport'.

So We current disable the tests these require api 29. 
