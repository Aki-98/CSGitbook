# 文件与编译

## 头文件

![image-20220701105233918](C++_imgs\xHQXSDu7U4O.png)

## 编译和执行过程

![image-20220701105321412](C++_imgs\q4X5BqgdRnD.png)

# 基本语法

## 关键字

![image-20220701105347930](C++_imgs\6gdcGasYZCj.png)

## 数据类型

### 整型

![image-20220701105440709](C++_imgs\bT5WTteFmmn.png)

sizeof()函数，传入变量，返回变量占用空间字节大小

### 实型（浮点型）

![image-20220701105711825](C++_imgs\EF6HvnBCYuk.png)

3.14默认为双精度 float f1=3.14 系统需要转换 建议写成float f1 = 3.14f

默认情况下输出一个小数会显示6位有效数字

科学计数法：float f=3e-2 (0.03)

### 字符型

a 97

A 65

#### 转义字符

![image-20220701105857770](C++_imgs\M2t4o8aHRdb.png)

#### 字符串

1.C风格字符串

char str[]="hello world"

cout << str << endl;

2.c++风格字符串

\#include <string>

string str="hello world";

cout << str <<endl

### 布尔型

bool 一个字节

非0 真 true

0 假 false

## 运算符

两个小数不能进行取模操作

## 数组

初始化一维数组

```c++
//后面未初始化的元素，默认值为0
int years[6] = {2020,2019,2018,2017}
//元素个数为2，不可再改变
int days[] = {2,3}
//错误！未知元素个数
int array[] = {}
//c++特性，初始化数组可以省略“=”
int days[]{1,15};
//c++特性，大括号可为空，所有元素置0
float m[100]{};

```

## 函数

## 指针

指针的大小：32位 4字节  64位8字节

 

空指针：

空指针指向的内存不可访问，指向编号为0的空间

0-255之间的内存编号是不可以访问的

 

野指针：指向非法内存空间

 

CONST 修饰指针（看const后面跟的是啥）

1.const修饰指针：常量（的）指针

const int * p = &a  （int* p指向的值是个常量）

指针的指向可以改，但指针指向的值不能改

2.const修饰常量：指针（是）常量

指针的指向不可以改，但指针指向的值可以改。

int * const p = &a (p的指向是个常量)

3.const既修饰指针，又修饰常量

const int * const p = &a

---



数据的输入

cin >> 变量

向量容器vector

![image-20220701110429000](C++_imgs\EOPuMNL5TK6.png)

![image-20220701110439851](C++_imgs\Rb31gJD2XCL.png)