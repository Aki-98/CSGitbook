AOSP编译及刷机：https://juejin.cn/post/704292166033630823
安装JDK 11
sudo apt-get install openjdk-11-jdk
安装其他程序包
sudo apt-get install git-core gnupg flex bison gperf build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache libgl1-mesa-dev libxml2-utils xsltproc unzip libncurses5

安装依赖：https://source.android.com/source/initializing?hl=zh-cn
sudo apt-get install git gnupg flex bison gperf build-essential zip curl zlib1g-dev libc6-dev lib32ncurses5-dev ia32-libs x11proto-core-dev libx11-dev lib32readline5-dev lib32z-dev libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc

获取AOSP仓库：https://source.android.com/source/build-numbers?hl=zh-cn#source-code-tags-and-builds
版本：OPR3.170623.008	android-8.0.0_r15	Oreo	Pixel XL、Pixel

下载源码：
repo init -u https://android.googlesource.com/platform/manifest -b android-8.0.0_r15
开始进行同步
repo sync -j8 #j8代表使用8个线程

报错：
error: RPC 失败。curl 56 GnuTLS recv error (-9): Error decoding the received TLS packet.
error: 预期仍然需要 45839 个字节的正文
fetch-pack: unexpected disconnect while reading sideband packet
fatal: 过早的文件结束符（EOF）
fatal: fetch-pack：无效的 index-pack 输出
解决：
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


报错：
fatal: 无法访问 'https://android.googlesource.com/platform/external/OpenCSD/'：gnutls_handshake() failed: The TLS connection was non-properly terminated.
error: Cannot fetch platform/external/OpenCSD from https://android.googlesource.com/platform/external/OpenCSD
解决：

Linux设置不锁屏
gsettings set org.gnome.desktop.session idle-delay 0


remote: Sending approximately 5.05 GiB ...Counting objects: 1           
remote: Counting objects: 19481           
remote: Counting objects: 30566           
error: RPC 失败。curl 56 GnuTLS recv error (-15): An unexpected TLS packet was received.
error: 预期仍然需要 54162 个字节的正文
fetch-pack: unexpected disconnect while reading sideband packet
fatal: 过早的文件结束符（EOF）
fatal: fetch-pack：无效的 index-pack 输出
error: Cannot fetch platform/frameworks/base from https://android.googlesource.com/platform/frameworks/base


TCP/IP问题？
https://source.android.com/docs/setup/build/known-issues?hl=zh-cn
sysctl -w net.ipv4.tcp_window_scaling=0

