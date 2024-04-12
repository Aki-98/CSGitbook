# C1 基本语法

## 1. 字符串

### 1.1 引号

单引号和双引号中的字符串完全相同

你可以使用三引号 ——（""" 或 '''）指定多行字符串。可以在三引号中自由地使用单引号和双引号。

```
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
```

### 1.2 format方法

**基本用法**

```python
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
```

output：

```
$ python str_format.py
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
```

**高级用法**

```python
# 取十进制小数点后的精度为 3 ，得到的浮点数为 '0.333'
print('{0:.3f}'.format(1.0/3))
# 填充下划线 (_) ，文本居中
# 将 '___hello___' 的宽度扩充为 11 
print('{0:_^11}'.format('hello'))
# 用基于关键字的方法打印显示 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

output：

```
0.333
___hello___
Swaroop wrote A Byte of Python
```

### 1.3 指定结尾

print 总是以一个不可见的 「新的一行」 字符（\n）作为结尾，因此对 print 的重复调用将在每个单独的行上打印输出。为了防止这个换行符被打印输出，你可以指定它以一个空（即，什么都没有）作为 end：

```python
print('a', end='')
print('b', end='')
```

output:

```
ab
```

### 1.4 转义序列

```
单引号 --> \`
表示反斜杠本身 --> \\
```

在字符串中，行末尾的单个反斜杠表示字符串在下一行中继续，但不添加换行符。例如：

```
"This is the first sentence.\
This is the second sentence."
```

等价于：

```
"This is the first sentence. This is the second sentence."
```

### 1.5 原始字符串

如果你需要指定一些没有特殊处理（转义序列等）的字符串，那么你需要指定一个 原始 字符串，指定方法是在字符串前面加上 r 或者 R 。例如：

```
r"Newlines are indicated by \n"
```

> 在处理正则表达式时，我们一般使用原始字符串。否则，可能需要进行大量的反向操作。例如，可以用 `'\\1'` 或 `r'\1'` 进行反向引用。

## 2. 对象

记住，在 Python 中，一切皆 对象 。这意味着一般情况下，在 Python 中，我们不会说「某物」而是说「对象」。

从某种意义上说，Python 的面向对象是非常纯粹的，因为一切皆对象，包括数字、字符串和函数。

## 3. 逻辑行和物理行

物理行是当你写程序的时候，你眼睛 看到 的行。逻辑行是 Python 看到 的一个程序语句。

如果你希望在单个物理行中编写更多的逻辑行，则必须使用分号 (;) 显式地指定此逻辑行 / 此语句的结尾。

```
i = 5
print(i)
```

等价于

```
i = 5;
print(i);
```

等价于

```
i = 5; print(i);
```

等价于

```
i = 5; print(i)
```

强烈建议 你坚持 一行最多一个语句 ，不要使用分号。

有一行很长的代码，你可以使用反斜杠将其分解为多个物理行。

```
i =\
5
```

等价于：

````
i = 5
````

有时候，有一种隐含的假设，你不需要使用反斜杠。在这种情况下，逻辑行有开始括号、开始方括号或者开始花括号，但是没有结束括号。我们称之为 *隐式行连接* 。

## 4. 缩进

空格在 Python 中非常重要。实际上， 行首的空格非常重要 。这就是所谓的 缩进 。逻辑行开头的前导空格（空格和制表符）用于确定逻辑行的缩进级别，然后用于确定语句的分组。

错误的缩进会导致报错

# C2 运算符与表达式

## 1.运算符

### ** 为 乘方

3\*\*4 即 3\*3\*3\*3 即81

### // 为 除且取整

x 除以 y 并返回小于商的最大整数，注意，如果操作数之一为浮点数，则返回值必为浮点数。

13 // 3 得到 4
-13 // 3 得到 -5
9//1.81 得到 4.0

### % 为 取模

返回作除法之后的余数。
13 % 3 得到 1

-25.5 % 2.25 得到 1.5

### << 为 左移

将数字位向左移动指定的位数。每个数字在内存中用位或二进制数（如 0 和 1 ）表示。

2 << 2 得到 8. 2 在二进制中用 10 表示。
将 10 向左移两位得到 1000 ，二进制 1000 表示十进制的 8 。

### \>\> 为 右移

将数字按位向右移动指定的位数。
11 >> 1 得到 5 。
11 的二进制表示为 1011 ，将其右移一位后，得到 101 也就是十进制的 5 。

### & 为 按位与

数字的按位与
5 & 3 得到 1

### | 为 按位或

数字的按位或
5 | 3 得到 7

### ^ 为 按位异或

数字的按位异或
5 ^ 3 得到 6

### ~ 为 按位取反

x 按位取反是 -(x+1)
~5 得到 -6

### not 为 布尔非

如果 x 为 True，它会返回 False。如果 x 为 False，它会返回 True。
x = True; not x 返回 False.

### and 为 布尔与

如果 x 为 False ， x and y 返回 False 。否则，返回 y 的值
由于 x 为 False ， x = False; y = True; x and y 返回 False 

在这种情况下， Python 不会计算 y ，因为它知道 ‘与’ 表达式的左边为 False ，这就意味着整个表达式必定是 False。这就是所谓的短路计算。

### or 为 布尔或

如果 x 为 True，它会返回真，否则返回 y 的值
x = True; y = False; x or y 返回 True。这里也用到了短路计算。

## 2.数学运算和赋值的快捷方式

```python
a = 2
a = a * 3
```

简写为：

```python
a = 2
a *= 3
```

## 3.计算顺序

优先级（从小到大）：

- lambda ：Lambda 表达式
- if - else ：条件表达式
- or ：布尔或
- and ：布尔与
- not x ：布尔非
- in, not in, is, is not, <, <=, >, >=, !=, == ：比较，包括成员资格测试和身份测试
- | ：按位或
- ^ ：按位异或
- & ：按位与
- <<, >> ：移位
- +, - ：加减法
- *, /, //, % ：乘除法，取整和取余
- +x, -x, ~x ：正负号，按位非
- ** ：求幂
- x[index], x[index:index], x(arguments...), x.attribute ：订阅，切片，调用，属性引用
- (expressions...), [expressions...], {key: value...}, {expressions...} ： 绑定或者元组显示，列表显示，字典显示，设置显示

一般而言，操作符从左到右进行关联。这意味着具有相同优先级的操作符按照从左到右的方式进行计算。

# C3 控制流

## if 语句

```python
if {条件1}:
    # 新程序块的开始处
    {语句1}
    {语句2}
    # 新程序块的结尾处
elif {条件2}:
    # 另一个程序块
    {语句3}
    # 你可以在程序块中“为所欲为”——做任何你想做的事情
else:
    {语句4}
    # 如果上述两个条件都不满足，则会执行到这里
```

## while 语句

```python
while {继续条件，当条件不为True时执行下面的代码，所以如果第一次这里的条件为True并执行了下面的代码，代码执行的过程中需要能够改变这个继续条件为False，不然程序会一直执行下去}:
    {语句1}
    {语句2}
else:
    {当不执行上面的代码时进入的语句块，可能第一次执行while条件为False直接进入这个语句块，也可能上面的代码执行多次后进入下面的语句块}
```

## for 循环

代码：

```python
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
```

输出：

```
$ python for.py
1
2
3
4
The for loop is over
```

## break 语句

break语句是用来 *中断* 循环语句的，即直接停止循环语句的执行，就算循环条件没有变为 false或者序列没有迭代到最后一项。

## continue 语句

continue 语句用来告诉 Python 跳过当前循环语句块中的其余部分，然后 继续 执行循环的下一个迭代。

# C4 函数

## global 语句

不在任何函数或类的定义内的变量也叫做程序的顶级 top level 变量。

如果你要在函数内给这种变量赋值，需要告诉 Python 这个变量并非本地变量，而是一个全局变量。

当函数没有同名变量时，程序会使用在函数外部定义的顶级变量，但是不应该这样做，因为读这段代码的人会不知道这个变量是在哪里定义的。

```python
x = 50

def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)

```

输出：

```
$ python function_global.py
x is 50
Changed global x to 2
Value of x is 2
```

可以在一个 global 语句中同时指定多个全局变量，就像这样：global x, y, z。

## 默认参数值

让某些形参成为可选项，当用户没有指定这些形参的值时，使用默认值

形参的默认值必须是常数

只有形参列表末尾的参数才能指定默认值，即你不能在声明参数列表时先声明有默认值的形参，然后再声明没有默认值的形参

```python
def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)
```

输出：

```
$ python function_default.py
Hello
WorldWorldWorldWorldWorld
```

## 关键字参数

给函数传递参数时使用参数的名字，可以不用位置来指定实参。

```python
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)
```

输出：

```
$ python function_keyword.py
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50
```

## 可变参数

可以使用星号 * 来定义一个能接收 *任意个* 数参数的函数

```python
def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中的所有项
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
```

输出：

```
$ python function_varargs.py
a 10
single_item 1
single_item 2
single_item 3
Inge 1560
John 2231
Jack 1123
None
```

当我们声明一个带星号的参数 *param 时，从这个参数开始，之后的所有参数都会被收集进入一个名为 param 的元组中。

类似的，当我们定义了一个带两个星号的参数 **param 时，从这个参数开始，之后的所有参数都会被收入名为 param 的字典中。

## return 语句

return 语句用于从一个函数 返回，即跳出这个函数。我们也可以从函数跳出时 返回一个值，返回值是可选的。

如果你的函数没有 return 语句，系统会自己在函数的结尾添加 return None 语句。你可以通过 print(some_function()) 来观察这一点，其中 some_function 函数没有 return 语句：

```python
def some_function():
    pass
```

输出：

```shell
>>> print(some_function())
None
```

pass 语句在 Python 中用于表示一个空的语句块，通常用于占位。

## 文档字符串 ——DocStrings

```python
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # 如果有必要，将参数转为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
```

输出：

```shell
$ python function_docstring.py
5 is maximum
Prints the maximum of two numbers.

    The two values must be integers.
```

一个函数逻辑上第一行的字符串是这个函数的 DocStrings。模块 和 类 都有各自的 DocStrings。

DocStrings 的书写惯例是：首行首字母大写，结尾有句号；第二行为空行；第三行以后为详细的描述。

建议为所有的函数编写DocStrings，除了那些只有几行的平凡函数。

我们可以通过函数的 \__doc__ 属性来访问它的 DocStrings。

help() 函数做的事情就是抓取对应函数的 \__doc__ 属性，并以美观的方式打印出来。

自动化工具也可以以同样的方式从你的程序中提取文档。

# C5 模块

编写模块的方式：

- 创建一个包含很多方法和变量并以 .py 为扩展的文件。
- 可以用 C 语言 来写模块。模块被编译好之后，使用标准 Python 解释器，就可在你的 Python 代码中调用这些模块。

引入模块的过程

- Python 解释器会在它的 `sys.path` 变量中列出来的目录中寻找这个模块
- 如果模块被找到，则运行该模块主体中的语句，这个模块就会被设为 *可用* 供你使用。 注意，初始化在我们 *第一次* 引入这个模块时就会完成。

sys 模块中的 argv 变量可以通过点表示法，即 sys.argv 访问。它清晰地指出这个名字就是 sys 模块的一部分。这种访问方式的另一优点就是这个名字不会与你程序中的任何 argv 的变量发生冲突。

sys.path 是模块导入时要搜索的目录列表。我们可以看到 sys.path 的第一个字符串是空的，空字符串意味着当前目录也是 sys.path 的一部分，这与 PYTHONPATH 环境变量是相同的。这意味着你可以直接从当前目录下导入模块。不然你还需要把你要导入的模块放到 sys.path 中的一个目录里。

## 字节码文件 .pyc

.pyc文件可以加快程序代码导入模块的过程，因为导入模块所必须的一部分操作已经被事先完成了。

这些 `.pyc` 文件一般会被创建在与它对应的 `.py` 文件相同的文件目录下。如果 Python 没有在该文件夹下写文件的权限，那么 `.pyc` 文件将不会被创建。

## from..import 语句

如果你希望直接把 argv 变量导入到你的程序中（以避免每次都要键入 sys.），那么你就可以使用 from sys import argv 语句。

警告：原则上来说，还是要 避免 使用 from..import 语句，而是使用 import 语句。这是因为如果使用 import 语句的话，你的程序会避免出现命名冲突的问题，并且代码的可读性更高。

## 模块的 \__name__

每一个模块都有一个名称，在模块中我们可以通过判断语句来确定模块的名称。这在一种情形下特别有用：确定模块被导入了？还是在独立地运行。如之前提到过的，当模块第一次被导入的时候，模块的代码将被执行。我们可以通过这一点，让模块在被导入和独立运行时执行不同的操作。通过模块的 \__name__ 属性可以实现这个功能。

```PYTHON
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
```

输出：

```
$ python module_using_name.py
This program is being run by itself

$ python
>>> import module_using_name
I am being imported from another module
>>>

```

警告：记住，你应该避免使用 * 导入，比如像 from mymodule import * 这样。

## dir 函数

内置的 dir() 函数能以列表的形式返回某个对象定义的一系列标识符。如果这个对象是个模块，返回的列表中会包含模块内部所有的函数、类和变量。

这个函数接收一个可选的参数。当参数是模块名时，函数会返回对应模块的标识符列表。没有参数时则会返回当前模块的标识符列表。

```
$ python
>>> import sys

# 获取 sys 模块内所有属性的标识符
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# 这里只列出了部分输出

# 获取当前模块内属性的标识符
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__', 'sys']

# 创建一个新的变量 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# 删除变量 'a'
>>> del a

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']
```

注意 dir 函数对 任何 对象都有效。例如：dir(str) 会列出 str (String) 类的属性。

还有一个 vars() 函数，它有时能给你对象的属性和它们的值，但这个函数并不总是有效。

## 程序包

程序包就是一个装满模块的文件夹，它有一个特殊的 __init__.py 文件，这个文件告诉 Python 这个文件夹是特别的，因为它装着 Python 的模块。

让我们假设你想创建一个叫做 world 的程序包，它有很多子程序包 asia、africa 等。这些子程序包依次包含 india、madagascar 等模块。

以下是一种组织文件夹的方式：

```
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py
```

# C6 数据结构

python 中有四种内置的数据结构 list、tuple、dictionary、set

## List 列表

保存有序项集合的数据结构。

一旦创建了列表，你就可以在列表中增加，删除或者搜索列表中的项 。

```python
# 这是我的购物清单
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
```

输出

```shell
$ python ds_using_list.py
I have 4 items to purchase.
These items are: apple mango carrot banana
I also have to buy rice.
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
The first item I will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```

## Tuple 元组

将多个对象组合在一起，和字符串一样是 不可变的 ，即你不能修改元组。

```python
# 尽管圆括号是可选的，
# 我还是建议使用圆括号，
# 来表示元组的开始和结束。
# 因为显式总比隐式要好。
zoo = ('python', 'elephant', 'penguin')

print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
```

输出：

```shell
$ python ds_using_tuple.py
Number of animals in the zoo is 3
Number of cages in the new zoo is 3
All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
Animals brought from old zoo are ('python', 'elephant', 'penguin')
Last animal brought from old zoo is penguin
Number of animals in the new zoo is 5
```

**包含0个项的元组**

由一对空的圆括号构成，例如：

```
myempty = ()
```

**包含1个项的元组**

一对空的圆括号和第一项后面的一个逗号构成，例如：

```
singleton = (2, )
```

## Dict 字典

- 字典是一组键值对
- 键必须是唯一的
- 键值对不以任何形式排序
- 字典的键只能用不可变对象（比如字符串），字典的值不可变对象或者可变对象都可以使用。

```python
# 'ab' 是 'a'ddress'b'ook 的缩写，意思是地址簿

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一个键值对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一个键值对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
```

输出：

```shell
$ python ds_using_dict.py
Swaroop's address is swaroop@swaroopch.com

There are 3 contacts in the address-book

Contact Swaroop at swaroop@swaroopch.com
Contact Matsumoto at matz@ruby-lang.org
Contact Larry at larry@wall.org

Guido's address is guido@python.org
```

## Seq 序列

列表，元组和字典都是序列的一种，但序列是什么，为什么它们这么特别呢？

序列的主要特征是：成员测试 (例如：in 与 not in 表达式) 和 索引操作，这两种操作让我们可以直接从序列中提取特定的部分。

上面提到了三种序列：列表、元组和字典。它们还有另一种特殊的操作 —— 切片 ，切片操作让我们可以得到序列的一部分。

```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# 字符串索引 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1]) # 返回最后一个元素
print('Item -2 is', shoplist[-2]) # 返回倒数第二个元素
print('Character 0 is', name[0])

# 列表切片 # 
# 数是可选的，冒号是必须的
# 冒号之前的第一个数表示切片开始的位置，冒号之后的第二个数表示切片到哪里终止。如果不指定第一个数，Python 会从序列首开始，不指定第二个数则到序列尾结束。
# 注意返回的切片从开始位置 开始，在结束位置之前 结束，即一个左闭右开区间。
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 字符串切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
```

输出：

```shell
$ python ds_seq.py
Item 0 is apple
Item 1 is mango
Item 2 is carrot
Item 3 is banana
Item -1 is banana 
Item -2 is carrot
Character 0 is s
Item 1 to 3 is ['mango', 'carrot']
Item 2 to end is ['carrot', 'banana']
Item 1 to -1 is ['mango', 'carrot']
Item start to end is ['apple', 'mango', 'carrot', 'banana']
characters 1 to 3 is wa
characters 2 to end is aroop
characters 1 to -1 is waroo
characters start to end is swaroop
```

还可以使用第三个参数——步长

如果给负数-1，则会返回文本的反转

```python
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
```

输出：

```shell
$ python3 io_input.py
Enter text: sir
No, it is not a palindrome

$ python3 io_input.py
Enter text: madam
Yes, it is a palindrome

$ python3 io_input.py
Enter text: racecar
Yes, it is a palindrome
```

## Set 集合

集合（set）是简单对象的 无序的 集合（collection）。当对象在集合（collection）中的存在比对象在集合（collection）中的顺序或者比对象在集合（collection）中出现的次数更为重要时，我们就会用到集合（set）。

你可以使用集合（set）来测试成员资格，看看它是否是另一个集合（set）的子集，找到两个集合之间的交集，等等。

```python
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> 'usa' in bri
False
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # 或者是 bri.intersection(bric)
{'brazil', 'india'}
```

> 在数学上， set 和 collection 的区别是是否具有互异性，即，包含的元素是否可以重复出现。set 中的元素具有互异性，而 collection 中的元素不具有互异性。

## 引用

当你创建了一个对象，并把它赋值给一个变量时，这个变量只是 *引用* 了这个对象，变量并不能代表对象自身！因此，你可以把变量名当作一个指针，它指向储存对象的那一块计算机内存。这称作 *绑定* 名称到对象。

```python
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一个对象的另一个别名！
mylist = shoplist

# 我买下了第一件商品，所以把它从列表中移除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 产生了同样的输出
# 输出的都是没有 'apple' 的相同列表
# 这验证了它们都指向着同一个对象

print('Copy by making a full slice')
# 通过全切片来获得一个副本
mylist = shoplist[:]
# 移除第一个元素
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在这两个列表有差异了
```

输出：

```shell
$ python ds_reference.py
Simple Assignment
shoplist is ['mango', 'carrot', 'banana']
mylist is ['mango', 'carrot', 'banana']
Copy by making a full slice
shoplist is ['mango', 'carrot', 'banana']
mylist is ['carrot', 'banana']
```

## 更多字符串操作

```
# 这是一个字符串对象
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
```

输出：

```
$ python ds_str_methods.py
Yes, the string starts with "Swa"
Yes, it contains the string "a"
Yes, it contains the string "war"
Brazil_*_Russia_*_India_*_China
```

# C7 面向对象编程

## 关于 self

类的方法在入口参数表的开头必须有一个额外的形式参数，指向对象本身，约定它的名字叫做self。（可以起其他名字，但是强烈建议不要这样做）

## 类

```python
class Person:
    pass  # 一个空的语句块

p = Person()
print(p)
```

输出：

```shell
$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>
```

## 方法

```python
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# 上面两行也可以写成下面这种形式
# Person().say_hi()
```

输出：

```shell
$ python oop_method.py
Hello, how are you?
```

## \__init__ 方法

\__init__ 方法将在类的对象被初始化（也就是创建）的时候自动的调用。这个方法将按照你的想法 初始化 对象（通过给对象传递初始值）。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# 上面两行也可以写成下面这种形式
# Person('Swaroop').say_hi()
```

输出：

```shell
$ python oop_init.py
Hello, my name is Swaroop
```

## 类和对象中的变量

有两种类型的 域 – 类变量和对象变量。这是通过他们是 属于 类还是 属于 对象这一点来区分的。

类变量是共享的 – 他们可以通过这个类所有的对象来访问。类变量只有一份拷贝，这意味着当一个对象改变了一个类变量的时候，改变将发生在所有这个类的对象中。

对象变量属于每一个对象（实例）自身。在这种情况下，每一个对象都有属于它自己的域（在不同的对象中，这些变量不是共享的，它们也并不相关，仅仅是名称相同。

类变量应该使用className.variableName或者self.\__class__.population来访问（self.\__class__指向每个对象自己的类）

对象变量应该使用self.variableName来访问

当一个方法属于类不属于对象，可以用classmethod 或者 staticmethod 来定义它。

```python
@classmethod #这是一个装饰器
def how_many(cls):
	"""显示当前人口数。"""
	print("We have {:d} robots.".format(cls.population))
```

装饰器可以被想象成为一个快捷的方式去调用一个包裹函数（一个包裹着另外一个函数的函数，因此可以在内部函数调用之前及之后做一些事情），因此使用 @classmethod 装饰器和如下调用等价：

所有的类成员都是公共的。只有一种情况除外：如果你使用 双下划线前缀 （例如 __privatevar ）时，Python 会使用命名粉碎规则 (name-mangling) 作用于这个变量，并使其变为私有变量。

相关链接：https://zhuanlan.zhihu.com/p/79280319

## 继承

```python
class SchoolMember:
    '''代表了学校中的任何一个成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我细节'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''表征一个老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''表征一个学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 输出一个空行
print()

members = [t, s]
for member in members:
    # 所有的老师和学生都可用
    member.tell()
```

# C8 输入与输出

## 文件

可以创建一个 file 类的对象来打开文件以供读写，使用 read, readline 或 write 中的恰当方法可以读取或写入文件。对文件的读写能力取决于你打开文件时选择的模式。当你处理完文件后，你可以使用 close 方法告诉 Python 你已经使用完文件了。

```python
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开文件进行 'w'riting 写操作
f = open('poem.txt', 'w')
# 将文本写入到文件
f.write(poem)
# 关闭文件
f.close()

# 如果没有指定文件打开方式
# 默认使用 'r'ead 读模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零行意味着 EOF 文件结尾
    if len(line) == 0:
        break
    # `line` 中已经自带换行了
    # 因为它是从文件中读取出来的
    print(line, end='')
# 关闭文件
f.close()
```

输出：

```shell
$ python3 io_using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```

## Pickle

```python
import pickle

# 这里我们将存储对象的文件的名称
shoplistfile = 'shoplist.data'
# 要买的东西的清单
shoplist = ['apple', 'mango', 'carrot']

# 写入文件
f = open(shoplistfile, 'wb')
# 将对象存储到文件
pickle.dump(shoplist, f)
f.close()

# 销毁 shoplist 变量
del shoplist

# 从存储中读回
f = open(shoplistfile, 'rb')
# 从文件加载对象
storedlist = pickle.load(f)
print(storedlist)
```

输出：

```shell
$ python io_pickle.py
['apple', 'mango', 'carrot']
```

# C9 异常

## 错误 Error

编译器可以检查到的

## 异常 Exception

## 处理异常

```python
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))
```

输出：

```shell
# 按下 ctrl + d
$ python exceptions_handle.py
Enter something --> Why did you do an EOF on me?

# 按下 ctrl + c
$ python exceptions_handle.py
Enter something --> ^CYou cancelled the operation.

$ python exceptions_handle.py
Enter something --> No exceptions
You entered No exceptions
```

## 引发异常

可以用 raise 语句 引发（ raise ） 异常，需要提供错误或异常的名字以及被 抛出（ thrown ） 的异常对象。

```python
class ShortInputException(Exception):
    '''用户定义的异常对象'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # 其他程序可以在这里正常执行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
```

## Try … Finally

```python
import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们通常读取文件的语句
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 让程序保持运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
```

输出：

```shell
$ python exceptions_finally.py
Programming is fun
Press ctrl+c now
You cancelled the reading from the file.
(Cleaning up: Closed the file)
```

## with 语句

```python
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
```

# C10 标准库

## sys模块

sys 模块有一个给出版本信息的 version_info tuple

```
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
```

## logging 模块

如果你希望将一些调试消息或重要消息存储在某个地方，以便你可以检查你的程序是否按照预期运行，该怎么办？你怎样将这些信息「存在某地」，这可以用 logging 模块收集。

```python
import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
```

输出：

```shell
$ python stdlib_logging.py
Logging to /Users/swa/test.log

$ cat /Users/swa/test.log
2014-03-29 09:27:36,660 : DEBUG : Start of the program
2014-03-29 09:27:36,660 : INFO : Doing something
2014-03-29 09:27:36,660 : WARNING : Dying now
```

首先，我们查看 platform.platform() （查看 import platform; help(platform) 获得更多信息）返回的字符串来检查我们所用操作系统类型。如果是 Windows，我们找到要存储信息的主驱动器、用户根文件夹和文件名。把这三个部分放在一起，我们就得到了文件的完整位置。对于其他平台，我们只需要知道用户的主文件夹，就可以得到文件的完整位置。

我们使用 os.path.join() 函数组合路径的三个部分。 使用特殊函数而不仅仅是将字符串拼接到一起的原因是，这个函数将确保完整位置与操作系统预期的格式相同。注意：我们在这里使用的 join() 方法是 os 模块的一部分，它与我们在本书的其他地方使用的字符串方法 join() 不同。

# C11 更多知识

## 传递元组

可以用于在函数中返回两个不同的值

```python
>>> def get_error_details():
...     return (2, 'details')
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'
```

请注意， a, b = <某些表达式> 会将表达式的结果解析为两个值组成的元组。

这也意味着在 Python 中交换两个变量的最快方法是：

```shell
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
```

## 魔术方法

- \__init__(self, ...)

在返回新创建可以使用的对象之前调用此方法。

- \__del__(self)

在对象被销毁之前调用（具有不可预测时机，所以避免使用它）

- \__str__(self)

当我们使用 print 函数或使用 str() 时调用。

- \__lt__(self, other)

使用小于（ less than ）运算符（<）时调用。 同样，所有运算符都有特殊的方法（+，> 等）

- \__getitem__(self, key)

使用 x[key] 索引操作时调用。

- \__len__(self)

当内置的 len() 函数用于序列对象时调用。

## 单个语句块

当语句块只包含一个语句，那么可以在条件语句或循环语句的同一行指定。

```shell
>>> flag = True
>>> if flag: print('Yes')
...
Yes
```

## Lambda 格式

lambda 语句用于创建新的函数对象。 基本上， lambda 采用一个参数，后跟一个表达式。 Lambda 成为函数的函数体。 新函数返回此表达式的值。

```python
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
```

输出：

```shell
$ python more_lambda.py
[{'y': 1, 'x': 4}, {'y': 3, 'x': 2}]
```

## 列表推导

列表推导用于从现有列表中导出新列表。

```python
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)
```

输出：

```
$ python more_list_comprehension.py
[6, 8]
```

## 在函数中接收元组和字典

有一种特殊的方法可以分别使用 * 或 ** 前缀将参数作为元组或字典接收到函数中。 当在函数中使用可变数量的参数时，这很有用。

```python
>>> def powersum(power, *args):
...     '''返回每个参数指定幂次的总和。'''
...     total = 0
...     for i in args:
...         total += pow(i, power)
...     return total
...
>>> powersum(2, 3, 4)
25
>>> powersum(2, 10)
100
```

因为我们在 args 变量上有一个 * 前缀，所有传递给函数的额外参数都作为元组存储在 args 中。 如果使用了 ** 前缀，那么额外的参数将被作为字典的键 / 值对。

## assert 语句

assert 语句用于断言某值为 True 。 例如，如果您非常确定您正在使用的列表中至少有一个元素并且想要检查它，并且如果不是 True 则引发错误，那么 assert 语句在这种情况下是理想的。 当 assert 语句失败时，会引发 AssertionError 。 pop（） 方法删除并返回列表中的最后一项。

```shell
>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

## 装饰器

装饰器是用于包装函数的快捷方式。 这有助于一遍又一遍地使用相同的代码『包装』功能。 例如，我为自己创建了一个 retry 装饰器，我能应用于任何函数，如果在运行期间抛出任何异常，则会再次重试，直到最多 5 次并且每次重试之间有间隔。 这对于你尝试向远程计算机进行网络连接的情况特别有用：

```python
from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapper_function

counter = 0

@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    # 这将在第一次调用中抛出异常
    # 并且在第二次调用中工作正常（即重试）
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database("Some bad value")
```

输出：

```shell
$ python more_decorator.py
Write to a database or make a network call or etc.
This will be automatically retried if exception is thrown.
ERROR:retry:Attempt 1/5 failed : (('Some bad value',), {})
Traceback (most recent call last):
  File "more_decorator.py", line 14, in wrapper_function
    return f(*args, **kwargs)
  File "more_decorator.py", line 39, in save_to_database
    raise ValueError(arg)
ValueError: Some bad value
Write to a database or make a network call or etc.
This will be automatically retried if exception is thrown.
```

