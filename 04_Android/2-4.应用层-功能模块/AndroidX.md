# AndroidX

Android Support Library 用于提供向下兼容的功能，比如support-v4、appcompat-v7。4、7代表API号码，对应系统版本1.6、2.1，指库能够向下兼容到的最低的版本。

现在安卓官方支持的最低系统版本已经是4.0.1，对应API号15.support-v4、appcompat-v7库也不再支持那么久远的系统了，但是它们的名字却一直保留了下来，虽然它们现在的实际作用已经对不上当初命名的原因了。

那么很明显，Android团队也意识到这种命名已经非常不合适了，于是对这些API的架构进行了一次重新的划分，推出了AndroidX。因此，AndroidX本质上其实就是对Android Support Library进行的一次升级，升级内容主要在于以下两个方面。

1. 包名。之前Android Support Library中的API，它们的包名都是在android.support.*下面的，而AndroidX库中所有API的包名都变成了在androidx.*下面。这是一个很大的变化，意味着以后凡是android.*包下面的API都是随着Android操作系统发布的，而androidx.*包下面的API都是随着扩展库发布的，这些API基本不会依赖于操作系统的具体版本。

2. 命名规则。吸取了之前命名规则的弊端，AndroidX所有库的命名规则里都不会再包含具体操作系统API的版本号了。比如，像appcompat-v7库，在AndroidX中就变成了appcompat库。

一个AndroidX完整的依赖库格式如下所示：

```xml
implementation 'androidx.appcompat:appcompat:1.0.2
```

AndroidX和Android Support Library中的库是非常不建议混合在一起使用的，因为它们可能会产生很多不兼容的问题。最好的做法是，要么全部使用AndroidX中的库，要么全部使用Android Support Library中的库。

而现在Android团队官方的态度也很明确，未来都会为AndroidX为主，Android Support Library已经不再建议使用，并会慢慢停止维护。另外，从Android Studio 3.4.2开始，新建的项目已经强制勾选使用AndroidX架构了。

那么对于老项目的迁移应该怎么办呢？由于涉及到了包名的改动，如果从Android Support Library升级到AndroidX需要手动去改每一个文件的包名，那可真得要改死了。为此，Android Studio提供了一个一键迁移的功能，只需要对着你的项目名右击 → Refactor → Migrate to AndroidX，就会弹出如下图所示的窗口。

![img](AndroidX_imgs\17.png)

这里点击Migrate，Android Studio就会自动检查你项目中所有使用Android Support Library的地方，并将它们全部改成AndroidX中对应的库。另外Android Studio还会将你原来的项目备份成一个zip文件，这样即使迁移之后的代码出现了问题你还可以随时还原回之前的代码。