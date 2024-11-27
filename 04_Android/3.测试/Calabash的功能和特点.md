# 介绍

Calabash 是一个自动化测试框架

- 它可以测试iOS 和 Android ,以及Hybrid App
- 同时支持模拟器和真机测试。
- Calabash支持Cucumber。(Cucumber是一个能够理解用普通语言描述的测试用例，支持BDD（行为驱动开发）的自动化测试工具，用Ruby编写，支持Java和 .Net等多种开发语言。)

# 更多的功能

## 查找视图

query(uiquery, *args)

可以根据坐标（coordinates）、类、content-description等查找视图元素（appium也可以）

```ruby
irb(main):002:0> query("button index:1")
=> [{"id"=>"save", "enabled"=>true, "contentDescription"=>nil, "class"=>"android.widget.Button", "text"=>"Save", "rect"=>{"center_y"=>724.0, "center_x"=>645.5, "height"=>64, "y"=>692, "width"=>71, "x"=>610}, "description"=>"android.widget.Button{4267b4a0 VFED..C. ........ 497,243-568,307 #7f070023 app:id/save}"}]
```

视图会被表示为一个ruby哈希表，因此可以查看key值

```ruby
irb(main):003:0> query("button index:1").first.keys
=> ["id", "enabled", "contentDescription", "class", "text", "rect", "description"]
```

*args 参数可以向查询到的结果执行方法。注意查询到的结果是APP内的Java代码，执行完成后会返回到Ruby脚本中。下面的代码获得了页面中button的文本（猜测）

```ruby
irb(main):005:0> query("button", "text")
=> ["Optional Settings", "Save", "Cancel", "Get a free blog at WordPress.com"]
```

下面的代码获得了页面中button的文本的长度（猜测）

```ruby
irb(main):007:0> query("button", "text", "length")
=> [17, 4, 6, 32]
```

下面的代码获得了页面中button的文本的小写版本

```ruby
irb(main):008:0> query("button", "text", "toLowerCase")
=> ["optional settings", "save", "cancel", "get a free blog at wordpress.com"]
```

甚至还可以设置页面中元素的文本

```ruby
irb(main):033:0> query("edittext index:1", setText:"1234")
=> ["<VOID>"]
```

ruby 1.8

```ruby
irb(main):034:0> query("edittext index:1", :setText => "1234")
=> ["<VOID>"]
```

## 等待

等待某个元素出现、等待某个元素不出现等。

## SP操作

读取、写入、清除SharedPreferences