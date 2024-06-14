lambda表达式通常用于实现函数式接口（接口中只有一个抽象方法的接口）

### Lambda 表达式的基本语法

```java
(parameters) -> expression
```

或者

```java
(parameters) -> { statements; }
```

### 使用场景和示例

1. **使用lambda表达式实现函数式接口**

首先，定义一个函数式接口（只有一个抽象方法的接口）。

```java
@FunctionalInterface
interface MyFunctionalInterface {
    void doSomething();
}
```

然后，使用lambda表达式来实现这个接口：

```java
public class LambdaExample {
    public static void main(String[] args) {
        MyFunctionalInterface func = () -> System.out.println("Doing something!");
        func.doSomething();
    }
}
```

1. **使用lambda表达式实现有参数的函数式接口**

例如，定义一个有参数和返回值的函数式接口：

```java
@FunctionalInterface
interface MyFunctionalInterface {
    int add(int a, int b);
}
```

使用lambda表达式来实现这个接口：

```java
public class LambdaExample {
    public static void main(String[] args) {
        MyFunctionalInterface adder = (a, b) -> a + b;
        int result = adder.add(5, 3);
        System.out.println("Result: " + result);
    }
}
```

1. **在集合操作中使用lambda表达式**

lambda表达式在Java的集合框架中非常有用，例如在`List`中使用`forEach`方法：

```java
import java.util.Arrays;
import java.util.List;

public class LambdaExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

        // 使用lambda表达式打印列表中的每个元素
        names.forEach(name -> System.out.println(name));
    }
}
```

1. **使用lambda表达式进行过滤和映射**

lambda表达式与Stream API结合使用，可以更高效地进行集合操作：

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

        // 使用lambda表达式进行过滤
        List<String> filteredNames = names.stream()
                                          .filter(name -> name.startsWith("A"))
                                          .collect(Collectors.toList());

        System.out.println(filteredNames);

        // 使用lambda表达式进行映射
        List<Integer> nameLengths = names.stream()
                                         .map(name -> name.length())
                                         .collect(Collectors.toList());

        System.out.println(nameLengths);
    }
}
```

### 变量作用域

1. **Lambda表达式中访问局部变量**：

   - Lambda表达式可以访问外部方法中的局部变量，但是这些变量必须是隐式最终（effectively final）的。隐式最终意味着变量实际上不可更改，即一旦赋值后就不应该再修改。Java编译器会强制要求这些变量是隐式最终的，否则会编译错误。

   ```java
   int x = 10;
   Runnable r = () -> {
       // 可以访问外部变量x
       System.out.println(x);
   };
   ```

2. **Lambda表达式中访问类成员变量**：

   - Lambda表达式可以直接访问和修改其所在类的成员变量和静态变量，没有限制。

   ```java
   public class LambdaScopeTest {
       private int x = 10;
   
       public void test() {
           Runnable r = () -> {
               // 可以访问类的成员变量x
               System.out.println(x);
           };
           r.run();
       }
   }
   ```

3. **Lambda表达式中的参数**：

   - Lambda表达式中可以使用传递给它的参数，它们的作用域只限于Lambda表达式的主体内部。

   ```java
   interface MyInterface {
       void myMethod(int x);
   }
   
   public class LambdaScopeTest {
       public void test() {
           MyInterface obj = (x) -> {
               // 可以访问参数x
               System.out.println("Value of x is: " + x);
           };
           obj.myMethod(5);
       }
   }
   ```

总结来说，Lambda表达式可以捕获外部方法的局部变量和类的成员变量（包括静态变量），但捕获的局部变量必须是隐式最终的。

