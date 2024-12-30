# windows程序内部运行原理

## Windows API

操作系统能完成的功能的函数集合

位置：Windows/System32/Kernel32.dll、 USER32.dll、GDI32.dll

使用：C和Windows SDK开发包( API函数是用纯C写的，都在windows.h中有声明)

## MFC

MFC > Microsoft Foundation Classes > 微软基础类库

一个对Windows API进行封装后产生的类库，提供了一个面向对象的编程方式。

MFC使Windows程序员能够利用C++面象对象的特性进行编程

**为什么要使用MFC？**

- 可重用性
- 封装后使方法和属性更紧密的捆绑
- 常用的功能自动化，减少编写代码的数量
- 提供应用程序的框架结构

框架结构提供了抽象功能，它远远超出了Windows API的功能。例如:MFC的文档/视图体系结构在API上建造了一个功能强大的基础结构,它把程序中数据的图形表示(或成为视图)与数据本身分开。这种抽象对API而言完全是陌生的，而且在MFC框架结构之外或类似的类库中也不存在。

## Windows编程模型

![image-20220301084146831](windows_imgs\YKPz3Jbmz9I.png)

**编写windows应用程序的要素**

- 入口函数
- 创建窗口
- 发送消息与消息循环
- 窗口过程与消息响应

## 句柄

操作系统通过句柄来找到对应的资源进行管理和操作。

按资源的类型，又可将句柄细分成<u>图标句柄</u>(HICON)，<u>光标句柄</u>(HCURSOR)，<u>窗口句柄</u>(HWND)，<u>应用程序实例句柄</u>(HINSTANCE)等等各种类型的句柄。

操作系统给每一个窗口指定的一个唯一的标识号即窗口句柄。 

## 创建窗口

API中对数据的宏定义

```c++
int x, y;
x = 30;	
y = 30;		
//x和y既可以用来表示坐标点，也可以用来表示宽度和高度，还可以用来表示身高和体重。

typedef int WIDTH
typedef int HEIGHT
WIDTH x;
HEIGHT y;
//我们从变量的类型上就可以知道x和y是用来表示宽度和高度。

```



```java
char str[255];
sprintf (str, "%s"，lpCmdLine);
//参数1：父窗口，默认为桌面
//参数2：显示的内容
//参数3：窗口标题
//参数4：窗口布局
//返回值：整型数，告诉程序用户按了哪个按钮
MessageBox (NULL, str,"命令行",O);
sprintf(str,"%d", nCmdShow) ;
MessageBox (NULL,str,"窗口状态", 0);
```

## 代码

```c++
#include <windows.h>
#include <stdio.h>

//声明窗口过程函数
LRESULT CALLBACK MyWndProc(
	HWND hwnd,//handle to window
    UINT uMsg,//message identifier
	WPARAM wParam,//first message parameter
    LPARAM lParam,// second message parameter
)
    
//1 入口函数
int WINAPI WinMain(
	HINSTANCE hInstance,//应用程序的实例句柄
	HINSTANCE hPrevInstance,//老版本需要，传入空
	LPSTR lpCmdLine,//命令行
	int nCmdShow,// 窗口显示时的状态
)
{
	//2 创建窗口
	//2.1 设计一个窗口类
    WNDCLASS MyWnd;
	MyWnd.cbClsExtra = NULL;//窗口类附加内存，用不到，设置为空就好
    MyWnd.cbWndExtra = NULL;//窗口附加内存，用不到，设置为空就好
	MyWnd.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);//背景颜色，getStockObject还可以获得画刷、画笔、字体、调色板，句柄类型不一样，c语言特性需要对这些资源进行强转
    MyWnd.hCursor = LoadCursor (NULL，IDC_ARROW);//鼠标形状
    MyWnd.hIcon = LoadIcon (NULL，IDI_APPLICATION );//窗口图标，LoadIcon的第一个参数为空代表图标资源由操作系统提供，不为空时只能传入hInstance，代表图标自己绘制
    MyWnd.hInstance = hISnstance;//应用程序实例句柄
    MyWnd.lpfnWndProc = MyWndProc;//指向窗口过程函数的指针
    MyWnd.lpszClassName = "Hello";//窗口型号名称
    MyWnd.lpszMenuName = NULL;//窗口没有菜单
	MyWnd.style = CS_HREDRAW | cS_VREDRAW;//样式，当水平尺寸或垂直尺寸变化时，窗口要重新绘制
    
    //2.2 对设计好的窗口类进行注册
	RegisterClass(&MyWnd) ;
	
    //2.3 创建窗口
    HWND hWnd;//定义了一个句柄，不代表窗口已经生成
	hWnd = CreateWindow("Hello","Windows编程", 
                        WS_OVERLAPPEDWINDOW & ~WS_MAXIMIZEBOX,
                        //~WS_MAXIMIZEBOX代表去掉最大化按钮
                        0,0,800,600,
                        //CW_USEDEFAULT,CW_USEDEFAULT,CW_USEDEFAULT,CW_USEDEFAULT
                        //代表不指定具体的位置和尺寸，使用默认的，操作系统会根据分辨率、窗口布局等显示窗口
                        NULL,NULL,hInstance,
                        "欢迎来到Windows编程!"
                        //CREATE消息携带的信息，打开窗口前显示
                       );
/**
	//API函数，创建窗口，调用时会发送消息W_CREATE
	HWND CreateWindow(
		LPCTSTR lpClassName,//已注册的窗口类名称
		LPCTSTR ipWindowName,//窗口标题栏中显示的文本
		DWORD dwStyle,//窗口类样式，代表共同都拥有的样式
		int x,//水平坐标,坐标原点是屏幕的左上角
		int y,//垂直坐标
		int nWidth,//宽度
		int nHeight,//高度
		HWND hWndParent,//父窗口句柄,桌面是操作系统原始的父窗口
		HMENU hMenu,//菜单句柄
		HINSTANCE hInstance,//应用程序实例句柄
		LPVOID lpParam//用于多文档程序的附加参数,单文档为NULL
	);
**/
    
/**
	//消息结构体
**/
    //2.4 显示及其更新窗口
    ShowWindow (hWnd,SW_SHOW);
    UpdateWindow (hWnd) ;
	//如果有无效区，则马上发送WM_PAINT到窗口处理过程，
	//不进消息队列进行排队等待，立即刷新窗口，否则，什么都不做。
    
    //3.消息循环
    //如果没有消息循环，窗口会一闪而过
	MSG msg;
    while (GetMessage (&msg, NULL,0,0))//从消息队列中获取消息,拿到QUIT消息则返回0，当程序异常时返回-1
    {
		TranslateMessage (&msg);//消息解释
        /**
        	TranslateMessage函数用于将虚拟键消息转换为字符消息。当我们敲击键盘上的某个字符键时，系统将产生WM_KEYDOWN和WM_KEYUP消息。这两个消息的附加参数(wParam和lParam）包含的是虚拟键代码和扫描码等信息，而我们在程序中往往需要得到某个字符的ASCII码，TranslateMessage这个函数就可以将WM_KEYDOWN和WM_KEYUP消息的组合转换为一条WM_CHAR消息，该消息的WParam附加参数包含了字符的ASCII码），并将转换后的新消息投递到调用线程的消息队列中。注意，Translate函数并不会修改原有的信息，他只是产生新的消息并投递到消息队列中。
        **/
		DispatchMessage (&msg) ;//将消息发送到“窗口过程”
    }
	return 0;

/**
	BOOL GetMessage(
		LPMSG lpMsg,              // 消息结构体指针，返回消息信息 
		HWND hWnd,               // 窗口句柄 ，通常设为NULL
		UINT wMsgFilterMin,   // 消息过滤最小值 
		UINT wMsgFilterMax   // 消息过滤最大值 
     ); 
	//GetMessage从线程的消息队列中取出消息，取出的消息保存在事先定义好的消息的结构体对象中。

**/
    //4.“窗口过程函数”(编写消息响应代码)

    
typedef struct _WNDCLASS { 
   UINT    	style;//窗口类样式
   WNDPROC	lpfnWndProc;//窗口过程函数指针
   int      cbClsExtra;//窗口类附加内存字节数，通常为0
   int      cbWndExtra;//窗口附加内存字节数，通常为0
   HANDLE 	hInstance;//应用程序实例句柄
   HICON   	hIcon;//标题栏图标
   HCURSOR 	hCursor;//光标
   HBRUSH  	hbrBackground;//窗口背景颜色
   LPCTSTR 	lpszMenuName;//菜单资源名称
   LPCTSTR 	lpszClassName;//窗口类名称
} WNDCLASS; 

WNDCLASS MyWnd;
MyWnd.cbClsExtra = NULL;
MyWnd.cbWnd Extra = NULL;
MyWnd.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
MyWnd.hCursor = LoadCursor (NULL, IDC_ARROW);
MyWnd.hIcon = LoadIcon (NULL,IDI_QUESTION);
MyWnd.hInstance = hInstance;
MyWnd.lpfnWndProc = MyWndProc;
MyWnd.lpszClassName = "He1lo";
MyWnd.lpszMenuName = NULL;
MyWnd.style = CS_HREDRAW | CS_VREDRAW;
    


```



```c
LRESULT CALLBACK MyWndProc (
    HWND hwnd,//handle to window
	UINT uMsg，//message identifier
    WPARAM wParam,//first message parameter
	LPARAM lParam//second message parameter
}

switch (uMsg){
    case WM_CREATE:
		//查看CreateWindow函数的最后一个参数
		MessageBox(hwnd,(char*) (((LPCREATESTRUCT)1Param)->lpCreateParams),"启动窗口",0);
		return 0;//返回值不能是-1，否则CreateWindow函数返回0
	case WM_CLOSE:
		if (IDYES == MessageBox (hwnd,"真的要退出吗?","退出",MB_YI)
			DestroyWindow (hwnd);
		break;
    case WM_DESTROY:
		PostQuitMessage(0);
        break;
    case WM_CHAR:
		char str[255];
		sprintf (str,"char is %d", wParam);
        MessageBox (hwnd,str,"按键响应",0);。
        break;
    case WM_LBUTTONDOWN:
        HDC hDC;
        hDC = GetDC(hwnd);
        TextOut(hDC,255,100,"Hello World!",strlen("Hello World!"));
        ReleaseDC(hwnd,hDC);
        break;
	case WM_PAINT://窗口无效-->重绘-->窗口重新变成有效状态
        HDC hpaintDC;
        PAINTSTRUCT ps;
        hpaintDC = BeginPaint(hwnd,&ps);//不能用getDC
        TextOut(hpaintDC,255,150,"Hello World!",strlen("Hello World"));//文本输出，应该在beginpaint下面
        EndPaint(hwnd,&ps);
    case WM_RBUTTONDOWN:
        sendMessage(hwnd,WM_SETTEXT,0,(LPARAM)"right button down");//改变当前窗口的标题
        sendMessage(FindWindow("CalcFrame",NULL),WM_SETTEXT,0,(LPARAM)"right button down");//改变其他窗口的标题，CalcFrame是系统计算器的窗口类名称
        break;
    default:
		return DefwindowProc(hwnd, uMsg, wParam，lParam);
}
return 0;
            
/**
大多数消息是由操作系统产生和发送，此外我们也可以人为调用SendMessage和PostMessage函数来自行发送消息。
SendMessage将消息直接发送给窗口，并调用该窗口过程进行处理。在窗口过程对消息处理完毕后,该函数才返回。
PostMessage函数将消息放入与创建窗口的线程相关联的消息队列后立即返回。
**/

```

# 编写Windows应用程序

**要素**

1.入口函数WinMain

2.创建窗口

3.消息循环与发送消息

4.窗口过程与消息响应

## 1.入口函数WinMain

```c++
int WINAPI WinMain(
    HINSTANCE hInstance,//当前应用程序实例句炳

    HINSTANCE hPrevInstance,//永远为NULL

    LPSTR lpCmdLine,//命令行参数

    int nCmdShow//窗口显示时的状态
);
```

## 2.创建窗口

- 设计一个窗口类
- 注册窗口类
- 创建窗口
- 显示及更新窗口

**设计窗口类**

```c++
typedef struct _WNDCLASS { 
   UINT    	style;//窗口类样式
   WNDPROC	lpfnWndProc;//窗口过程函数指针
   int      cbClsExtra;//窗口类附加内存字节数，通常为0
   int      cbWndExtra;//窗口附加内存字节数，通常为0
   HANDLE 	hInstance;//应用程序实例句柄
   HICON   	hIcon;//标题栏图标
   HCURSOR 	hCursor;//光标
   HBRUSH  	hbrBackground;//窗口背景颜色
   LPCTSTR 	lpszMenuName;//菜单资源名称
   LPCTSTR 	lpszClassName;//窗口类名称
} WNDCLASS; 
```

**创建窗口**

```c++
HWND CreateWindow(
	LPCTSTR lpClassName,//己注册的窗口类名称
    LPCTSTR lpWindowName,//窗口标题栏中显示的文本
    DWORD dwStyle,//窗口样式
    int x,//水平坐标
	int y,//垂直坐标
	int nWidth,//宽度
	int nHeight,//高度
	HWND hWndParent,//父窗口句柄
	HMENU hMenu,//菜单句柄
	HINSTANCE hInstance,//应用程序实例句柄
	LPVOID lpParam//用于多文档程序的附加参数,单文栏为NULL
);
```

## 3.消息循环与发送消息

```c++
MSG msg;
while (GetMessage(&msg,NULL,0,0))// 从消息队列获取消息
{
	TranslateMessage(&msg);//消息解释
	DispatchMessage(&msg);//将消息发送到“窗口过程”
}
```

**GetMessage**

```c++
BOOL GetMessage(
	LPMSG IpMsg,//消息结构体指针,返回消息信息
	HWND hWnd,//窗口句柄,通常设为NULL
	UINT wMsgFilterMin,//消息过滤最小值
	UINT wMsgFilterMax//消息过滤最大值
);
```

GetMessage从线程的消息队列中取出消息，取出的消息保存在事先定义好的消息的结构体对象中。

GetMessage函数取到除WM_QUIT外的消息均返回非零值,只有在接收到WM_QUIT消息时，才返回0。

什么时候才会收到WM_QUIT呢?(见窗口过程)

**TranslateMessage**

TranslateMessage函数用于将虚拟键消息转换为字符消息。当我们敲击键盘上的某个字符键时,系统将产生WM_KEYDOWN和WM_KEYUP消息。这两个消息的附加参数(wParam和IParam)包含的是虚拟键代码和扫描码等信息,而我们在程序中往往需要得到某个字符的ASCII码，TranslateMessage这个函数就可以将WM KEYDOWN和WM_KEYUP消息的组合转换为一条WM_CHAR消息，该消息的WParam附加参数包含了字符的ASClI码),并将转换后的新消息投递到调用线程的消息队列中。注意, Translate函数并不会修改原有的信息，他只是产生新的消息并投递到消息队列中。

**DispatchMessage**

DispatchMessage分派一个消息到窗口过程。由窗口过程函数对消息进行处理。

DispatchMessage实际上是将消息回传给操作系统,再由操作系统调用窗口过程函数对消息进行处理。

## 4.窗口过程与响应消息

**窗口过程函数**

窗口类第二个成员变量<u>lpfnWndProc</u>指定了这一类型的<u>窗口过程函数</u>，也称<u>回调函数</u>。

当应用程序收到给某一窗口的消息时，操作系统调用回调函数来处理这条消息。回调函数本身的代码必须由应用程序自己完成。

**回调函数**

凡是由你设计而却由Windows系统调用的函数,统称为Callback函数。这些函数都有一定的类型,以配合Windows的调用操作。
除了窗口过程函数,Windows API还有一些其它的回调函数，例如SetTimer、LineDDA、
EnumObject。这种函数会在进行某种行为之后或满足某种状态之时，操作系统自动调用该函数。

**响应消息实例**

```c++
LRESULT CALLBACK MyWndProc(
    HWND hwnd,//handle to window
	UINT uMsg,//message identifier
	WPARAM wParam,//first message parameter
    LPARAM lParam//second message parameter
)
{
	switch (uMsg){
		case WM PAINT://响应消息
		case WM KEYDOWN://响应消息
		case WM LBUTTONDOWN://响应消息
		default:
			return  DefWindowProc(hwnd,uMsg,wParam,lParam);
	}
	return 0;
}
```

**DefWindowProc**
我们的程序无论多大都不可能将所有的消息都处理,所以我们必须有一个机制让不感兴趣的、不需要我们处理的消息，交还给Windows操作系统为我们处理,这个过程就是由DefWindowProc函数来实现的，也是每个程序所必备的。

# 掌握C++

## 虚函数与多态

当C++编译器在编译的时候,发现基类的函数是虚函数,这个时候C++就会采用迟绑定(late binding）的技术，在运行时，依据对象的类型(在示例程序中，我们传递的派生类对象的地址)来确认调用的哪一个函数,这种能力就做C++的<u>多态性</u>。

在基类的函数前加上virtual关键字，该函数则为<u>虚函数</u>。<u>虚函数派生下去仍为虚函数</u>,而且可以省略virtual关键字。

在派生类中重写该函数,<u>运行时将会根据指针实际所指的对象的类型来调用相应的函数</u>。如果对象类型是派生类,就调用派生类的函数;如果对象类型是基类，就调用基类的函数。

<u>纯虚函数</u>是指被标明为不具体实现的虚函数。纯虚函数可以让类先具有一个操作名称,而没有操作内容,让派生类在继承时再去具体地给出定义。凡是含有纯虚函数的类叫做<u>抽象类</u>。这种可不能实例化对象，只能作为基类为派生类服务。

注意:派生类中必须实现基类的纯虚函数,否则，派生类也变成了抽象类，不能实例化对象。

纯虚函数多用在一些方法行为的实际上。在设计基类时,不太好确定或将来的行为多种多样，而此行为又是必需的，我们就可以在基类的设计中，以纯虚函数来声明次中行为，而不具体实现它。

**关于“相同名称之成员函数”**

1.如果你以一个“基类之指针”指向“派生类之对象”那么经由该指针你只能够调用基类所定义的函数。

2.如果基类和派生类都定义了“相同名称之成员函数”，那么通过对象指针调用成员函数时，到底调用哪一个函数,必须视该指针的原始类型而定,而不是指针实际所指的对象的类型而定,这一点与第1点其实意义相同。

**C++中虚函数与纯虚函数的区别**

定义一个函数为虚函数，不代表函数为不被实现的函数。 定义他为虚函数是为了允许用基类的指针来调用子类的这个函数。 定义一个函数为纯虚函数，才代表函数没有被实现。 定义纯虚函数是为了实现一个接口，起到一个规范的作用，规范继承这个类的程序员必须实现这个函数。

## 引用

引用的使用规则及其与指针的比较

(1)引用被创建的同时必须被初始化;指针则可以在任何时候被初始化。

(2)不能有NULL引用,引用必须与合法的存储单元关联;指针则可以是NULL。

(3)一旦引用被初始化，就不能改变引用的关系;指针则可以随时改变所指的对象。

![image-20220628174109763](windows_imgs\3JkRwORGN7A.png)

## const

任何不会修改数据成员的函数都应该声明为<u>const</u>类型。如果在编写const成员函数时,不慎修改了数据成员,或者调用了其它非const成员函数，编译器将指出错误，这无疑会提高程序的健壮性。

## 静态与非静态

<u>静态成员函数</u>和<u>静态成员变量</u>属于类本身，在类加载的时候(编译阶段)，即为它们分配了空间，因此可以通过<u>类名::函数名</u>或<u>类名::变量名</u>来访问。

而<u>非静态函数</u>和非静态成员属于对象的方法和数据，也就是应该首先产生类的对象,然后通过类的对象去引用。

静态函数不属于某个具体的对象，也就是说，在还没有产生类的任何一个具体对象时，静态函数就已经存在于程序的代码区了。但这是类的非静态成员还没有分配内存空间，这样，在静态成员函数中是没有办法对类非静态成员进行操作的。因此，在静态成员函数中只能访问静态成员变量，不能访问非静态成员函数和非静态成员变量。非静态成员函数中可以调用静态成员函数。

## 四种不同对象的生与死

在C++中,产生一个对象有四种方法：

```c++
void MyFunc(){
	CObject ob; //1.一般局部对象，在栈(Stack)之中产生
}
void MyFunc(){
	CObject* pOb = new CObject; //2.new局部对象，在堆(Heap)中产生
}
//3.全局对象（必然也是个静态对象)
CObject ob ;//在任何函数范围之外做此操作
void MyFunc(){
	static CObject ob;//4.局部静态对象，在函数范围内的一个静态对象
}
```

对于一般局部对象(栈Stack中产生):当对象产生时，构造函数被执行;当函数结束时(以至于对象将毁灭)，析构函数被执行。

对于new操作局部对象(堆Heap中产生):当对象产生时(执行new操作)，构造函数被执行;当delete对象语句被执行时，析构函数被执行。

对于全局对象:程序一开始，其构造函数就先被执行（比入口函数main、WinMain更早);程序结束前，析构函数被执行。

对于局部静态(static）对象:只会有一个实例产生，而且在固定的内存上(既不是stack也不是heap)，执行到第一次声明处（也就是在MyFunc第一次调用)时，构造函数被调用;当程序结束时(对象因此遭致毁灭)，析构函数被执行，但比全局对象的析构函数先一步执行。

## 函数的重载

两个函数的函数名一样,参数的类型和个数不同，这在C语言中不允许,而在C++中是合法的,这就是C++中函数的重载。
(overload)。C++编译器将根据参数的类型和参数的个数来确定执行哪一个函数。
重载的条件:函数的参数类型、参数个数不同，才能构成函数的重载。分析:
(1) void output( 与int output(
(2) void output(int a, int b=5)与void output(int a)

注意:
<u>只有函数的返回类型不同是不能构成函数的重载的。</u>
<u>要注意函数带有默认参数的这种情况,也不能构成函数重载。</u>

# MFC框架程序剖析

## test.h、 test.cpp

应用程序类:CTestApp（由CWinApp继承而来），每一个MFC程序有且仅有一个主应用程序类对象 theApp，它代表一个程序本体,用于管理和维护主应用程序

## MainFrm.h、 MainFrm.cpp

主框架类CMainFrame（由CWnd继承而来)，主框架是应用程序的主体窗口，其他的窗口（如视类窗口、工具条、状态条）都依附于主框架窗口(覆盖在它上面）。

## testView.h、 testView.cpp

视图类:CTestView（由CWnd继承而来），负责管理和维护图形显示操作。

## testDoc.h、 testDoc.cpp

文档类:CTestDoc（由CDocumet继承而来），负责显示数据的后台管理和维护。

## MFC中的全局对象theApp

初始化CTestAPP对象，应用程序内存获得配置

调用基类CWinApp构造函数（在MFC源码目录的文件中AppCore.cpp），初始化完成程序运行时的一些初始化工作。

注意:由于theApp是个全局对象，所以CWinApp构造函数会在入口函数WinMain之前运行。

## 消息映射

消息是Windows程序的血液，Windows程序靠消息的流动而维护生命。

在Windows API程序当中，消息的处理方法是在窗口函数中借助一个大大的switch/case比较操作,判别消息，再执行对应的处理代码。

在MFC中,为了让大大的switch/case比较操作简化,也让程序代码模块化,MFC采用了一种“Message Mapping”(消息映射表)的做法，把消息和其处理程序关联起来。

Message Mapping的基本原理
首先定义一个MSCMAP ENTRY结构

```c++
struct MSGMAP_ENTRY {
	UNIT nMessage;
	LONG (*pfn) (HWND, UNIT,WPARAM, LPARAM);
};
```

注意：pfn是一个函数指针,而该指针所指的函数处理nMessage消息。这正是面向对象观念中把“数据”和“处理数据的方法”封装起来的一种具体实现。

接下来,组织一个MSGMAP_RNTRY结构的数组_messageEntries[]把程序终欲处理的若干消息以及消息处理函数的关联性建立起来:

```c++
struct MSGMAP ENTRY_messageEntries[] =
{
    //消息,消息处理函数
	WM_CREATE, OnCreate,
	WM_PAINT, OnPaint,
	WM_COMMAND, OnCommand
	WM_CLOSE, OnClose
};
```

于是窗口函数可以这么写:

```c++
LRESULT CALLBACK MyWndProc( HWND hwnd, UINT uMsg,
WPARAM wParam, LPARAM IParam)
{
	for (int i=0; i< sizeof(__messageEntries); i++){
        if (message == messageEntries[i].nMessage)
			return ((*_messageEntmies[i]-pfm)(hwnd, nMsg, wParam,lParam));
    }               
}
```

这么一来,窗口过程函数WndProc永远不必改变,每当有新的要处理的消息,只要在_messageEntries[]数组中加上新的数组元素，并针对新消息写新的处理函数就OK了。

**MFC框架程序中是如何实现消息映射操作的呢?**

在MFC框架程序中,消息映射通过消息映射宏来实现消息映射的操作。

举例:在MFC框架程序中为视类增加一个鼠标左键按卞消息。在源文件中会增加兰处代码:

(1)消息响应函数原型(作为类成员函数，在类h头文件中声明)

(2)消息映射宏(CPP源文件)

(3)消息响应函数定义(在类CPP源文件实现该消息响应函数)

**消息映射宏**

![image-20240412105105746](windows_imgs\UUOP3j5RYLQ.png)

其中BEGIN_MESSAGE_MAP和END_MESSAGE_MAP这两个宏之间定义了CTestView类的消息映射表，即前面所讲的_messageEntries[]数组;而ON_WM_LBUTTONDOWNO这个宏的作用是在_messageEntries[]数组中添加一个消息映射元素，把WM_LBUTTONDOWN消息与
OnButtonDown函数关联起来。

通过这种机制，一旦有消息产生,程序就会调用相应的消息响应函数来进行处理。

## MFC类层次结构

![image-20220628181500283](windows_imgs\do52SN42YUC.png)

# 设备描述表DC

在Windows平台下，窗口的所有图形操作都是利用DC来完成的。

<u>如果使用GetDC来得到DC的句柄，在完成图形操作后，必须调用ReleaseDC来释放DC所占用的资源,以避免内存泄漏</u>。

利用计算机作图，窗口相当于画布,因此，<u>在获取DC的句柄时，总是和一个指定的窗口相关联</u>。

# 绘图

## 1.利用API全局函数实现画线功能

```c++
void CDrawView::OnLButtonDown(UINT nFlags,CPoint point){
	//TODO: Add your message handler code here and/or call default
    m_ptOxigin = point;
    CView::OnLButtonDown(nFlags, point);
}
void CDrawView::OnLButtonUp(UINT nFlags,CPoint point){
	HDC hdc;
	hdc =::GetDC(m_hWnd);
	::MoxeToEx(hdc, m_ptOrigin.x, m_ptOrigin.y, NUL);
    ::LineTo(hdc, point.x, point.y);
	::ReleaseDC(m_hWnd,hdc);
	CView::OnLButtonUp(nFlags, point);
}
```

## 2.利用CDC类实现画线功能

```c++
void CDraw.View::OnLButtonUp(UINT nFlags, CPoint point){
	CDC* pDC = GetDC();
	pDC->MoveTo(m_ptOrigin);
    pDC->LineTo(point);
	ReleaseDC(pDC);
	CView::OnLButtonUp(mFlags, point);
}
```

## 3.利用CClientDC、CWindowDC类绘图

CClientDC派生于CDC类,并且在构造时调用GetDC函数，在析构时调用ReleaseDC函数。它与CDC一样,都是实现在窗口的客户区绘图。

```c++
void CDrawView::OnLButtonUp(UINT nFlags,CPoint point){
	CClientDC dc(this);
	dc.MoveTo(m_ptOrigin);
    dc.LineTo(point);
	CView::OnLButtonUp(nFlags, point);
}
```

CWindowDC派生于CDC类,并且在构造时调用GetWindowDC函数,在析构时调用ReleaseDC函数。该对象可以访问整个窗口区域，包括客户区与非客户区。

```c++
void CDrawView::OnLButtonUp(UINT nFlags, CPoint point){
	CWindowDC dc(this);
    dc.MoveTo(m_ptOrigin);
    dc.LineTo(point);
	CView::OnLButtonUp(nFlags, point);
}
```

**CClientDC和CWindowDC的区别**

<u>CClientDC</u>派生于CDC类，并且在构造时调用GetDC函数，在析构时调用ReleaseDC函数。它与CDC一样，都是实现在窗口的客户区绘图。
<u>CWindowDC</u>派生于CDC类，并且在构造时调用GetWindowDC函数，在析构时调用ReleaseDC函数。该对象可以访问整个窗口区域,包括客户区与非客户区。

**客户区与非客户区**

![image-20220628135859155](windows_imgs\YKPz3Jbmz9I.png)

这种类型的窗口叫做应用程序窗口（application window）或者主窗口（ main window）。典型的主窗口框架通常包括标题栏、最小化按钮和最大化按钮以及一些其它的 UI 组件。这个框架本身叫做窗口的非客户区（non-client area）。

Windows 操作系统负责管理非客户区的响应操作，例如拖拽，改变大小，最大化最小化等等。框架之外剩余的区域，叫做客户区（client area），这部分是由程序自身负责管理的。

MFC框架程序界面中，整个程序窗口就是框架窗口,工具栏以下白色区域才是视类窗口。

<u>视类窗口</u>只有客户区(即视类窗口本身)

<u>框架窗口</u>既有客户区(菜单栏以下部分)，还有非客户区(标题栏和菜单栏)。

绘图操作一般都是在窗口的客户区进行的（(使用CDC或CClientDC);要在非客户区绘图,则要使用CWindowDC.

## 4.绘制彩色线条—使用CPen类

```C++
CPen pen(PS_SOLID,5,RGB(255,0,0));//声明一个Cpen对象
CClientDC dc(this);//声明一个CClientDC对象
CPen* pOldPen = dc.SelectObject(&pen);
dc.MoveTo(m_ptOrigin);
dc.LineTo(point);
dc.SelectObject(pOldPen);
```

注意:当构造一个GDI对象后，该对象并不会立即生效，必须通过SelectObject函数选入设备描述表,它才会在以后的绘制操作中生效。在完成绘图操作之后，都要利用SelectObject把先前的GDI对象选入设备描述表，以便使其恢复到先前的状态。

## 5.使用画刷CBrush类绘图

```c++
//绘制矩形填充块
CBrush brush(RGB(255,0,0));
CClientDC dc(this);
dc.FillRect(CRect(m ptOrigin,point), &brush);
//绘制位图填充块
CBitmap bmp;
bmp.LoadBitmap(IDB_BITMAP1);
CBrush brush(&bmp);
CClientDC dc(this);
dc.FillRect(CRect(m_ptOrigin,point), &brush);
```

## 6.绘制矩形框

```c++
CPen pen(PS_SOLID,5,RGB(255,0,0));CClientDC dc(this);
CPen* pOldPen = dc.SelectObject(&pen);
dc.Rectangle(CRect(m_ptOrigin,point));
dc.SelectObject(pOldPen);
//若要绘制空心的矩形框,需要在设备描述表中将默认画刷(填充白色)换成透明画刷
CBrush* pOldBrush
=(CBrush*)dc.SelectStockObject(HOLLOW_BRUSH);dc.SelectObject(pOldBrush);
```

## 7.绘制连续线条

```c++
m_ptOrigin = point; //OnLButtionDown
//OnMouseMove
CClientDC dc(this);
if (nFlags ==MK_LBUTTON ){
	dc.MoveTo(m_ptOrigin);
    dc.LineTo(point);
	m_ptOrigin = point;
}
```

## 8.橡皮筋技术

```C++
//OnLButtionDown
m_ptOrigin = m_ptEnd = point;
//OnMouseMove
CClientDC dc(this);
if (nFlags== MK_LBUTTON){
	//通过取反的模式擦除旧线条
    dc.SetROP2(R2_NOT);
	dc.MoveTo(m ptOrigin);
    dc.LineTo(m_ptEnd);
    //绘制新线条
	m_ptEnd = point;
	dc.MoveTo(m_ptOrigin); 
    dc.LineTo(m_ptEnd);
}
```

# 文本编程

## 1.在窗口输入文字——视类OnDraw函数

MFC中专门为视类提供了响应WM_PAINT消息的响应函数OnDraw(CDC* pDC)
如果要防止窗口重绘时显示的文字或图形被刷新,文字输出和图形绘制的操作都应该在OnDraw函数里完成。

```c++
void CTextView::OnDraw(CDC* pDC){
	CTextDoc* pDoc-GetDocument();
    ASSERTVALID(pDoc);
	pDC->TextOut(100,100,"第四讲文本编程");
}
```

## 2.在窗口输入文字——CString类

MFC中提供了一个字符串类:CString,这个类没有基类。一个CString对象由一串可变长度的字符组成。
利用CString操作字符串时，无论存储多少个字符,我们都不需要对它进行内存分配,因为这些操作在CString类的内部都已经替我们完成了。

```c++
void CTextView::OnDraw(cDC* pDC){
	CTextDoc* pDoc = GetDocumentO;
    ASSERT VALID(pDoc);
	//TODO: add draw code for native data here
    CString str("第四讲文本编程");
	pDC->TextOut(100,100, str);
}
```

## 3.添加字符串资源

CString提供了一个成员函数:LoadString

该函数可以装载一个由nID标识的字符串资源。其好处是,在需要使用的时候将其装载到字符串变量中，这样就不需要在程序中对字符串变量直接赋值。

在VC开发界面左边的Resource View中，通过StringTable可添加字符串资源

```c++
void CTextView::OnDraw(CDC* pDC){
	CString str;
	str.LoadString(1DS_MYSTRING);
	pDC->TextOut(100,100,str);
}
```

## 4.创建文本插入符

```c++
int CDrawView::OnCreate(LPCREATESTRUCT lpCreateStruct){
	if (CView::OnCreate(lpCreateStruct)==-1)
		return -1;
		//TODO: Add your specialized creation code here
    CreateSolidCaret(20,200);
	ShowCaret();
	return 0;
}
```

通常，插入符的大小应当根据当前所选的字号来变化。

调用CDC类的GetTextMetrics成员函数可以得到设备描述表中当前字体的度量信息。

BOOL GetTextMetrics(LPTEXTMETRIC lpMetrics) const//详见MSDN

![image-20220628185946602](windows_imgs\Uor16fm8zDR.png)

## 5.根据当前所选字号设置插入符大小

```c++
int CTextView::OnCreate(LPCREATESTRUCT lpCreateStruct){
	if (CView::OnCreate(lpCreateStruct)==-1)
		return -1;
	//TODO: Add your specialized creation code here
    CClientDC dc(this);
	TEXTMETRIC tm;
	dc.GetTextMetrics(&tm);
	CreateSolidCaret(tm.tmAveCharWidth/8, tm.tmHeight);
    ShowCaret();
	return 0;
}
```

## 6.创建图形插入符

```c++
int CTextView::OnCreate(LPCREATESTRUCT lpCreateStruct){
	if (CView::onCreate(lpCreateStruct)==-1)
		return-1;
    //TODO: Add your specialized creation code here
    CBitmap bmp;
	bmp.LoadBitmap(IDB_ BITMAP1);
    CreateCaret(&bmp);
	ShowCaret();
	return 0;
}
```

注意:以上代码的结果并非如我们所愿。因为这bmp对象是一个局部变量,当onCreate函数执行完成后，bmp对象就被销毁。有两种方法可以解决这一问题:
①将这个CBitmap对象修改为视类的成员变量。
②如果CBitmap对象是一个临时对象,则在加载完成之后必须加上bmp.Detach()。Detach会把位图句柄与这个位图对象分离，这样,当这个局部对象的生命周期结束时，它不会去销毁一个它不再具有拥有权的位图资源。

## 7.插入符位置随鼠标单击而移动

```c++
void CTextView::OnLButtonDown(UINT nFlags, CPoint point){
	//TODO: Add your message handler code here and/or call default
    SetCaretPos(point);
	CView::OnLButtonDown(nFlags, point);
}
```

## 8.字符输入

首先让CTextView类捕获WM_CHAR消息,接着为该类定义一个CString类型的成员变量:m_strLine,用来存储输入的字符串。

输入的字符从插入符位置开始输出,因此当鼠标左键单击时,需要把m_strLine清空，同时保存左键单击点的坐标，确定字符串显示的位置。

```c++
void CTextView::OnLButtonDown(UINT nFlags,CPoint point){
	SetCaretPos(point);
    m_strLine.Empty();
    m_ptOrigin = point;
	CView::OnLButtonDown(nFlags, point);
}
```

```c++
void CTextView::OnChar(UINT nChar, UINT nRepCnt, UINT nFlags){
	//TODO: Add your message handler code here and/or call default
    CClientDC dc(this);
	mstrLine += nChar;
	dc.TextOut(m_ptOrigin.x, m_ptOrigin.y, m_strLine);
    CView::OnChar(nChar,nRepCnt,nFlags);
}

```

## 9.字符输入——回车键的处理

按下回车键后，插入符应换到下一行，随后的输入也应从这一新行开始·输出。因此需要清空上一行保存的字符，并计算插入下一行的新位置。

```c++
void CTextView::OnChar(UINT nChar,UINT nRepCnt, UINT nFlags){
	if (13==nChar){//回车键的ASCI码为13i
		TEXTMETRIC tm;
		dc.GetTextMetrics(&tm);
        m_strLine.Empty();
		m_ptOrigin.y += tm.tmHeight;
    }
	CView::OnChar(nChar, nRepCnt, nFlags);
}
```

## 10.字符输入——退格键的处理

按下退格键后,应该删除屏幕上位于插入符前面的字符，同时,插入符的位置应回退一个字符。

先把文本的颜色设置为背景色,在窗口中把该文本输出一次(相当于从屏幕中抹去文本);再把文本的颜色设置为原来的颜色,把删除最后一个字符的字符串在窗口中输出一次。

CDC类中,获取背景色成员函数为GetBkColor;设置文本颜色的函数为SetTextColor。

从字符串中删除最右边的字符,可以利用CString类的Left函数。

```c++
else if (8== nChar)//退格键的ASCII码为8
{
	COLORREF clr= dc.SetTextColor(dc.GetBkColor());
    dc.TextOut(m_ptOrigin.x, m_ptOrigin.y, m_strLine);
	m_strLine = m_strLine.Left(m_strLine.GetLength() - 1);
    dc.SetTextColor(clr);
}
else
	m_strLine+= nChar;
dc.TextOut(m_ptOrigin.x, mptOrigin.y,m_strLine);
```

## 11.字符输入——调整插入符的位置

插入符应该随着字符的输入而移动。插入符横向移动的距离就是输入字符的宽度，其纵坐标不变。
GetTextExtent函数可以得到字符串在屏幕上显示的宽度。

```c+
CSize sz = dc.GetTextExtent(m_strLine);
CPoint pt;
pt.x = mptOrigin.x +Sz.cx;
pt.y = m_ptOrigin.y;
SetCaretPos(pt);
```

## 12.设置字体——CFont

CFont的初始化函数有“CreateFont”、"CreateFontIndirect”、"CreatePointFont”、"CreatePointFontIndirect"。

```c++
CClientDC dc(this);
CFont font;
font.CreatePointFont(200,"华文琥珀");
CFont* pOldFont = dc.SelectObject(&font);
dc.SelectObject(pOldFont);
```

# 消息

## Windows消息的分类

- 标准消息
  除WM_COMMAND之外，所有以WM_开头的消息。从cWnd派生的类，都可以接收到这类消息。
- 命令消息
  来自<u>菜单、加速键或工具栏按钮</u>的消息。这类消息都以<u>WM_COMMAND</u>呈现。在MFC中，通过菜单项的<u>标识（ID)</u>来区分不同的命令消息;在SDK中,通过消息的<u>wParam参数</u>识别。
  从CCmdTarget派生的类，都可以接收到这类消息。
- 通告消息
  <u>由控件产生的消息</u>，例如，按钮的单击，列表框的选择等均产生此类消息为的是向其父窗口(通常是对话框）通知事件的发生。这类消息也是以<u>WM_COMMAND</u>形式呈现。
  从CCmdTarget派生的类，都可以接收到这类消息。

## MSG结构体

操作系统将每个事件都包装成一个称为消息的结构体MSG来传递给应用程序。

MSG结构定义如下： 

```c++
typedef struct tagMSG {       
    	HWND   hwnd;      
    	UINT   message;
    	WPARAM wParam;
    	LPARAM lParam;
    	DWORD  time;
    	POINT  pt;
} MSG; 
```

## WM_PAINT

Windows把一个最小的需要重绘的正方形区域叫做“无效区域”。当Windows发现了一个“无效区域“后，它就会向该应用程序发送一个WM_PAINT消息，通知应用程序重新绘制窗口。

当窗口<u>从无到有</u>、<u>改变尺寸</u>、<u>最小化后再恢复</u>、被其他窗口遮盖后再显示时,窗口的客户区都将变为无效。

## WM_DESTROY

当窗口被销毁时会产生这个消息(通常也是准备退出应用程序的时候),对于这个消息的响应是每个程序所必备的。怎样响应呢?

响应方式就是调用<u>PostQuitMessage</u>函数，该函数会在消息队列中添加一个WM _QUIT消息,准备让由消息循环中的GetMessage取得。当消息循环中的收到wM QUIT消息时，GetMessage会传回0，从而结束消息循环,进而结束整个程序。

PostQuitMessage会发送WM_QUIT给消息队列。注意，<u>WM_QUIT永远不会到达窗口过程,</u>因为GetMessage得到WM_QUIT后就会返回0，从而结束消息循环,程序退出。

强烈建议PostQuitMessage放在WM_DESTROY消息响应里面调用，让程序正常有序的结束，因为通常销毁窗口是程序运行的最后一步。

当然, PostQuitMessage可以放在窗口过程的任何一个地方，让程序随时结束,但是这种做法就像采用拔电源的野蛮方式来关机,不可取~!

## WM_CLOSE

当我们按下窗口右上角的叉号或者按下左上角系统菜单中的“关闭”命令时,系统会送出WM_CLOSE消息。通常程序的窗口过程函数不拦截此消息，而是交由DefWindowProc函数来处理。 DefWindowProc函数在收到WM_CLOSE消息后，会自动调用DestroyWindow把窗口销毁。(调用DestroyWindow会产生WM_DESTROY消息)

当然，你可以不让DefWindowProc处理,而是自己处理WM_CLOSE消息。例如询问用户是否真的退出程序:如果用户选择“取消”,你忽略此消息,那么程序照常运行;如果用户确认要退出,必须手工调用DestroyWindow.

## 自行发送消息的两种方式

发送消息可以使用SendMessage和PostMessage函数。

<u>SendMessage</u>将消息直接发送给窗口，并调用该窗口过程进行处理。在窗口过程对消息处理完毕后，该函数才返回。

<u>PostMessage</u>函数将消息放入与创建窗口的线程相关联的消息队列后立即返回。

# 菜单

MFC中，设置为Pop-up类型的菜单称为弹出式菜单,VC++默认顶层菜单为弹出式菜单,这种菜单不能响应命令。

将菜单的属性对话框中的Pop-up选项去掉，该菜单成为一个菜单项，对应有一个ID号,可以响应命令。

## 菜单命令消息路由的过程(简答题)

①当点击某菜单项时，最先接收到这个菜单命令消息的是<u>框架类</u>。

②框架类把接收到的这个消息传给它的子窗口，即<u>视类</u>。视类根据命令消息映射机制查找自身是否对这个消息进行了响应，如果响应了，则调用自身相应响应函数。
③如果视类没有对此命令消息作出响应，就交由<u>文档类</u>，文档类同
样查找自身是否这个消息进行了响应，如果响应了，则调用自身相应响应函数。
④如果文档类也未做出响应，就把这个命令消息交还给视类，后者
再交还给框架类。
⑤框架类查看自己是否对这个命令消息进行了响应，如果它也没有
相应，就把这个菜单命令消息交给<u>应用程序类</u>,由后者来处理。

## 菜单的结构

![image-20220628194143760](windows_imgs\Sh7QA2dtbDO.png)

## 标记菜单

UNIT CheckMenultem(UINT nIDCheckltem, UINT nCheck)

实例一:
GetMenu0->GetSubMenu(0)->CheckMenuItem(0,MF_BYPOSITION |MF_CHECKED);

实例二:

GetMenu(->GetSubMenu(0)->
CheckMenuItem(ID FILE_NEW,MF_CHECKED);

## 图形标记菜单（在菜单项签名加上位图）

UNIT SetMenuItemBitmaps(UINT nPosition, UINTnFlag, const CBitmap* pBmpUnchecked, constCBitmap* pBmpChecked)

实例:

bmp1.LoadBitmap(IDB_ BITMAP1);

bmp2.LoadBitmap(IDB_BITMAP2);

GetMenu(->GetSubMenu(0)->SetMenuItemBitmaps(0,
MF BYPOSITION, &bmp1, &bmp2);

注意:

位图大小必须为13 x 13。 bmp1、bmp2为主框类的成员对象;

若为局部变量,菜单标记后要加上bmp.Detach()

## 移除和加载菜单

BOOL SetMenu(CMenu* pMenu)

移除菜单:

SetMenu(NULL); 

加载菜单:

CMenu menu;

menu.LoadMenu(IDR_MAINFRAME);

SetMenu(&menu);

注意:如果CMenu对象是一个临时对象，则在加载完成之后必须加
上menu.Detach(。Detach会把菜单句柄与这个菜单对象分离,这样,当这个局部对象的生命周期结束时，它不会去销毁一个它不再具有拥有权的菜单资源。

## MFC菜单命令更新机制

菜单项状态的维护是依赖于CN_UPDATE_COMMAND_UI消息，谁捕获CN_UPDATE_COMMAND_UI消息，MFC就在其中创建一个CCmdUI对象。我们可以通过ClassWizard在消息映射中添加ON_UPDATE_COMMAND_UI宏来捕获CN UPDATE_COMMAND_UI消息。

在后台所做的工作是:当显示菜单的时候,操作系统发出WM_INITMENUPOPUP消息,然后由MFC的基类如CFrameWnd接管。它创建一个CCmdUI对象,并与第一个菜单项相关联,调用对象的一个成员函数DoUpdate()。这个函数发出CN_UPDATE_COMMAND_UI消息,这条消息带有指向CCmdUI对象的指针。同一个CCmdUI对象就设置为与第二个菜单项相关联，这样顺序进行，直到完成所有菜单项。

更新命令UI处理程序仅应用于弹出式菜单项上的项目(有ID号)，不能应用于顶层菜单项目(无ID号)。

```c++
void CMainFrame::OnUpdateEditCopy(CCmdUI* pCmdUD){
	//TODO: Add your command update UI handler code here
    pCmdUI->Enable(TRUE);
    pCmdUI->SetCheckO;
    pCmdUI->SetText("123");
}
```

## 制作快捷菜单

**Step1:为Menu程序增加一个新的菜单资源**

在ResouceView上的Menu分支上单击鼠标右件,选择"Insert Menu”命令，为这个菜单资源添加菜单项。

由于在显示快捷菜单时顶级菜单不出现,所以可以给它设置任意的文本。

**Step2:给视类添加WM_RBUTTONDOWN消息响应函数**

加载菜单资源到CMenu对象

```c++
void CMenuView::OnRButtonDown(UINT nFlags, CPointpoint){
	CMenu menu;
	menu.LoadMenu(IDR_MENU1);
	CView::OnRButtonDown(nFlags, point);
}
```

**Step3:调用TrackPopupMenu函数**

```c++
void CMenuiew:: OnRButtonDown(UINT nElags,CPoint point){
	CMenu menu;
	menu.LoadMenu(IDR_MENU1);
	CMenu* pPopup = menu.GetSubMenu(0);
	pPopuP->TrackPopupMenu(TPM_LEFTALIGN,point.x,point.y, this);
	CView::OnRButtonDown(nFlags,point);
}
```

**将鼠标点的客户去坐标转换为屏幕坐标**

```c++
void CMenu View::onRButtonDown(UINT nFlags,CPoint point)
{
	CMenu menu;
	menu.LoadMenu(IDR_MENU1);
    ClientToScreen(&point);
	CMenu* pPopup = menu.GetSubMenu(O);
	pPopup->TrackPopupMenu(TPM_LEFTALIGN,point.x,point.y, this);
	CView::OnRButtonDown(nFlags, point);
}
```

**Step4:添加响应函数**

```c++
利用ClassWizard添加。
void CMenu View::OnTest1(){
	//TODO: Add your command handler code here
    MessageBox("View Test1");
}
void CMenuView::OnTest2(){
	//TODO: Add your command handler code here
    MessageBox("View Test2");
}
```

**关于快捷菜单中的菜单项的命令响应的说明**

对于快捷菜单,如果将其拥有者窗口设置为框架类窗口,则框架类窗口才能有机会获得对该快捷菜单中的菜单项的命令响应,否则，就只能有视类窗口作出响应。

## 动态菜单操作

**添加菜单项目（AppendMenu)**

添加顶层菜单:

```c++
CMenu my_menu;
my_menu.CreateMenu();
GetMenu()->AppendMenu(MF_POPUP, (UINT)my_menu.m_hMenu, "my_menu");
my_menu.Detach();
```

添加顶层菜单下的菜单项:

GetMenu()->GetSubMenu(0)->AppendMenu(MF_STRING, 777, "Hello");

**插入菜单项目（InsertMenu)**
插入顶级菜单:

```c++
CMenu my menu;
my_menu.CreateMenu();
GetMenu()->InsertMenu(2, MF_BYPOSITION | MF_POPUP,
(UINT)my_menu.m_hMenu,"my_menu");
my_menu.Detach();
```

插入顶级菜单下的菜单项

```c++
GetMenu)->GetSubMenu(O)->InsertMenu (0, MF_STRINGI
MF_BYPOSITION, 777,"Hello");
GetMenu()->GetSubMenu(O)->InsertMenu (ID_FILE_OPEN,
MF_STRING, 777, "Hello");
```

**删除菜单项目（DeleteMenu)**

删除顶级菜单:

GetMenu(->DeleteMenu(1, MF_ BYPOSITION);

删除顶级菜单下的菜单项:

GetMenu(->GetSubMenu(O)->DeleteMenu (o,
MF_ BYPOSITION);
GetMenu()->GetSubMenu(0)->DeleteMenu
(D_FILE_NEW, MF_ BYCOMMAND);\

**动态添加的菜单项的命令响应**

遵循MFC的消息映射机制，需要手动添加三处代码来实现命令消息的响应。

可先利用ClassWizard对程序中某个已有的静态菜单项添加命令消息响应，然后参照ClassWizard在程序中为其添加的内容,来完成动态菜单添加命令响应。

# 工具栏编程

工具栏是把常用的菜单命令集合起来,以按钮的形式提供给用户使用,目的是方便用户的操作。

工具按钮的添加、删除都在资源编辑器窗口中的工具栏编辑窗口中完成。

添加按钮响应命令的方法与菜单相同。通常工具栏与其对应的菜单项ID相同，这样,在程序运行时。可以通过单击工具栏上的按钮来调用相应菜单项的命令。

**创建工具栏——4个步骤**

Step1:创建工具栏资源;

Step2:构造CToolBar对象;

Step3:调用Create或CreateEx函数创建Window工具栏(工具栏也是窗口)

Step4:调用LoadToolBar函数加载工具栏资源。

![image-20220629014238167](windows_imgs\F1CXP11l6j4.png)

![image-20220629014249501](windows_imgs\fZg2WrF7pGT.png)

![image-20220629014301253](windows_imgs\KO2GXFmoPkz.png)

# 状态栏编程

状态栏的提示行与指示器

状态栏分为两部分:提示行与指示器。

左边最长的部分为提示行，通常用于显示菜单项或工具按钮的提示信息。右边由若干窗格组成的部分为状态栏指示器,通常用来显示大小写键、数字锁定键等信息。

框架程序专门提供了一个indicators数组来管理提示行与指示器。如果要修改状态栏的外观,则只需在
indicators数组中添加或减少相应的字符串资源ID即可。

![image-20220629014418872](windows_imgs\LeNZ5VUDGxt.png)

![image-20220629014430176](windows_imgs\sRd6zBrxEdM.png)

![image-20220629014451311](windows_imgs\AdbZ1aotagD.png)

![image-20220629014507572](windows_imgs\8DWECVt1sZ8.png)

![image-20220629014517454](windows_imgs\7ZMX2DekOXg.png)

![image-20220629014531530](windows_imgs\6oI16Z4v6ua.png)

# 对话框

对话框是一个窗口,与对话框资源相关的类为CDialog,由CWnd类派生而来。

可以将对话框看成是一个大容器，在它上面能够放置各种标准和扩展控件，是用户与程序进行交互的重要手段。

在MFC中，所有的控件都是由CWnd派生而来,因此，<u>控件实际上也是窗口</u>。

## 对话框的种类

- **模式对话框:**
  当其显示时,程序会暂停执行，直到关闭这个对话框后,才能继续执行程序中其他任务。例如“文件/打开”对话框。
- **无模式对话框:**
  当其显示时，允许转而执行程序中其他任务，而不用关闭这个对话框。该类型对话框不会垄断用户的操作，用户仍可以与其他界面对象进行交互。例如“查找”对话框。

## 创建模式对话框

### DoModal()函数

创建模式对话框需要调用CDialog类的成员函数:DoModal，该函数的功能就是创建并显示一个模式对话框。

```C++
void CMainFrame::OnTest(){
    //TODO: Add your command handler code here
    CMyDialog dlg;
    dlg.DoModal();
}
```

## 创建无模式对话框

### Create()函数

创建非模式对话框需要调用CDialog类的成员函数:

BOOL Create(UINT nIDTemplate,CWnd*pParentWnd = NULL);

```C++
void CMainFrame::OnTest(){
    //TODO: Add your command handler code here
    CMyDialog dlg;
	dlg.Create(IDD_DIALOG1, this);
}

```

注意:运行程序，对话框并未显示~!

### ShowWindow()函数

当利用Create函数创建非模式对话框时,还需要调用Show Window函数将这个对话框显示出来。

```C++
void CMainFrame::OnTest(){
    CMyDialog dlg;
    dlg.Create(IDD_DIALOG1,this);
    dlg.ShowWindow(SW_SHOW);
}
```


注意:运行程序，对话框仍未显示~!

**对话框未显示之原因分析**

这里创建的非模式对话框对象（dlg）是一个局部对象，当OnTest函数结束时，dlg这个对象的生命周期也就结束了，它会销毁与之相关联的对话框资源,因此对话框不会显示。

为什么模式对话框不会出现这样的问题?

在创建模式对话框时，当执行到DoModal函数显示这个对话框时，程序会暂停执行，直到关闭模式对话框之后，程序才继续执行。也就是说，当模态对话框显示时，dlg这个对象的生命周期并未结束。

结论:在创建非模式对话框时，不能把对话框对象定义为局部对象。

**解决方法1———使用成员变量**

把对话框对象定义为视类的成员变量。

注意:在销毁对话框之前，Create函数只能调用一次，否则会出错。

```C++
void CMainFrame::OnTest()
{
	static BOOL bFlag = TRUE;
    if (TRUE == bFlag){
        dlg.Create(IDD_DIALOG1, this);
        bFlag = FALSE;
    }
    dlg.ShowWindow(SW_SHOW);
}
```

**销毁无模式对话框**

若要在程序中主动销毁无模式对话框（例如在没有“确定”和“取消”按钮的情况下销毁对话框),需调用函数DestroyWindow。

```c++
void CTestView::OnTest(){
    static BOOL bFlag = FALSE;
    if (FALSE == bFlag){
		dlg.Create(IDD_DIALOG1,this);
        dlg.ShowWindow(SW_SHOW);
        bFlag =TRUE;
	}else{
		dlg.DestroyWindow();
        bFlag = FALSE;
    }
}
```

**解决方法2——使用堆内存**

把对话框对象定义为指针,在堆上分配内存。

```c++
void CMainFrame ::OnTest(){
    CMyDialog* pDlg = new CMyDialog;
    pDlg->Create(IDD_DIALOG1, this);
    pDlg->ShowWindow(SW_SHOW);
}
```

注意:该程序存在问题。由于没有办法释放这个指针变量所指向的那块内存，会出现内存泄漏~!

消除内存泄漏的办法:1.指针变量定义成全局变量;或者⒉重载对话框的PostNcDestroy函数，添加代码delete this.

**利用GetDlgltem改变控件文本内容**

```c++
void CMyDialog::OnNumber1()
{
    CString str;
    GetDIgItem(IDC_NUMBER1)->GetWindowText(str);
    if (str =="Number1:")
        GetDlgItem(IDC_NUMBER1)->SetWindowText("数值1:");
    else
        GetDlgItem(IDC_NUMBER1)->SetWindowText("Number1:");
}
```

注意:静态文本框在默认状态下是不发送通告消息的。
改变这一默认状态,必须在属性窗口选中Notify这个选项。

## 访问控件的七种方法

### 1.MFC的DDX数据交换—控件和整型变量关联

最简单的访问控件的方式:通过类向导，在对话框函数
DoDataExchange内部实现对话框控件与对话框类的成员变量相关联。

重要函数:BOOL UpdateData(BOOL bSaveAndValidate= TRUE)

```c++
void CMyDialog::OnButton1(){
	UpdateData();//成员变量从对话框控件中获取数据
    m_num3 = m_num1 + m_num2;
	UpdateData(FALSE); //以成员变量的值初始化对话框控件
}
```

### 2.MFC的DDX数据交换——控件和控件变量关联

重要函数: Get/SetWindowText

```c++
void CMyDialog::OnButton2(){
	int num1, num2, num3;
    char c1[10], c2[10],c3[10];
	m_edit1.GetWindowText(c1, 10);
    m_edit2.GetWindowText(c2, 10);
    num1 = atoi(c1);
    num2 = atoi(c2);
    num3 = num1 + num2;
    itoa(num3,c3,10);
	m_edit3.SetWindowText(c3);
}
```

### 3.GetDIgltem + Get/SetWindowText

重要函数:cWnd * GetDlgltem( int nID) const;

该函数返回一个指向由参数nID指定的控件对象的指针。

```c++
void CMyDialog::OnButton3()
{
	int num1, num2, num3;
    char c1[10], c2[10], c3[10];
	GetDlgltem(IDC EDIT1)->GetWindowText(c1, 10);
    GetDlgltem(IDC EDIT2)->GetWindowText(c2, 10);
    num1 = atoi(c1);
    num2 = atoi(c2);
    num3 = num1 + num2;
    itoa(num3,c3,10);
	GetDlgItem(IDC_EDIT3)->SetWindowText(c3);
}
```

**利用GetDlgltem改变控件文本内容**

```c++
void CMyDialog::OnNumber1()
{
	CString str;
	GetDlgltem(IDC_ NUMBER1)->GetWindowText(str);
    if (str--"Number1:")
		GetDlgItem(IDC NUMBER1)->SetWindowText("数值1:");
    else
	GetDlgItem(IDC_NUMBER1)->SetWindowText("Number1:");
}
```

注意:静态文本框在默认状态下是不发送通告消息的。改变这一默认状态,必须在属性窗口选中Notify这个选项。

**利用GetDlgltem在控件中绘图**

```c++
void CMyDialog::OnNumber(){
	CWnd* pWnd = GetDlgItem(IDC_NUMBER2);
	CRect rc;
	pWnd->GetClientRect(&rc);
	CBrush brush(RGB(255,0,0));
	CDC* pDC- pWnd->GetDC();
	pDC->FillRect(&rc,&brush);
	pDC->SetBkMode(TRANSPARENT);
	pDC->TextOut(13,5,"刘晓翔");
	ReleaseDC(pDC);
}
```

### 4.Get/SetDlgltemText

该函数返回对话框中指定nID的控件上的文本。也就是说:GetDlgItemText函数把方法③中介绍的GetDlgItem和GetWindowText这两个函数的功能组合起来了。

```c++
void CMyDialog::OnButton4(){
    int num1, num2, num3;
    char c1[10], c2[10], c3[10];
    GetDlgItemText(IDC_EDIT1, c1, 10);
    GetDlgItemText(IDC_EDIT2, c2,10);
    num1 = atoi(c1);
	num2 = atoi(c2);
	num3 = num1 + num2;
    itoa(num3,c3,10);
	SetDlgItemText(IDC_EDIT3, c3);
}
```

### 5.Get/SetDlgltemlnt

该函数首先获得对话框中指定nID的控件上的文本，然后将其转换为一个整型数值返回

```c++
void CMyDialog::OnButton5(){
	int num1, num2, num3;
	num1 = GetDlgItemInt(IDC_EDIT1);
    num2 = GetDlgltemInt(IDC_ EDIT2);
    num3 - num1 +num2;
	SetDlgItemInt(IDC_EDIT3, num3);
}
```

### 6.发送消息——SendMessage

Windows程序是基于消息的系统，因此,只要获取设置窗口文本的消息，就可以通过SendMessage来发送这条消息，从而获取/设置窗口的文本。

```c++
void CMyDialog::OnButton6(){
	int num1, num2, num3;
    char c1[10], c2[10], c3[10];
	::SendMessage(GetDIgltem(IDC_EDIT1)->m_hWnd, WM_ GETTEXT,10, (LPARAM)c1);
    ::SendMessage(m_edit2.m_hWnd, WM_GETTEXT, 10, (LPARAMI)c2);
    num1 = atoi(c1);
	num2 = atoi(c2);
	num3 = num1 + num2;
    itoa(num3, c3, 10);
	m_edit3.SendMessage(WM_SETTEXT, 0, (LPARAM)c3);
}
```

### 7.发送消息——SendDlgltemMessage

直接给对话框的子控件发送消息:
LRESULT SendDIgItemMessage(int nID, UINT message,WPARA wParam -0, LPARAM lParam=0)
该函数功能相当于把上面GetDlgltem和SendMessage这两个函数的组合。

```c++
void CMyDialog:onButton7(){
	int num1, num2, num3;
	char c1[10], c2[10], c3[10];
	
    SendDIgltemMessage(IDC_EDIT1,WM_GETTEXT, 10, (LPARAMI)c1);
    SendDIgltemMessage(IDC_EDIT2, WM_GETTEXT, 10, (LPARAM)c2);
	
    num1 = atoi(c1);
	num2 = atoi(c2);
	num3 = num1 + num2;
    itoa(num3, c3, 10);

    sendDIgItemMessage(DC_EDIT3,WM_SETTEXT, 0, (LPARAMI)c3);
}
```

## 改变对话框/窗口外观

**设置窗口的位置与大小**

BOOL SetWindowPos(const CWnd* pWndInsertAfter,
int x, int y, int cx, int cy,UINT nFlags);

pWndInsertAfter:在以Z次序排序的窗口中位于当前窗口前面的那个窗口对象，通常可忽略该参数,置为NULL。

x,y:窗口左上角的x和y坐标(相对于屏幕左上角的原点)。

cx, cy:窗口的宽度和高度。

nFlags:设定窗口位置与大小的相关参数。

**设置窗口的形状**

int SetWindowRgn(HRGN hRgn, BOOL bRedraw)

hRgn: CRgn对象的资源句炳。

bRedraw:通常设为TRUE,表示设置窗口的形状后立即重绘窗口。

CRgn:与CFont、CPen、CBrush、CBitmap一样,属于Windows
GDI对象,用来描述自定义形状的区域。

例如，将窗口形状设置为椭圆形的代码:

```c++
CRect rc;
GetClientRect(rc);
CRgn rgn;
rgn.CreateEllipticRgn(0, 0, rc.Width(),rc.Height());
SetWindowRgn((HRGN) rgn.m_hObject, TRUE);
```

# 窗口

## 在窗口创建之前更改

如果希望在应用程序窗口创建之前修改它的大小、标题和风格应该在<u>CMainFrame</u>类的<u>PreCreateWindow</u>成员函数进行。

该函数有个类型是CREATESTRUCT结构的参数，如果在修改了这个参数中的成员变量的值，那么这种改变会反映到MFC底层代码中，当MFC底层代码调用CreateWindowEx函数去创建窗口时，它就会使用改变后的参数值去创建这个窗口。

### **更改窗口大小**

```c++
BOOL CMainFrame::PreCreateWindow(CREATESTRUCT& cs){
	if( !CFrameWnd::PreCreateWindow(cs) )
		return FALSE;
	cs.cx = 300;
	cs.cy = 200;
    return TRUE;
}
```

### **更改应用程序标题**

```c++
BOOL CMainFrame::PreCreateWindow(CREATESTRUCT& cs){
	if( !CFrameWnd::PreCreateWindow(cs) )
		return FALSE;
	cs.lpszName ="暨南大学";
    return TRUE;
}
```

注意:此时应用程序的标题并未改变，原因及解决方法见下页。

**在MFC框架程序中更改标题栏文字应注意**

框架的默认窗口样式是wS_OVERLAPPEDWINDOW和FWS_ADDTOTITLE样式的组合。其中FWS_ADDTOTITLE是MFC特定的一种样式,指示框架将文档标题添加到窗口标题上。因此,如果想让窗口显示自己的标题,只需将窗口的
FWS_ADDTOTITLE样式去掉即可。设置窗口标题的代码之前加上:

cs.style = cs.style&~FWS_ADDTOTITLE;
或者:
cs.style = WS_OVERLAPPEDWINDOW;

### 修改光标、图标、背景

之前对于窗口的大小、标题和风格是在创建窗口时设定的。而光标、图标和背景是在设计窗口类时指定的。

窗口类的设计与注册是由MFC底层代码自动完成的,我们不可能、也不应该去修改MFC底层代码。但是我们可以编写自己的窗口类注册,然后让随后的窗口按照我们编写的窗口类去创建。

```c++
BOOL CMaimExam::PreCeateWwimdow(CREATESTRUCT& cs)
{
    WNDCLASS MvWnd;
	MyWnd.cbClsExtra=NULL;
    MyWnd.cbWndExtra=NULL;
	MyWnd.hbrBackground = (HBRUSH)GetStockObiect(BLACK_BRUSH);
	MyWnd.hCursor= LoadCursor(NULL, IDC_CROSS);
    MyWnd.hIcon = LoadIcon(NULL,IDI_WARNING);
    MyWnd.hInstance- AfxGetInstanceHandle();
    MyWnd.lpfnwWndProc = ::DeindowProc;
    MyWnd.lpszClassName ="Hello";
	Mywnd.lpszMenuName=NULL;
	MyWnd.style =CS_HREDRAW| CS_VREDRAW;
    RegisterClass(&MyWnd);
	cs.IpszClass="hello";
    return TRUE;
}
```

**以上代码存在的问题、原因及解决方法**

上述代码的运行结果是:仅仅是程序的标题栏图标发生了改变，但窗口的背景和光标没有改变。

原因是:视类窗口覆盖在主窗口上面,我们看到的窗口实际上是视类窗口，而上述代码修改的是框架类窗口的背景和光标。应用程序的图标属于框架窗口,因此上述程序运行后,图标发生了改变。

结论:在MFC中，如果要修改应用程序窗口的图标,则应该框架类中进行，因为框架窗口才有标题栏;如果要修改程序窗口的背景和光标,则应该在视类中进行。

解决方法:在视类的PreCreateWindow函数中添加代码:
cs.lpszClass = "hello";

**一个简单的修改函数**

```c++
BOOL CMainFrame::PreCreateWindow(CREATESTRUCT& cs){
    if( !CErameWnd;:PreCreateWindow(cs))
		return FALSE;
	cs.lpszClass= AfxRegisterndClass(CS_HREDRAW |CS_VREDRAW,0,0,LoadIcon(NULL, IDI_ WARNING));
		return TRUE;
}
BOOL CUIView::PreCreateWindow(CREATESTRUCT& cs){
	cs.lpszClass = AfxRegisterWndClass(CS_HREDRAW  CS_VREDRAW,LoadCursor(NULL,IDC_CROSS),(HBRUSH)GetStockObject(BLACK_BRUSH),0);
    return CView::PreCreateWindow(cs);
}
```

## 在窗口创建之后更改

### 更改风格

在应用程序窗口创建之后修改它的<u>风格属性</u>,可在
<u>CMainFrame</u>类的<u>OnCreate</u>函数中调用S<u>etWindowLong</u>函数实现。

SetWindowLong(HWND hWnd, int nIndex, LONG dwNewLong)

该函数的作用是改变制定窗口的属性（包括设置新的窗口风格设置新的窗口过程、设置新的应用程序实例局柄等）。要改变窗口的风格，则将该函数的第二个参数指定为GWL_STYLE，然后由第三个参数指定新的窗口风格。

```c++
int CMainFrame::OnCreate(LPCREATESTRUCT lpCreateStruct)
{
	if (CFrameWnd::OnCreate(lpCreateStruct)==-1)
		return -1;
	SetWindowLong(m_hWnd, GWL_STYLE, WS_OVERLAPPEDWINDOW);
    return 0;
}
```

### 更改标题与大小

在应用程序窗口创建之后修改标题,可在CMainFrame类的OnCreate函数中调用SetWindowText函数实现。

在应用程序窗口创建之后修改大小,可在CMainFrame类的OnCreate函数中调用SetWindowPos函数实现。



如果是在已有类型的基础上进行修改的话，那么可以利用GetWindowLong这个函数获得这个窗口的现有类型，然后修改。

例如:

```c++
SetWindowLong(m hWnd, GWL STYLE,
GetWindowLong(m_hWnd,GWL_STYLE) &~WS_MAXIMIIZEBOX);
```

**更改光标、标题栏图标、窗口背景**

要在应用程序窗口创建之后修改它的<u>光标、图标和背景</u>，可在<u>OnCreate</u>函数中调用<u>SetClassLong</u>函数实现。

SetClassLong(HWND hWnd, int nIndex, LONG dwNewLong)

该函数的作用是:重新设置指定窗口所属窗口类的
WNDCLASS结构体中指定数据成员的属性（包括设置新的窗口背景画刷、光标、图标和窗口类样式）。

注意:在MFC中，如果要修改应用程序窗口的图标，则应该框架类中进行因为框架窗口才有标题栏;如果要修改程序窗口的背景和光标，则应该在视类中进行。

```c++
int CMainErame::OnCreate(LPCREATESTRUCT IDCreateStruct){
	SetClassIong(m_hWnd,GCL_HICON,(LONG)LoadIcon(NULL,IDI_WARNING));
    return 0;
}
int CUIView::OnCreate(LPCREATESTRUCT lpCreateStruct){	
    SetClassLong(m_hWnd,GCL_HBRBACKGROUND,(LONG)GetStockObject(BLACK BRUSH));
    SetClassLong(m_hWnd,GCL_HCURSOR,(LONG)LoadCursor(NULL,IDC_CROSs));
    return 0;
}
```

## 动画图标

加载图标资源、设置定时器、添加定时器消息响应函数

```c++
HICoN m hlcon[41; //MainErm.h文件
int CMainFrame::OnCreate(LPCREATESTRUCT lpCreateStruct){
    m_hIcon[0]=::LoadIcon(AfxGetInstanceHandle(),
MAKEINTRESOURCE(IDI ICON1));
    m_hIcon[1]=::LoadIcon(theApp.m_hInstance,MAKEINTRESOURCE(IDI_ ICON2));
    m_hIcon[2]=::LoadIcon(AfxGetAppO->m_hInstance,MAKEINTRESOURCE(IDI ICON3));
    m_hIcon[3]=AfxGetApp()->LoadIcon(IDI_ICON4);
    SetClassLong(m_hWnd, GCL_HICON,(LONG)m_hlcon[0]);
    SetTimer(1,1000, NULL);
    return 0;
}
void CMainFrame::OnTimer(UINT nIDEvent){
	static int index=1;
	SetClassLong(m_hWnd, GCL_HICON,(LONG)m_hIcon[index]);
    index = ++index % 4;
	CFrameWnd:: OnTimer(nIDEvent);
}
```

# 进程与线程

## 内核对象

Windows操作系统和应用程序使用内核对象来管理各种各样的重要资源。比如进程、线程和文件。

内核对象是Windows内核分配的一个内存块,该内存块是一种数据结构,它的成员负责维护该对象的各种信息。

内核对象的数据结构只能被内核访问,因此应用程序无法在内存中找到这些数据结构并直接改变它们的内容。Windows提供了一组函数来对内核对象进行操作和访问。

内核对象的创建函数都有一个设定安全属性的参数,这一点可与Windows中的用户对象或GDI对象(窗口、菜单、光标、字体、画刷等)区分开。

## **程序与进程**

程序:计算机指令的集合，它以文件的形式存储在磁盘上。

进程:通常被定义为一个正在运行的程序的实例，是一个程序在其自身的地址空间中的一次执行活动。

进程是活的，是资源申请、调度和独立运行的单位，因此，它使用系统中的运行资源;而程序是死的,它不占用系统的运行资源。

**进程由两个部分组成:**

1、操作系统用来管理进程的<u>内核对象</u>。内核对象也是系统用来存放关于进程的统计信息的地方。(注意:内核对象不是进程本身)

2、<u>地址空间</u>。它包含所有可执行模块或DLL模块的代码和数据。它还包含动态内存分配的空间。如线程堆栈和堆分配空间。

## **进程与线程**

进程是不活泼的。进程从来不执行任何东西,它只是线程的容器。若要使进程完成某项操作，它必须拥有一个在它的环境中运行的线程,此线程负责执行包含在进程的地址空间中的代码。

单个进程可能包含若干个线程，这些线程都“同时”执行进程地址空间中的代码。

每个进程至少拥有一个线程，来执行进程的地址空间中的代码。当创建一个进程时，操作系统会自动创建这个进程的第一个线程,称为<u>主线程</u>。此后，该线程可以创建其他的线程。

## 线程

线程由两个部分组成:

1、线程的<u>内核对象</u>,操作系统用它来对线程实施管理。内核对象也是系统用来存放线程统计信息的地方。

2、<u>线程堆栈</u>,它用于维护线程在执行代码时需要的所有参数和局部变量。
当创建线程时，系统创建一个线程内核对象。该线程内核对象不是线程本身，而是操作系统用来管理线程的较小的数据结构。可以将线程内核对象视为由关于线程的统计信息组成的一个小型数据结构。

线程总是在某个进程环境中创建。系统从进程的地址空间中分配内存,供线程的堆栈使用。新线程运行的进程环境与创建线程的环境相同。因此,新线程可以访问进程的内核对象的所有句柄、进程中的所有内存和在这个相同的进程中的所有其他线程的堆栈。这使得<u>单个进程中的多个线程确实能够非常容易地互相通信</u>。

线程只有一个内核对象和一个堆栈，保留的记录很少，因此所需要的内存也很少。

因为线程需要的开销比进程少,因此在编程中经常采用多线程来解决编程问题,而尽量避免创建新的进程。

## 线程的运行

对于多线程程序，操作系统会为每一个运行线程安排一定的CPU时间——时间片。系统通过一种循环的方式为线程提供时间片,线程在自己的时间内运行,因时间片相当短，因此,给用户的感觉,就好像线程是同时运行的一样。

如果计算机拥有多个CPU,线程就能真正意义上同时运行了。

## 简单多线程实例

![image-20220629062336780](windows_imgs\kMcalNgIJHH.png)

![image-20220629062404761](windows_imgs\ltUlTzoUdMF.png)

![image-20220629062532312](windows_imgs\d5KRvWoqewb.png)

![image-20220629062548782](windows_imgs\Q7CGiEtRDpZ.png)

注意1:

Main函数中调用CloseHandle语句没有终止新创建的线程，只是表示在主线程中对新创建的线程的引用不感兴趣，因此将其句柄关闭。

另一方面,当关闭该句柄时，系统会递减该线程内核对象的使用计数。当实用计数为0时,系统就会释放该线程内核对象。如果没有关闭线程句柄，系统就会一直保持着对线程内核对象的引用,这样，即使该线程执行完毕,它的引用计数仍不会为0。这样该线程内核对象也就不会被释放,只有等到进程终止时,系统才会清理这些残留的对象。

因此,在程序中,当不再需要线程句柄时，应将其关闭，让这个线程内核对象的引用计数减1。

注意2:

上述程序只运行了主线程,新建的线程并没有运行。为什么会出现这样的结果?线程创建失败了吗?

实际情况并非如此,对于主线程来说，操作系统为它分配了时间片,因此它能够运行。当主线程创建新的线程后，会接着执行下一行代码，然后该线程结束，也就是说主线程执行完成了。此时,进程也就退出了，进呈中的所有资源,包括还没有执行的线程都要退出。所以,不是新的线程创建失败，而是没有机会执行，进程就退出了。

**Sleep函数**

通过调用API函数 Sleep,线程可以让自己睡眠指定的一段时间。正在睡眠的线程将暂停自己的运行，放弃执行的权利,而且睡眠的时候不占用处理器时间。一旦放弃了执行权力,操作系统就会从等待运行的其他线程队列中选择一个线程来执行。

因此,可以在上述程序的main函数最后添加:Sleep(10);

让主线程睡眠10ms,使其放弃执行的权利,操作系统就会选择新创建的线程让其运行。当10ms时间一过,主线程睡醒恢复运行，main函数退出，进程结束。

![image-20220629063522614](windows_imgs\9WOh7Glw4kc.png)

## **利用互斥对象实现线程同步**

**互斥对象**

![image-20220629063936393](windows_imgs\v30aLq4uq7g.png)

**获得互斥对象的所有权**

线程必须主动请求共享对象的使用权才能获得该所有权，这可以通过调用WaitForSingleObject函数实现。

DWORD WatiForSingleObject(HANDLE hHandle, DWORD dwMillisecond;

- HANDLE hHandle
  所请求对象的句柄。本例为互斥对象句柄:hMutex。一旦互斥对象处于有信号状态,则该函数返回，接着，操作系统会将这个互斥对象设为未通知状态。如果该互斥对象处于无信号状态，则该函数会一直等待，这样会暂停线程的执行。
- DWORD dwMillisecond
  指定等待的时间，如果指定的时间间隔已过，即使所请求的对象处于无信号状态，该函数也返回。如果该参数为0，该函数立即返回。如果该参数为INFINTE,则该函数永远等待，直到互斥对象处于由信号状态才返回。

**释放互斥对象的所有权**

当线程对共享资源访问结束后,应释放互斥对象的所有权，让该对象处于有信号状态。这时需要调用函数:ReleaseMutex

BOOL ReleaseMutex(HANDLE hMutex);

**火车站售票系统模拟程序**

```c++
#include <windows.h>
#include <iostream.h>

DwORD WINAPI ThreadProc1( LPVOID lpParameter);
DWORD WINAPI ThreadProc2( LPVOID IpParameter);

int tickets = 1;
HANDLE hMutex;
void main(){
    HANDLE hThread1;
    HANDLE hThread2;
    hThread1 = CreateThread(NULL,0,ThreadProc1,NULL,0,NULL);
    hThread2 = CreateThread(NULL,0,ThreadProc2,NULL,0,NULL);
	CloseHandle(hThread1);
	CloseHandle(hThread2);
    //创建互斥对象
	hMutex = CreateMutex(NULL, FALSE, NULL);
	Sleep(5000); 
}
//线程1的入口函数（售票窗口1)
DWORD WINAPI ThreadProc1(LPVOID IpParameter){
	while (TRUE){
        //等待互斥对象的所有权
		WaitForSingleObject(hMutex,INFINITE);
        if (tickets<=100){
			Sleep(1);
			cout << "thread1 sell ticket : " <<tickets ++<<endl;
		}else
			break;
        //释放互斥对象的所有权
		ReleaseMutex(hMutex);
    }
	return 0;
}
//线程2的入口函数(售票窗口2)
DWORD WINAPI ThreadProc2(LPVOID lpParameter){
	while (TRUE){
    //等待互斥对象的所有权
	WaitForSingleObject(hMutex,INFINITE);
        if (tickets<=100){
			Sleep(1);
			cout << "thread2 sell ticket : " << tickets ++ <<endl;
		}else
			break;
        //释放互斥对象的所有权
		ReleaseMutex(hMutex);
    }
	return 0;
}
```

**（没用互斥对象前）上述程序的隐患**

事实上,上述程序存在隐患,比如以下情况:

当tickets为100时，线程1函数进入if语句块后,正好该线程的时间片到了，操作系统就会选择线程2让其进行,而这时变量tickets的值还没有加1,因此这时变量tickets的值仍是100，线程2进入它的if语句块中，于是线程2执行卖票操作,打印票号100,然后tickets变量加1，其值变为101。如果当线程2执行完成上述操作之后,正好又轮到线程1开始运行了。而这时线程1将从原先的if语句块开始执行,于是它输出当前的票号,而此时tickets变量的值已经是101了，也就是说,我们会看到线程1卖了号码为101的票。显然这种情况时不允许的。

上述情况再现:在两个if语句内的第一行加入Sleep(1);再看运行结果

## 利用临界区实现线程同步

**临界区对象**

临界区,也称关键代码段,它是指一个小代码段,在代码能够执行前，它必须独占对某些资源的访问权。

通常把多线程中访问统一资源的那部分代码当作临界区，从而达到线程同步的目的。

**相关API函数**

初始化临界区对象:

void InitializeCriticalSection(LPCRITICAL_SECTIONlpCriticalSetion);

获得临界区对象所有权:

void EnterCriticalSection(LPCRITICAL_SECTIONlpCriticalSetion);

释放临界区对象所有权:

void LeaveCriticalSection(LPCRITICALSECTIONlpCriticalSetion);

释放临界区对象:

void DeleteCriticalSection(LPCRITICAL_SECTIONlpCriticalSetion);

**实例**

![image-20220629064426710](windows_imgs\Bujm2rnrgZH.png)

![image-20220629064440794](windows_imgs\OW0wFGgzqyN.png)

![image-20220629064451828](windows_imgs\kQRWoQlXLk3.png)

## 互斥对象与临界区的比较

互斥对象属于内核对象，利用内核对象进行线程同步，速度较慢，但利用互斥对象这样的内核对象,可以在多个进程中的各个线程间进行同步。

临界区只能在同一进程内的线程间进行同步，但使用最简单，同步速度较快，因此是实现同步化的首选方法。在使用临界区时，由于在等待进入关键代码段时无法设定超时值,容易进入死锁状态。

# 动态链接库DLL

## DDL概述

微软任何一个版本的Windows操作系统，动态链接库（DLL)都是其核心和基础。

动态链接库不能直接运行。它们是一些独立的文件，其中包含能被可执行程序或其它DLL调用来完成某项工作的函数。只有在其它模块调用动态链接库中的函数时，它才发挥作用。

Windows API中的所有函数都包含在DLL中。其中有3个最重要的DLL， Kernel32.dll，它包含用于管理内存、进程和线程的各个函数;User32.dll，它包含用于执行用户界面任务（如窗口的创建和消息的传送)的各个函数; GDI32.dll，它包含用于画图和显示文本的各个函数。

## 静态库（LIB）和动态库（DLL）

静态库:

函数和数据被编译进一个二进制文件(通常扩展名为<u>.LIB</u>)。在使用静态库的情况下，在编译链接可执行文件时,链接器从库中<u>复制</u>这些函数和数据，并把它们和应用程序的其它模块组合起来创建最终的可执行文件(.EXE文件)。

动态库：

在使用动态库的时候,往往提供两个文件:一个引入库和一个DLL。引入库包含被DLL导出的函数和变量的符号名,DLL包含实际的函数和数据。在编译链接可执行文件时，只需要链接引入库,DLL中的函数代码和数据并不复制到可执行文件中,在运行的时候,再去加载DLL，访问DLL中导出的函数。

## 使用动态链接库的好处(简答)

- 增强程序的扩展性
- 可以采用多种编程语言来写
- 提供二次开发的平台
- 简化项目管理
- 节省磁盘空间和内存
- 有助于资源共享

## 创建DLL文件

![image-20220629065011665](windows_imgs\opuqcLXphKV.png)

## 导出DLL中的函数

注意:应用程序如果想要访问DLL中的函数,那么该函数必须是已经被导出的函数。

为了让DLL导出函数，需要在每一个将要被导出的函数前添加标识符:<u>_declspec (dllexport)</u>。

```c++
_declspec (dllexport) int add(int a, int b){
	return a + b;
}
_declspec (dllexport) int subtract(int a, int b){
    return a - b;
}
```

Build后，在Debug目录下会产生一个动态库DII1.dIl文件和一个引入库文件DIl1.lib。

## 导出DLL中的类

在动态链接库中，除了函数能被导出，C++类同样也能够被导出。

为了让DLL导出类,在DLL中定义类时，需要在class关键字和类名之间加入标识符:<u>_declspec (dllexport)</u>。

另外，在实现动态链接库时,可以不导出整个类,而只导出该类中的某些成员函数。具体做法是将标识符添加到成员函数前。

注意:在访问导出类的函数时,仍受限于函数自身的访问权限。也就是说，如果该类的某个函数访问权限不是Pubilc，那么外部程序仍无法访问这个函数。

## 使用引入库文件

以上程序能够成功通过编译，但在程序链接时会产生三个错误，因为此时链接器不知道这两个函数是在哪个地方实现的。

为了解决这个问题，就需要利用动态链接库的引入库文件。引入库文件并没有包含实际的代码，它是用来为链接程序提供必要的信息，以便在可执行文件中建立动态链接时需要用到的重定位表。

加载引入库文件的两种方法（加载之前先把dll1.lib复制到dlltest工程目录中) :

- 选择“project\Settings”命令，选择link选项卡，在“Object/librarymodules”选项编辑框中输入:dll1.lib
- 通过“add files to project..”直接将dll1.lib加入到工程中。

## 隐式链接方式加载DLL

![image-20220629065211907](windows_imgs\hOXpEiN5O1i.png)

![image-20220629065228668](windows_imgs\R5xKQJDlBIB.png)

![image-20220629065310475](windows_imgs\WmJoIOo5OQB.png)

![image-20220629065327102](windows_imgs\hGdsLTdIaFb.png)

## 显式加载方式加载DLL

![image-20220629065404533](windows_imgs\rbQrsoB97DV.png)

![image-20220629065425940](windows_imgs\hufxZmtjvfT.png)

**实例**

![image-20220629065455026](windows_imgs\gtgmNEMLXdO.png)

## 名字改编问题

如果希望动态链接库在编译时，导出函数的名称不要发生改变，在定义导出函数时，需要加上限定符:extern“C"

```c++
extern "C"_declspec (dllexport) int add(int a, int b){
	return a + b;
}
extern "C"_declspec (dllexport) int subtract(int a, int b){
	return a - b;
}
```


extern "C”可以解决C++对C语言之间的函数名改编问题，但这种方法有一个缺陷，就是不能用于导出一个类的成员函数，只能用于导出全局函数这种情况。

## DlIMain函数介绍

一个Win32程序，对可执行模块来说，其入口函数是WinMain;而对DLL来说，其入口函数是DIlMain，该函数是可选的。也就是说，在编写DLL程序时，可以提供也可以不提供DIIMain函数。

注意:如果提供了DIIMain函数，那么在此函数中不要进行太复杂的调用。因为在加载该动态链接库时，user32.dll或GDI32.dll等一些Windows核心DLL还没有加载，这时会导致程序终止。

## MFC AppWizard(dll)

VC++集成开发工具提供了一个向导: MFC App Wizard(dl),它可以帮助我们创建一个支持MFC类库的DLL。

编写支持MFC的DLL与前面编写Win32 DLL的方法是类似的，只是前者对MFC提供了很好的支持。
