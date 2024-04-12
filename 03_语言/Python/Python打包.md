pyinstaller -F -w --hidden-import urllib.request --hidden-import requests --hidden-import pytz --hidden-import jira -i JES.ico --onefile --add-data "D:\Automation\common;." --clean pa.py

1.pyinstaller 需要使用pip安装
2.-F 生成结果是一个 exe 文件，所有的第三方依赖、资源和代码均被打包进该 exe 内
3.-w 不显示命令行窗口
4.--hidden-import 解决直接打包部分依赖包找不到的问题，一个包对应一次命令
5.-i 指定icon
6.--onefile 整合依赖库生成同一的java文件
7.--add-data 用于添加本地自定义依赖库的路径
8.--clean 清除上一次pyinstaller生成的目录与文件

pyinstaller生成的目录与文件解析：
/build 构建日志等
/dist 生成的.exe文件默认放置路径
.spec pyinstaller的配置文件