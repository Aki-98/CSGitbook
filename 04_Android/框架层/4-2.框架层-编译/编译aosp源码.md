# 开始编译

1.加载源码编译环境

```shell
source build/envsetup.sh
```

2.选择编译目标

```shell
lunch
```

输入num选择

3.构建代码同时编译log输出到文件

```shell
make -j32 2>&1 | tee build.log
make -j16 2>&1 | tee build.log
```

>### 命令拆解：
>
>- **make:** 这是 GNU Make 工具，用于自动化编译过程。在 AOSP 中，它会根据 Makefile 中的规则来编译源代码。
>- **-j16:** 这个选项告诉 Make 工具同时使用 16 个进程来进行编译。这可以显著加快编译速度，特别是在多核处理器上。
>- **2>&1:** 这个部分会将标准错误输出（文件描述符 2）重定向到标准输出（文件描述符 1）。也就是说，无论是编译过程中的正常输出还是错误信息，都会被输出到同一个地方。
>- **|:** 管道符号，将前一个命令的输出作为后一个命令的输入。
>- **tee build.log:** 这个命令会将管道过来的数据同时输出到终端和一个名为 `build.log` 的文件中。这样，你可以在终端实时查看编译进度，同时将所有输出保存到日志文件中，方便以后查看和分析。

make -jN N数量采用CPU核数的4倍

确认自己cpu的核数

```shell
lscpu
```

看下 CPU(s)的数量

# 重置编译环境

清除编译产物，out目录下的文件会被删除

```shell
make clean
```



重置源码

```shell
repo forall -c "git add -A" && repo forall -c "git reset HEAD^^^ --hard" && repo sync
```

清理 out/ 目录：
```shell
rm -rf out/
```



# 疑难解决

编译期间电脑很卡乃至于终端退出或电脑重启，因为交换内存不够，解决方法：

> https://blog.csdn.net/zxj2589/article/details/138728945
