 【jar包依赖项检查】

```shell
jdeps -verbose -R classes.jar | grep -v "java\." | grep -v "android\." | grep -v "com.ktcp\." | grep -v "com.sony\."
```

- AAR的话解压之后对classes.jar运行jdeps就行了



【给apk重新签名】

apksigner

```
java -jar apksigner.jar sign --ks <jks_location> --ks-key-alias <key_alias> --in <source_apk_location> --out <output_apk_location>

apksigner sign --ks <jks_location> --ks-key-alias <key_alias> --in <source_apk_location> --out <output_apk_location>
```

jarsigner

```shell
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore <jks_location> <apk_location> <key_alias>
```

- jarsigner只能进行V1签名，而V2签名是SDK>=24时才支持的，所以使用jarsigner签名后，在强制要求V2签名的系统上安装时会报错：INSTALL_PARSE_FAILED_NO_CERTIFICATES

  

【apk打包解包】

apktool最新版（v2.6.1）已经能够自动对SDK版本大于等于30的项目打包时跳过resource.arsc文件的压缩。

如果使用的是旧版或者自己编译的apktool，可以在打包apk时指定参数-api 30或者在解包文件夹的apktool.yml文件的doNotCompress节点中追加- resources.arsc，即可跳过resource.arsc文件的压缩。

逆向apk文件: apktool     d xx.apk,逆向之后只能看到代码的smali格式文件,需要学习smali语法才能看懂.

重新打包: apktool     b xx,打包出来的是没有签名的apk,需要签名才能安装



【强制对齐】

zipalign -f -v 4 input.apk output.apk



【APK Compare Tool】

chmod +x compare.sh &&./compare.sh