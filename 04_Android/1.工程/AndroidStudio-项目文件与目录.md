# 一、总项目的目录结构

![img](AndroidStudio-项目文件与目录_imgs\v2-de9c6550f5ded5de1ee348448c568fdc_720w.webp)

| 目录名/文件名       | 作用                                                         |
| ------------------- | ------------------------------------------------------------ |
| .idea/.build        | 自动生成的文件                                               |
| app                 | 项目的代码文件和资源文件                                     |
| build               | 编译时自动生成的文件                                         |
| gradle              | 构建项目的gradle。                                           |
| .gitignore          | 将指定的文件排除在版本控制之外                               |
| build.gradle(proj)  | 项目全局的gradle构建脚本                                     |
| gradle.properties   | 全局的gradle配置文件，这里配置的属性能影响到项目所有的gradle编译脚本 |
| gradlew/gradlew.bat | 用于在命令行界面下执行gradle命令，gradlew在linux和mac中执行，gradlew.bat则在windows下执行 |
| local.properties    | 本机中AndroidSDK的路径，一般自动生成，除非发生变化，则要修改 |
| XXX.iml             | 表示该项目是IntelliJIDEA项目                                 |
| setting.gradle      | 用于指定项目中所有引入的模块。一般可自动生成，也可自行设置，比如引入flutter模块时，可在此文件上设置该模块路径等 |

注意：而gradle文件里面包含gradlewrapper配置文件，使用gradle wrapper方式会自动联网下载gradle,，当然AndroidStudio会首先检查本地是否有缓存gradle，没有就会自动联网下载gradle，这样就不用自己先下载gradle，当然如果要使用离线模式，也可以自己setting：File---Settings---Build,Execution,Deployment---Gradle

![img](AndroidStudio-项目文件与目录_imgs\v2-4b195082c091c9f241e57a4546f7b5f1_720w.png)

# 二、app目录下的结构

![img](AndroidStudio-项目文件与目录_imgs\v2-bd09386eeec3e2b826d1f566ed8feba9_720w.png)

| 目录名/文件名       | 作用                                                         |
| ------------------- | ------------------------------------------------------------ |
| libs                | 放置jar包                                                    |
| release             | 该目录并不是非得有，也可以在外面项目层路径下，它是存放你打包后的apk文件，你在打包的时候是可以设置它的路径的 |
| src/androidTest     | 编写Android Test测试用例，进行自动化测试用的。               |
| src/test            | 用来编写Unit Test测试，也是进行自动化测试用的                |
| main/java           | 存放所有你的项目源代码                                       |
| main/res            | 存放资源文件                                                 |
| main/res/layout     | 存放布局文件                                                 |
| main/res/values     | 存放字符串文件                                               |
| main/res/mipmap     | 存放图标                                                     |
| main/res/drawable   | 存放图片                                                     |
| AndroidManifest.xml | 注册四大组件、添加应用权限                                   |
| .gitignore          | 将app中的文件和目录排除在版本控制之外                        |
| app.iml             | IntelliJIDEA自动生成的文件                                   |
| build.gradle(app)   | app模块的gradle构建脚本，指定项目构建相关的配置              |
| proguard-rules.pro  | 混淆文件，指定项目代码的混淆规则，为了防止apk文件被别人破解时采取混淆代码 |

# 三、build.gradle(proj)和build.gradle(app)

## (1)build.gradle(proj)

代码如图所示：

```
//构建描述
buildscript {
	//添加依赖库
	respsitories {
		//google官方依赖库
		google()
		//第三方开源库
		jcenter()
	}
	dependencies {
		//gradle插件，因为Gradle插件不仅仅为构建Android项目服务的，它还可以构建java项目和C++项目的，所以要声明Gradle插件是构建Android项目的，版本号跟Android Studio的版本号一致
	 	classpath 'com.android.tools.build:gradle:3.5.2'
	}
}

//同上
allprojects {
	respositories {
		google()
		jcenter()
	}
}
```

## (2)build.gradle(app)

```
//应用程序模块，可以直接运行
apply plugin:'com.android.application'
//库模块，需要依附于应用程序模块
apply plugin:'com.android.library'

//android闭包
android {
	//指定项目的编译版本
	compileSdkVersion 30
	//指定构建项目工具的版本
	buildToolsVersion "30.0.2"
	defaultConfig {
		//指定项目的包名，具有唯一性，是项目的唯一标识
		applicationId "com.example.myapplication"
		//最低兼容的Android系统版本
		minSdkVersion 19
		//指定目前使用到最高的Android系统版本
		targetSdkVersion 30
		//项目版本号
		versionCode 1
		//项目版本名
		versionName "1.0"
		testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
		multiDexEnabled true
	}
	//项目生成安装文件的相关配置，release和debug都可以指定
	buildTypes {
		release {
			//是否使用混淆
			minifyEnabled false
			//设置使用的混淆文件，凡是在Android Studio运行生成的都是测试版安装文件。正式版需Build—Generate Signed Bundle/Apk里产生。
			proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'),'proguard-rules.pro'
		}
	}
}

//指定了项目所有的依赖关系：本地依赖、库依赖、远程依赖
dependencies {
	implementation fileTree(dir:'libs',include:['*.jar'])
	implementation 'androidx.appcompat:appcompat:1.0.2'
	implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
	testImplementation 'junit:junit:4.12'
	androidResr
}
```

| 库类型   | 使用                                                         |
| -------- | ------------------------------------------------------------ |
| 本地依赖 | 对本地的jar包和目录添加依赖关系，implementationfileTree声明，将libs中的.jar文件都添加到构建目录中 |
| 远程依赖 | 对jcenter仓库的上的开源项目添加依赖关系，也就是平时我们在github上添加的第三方开源库，也是直接implementation，先检查本地是否有缓存，没有就直接联网下载到构建路径 |
| 库依赖   | 对项目中的库模块进行依赖，implementation project声明，通常格式为implementation project(‘:库名’) |

