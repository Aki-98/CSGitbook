## Menu

### 历史

3.0以前：在Android3.0，当用户按“菜单”按钮时，选项菜单的内容会出现在屏幕底部，如图1所示,可包含多达6个菜单项，超出部分则以“更多”来显示。

![image-20220302095554245](Menu_imgs\image-20220302095554245.png)

3.0以后：在Android3.0及更高版本的系统中，选项菜单中的项目将出现在操作栏中，用户可以使用操作栏右侧的图标或者按设备的菜单键显示操作溢出菜单。

![image-20220302095630664](Menu_imgs\image-20220302095630664.png)

### 选项菜单（OptionMenu）

#### 使用

step1 新建菜单资源文件

![image-20220302095701112](Menu_imgs\image-20220302095701112.png)

在Design模式下编辑

![image-20220302095735376](Menu_imgs\image-20220302095735376.png)

在Text模式下编辑

图片丢失

step2 在相应的Activity类下创建OptionMenu

![image-20220302095859000](Menu_imgs\image-20220302095859000.png)

#### 属性

##### showAsAction

always表示菜单内容显示在导航栏上

图片丢失

当有图标时默认只显示图标

![image-20220302100118329](Menu_imgs\image-20220302100118329.png)

withText表示不仅显示图标还显示文字

![image-20220302100155105](Menu_imgs\image-20220302100155105.png)

never表示不显示

ifRoom表示如果有足够的空间再显示

#### 点击响应

![image-20220302100248624](Menu_imgs\image-20220302100248624.png)

#### 注意

最多允许两级菜单

### 上下文菜单（ContextMenu）

使用：长按某个 view不放，就会在屏幕中间弹出ContextMenu

#### 使用

step1 在Activity中注册

![image-20220302100430780](Menu_imgs\image-20220302100430780.png)

step2 在Activity中重写onCreateContextMenu方法

![image-20220302100507192](Menu_imgs\image-20220302100507192.png)

step3 重新onContextItemSelected方法进行菜单项的操作

![image-20220302100544312](Menu_imgs\image-20220302100544312.png)

step4 为按钮设置上下文操作模式

①实现ActionMode CallBack
②在view的长按事件中去启动上下文操作模式

![image-20220302100652889](Menu_imgs\image-20220302100652889.png)

![image-20220302100738480](Menu_imgs\image-20220302100738480.png)

![image-20220302100753240](Menu_imgs\image-20220302100753240.png)

![image-20220302100806920](Menu_imgs\image-20220302100806920.png)

![image-20220302100821008](Menu_imgs\image-20220302100821008.png)

![image-20220302100832400](Menu_imgs\image-20220302100832400.png)

### 弹出菜单（PopupMenu）

使用：一个模态形势展示的弹出风格的菜单，绑定在某个View上，一般出现在被绑定的View的下方

#### 使用

![image-20220302100929032](Menu_imgs\image-20220302100929032.png)

![image-20220302100940504](Menu_imgs\image-20220302100940504.png)

![image-20220302100950311](Menu_imgs\image-20220302100950311.png)

### Menu创建方式的优缺点

option1 通过xml定义：菜单一般在res中创建menu目录放置资源文件

![image-20220302101041759](Menu_imgs\image-20220302101041759.png)

清晰的菜单结构

将菜单内容与应用的逻辑代码分离

资源适配更容易

option2 通过java定义

![image-20220302101142481](Menu_imgs\image-20220302101142481.png)

![image-20220302101150072](Menu_imgs\image-20220302101150072.png)

### 处理Menu显示问题

![image-20220302101249560](Menu_imgs\image-20220302101249560.png)

- onCreateOptionsMenu()必须返回true，否则菜单不显示
- onOptionsItemSelected()方法返回true，告诉系统此处的操作已经完成；同时在switch中添加default实现父类功能避免有些操作未完成

![image-20220302101319360](Menu_imgs\image-20220302101319360.png)