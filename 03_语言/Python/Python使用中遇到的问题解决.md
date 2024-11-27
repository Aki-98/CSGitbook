可以运行包含中文的.py文件，但输出中文时会显示一个方形中间一个问号

相关链接：https://blog.csdn.net/qq_15971883/article/details/108572801

解决方案1：用git-bash运行python文件，并在最前面加上PYTHONIOENCODING=utf-8 

如：

```shell
PYTHONIOENCODING=utf-8 python hello.py
```

解决方案2：在python脚本中添加如下代码：

```python
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
```

