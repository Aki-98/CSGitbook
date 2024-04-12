# 前言

复杂的软件必须有清晰合理的架构，否则无法开发和维护。你能想象你把一个软件的几乎所有代码都堆在一个文件里吗？一个文件上万行，你让后期的人员如何开发维护呢？

MVC（Model-View-Controller）是最常见的软件架构之一，业界有着广泛应用。它本身[很容易理解](https://link.juejin.cn?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2007%2F11%2Fmvc.html)。同时它与衍生的 MVP 和 MVVM 架构也有着一定的区别。

# MVC

MVC最最主要的思想就是分层，不再大杂烩了。MVC模式的意思是，软件可以分成三个部分：

![img114971984](App的几种架构_imgs\66.png)

- 视图（View）：用户界面，专门用来控制页面的。
- 控制器（Controller）：业务逻辑，用来获取用户的输入，操作 M 和 V，说白了就是调用 M 和 V 中的方法。
- 模型（Model）：用来专门用来做一些和数据（增删改查）有关的逻辑。

## MVC互动方式

至于它们之间的具体相互关系，就看你具体代码的体现，并没有一个书面话的定义，最常见的是这种：

![img](App的几种架构_imgs\67.png)

所有通信都是单向的：

- View ：接受用户指令，传送指令到 Controller。
- Controller ：完成业务逻辑后，要求 Model 改变状态。
- Model ：将新的数据发送到 View，用户得到反馈。

但MVC在真正大型运用的时候，最接近这种：

![img](App的几种架构_imgs\68.png)

也就是说如果不触及复杂逻辑或者数据的情况下，一些简单逻辑就直接在Controller处理了，然后 Controller 再作用于 View 。还有一点就是MVC中View是可以和 Model 直接进行交流的。

# MVP

如果非要切断 Model 和 View 之间的关系的话，那样就演变成 MVP 了。MVP 模式将 Controller 改名为 Presenter，同时改变了通信方向。

![img](App的几种架构_imgs\69.png)

- 各部分之间的通信，都是**双向**的。
- **View 与 Model 不发生联系**，都通过 Presenter 传递。
- View 非常薄，不部署任何业务逻辑，称为"被动视图"（Passive View），即没有任何主动性，而 Presenter非常厚，所有逻辑都部署在那里。

## MVP产生的原因

MVC 架构方式虽然比之前的大杂烩好很多，但是 M C 之间相互依赖过多，由于 View 可以和 Model 直接通信，这就造成了 **View 既依赖于 Controller 又依赖于 Model** 。Controller 同样依赖于 View 和 Model。耦合性还是太高，于是进行了进一步的优化处理。**让 M 和 V 彻底断了联系，只通过 P 来进行通信**。

# MVVM

MVVM 模式将 Presenter 改名为 ViewModel，基本上与 MVP 模式完全一致。

![img](App的几种架构_imgs\70.png)

唯一的区别是，它采用**双向绑定**（data-binding），View的变动，自动反映在 ViewModel，反之亦然。

举个例子，用户登录时，ViewModel差不多是这个样子的：

```java
java复制代码public class UserViewModel(){
    String username;
    String password;
}
```

当用户在界面上点击「登录」按钮的时候，只需要对 `UserViewModel` 做出改变就行了。View 会根据 ViewModel 的变化**自动更新**，**不用手工去设置**。

## MVVM产生的原因

MVP 使用一段时间后，发现让 View 调用 Presenter 的方法去设置界面，仍然需要大量的、烦人的代码。

于是提出：**能不能告诉 View 一个数据结构，然后 View 就能根据这个数据结构变化而自动随之变化呢？**

于是有了一个叫 **ViewModel** 的东西，它可以**和 View 层绑定**。ViewModel 的变化，View 立刻就会变化。

# 总结

再次强调上面讲的都是 `MVC` `MVP` `MVVP` 大的设计思路，具体到不同的语言程序体现起来是不同的，没有准确的定义，具体的书写方式要根据开发者自己的思想来定义。目的就是让代码不同功能间相互独立，可阅读性强，便于扩充和重复利用。