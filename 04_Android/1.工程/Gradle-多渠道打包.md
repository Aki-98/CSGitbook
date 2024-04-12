> 我们都知道国内应用市场非常多，为了统计各个应用市场的app下载量和使用情况，我们需要多渠道的打包。如果一个一个的手动去打包岂不烦死了，要多麻烦就有多麻烦。这就要求我们学会使用Gradle进行多渠道打包。废话不多说了，直接进入正题吧！

## 第一步：配置AndroidManifest.xml

以友盟渠道为例，渠道信息一般都是写在 AndroidManifest.xml文件中，大约如下：

```text
<meta-data android:name="UMENG_CHANNEL" android:value="xiaomi" />
```

如果不使用多渠道打包方法，那就需要我们手动一个一个去修改value中的值，xiaomi，360，qq，wandoujia等等。使用多渠道打包的方式，就需要把上面的value配置成下面的方式：

```text
<meta-data    android:name="UMENG_CHANNEL"    android:value="${UMENG_CHANNEL_VALUE}" />
```

其中${UMENG_CHANNEL_VALUE}中的值就是你在gradle中自定义配置的值。

## 第二步： 在build.gradle设置productFlavors

```text
productFlavors {
     wandoujia {
          manifestPlaceholders = [UMENG_CHANNEL_VALUE: "wandoujia"]
     }

     xiaomi{
          manifestPlaceholders = [UMENG_CHANNEL_VALUE: "xiaomi"]
     }

     qq {
          manifestPlaceholders = [UMENG_CHANNEL_VALUE: "qq"]
     }

     _360 {
          manifestPlaceholders = [UMENG_CHANNEL_VALUE: "360"]
     }

}
```

其中[UMENG_CHANNEL_VALUE: “wandoujia”]就是对应${UMENG_CHANNEL_VALUE}的值。我们可以发现，按照上面的方式写，比较繁琐，其实还有更简洁的方式去写，方法如下：

```text
android { 
    productFlavors {
        wandoujia{}
        xiaomi{}
        qq{}
        _360 {}
    } 

    productFlavors.all { 
        flavor -> flavor.manifestPlaceholders = [UMENG_CHANNEL_VALUE: name] 
        }
}
```

其中name的值对相对应各个productFlavors的选项值，这样就达到自动替换渠道值的目的了。这样生成apk时，选择相应的Flavors来生成指定渠道的包就可以了，而且生成的apk会自动帮你加上相应渠道的后缀，非常方便和直观。大家可以自己反编译验证。

## 第三步：一次生成所有渠道包

我们可以使用CMD命令，进入到项目所在的目录，直接输入命令：

```text
gradle assembleRelease
```

就开始打包了，如果渠道很多的话，时间可能会很长。

或者，当然Android Studio中的下方底栏中有个命令行工具Terminal，你也可以直接打开，输入上面的命令：

```text
gradle assembleRelease
```

用CMD进入到项目所在目录执行，或者用AS中自带的命令行工具Terminal其实性质都是一样的。

**注意：如果没有对gradle配置的话，可能输入上面的命令，会提示“不是内部或者外部命令”，不要着急，我们只需要找到gradle的目录，把它配置到电脑中的环境变量中去即可。**

配置方式如下：

先找到gralde的根目录，在系统变量里添加两个环境变量：

变量名为：GRADLE_HOME，变量值就为gradle的根目录；

所以变量值为：D:\android\android-studio-ide-143.2739321-windows\android-studio\gradle\gradle-2.10

还有一个在系统变量里PATH里面添加gradle的bin目录

我的就是D:\android\android-studio-ide-143.2739321-windows\android-studio\gradle\gradle-2.10\bin

这样就配置完了，不信赶紧去试试，执行以下这个命令：gradle assembleRelease。是不是可以了。

## 第四步：如果要带签名的话，就得在build.gradle进行相关签名的配置

```text
//签名
signingConfigs{
     release {
          storeFile file("keystore路径")
          storePassword "***"
          keyAlias "***"
          keyPassword "***"
     }
}

buildTypes {
        release {
            runProguard false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.release
        }
    }
```

## 第五步：修改导出包的apk名称

我们打包有非常多的渠道包，所以我们可以根据渠道自定义apk的名称，方便运营人员看嘛，知道哪个apk对应的哪个渠道嘛。

```text
android {

    applicationVariants.all { variant ->

        variant.outputs.each { output ->

            output.outputFile = new File(

                    output.outputFile.parent,

                    "xxxx(apk的名字)-${variant.buildType.name}-${defaultConfig.versionName}-${variant.productFlavors[0].name}.apk".toLowerCase())

        }

    }

}
```

最后打包完成之后，apk文件就会生成在项目的build\outputs\apk下。