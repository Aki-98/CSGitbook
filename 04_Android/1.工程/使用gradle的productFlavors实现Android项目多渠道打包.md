**productFlavors 用法**

在build.gradle中加入productFlavors结构

在app(module)目录下的build.gradle文件中加入productFlavors结构:

    android{
        ......
        productFlavors{
            productA{
                //这里定义产品A的特性
            }
    
            productB{
                //这里定义产品B的特性
            }
    
           //更多产品 ...
        }
可以看到我们在android节点下建立了一个productFlavors节点,里面包含了两个产品, productA与productB就是产品名

在AndroidStudio左下角的Build Variants菜单中可以看到如下界面:

![这里写图片描述](使用gradle的productFlavors实现Android项目多渠道打包_imgs\78.png)

平时调试的时候可以在这里通过选择一个产品的Debug版本来调试

**productFlavors的应用场景**

1. 不同包名的产品

通过为产品设置不同的applicationId就可以编译出不同包名的APK

     productFlavors{
        productA{
            applicationId "com.gavinandre.product.a"
            versionName "version-a-1.0"
        }
    
        productB{
            applicationId "com.gavinandre.product.b"
            versionName "version-b-1.0"
        }
    }
2. 不同渠道包的产品

由于国内引用市场较多,因此需要为不同市场打包相应的包,通常这种包就叫做渠道包,我们可以使用productFlavors配合manifestPlaceholders属性的方法来替换渠道值

一般用渠道的统计无非是用友盟或者其它之类的,以友盟为例

      productFlavors{
        wandoujia {
            manifestPlaceholders = [UMENG_CHANNEL_VALUE: "wandoujia"]
        }
    
        baidu {
            manifestPlaceholders = [UMENG_CHANNEL_VALUE: "baidu"]       }
    
        c360 {
            manifestPlaceholders = [UMENG_CHANNEL_VALUE: "c360"]
        }
    
        uc {
        manifestPlaceholders = [UMENG_CHANNEL_VALUE: "uc"]
        }
      }
或者

```
productFlavors {

    wandoujia {}
    baidu {}
    c360 {}
    uc {}

    productFlavors.all { flavor ->
    flavor.manifestPlaceholders = [UMENG_CHANNEL_VALUE: name]
    }

}
```

然后在AndroidManifest中使用：

3. 不同依赖库的产品

productFlavors还支持自定义依赖,产品A只编译自己需要的依赖库，不需要编译对自己无用的依赖库

```
dependencies {
    # ....
    productACompile "com.android.support:appcompat-v7:25.1.1"
    productBCompile "com.android.support:support-v4:25.1.1"
}
```


这里使用productFlavors里定义的产品名+Compile关键字来替代compile关键字

4. 不同代码和资源的产品

gradle中有一个source set概念,不同产品可以设置不同的source set,通常src/main目录是ide自动帮我们创建的文件夹,因此我们可以在src目录下创建productA/productB这样的目录,目录名需要和productFlavors中定义的产品名对应

![这里写图片描述](使用gradle的productFlavors实现Android项目多渠道打包_imgs\98.png)

这样src/productA/java文件内可以放不同的代码,src/productA/res文件夹内可以放不同的资源文件,同时也可以定义不同的AndroidManifest文件,比如申请不同的权限之类

**assemble命令实现多渠道打包**

上面介绍了productFlavors,下面来介绍如何一次性编译打包多个渠道或产品
可以在Android Studio底部的terminal里输入命令

assemble命令介绍:

assemble 是和 Build Variants 一起结合使用的，而 Build Variants = Build Type(Debug/Release) + Product Flavor(如wandoujia)

使用实例:

- ./gradlew assembleDebug
  编译并生成Debug包,包含productFlavors下所有定义的产品或渠道包
- ./gradlew assembleRelease
  编译并生成Release包,包含productFlavors下所有定义的产品或渠道包
- ./gradlew assembleWandoujia
  编译并生成Release和Debug包,仅生成productFlavors下定义的wandoujia渠道
- ./gradlew assembleWandoujiaRelease
  编译并生成Release包,仅生成productFlavors下定义的wandoujia渠道

apk生成目录在rootProject/app/build/outputs/apk目录下

**图形操作实现多渠道打包**

如果不想用命令行方式也可以另外两种方式来统一打包apk

Generate Signed APK方式
点击Android Studio上方工具栏 build ->Generate Signed APK…
然后多选要打包的渠道包,同时可以指定APK生成目录和指定BuildType

![这里写图片描述](使用gradle的productFlavors实现Android项目多渠道打包_imgs\97.png)

Gradle 工具方式
定位到图中的目录后选择则相应的命令即可

![这里写图片描述](使用gradle的productFlavors实现Android项目多渠道打包_imgs\100.png)