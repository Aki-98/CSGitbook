Android 提供对应的 android 插件用于项目的构建配置，在 Android 中项目的类型有以下四种：

- AppExtension：对应 com.android.application。
- LibraryExtension：对应 com.android.library。
- TestExtension：对应 com.android.test。
- FeatureExtension：对应 com.android.feature，及时应用。

# Android 插件脚本块配置

Android 构建系统编译应用资源和源代码，然后将它们打包成可供测试、部署、签署和分发的 APK。Android Studio 使用 Gradle 这一高级构建工具包来自动化执行和管理构建流程，同时也允许您定义灵活的自定义构建配置。每个构建配置均可自行定义一组代码和资源，同时对所有应用版本共有的部分加以重复利用。Android Plugin for Gradle 与这个构建工具包协作，共同提供专用于构建和测试 Android 应用的流程和可配置设置。

## ？1 aaptOptions { }

配置 Android 资源打包工具 AAPT 选项。

```groovy
aaptOptions {
    additionalParameters '-S',
            '/Users/yifan/dev/github/Testapp/app/src/main/res3',
            '-S',
            '/Users/yifan/dev/github/Testapp/app/src/main/res2',
            '--auto-add-overlay'
    noCompress 'foo', 'bar'
    ignoreAssetsPattern '!.svn:!.git:!.ds_store:!*.scc:.*:<dir>_*:!CVS:!thumbs.db:!picasa.ini:!*~'
}
```

这个选项用于配置 AAPT 资源打包时的一些处理，比如资源替换，这块内容可参照[编译时替换资源](http://blog.zhaiyifan.cn/2016/02/18/android-resource-overlay/)。

## ？2 adbOptions { }

配置 Android 调试工具 ADB 选项。通常我们通过 adb 指令来进行 Apk 的安装或卸载，或者一些文件拷贝工作，通过 adbOptions {} 脚本块同样可以在 Android Plugin 中进行配置，adbOptions {} 脚本块对应 AdbOptions 类，该类有两个属性：

- installOptions：adb 配置选项，是 List<String> 类型。
- timeOutInMs：是设置超时时间的，单位是毫秒，这个超时时间是执行adb这个命令的超时时间，int 类型。

```groovy
android {
    adbOptions {
        timeOutInMs 10 * 1000
        installOptions '-r','-s'
    }
}
```

- -l：锁定该应用程序
- -r：替换已存在的应用程序，也就是我们说的强制安装
- -t：允许测试包
- -s：把应用程序安装到 SD 卡上
- -d：允许进行降级安装，也就是安装的比手机上带的版本低
- -g：为该应用授予所有运行时的权限

## 3 buildTypes { }

当前项目的构建类型配置，对应的配置类型 BuildType 类，在 Android Studio 的中已经给我们内置了 release 和 debug 两种构建类型，这两种模式的主要差异在于能否在设备上调试以及签名不一样，这里会涉及到很多属性可以配置。

- ? applicationIdSuffix：配置基于应用默认的 applicationId 的后缀，常用于构建变体应用。
- ? consumerProguardFiles：配置 .aar 文件中是否使用 Proguard 混淆。
- ? crunchPngs：针对 png 的优化，设置为 true 的时候会增加编译时间。
- debuggable：配置构建的 apk 是否能够进行 debug。
- javaCompileOptions：配置 Java 编译的配置
- ? jniDebuggable：配置构建类型的 apk native code 是否能够进行 debug。
- minifyEnabled：是否启用 Proguard 混淆。
- ? multiDexEnabled：是否使用分包。
- ? multiDexKeepFile：指定放到主 dex 中的文件。
- ? multiDexKeepProguard：配置指定的文件使用 Proguard。
- proguardFiles：混淆文件。
- shrinkResources：用于配置是否自动清理未使用的资源，默认为 false。
- signingConfig：签名文件。
- ? useProguard
- ? versionNameSuffix：类似于 applicationIdSuffix。
- ? zipAlignEnabled：zipAlign 优化 apk 文件的工具。

```groovy
buildTypes {

    release {
        minifyEnabled false
        crunchPngs true
        debuggable false
        shrinkResources true
        multiDexEnabled true
        multiDexKeepProguard file('proguard-rules.pro') // keep specific classes using proguard syntax
        multiDexKeepFile file('multiDexKeep.txt')
        minifyEnabled true
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        signingConfig
        zipAlignEnabled true
        applicationIdSuffix '.release'
        versionNameSuffix '.release'
    }

    debug {
        applicationIdSuffix '.debug'
        versionNameSuffix '.debug'
    }
}
```

## 4 compileOptions { }

Java 编译选项，通常是针对 JDK 进行编码格式修改或者指定 JDK 的版本,对应的类是 CompileOptions。

```groovy
compileOptions {
    encoding = 'utf-8'
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
}
```

## ? 5 dataBinding { }

DataBinding 配置选项，查看源码可以发现对应 DataBindingOptions 类，该类包含四个属性：

- version：版本号。
- enabled：是否可用。
- addDefaultAdapters：是否使用默认的 Adapter。
- enabledForTests：是否用于 Test。

```groovy
dataBinding {
    enabled true
    version 1.0
}
```

## 6 defaultConfig { }

defaultConfig 也是 Android 插件中常见的一个配置块，负责默认的所有配置。同样它是一个 ProductFlavor，如果一个 ProductFlavor 没有被特殊配置，则默认使用 <u>defaultFlavor</u> 的配置，比如报名、版本号、版本名称等。常见的属性有：

- **applicationId**：applicationId 是 ProductFlavor 的一个属性，用于配置 App 生成的进程名，默认情况下是 null。
- **minSdkVersion**：指定 Apk 支持的最低 Android 操作系统版本。
- **targetSdkVersion**：用于配置 Apk 基于的 SDK 哪个版本进行开发。
- **versionCode**：同样是 ProductFlavor 的一个属性，配置 Apk 的内部版本号。
- **versionName**：配置版本名称。
- **testApplicationId**：配置测试 App 的报名，默认情况下是 applicationId + ".test"。
- **testInstrumentationRunner**：配置单元测试使用的 Runner，默认是 android.test.InstrumentationTestRunner,或者可以使用自定义的 Runner。
- **signingConfig**：配置默认的签名信息，对生成的 App 签名。
- **proguardFile**：用于配置使用的混淆文件。
- **proguardFiles**：配置混淆使用的文件，可以配置多个。

```groovy
defaultConfig {
    applicationId 'com.andoter.dsw'
    minSdkVersion 15
    targetSdkVersion 28
    versionCode 1
    versionName "1.0"
    testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
    signingConfigs signingConfigs.release
}
```

## ？7 dexOptions { }

dex 的配置项，通常在开发的过程中，我们可以通过配置 dexOptions {} 提高编译速度，与之对应的是 DexOptions 接口，该接口由 DefaultDexOptions 默认实现，DefaultDexOptions 类中包含以下属性：

- preDexLibraries：默认 true
- jumboMode：默认 false
- dexInProcess：默认为 true，所有的 dex 都在 process 中，提高效率
- javaMaxHeapSize：最大的堆大小
- maxProcessCount：最大的 process 个数
- threadCount：线程个数

```groovy
dexOptions {
    incremental true //是否增量，如果开启multi-dex, 此句无效
    preDexLibraries true
    javaMaxHeapSize "4g" //java 编译的 Heap 大小
    jumboMode true
    threadCount 8 //gradle输就输在了并行上, 都是串行, 增加线程数没用
    // 设置最大的进程数：Memory = maxProcessCount * javaMaxHeapSize
    maxProcessCount 8
}
```

## ？8 lintOptions { }

Lint 是Android Studio 提供的 代码扫描分析工具，它可以帮助我们发现代码结构/质量问题，同时提供一些解决方案，而且这个过程不需要我们手写测试用例。Lint 发现的每个问题都有描述信息和等级（和测试发现 bug 很相似），我们可以很方便地定位问题同时按照严重程度
 进行解决。

```groovy
android {
    lintOptions {
        // true--关闭lint报告的分析进度
        quiet true
        // true--错误发生后停止gradle构建
        abortOnError false
        // true--只报告error
        ignoreWarnings true
        // true--忽略有错误的文件的全/绝对路径(默认是true)
        //absolutePaths true
        // true--检查所有问题点，包含其他默认关闭项
        checkAllWarnings true
        // true--所有warning当做error
        warningsAsErrors true
        // 关闭指定问题检查
        disable 'TypographyFractions','TypographyQuotes'
        // 打开指定问题检查
        enable 'RtlHardcoded','RtlCompat', 'RtlEnabled'
        // 仅检查指定问题
        check 'NewApi', 'InlinedApi'
        // true--error输出文件不包含源码行号
        noLines true
        // true--显示错误的所有发生位置，不截取
        showAll true
        // 回退lint设置(默认规则)
        lintConfig file("default-lint.xml")
        // true--生成txt格式报告(默认false)
        textReport true
        // 重定向输出；可以是文件或'stdout'
        textOutput 'stdout'
        // true--生成XML格式报告
        xmlReport false
        // 指定xml报告文档(默认lint-results.xml)
        xmlOutput file("lint-report.xml")
        // true--生成HTML报告(带问题解释，源码位置，等)
        htmlReport true
        // html报告可选路径(构建器默认是lint-results.html )
        htmlOutput file("lint-report.html")
        //  true--所有正式版构建执行规则生成崩溃的lint检查，如果有崩溃问题将停止构建
        checkReleaseBuilds true
        // 在发布版本编译时检查(即使不包含lint目标)，指定问题的规则生成崩溃
        fatal 'NewApi', 'InlineApi'
        // 指定问题的规则生成错误
        error 'Wakelock', 'TextViewEdits'
        // 指定问题的规则生成警告
        warning 'ResourceAsColor'
        // 忽略指定问题的规则(同关闭检查)
        ignore 'TypographyQuotes'
    }
}
```

## ？9 packagingOptions { }

Android 打包配置项，可以配置打包的时候哪些打包进 Apk。当项目中依赖的第三方库越来越多时，有可能会出现两个依赖库中存在同一个
 （名称）文件。如果这样，Gradle在打包时就会提示错误（警告）。那么就可以根据提示，然后使用以下方法将重复的文件剔除。

```groovy
packagingOptions {
    //这个是在同时使用butterknife、dagger2做的一个处理。同理，遇到类似的问题，只要根据gradle的提示，做类似处理即可。
    exclude 'META-INF/services/javax.annotation.processing.Processor'
}
```

## 10 productFlavors { }

用于构建不同的产品风味，在上面我们提到 defaultConfig{} 也是一种产品风味，可作为所有产品风味的“基类”共同部分。风味(Flavor) 对应 ProductFlavor 类，该类的属性与配置属性相匹配。

```groovy
android {
    ...
    defaultConfig {...}
    buildTypes {...}
    productFlavors {
        demo {
            applicationIdSuffix ".demo"
            versionNameSuffix "-demo"
        }
        full {
            applicationIdSuffix ".full"
            versionNameSuffix "-full"
        }
    }
}
```

在创建和配置您的产品风味之后，在通知栏中点击 Sync Now。同步完成后，Gradle会根据您的构建类型和产品风味自动创建构建变体，
 并按照 <product-flavor><Build-Type>的格式命名这些变体。例如，如果您创建了“演示”和“完整”这两种产品风味并保留默认的“调试”和“发布”构建类型，Gradle 将创建以下构建变体：

- 演示调试
- 演示发布
- 完整调试
- 完整发布

您可以将构建变体更改为您要构建并运行的任何变体，只需转到 Build > Select Build Variant，然后从下拉菜单中选择一个变体。

### **产品风味组合**

通常在适配多个渠道的时候，需要为特定的渠道做部分特殊的处理，这里就会涉及到结合 buildTypes{} 组合不同的产品风味组合。

```groovy
android {
  ...
  buildTypes {
    debug {...}
    release {...}
  }

  // Specifies the flavor dimensions you want to use. The order in which you
  // list each dimension determines its priority, from highest to lowest,
  // when Gradle merges variant sources and configurations. You must assign
  // each product flavor you configure to one of the flavor dimensions.
  flavorDimensions "api", "mode"

  productFlavors {
    demo {
      // Assigns this product flavor to the "mode" flavor dimension.
      dimension "mode"
      ...
    }

    full {
      dimension "mode"
      ...
    }

    // Configurations in the "api" product flavors override those in "mode"
    // flavors and the defaultConfig {} block. Gradle determines the priority
    // between flavor dimensions based on the order in which they appear next
    // to the flavorDimensions property above--the first dimension has a higher
    // priority than the second, and so on.
    minApi24 {
      dimension "api"
      minSdkVersion '24'
      // To ensure the target device receives the version of the app with
      // the highest compatible API level, assign version codes in increasing
      // value with API level. To learn more about assigning version codes to
      // support app updates and uploading to Google Play, read Multiple APK Support
      versionCode 30000 + android.defaultConfig.versionCode
      versionNameSuffix "-minApi24"
      ...
    }

    minApi23 {
      dimension "api"
      minSdkVersion '23'
      versionCode 20000  + android.defaultConfig.versionCode
      versionNameSuffix "-minApi23"
      ...
    }

    minApi21 {
      dimension "api"
      minSdkVersion '21'
      versionCode 10000  + android.defaultConfig.versionCode
      versionNameSuffix "-minApi21"
      ...
    }
  }
}
```

Gradle 创建的构建变体数量等于每个风味维度中的风味数量与您配置的构建类型数量的乘积。在 Gradle 为每个构建变体或对应 APK 命名时，属于较高优先级风味维度的产品风味首先显示，之后是较低优先级维度的产品风味，再之后是构建类型。以上面的构建配置为例，Gradle 可以使用以下命名方案创建总共 12 个构建变体：

```css
构建变体：[minApi24, minApi23, minApi21][Demo, Full][Debug, Release]
对应 APK：app-[minApi24, minApi23, minApi21]-[demo, full]-[debug, release].apk
```

同样我们在 Terminal 中通过 gradle 指令执行构建变体的任务：**变体名称(flavorDimensions 的第一个维度的 Flavor) + flavorDimensions 的别的维度的 Flavor + buildTypes**，例如：minApi24DemoDebug，构建出来的对应 Apk：app-minApi24-demo-debug.apk

### **过滤变体**

Gradle 会自动根据设置的 buildTypes{} 和 flavorDimensions{} 创建很多变体的组合体，但是有些是我们不需要的，这里就涉及到过滤变体的操作。Gradle 提供了 variantFilter {} 脚本块来过滤，脚本块对应 VariantFilter 接口，接口中包含：

- setIgnore(boolean ignore)：设置是否忽略某个变体
- getBuildType：获取变体的构建类型
- List<ProductFlavor> getFlavors()：返回所有变体的列表
- getName：获取变体的 name 名称

```groovy
variantFilter { variant ->
    def names = variant.flavors.name
    // To check for a certain build type, use variant.buildType.name == "<buildType>"
    if (names.contains("minApi23") && names.contains("demo")) {
        // Gradle ignores any variants that satisfy the conditions above.
        setIgnore(true)
    } else {
        setIgnore(false)
    }
}
```

更多关于构建变体内容参照官方：[构建变体](https://developer.android.com/studio/build/build-variants?hl=zh-cn)

## 11 signingConfigs { }

配置签名信息，常用于 BuildType 和 ProductFlavor 配置，在构建变体的过程中，会出现很多种类，所以针对不同类别的变体所使用的签名可能也是不同的，这就需要使用 signingConfigs{} 配置签名信息合集，然后按需所取。

```groovy
signingConfigs {
    release {//发布版本的签名配置
      storeFile file(props['KEYSTORE_FILE'])
      keyAlias props['KEY_ALIAS']
      storePassword props['KEYSTORE_PWD']
      keyPassword props['KEY_PWD']
    }
    debug {//调试版本的签名配置
      storeFile file(props['DEBUG_KEYSTORE'])
      keyAlias props['DEBUG_ALIAS']
      storePassword props['DEBUG_KEYSTORE_PWD']
      keyPassword props['DEBUG_KEY_PWD']
    }
}

buildTypes {
    signingConfig signingConfigs.release
}
```

## 12 sourceSets { }

在 AndroidStudio 中，在 src/main/java 目录下创建我们的 .java 文件，这些都是系统通过 sourceSet{} 设置好的，比如我们在外部创建一个文件夹，选中文件夹右键就无创建 .java 文件的选项。就需要我们通过 sourceSets 进行配置，脚本块对应 AndroidSourceSet 接口，接口中有：

- AndroidSourceSet java(Closure configureClosure)：配置 java 文件存放路径
- AndroidSourceSet resources(Closure configureClosure)：配置 resource 目录
- AndroidSourceSet jniLibs(Closure configureClosure)：配置 jniLibs 目录
- AndroidSourceSet jni(Closure configureClosure)：配置 jni 文件目录
- AndroidSourceSet renderscript(Closure configureClosure)：配置 renderscript 目录
- AndroidSourceSet aidl(Closure configureClosure)：配置 aidl 文件目录
- AndroidSourceSet assets(Closure configureClosure)：配置 assets 目录
- AndroidSourceSet res(Closure configureClosure)：配置 res 目录
- AndroidSourceSet manifest(Closure configureClosure)：配置 manifest 目录

```groovy
sourceSets {
    main {
        java {
            srcDir 'src/main/testjava'
        }
        resources {
            srcDir 'src/resources'
        }
    }
}
```

## ？13 splits { }

拆分机制比起使用 flavors，能让应用程序更有效地构建一些形式的多个apk。
 多 apk 只支持以下类型:

- 屏幕密度
- ABI

脚本块对应 Splits 类，该类中有三个属性：

- density：像素密度
- abi：abi 类型
- language：语言

```groovy
splits {
    density {
        enable true
        exclude "ldpi", "tvdpi", "xxxhdpi"
        compatibleScreens 'small', 'normal', 'large', 'xlarge'
    }

    abi {
        enable true
        reset()
        include 'x86', 'armeabi-v7a', 'mips'
        universalApk true
    }
}
```