全样式列表：

https://android.googlesource.com/platform/frameworks/base/+/refs/heads/master/core/res/res/values/themes.xml

# ThemeOverlay使用特点

当在某个Activity有些特殊要求的时候就可以用ThemeOverlay继承全局的样式,来修改自己的个性化样式,注意了该样式的引用只能设置在布局文件上,不能在清单文件里面进行设置 
定义:

```xml
<style name="AppTheme.Secondary" parent="ThemeOverlay.AppCompat">
    <item name="colorAccent">@color/colorPrimary</item>
</style>
```

调用:

```xml
    android:background="@color/dark_background"
    android:theme="@style/ThemeOverlay.AppCompat.Dark">
```

单独给toolbar设置样式

```xml
<android.support.v7.widget.Toolbar xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="?android:attr/actionBarSize"
    android:theme="@style/ThemeOverlay.AppCompat.Dark.ActionBar"
    android:background="?attr/colorPrimary">
</android.support.v7.widget.Toolbar>
```

**自定义样式属性**

首先在attrs.xml 定义属性名称

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <declare-styleable name="AppTheme.NoActionBar">
        <attr name="baseTitleTextColor" format="reference|color" />
        <attr name="titleDividerColor" format="reference|color" />
        <attr name="titleDividerLine" format="dimension" /> 
    </declare-styleable>
</resources>
```

在style.xml中使用自定义的属性

```xml
<style name="AppTheme.NoActionBar">
        <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
        <item name="baseTitleTextColor">#2a2a2a</item>
        <item name="titleDividerLine">1dp</item>
        <item name="titleDividerColor">@android:color/transparent</item>
</style>
```

在布局文件中引用样式

```xml
  <View
            android:id="@+id/view_divider"
            android:layout_width="match_parent"
            android:layout_height="?attr/titleDividerLine"
            android:background="?attr/titleDividerColor"/>
```

**自定义一个tootbar的样式**

定义一个NoActionBar的样式

```xml
<style name="TestAppTheme" parent="Theme.AppCompat.Light">
            <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
        <item name="colorPrimary">#6a1b9a</item>
        <item name="colorPrimaryDark">#ec407a</item>
        <item name="colorAccent">#f44336</item>
    </style>
```

布局中引人Toolbar

```xml
<android.support.v7.widget.Toolbar   
xmlns:android="http://schemas.android.com/apk/res/android"
              android:orientation="vertical"
              android:layout_width="match_parent"
              android:background="#4e342e"
              android:layout_height="wrap_content"
              android:minHeight="?attr/actionBarSize">
</android.support.v7.widget.Toolbar  >
```

在Activity中设置Toobar为ActionBar

```java
public class TestAppComActivity extends AppCompatActivity{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_testappcompat);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
    }
}
```

## 