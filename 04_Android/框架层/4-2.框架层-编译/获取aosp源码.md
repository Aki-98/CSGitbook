# Manifest

## 初始化repo

```shell
repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r28
```

> android 14 有一个版本的revision是不可用的, 忘记了

#### **(1) `.repo` 中的 `manifest` 将被覆盖**

- 新的 `repo init` 会更新 `.repo/manifest.xml` 文件，以及 `.repo/manifests` 仓库的状态。
- 之前指定的分支、URL 或其他配置将被新的 `repo init` 覆盖。

#### **(2) 本地代码不自动更新**

`repo init` 只会更新 `.repo` 配置，不会直接修改已同步的代码。需要运行 `repo sync` 来应用新配置并同步新的代码分支。

## 后续查看源码来自的remote和branch

运行以下命令

```shell
repo info
```

# Download

开始进行同步

```
repo sync 
```

使用八个线程  #j8代表使用8个线程

```
repo sync -j8
```

强制同步所有内容

```shell
repo sync --force-sync
```



# 踩坑

## 问题：Git缓存不够

报错：

```
error: RPC 失败。curl 56 GnuTLS recv error (-9): Error decoding the received TLS packet.
error: 预期仍然需要 45839 个字节的正文
fetch-pack: unexpected disconnect while reading sideband packet
fatal: 过早的文件结束符（EOF）
fatal: fetch-pack：无效的 index-pack 输出
```


解决：

```shell
apt install gnutls-bin
git config --global http.sslVerify false
git config http.postBuffer 1048576000
git config https.postBuffer 1048576000
git config --system core.longpaths true
root@aki-OptiPlex-7090:/aosp# git config --global http.postBuffer 10485760000
root@aki-OptiPlex-7090:/aosp# git config --global https.postBuffer 10485760000
root@aki-OptiPlex-7090:/aosp# git config --global http.lowSpeedLimit 0
root@aki-OptiPlex-7090:/aosp# git config --global https.lowSpeedLimit 0
root@aki-OptiPlex-7090:/aosp# git config --global https.lowSpeedTime 999999
root@aki-OptiPlex-7090:/aosp# git config --global http.lowSpeedTime 999999
```



## 问题： TLS（传输层安全性）连接问题

报错：

```
fatal: 无法访问 'https://android.googlesource.com/platform/external/OpenCSD/'：gnutls_handshake() failed: The TLS connection was non-properly terminated.
error: Cannot fetch platform/external/OpenCSD from https://android.googlesource.com/platform/external/OpenCSD
```


解决：Linux设置不锁屏（可能是锁屏了导致中断）

```
gsettings set org.gnome.desktop.session idle-delay 0
```

## 同步源代码树时遇到的问题（TCP 问题）

**症状**：在同步时 `repo sync` 挂起，通常是在同步操作完成 99% 时出现这种情况。

**原因**：TCP/IP 堆栈中的某些设置在有些网络环境中会导致出现问题，使得 `repo sync` 既无法完成，也不会失败。

**解决方法**：在 Linux 中，请输入以下命令：

```
sysctl -w net.ipv4.tcp_window_scaling=0
```
