存放一些类似登录的配置信息

本质上是一个xml文件，通过类似键值对的方式存放信息

位于程序私有目录中，即data/data/[packageName]/shared_prefs

覆盖安装后sp文件依旧存在

**SharedPreferences操作模式**

- MODE_APPEND:追加方式存储(先检查，不存在则创建，存在则追加)（现在不能使用了）
- MODE_PRIVATE:私有方式存储,其他应用无法访问
- MODE_WORLD_READABLE:可被其他应用读取
- MODE_WORLD_WRITEABLE:可被其他应用写入

在安卓中，您可以使用SharedPreferences（以下简称为sp）来存储和获取应用程序的数据。以下是获取和设置sp中的值的示例代码：

获取sp中的值：

```
javaCopy code// 获取SharedPreferences对象
SharedPreferences sharedPreferences = getSharedPreferences("myPrefs", Context.MODE_PRIVATE);

// 从SharedPreferences中获取一个值
String value = sharedPreferences.getString("key", defaultValue);
```

在这里，"myPrefs"是您想要使用的SharedPreferences文件的名称，"key"是要获取的值的键，defaultValue是如果找不到该键时返回的默认值。

设置sp中的值：

```
javaCopy code// 获取SharedPreferences对象
SharedPreferences sharedPreferences = getSharedPreferences("myPrefs", Context.MODE_PRIVATE);

// 使用SharedPreferences.Editor对象来编辑SharedPreferences
SharedPreferences.Editor editor = sharedPreferences.edit();

// 将值存储到SharedPreferences中
editor.putString("key", value);

// 应用更改
editor.apply();
```

在这里，您首先获取了SharedPreferences对象，然后创建了一个SharedPreferences.Editor对象来编辑SharedPreferences。接下来，您可以使用putString()方法将键值对存储到SharedPreferences中。最后，调用apply()方法来应用更改。

请注意，"key"是您要存储的值的键，value是要存储的值。此外，要确保在更改完SharedPreferences之后调用apply()方法，以确保更改得到应用。