**共性：**

- 都可以实现序列化，使对象可以变为二进制流在内存中/网络上传输数据。



**区别：**

- Parcelable是Android提供的序列化接口，Serializable是Java提供的序列化接口。因此Parcelable只能在Android中使用，而Serializable可以在任何使用Java语言的地方使用。
- Serializable只需要将对象标记为Serializable，比较简单，无需额外的实现；Parcelable需要<u>手动实现Parcelable接口</u>，包括编写序列化和反序列化过程的代码。
- <u>Serializable的序列化和反序列化都需要使用到IO操作；而Parcelable不需要IO操作</u>，<u>Parcelable的效率要高于Serializable</u>，Android中推荐使用Parcelable。
- 如果需要简单地实现对象的序列化和反序列化，并且性能不是关键问题，可以使用 `Serializable`；<u>如果要把对象持久化到存储设备或者通过网络传输到其它设备，最好使用`Serializable`</u>；如果需要高效的对象传递，并且性能要求较高，可以选择实现 `Parcelable`。



**二者使用的详解：**

- Parcelable使用起来比较麻烦
  - 序列化过程需要实现Parcelable的`writeToParcel(Parcel dest, int f1ags)`方法和`describeContents()`方法。
  - 其中`describeContents()`方法直接返回0就可以了。
  - 为了反序列化，还需要提供一个非空的名为`CREATOR`的静态字段，该字段类型是实现了Parcelable.Creator接口的类，一般用一个匿名内部类实现就可以了。
  - 现在也有一些插件可以方便地实现Parcelable接口。

- Serializable的使用就比较简单
  - 直接实现Serializable接口即可，该接口没有任何方法。
  - 序列化机制依赖于一个long型的`serialVersionUID`，如果没有显式的指定，在序列化运行时会基于该类的结构自动计算出一个值。如果类的结构发生变化就会导致自动计算出的`serialVersionUID`不同。这就会导致一个问题，序列化之后类如果新增了一个字段，反序列过程就会失败。一般会报**InvalidClassException**这样的异常。
  - 而如果显式的指定了`serialversionUID`，只要类的结构不发生重大变化，如字段类型发生变化等，仅仅添加或者删除字段等都可以反序列化成功。



**自定义一个类让其实现Parcelable的大致流程：**

1. 先实现该接口的`writeToParcel(Parcel dest, int flags)`和`describeContents()`方法
2. 添加一个Parcelable.Creator类型的名字为`CREATOR`的非空字段

```java
public class Person implements Parcelable {
    private String name;
    private int age;
    
    //...
    
    @Override
    public int describeContents() {
        return 0;
    }
    
    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(name); // 写出name
        dest.writeInt(age); // 写出age
    }
    
    public static final Parcelable.Creator<Person> CREATOR = new Parcelable.
            Creator<Person>() {
            
        @Override
        public Person createFromParcel(Parcel source) {
            Person person = new Person();
            person.name = source.readString(); // 读取name
            person.age = source.readInt(); // 读取age
            return person;
        }
        
        @Override
        public Person[] newArray(int size) {
            return new Person[size];
        }
    };
}
```

该类中的字段类型除了基本类型和String及它们对应的数组，如果有其它自定义的类型，也需要实现Parcelable或者Serializable接口。