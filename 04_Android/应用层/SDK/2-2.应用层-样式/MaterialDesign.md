## Toolbar

一、简介

Toolbar 是在 Android 5.0 开始推出的一个 Material Design 风格的导航控件 ，Google 非常推荐大家使用 Toolbar 来作为Android客户端的导航栏，以此来取代之前的 Actionbar 。与 Actionbar 相比，Toolbar 明显要灵活的多。它不像 Actionbar 一样，一定要固定在Activity的顶部，而是可以放到界面的任意位置。



二、建立前提：

1. 加入 appcompat 库
2. extend AppCompatActivity
3. 设置主题
   - 设置NoActionBar主题
   - 或者在主题中设置属性

```xml
<item name="windowActionBar">false</item>
<item name="windowNoTitle">true</item>
```

1. 在Activity中的onCreate()方法中，调用setSupportActionBar() 方法建立Toolbar

```java
@Override
 protected void onCreate(Bundle savedInstanceState) {  
        setContentView(R.layout.activity_main);  
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);  
        setSupportActionBar(toolbar);   
        //...   
}
```



三、使用

为了方便Toolbar的调用，可以把Toolbar封装成一个单独的layout，并且在需要使用到它的时候在布局中include这个layout

1. Toolbar的组成如下:

![img](MaterialDesign_imgs\4pGdT1qgZ95.png)

组成：

- Home：导航按钮，类型为ImageButton，可设置点击事件，用于返回上个页面或者滑出侧滑菜单为

- Logo：Logo展示图，类型为ImageView，不响应事件，仅仅作为展示

- Title：主标题

- SubTitle：副标题

- CustomView：标题和菜单之间是留给我们添加子View的区域

- Menu/Action：负责管理选项菜单，菜单本身可以点击

```xml
<android.support.v7.widget.Toolbar
        android:id="@+id/toolbar"
        android:layout_width="match_parent"
        android:layout_height="?attr/actionBarSize"
        android:background="@color/colorPrimary"
        app:logo="@mipmap/ic_launcher"
        app:title="标题"
        app:titleTextColor="#fff"
        app:subtitle="副标题"
        app:subtitleTextColor="#fff"
        app:navigationIcon="@drawable/ic_menu"
        app:popupTheme="@style/toolBar_pop_item"
```

属性：

- android:theme是ToolBar单独使用的主题

- app:popupTheme是弹出来的菜单项使用的主题

- app:titleTextAppearance 设置title text 相关属性，如：字体,颜色，大小等等
- app:subtitleTextAppearance 设置subtitletext相关属性，如：字体,颜色，大小等等
- app:logoDescription logo 描述
- android:background Toolbar 背景

2. Toolbar使用的颜色：

![img](MaterialDesign_imgs\5t2nF4PdmQQ.png)

颜色：

- 状态栏颜色(statusBarColor/colorPrimaryDark/)(只在api21及以上有效)

- 标题栏背景颜色(ToolBar/colorPrimary)

- 弹出菜单背景颜色(OptionMenu)

- 内容区域背景颜色(Background)

- 导航栏颜色(NavigationBar)(只在api21及以上有效)

- 标题文字颜色 (TitleBarTextColor/TextColorPrimary)

- 弹出菜单文字颜色(TextColor)

- 内容文字颜色(TextColor)

- 控件颜色(ColorAccent)



三、Toolbar的操作

使用getsupportactionbar()方法获得ActionBar对象，然后调用ActionBar的方法调整应用程序栏。例如，调用ActionBar.hide()方法隐藏应用程序栏。

1. 添加操作按钮

Toolbar上所有的操作按钮和下拉条目都需要在menu中定义，res/menu/目录下新建一个xml文件，在该文件下定义Toolbar所需要的操作按钮，代码如下：

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android" >   
    <!-- "Mark Favorite", should appear as action button if possible --> 
    <item  
        android:id="@+id/action_favorite"  
        android:icon="@drawable/ic_favorite_black_48dp"  
        android:title="@string/action_favorite"  
        app:showAsAction="ifRoom"/>  
    <!-- Settings, should always be in the overflow -->  
    <item   
        android:id="@+id/action_settings"   
        android:title="@string/action_settings"   
        app:showAsAction="never"/>
</menu>
```

①app:showAsAction：指定了这个操作按钮是否显示在Toolbar上；

- always表示永远显示在ToolBar中，如果屏幕空间不够则不显示；
- ifRoom：如果Toolbar上有足够的空间，则在Toolbar上显示为一个操作按钮；如果没有足够的空间，则在下拉菜单列表中；
- never：设置操作按钮在下拉菜单中显示，而不在Toolbar中显示。

2. 设置操作按钮的监听事件

在menu设置了显示在Toolbar上的item之后，需要把Toolbar和menu关联才能显示定义的item，重写Activity提供的onCreateOptionsMenu()方法可以关联Toolbar和menu。

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {      
        // Inflate the menu; this adds items to the action bar if it is present.     
        getMenuInflater().inflate(R.menu.menu_main,menu);      
        return true;  
}
```

这样，你就能在Toolbar上看到你关联的item了，然后重写onOptionsItemSelected()方法就可以对Toolbar的按钮设置监听。

```java
@Override
 protected boolean onOptionsItemSelected(MenuItem item) {  
        Intent intent;  
        switch (item.getItemId()) {  
        case R.id.action_favorite:    
            // User chose the "Favorite" action, mark the current item
            // as a favorite...
            return true;   
        case R.id.action_favorite: 
            // User chose the "Favorite" action, mark the current item    
            // as a favorite...            
            return true;        
        default:            
            // If we got here, the user's action was not recognized.   
            // Invoke the superclass to handle it.            
            return super.onOptionsItemSelected(item);
        }  
}
```

3. 添加Toolbar的返回按钮

setSupportActionBar(toolbar)之后getSupportActionBar().setDisplayHomeAsUpEnabled(true);   

```java
@Override
 protected void onCreate(Bundle savedInstanceState) {  
        setContentView(R.layout.activity_main);  
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);  
        setSupportActionBar(toolbar);     
        if(getSupportActionBar() != null)  
                // Enable the Up button 
                getSupportActionBar().setDisplayHomeAsUpEnabled(true);   
        }
        //...   
}
```

4. 对NavigationIcon设置点击监听

NavigationIcon就是左上角的那个默认是返回箭头的键的图标

```java
binding.toolbar.setNavigationOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Toast.makeText(MainActivity.this,"navigationOnClickListener",Toast.LENGTH_SHORT).show();
    }
});
```

5. 自定义Toolbar弹出菜单的样式

首先定义菜单样式的theme


```xml
<!--自定义toolbar菜单样式-->
<style name="toolbarMenuStyle" parent="@style/Widget.AppCompat.PopupMenu.Overflow">
    <!-- 是否覆盖锚点，默认为true，即盖住Toolbar -->
    <item name="overlapAnchor">false</item>
    <!-- 弹出层背景颜色 -->
    <item name="android:popupBackground">@color/material_deep_teal_500</item>
    <!-- 弹出层垂直方向上的偏移，负值会覆盖toolbar -->
    <item name="android:dropDownVerticalOffset">5dp</item>
    <!-- 弹出层水平方向上的偏移，即距离屏幕左边的距离，负值会导致右边出现空隙 -->
    <item name="android:dropDownHorizontalOffset">-2dp</item>
    <!--文字颜色-->
    <item name="android:textColor">@color/white</item>
</style>
```

在Theme中定义使用

```xml
<style name="Theme.AndroidLearning" parent="Theme.MaterialComponents.DayNight.NoActionBar">
    ...
    <item name="actionOverflowMenuStyle">@style/toolbarMenuStyle</item>
    ...
</style>
```