**多渠道打包如何使用不同的签名？**

在android{signingConfigs{}}中定义多个签名配置

```groovy
    signingConfigs {
        config_m {
            keyAlias 'androiddebugkey'
            keyPassword 'android'
            storeFile file('../key_m/platform.jks')
            storePassword 'android'
        }
        config_t6y {
            keyAlias 'androiddebugkey'
            keyPassword 'android'
            storeFile file('../key_t6y/platform.jks')
            storePassword 'android'
        }
    }
```

在多渠道配置时，使用不用的签名，这样打包时会根据渠道自动使用签名

```groovy
    productFlavors {
        M {
            minSdkVersion 29
            dimension "model"
            signingConfig signingConfigs.config_m
        }
        T6Y {
            minSdkVersion 30
            dimension "model"
            signingConfig signingConfigs.config_t6y
        }
    }
```

另外 需要在 buildTypes{debug{}}中设置 signingConfig null，否则debug会使用默认的签名文件

相关链接：https://blog.csdn.net/liuyu0915/article/details/90485863

