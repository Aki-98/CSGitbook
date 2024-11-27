## 一、ArrayList的基本特点

1. 快速随机访问
2. 允许存放多个null元素
3. 底层是Object数组
4. <u>增加元素个数可能很慢(可能需要扩容),删除元素可能很慢(可能需要移动很多元素),改对应索引元素比较快</u>

## 二、ArrayList的继承关系

来看下源码中的定义

```java
public class ArrayList<E> extends AbstractList<E> 
    implements List<E>, RandomAccess, Cloneable, java.io.Serializable
```

- 可以看到继承了AbstractList,此类提供 List 接口的骨干实现，以最大限度地减少实现"随机访问"数据存储（如数组）支持的该接口所需的工作.<u>对于连续的访问数据（如链表），应优先使用 AbstractSequentialList</u>，而不是此类.
- 实现了**List**接口,意味着ArrayList元素是<u>有序的,可以重复的</u>,可以有null元素的集合.
- 实现了**RandomAccess**接口标识着其<u>支持随机快速访问</u>,实际上,我们查看RandomAccess源码可以看到,其实里面什么都没有定义.因为<u>ArrayList底层是数组</u>,那么随机快速访问是理所当然的,访问速度<u>O(1)</u>.
- 实现了**Cloneable**接口,标识着可以它可以被复制.注意,ArrayList里面的clone()复制其实是<u>浅复制</u>(不知道此概念的赶快去查资料,这知识点非常重要).
- 实现了Serializable 标识着集合可被序列化。

## 三、ArrayList 的构造方法

在说构造方法之前我们要先看下与构造参数有关的几个全局变量：

```
/**
 * ArrayList 默认的数组容量
 */
 private static final int DEFAULT_CAPACITY = 10;

/**
 * 用于空实例的共享空数组实例
 */
 private static final Object[] EMPTY_ELEMENTDATA = {};

/**
 * 另一个共享空数组实例，用的不多,用于区别上面的EMPTY_ELEMENTDATA
 */
 private static final Object[] DEFAULTCAPACITY_EMPTY_ELEMENTDATA = {};

/**
 * ArrayList底层的容器  
 */
transient Object[] elementData; // non-private to simplify nested class access

//当前存放了多少个元素   并非数组大小
private int size;
```

**transient**标识之后是不被序列化的

但是ArrayList实际容器就是这个数组为什么标记为不序列化??那岂不是反序列化时会丢失原来的数据?

其实是ArrayList在序列化的时候会调用writeObject()，直接将size和element写入ObjectOutputStream；反序列化时调用readObject()，从ObjectInputStream获取size和element，再恢复到elementData。

原因在于elementData是一个缓存数组，它通常会预留一些容量，等容量不足时再扩充容量，那么有些空间可能就没有实际存储元素，采用上诉的方式来实现序列化时，就可以保证只序列化实际存储的那些元素，而不是整个数组，从而节省空间和时间。