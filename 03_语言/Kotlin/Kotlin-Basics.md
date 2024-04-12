# 一、Types

## Basic types

### String

#### 字符串类型

Kotlin有两种String类型

- Escaped strings 转义字符串
- Raw strings 原始字符串

转义字符串：可以包含转义字符：

```kotlin
val s = "Hello, world!\n"
```

原始字符串：可以包含换行符和任意文本。它由三引号 （“”“） 分隔，不包含转义，可以包含换行符和任何其他字符：

```kotlin
val text = """
    for (c in "foo")
        print(c)
"""
```

要从原始字符串中删除前导空格，请使用 trimMargin（） 函数：

```kotlin
val text = """
    |Tell me and I forget.
    |Teach me and I remember.
    |Involve me and I learn.
    |(Benjamin Franklin)
    """.trimMargin()
```

默认情况下，管道符号|用作边距前缀，但您可以选择另一个字符并将其作为参数传递，例如 trimMargin（“>”）。

#### 字符串模板

字符串文本可能包含模板表达式 - 经过计算的代码片段，其结果连接到字符串中。模板表达式以美元符号 （$） 开头，由名称组成：

```kotlin
val i = 10
println("i = $i") // Prints "i = 10"
```

或大括号中的表达式：

```kotlin
val s = "abc"
println("$s.length is ${s.length}") // Prints "abc.length is 3"
```

可以在原始字符串和转义字符串中使用模板。若要在任何允许作为标识符开头的符号（允许作为标识符的开头）之前插入原始字符串（不支持反斜杠转义）中的美元符号 $，请使用以下语法：

```kotlin
val price = """
${'$'}_9.99
"""
```

## Type checks and casts

### is and !is operators﻿

Use the `is` operator or its negated form `!is` to perform a runtime check that identifies whether an object conforms to a given type:

```kotlin
if (obj is String) {
    print(obj.length)
}

if (obj !is String) { // same as !(obj is String)
    print("Not a String")
} else {
    print(obj.length)
}
```



### Smart casts﻿

In most cases, you don't need to use explicit cast operators in Kotlin because the compiler tracks the `is`-checks and [explicit casts](https://kotlinlang.org/docs/typecasts.html#unsafe-cast-operator) for immutable values and inserts (safe) casts automatically when necessary:

```kotlin
fun demo(x: Any) {
    if (x is String) {
        print(x.length) // x is automatically cast to String
    }
}
```



The compiler is smart enough to know that a cast is safe if a negative check leads to a return:

```kotlin
if (x !is String) return

print(x.length) // x is automatically cast to String
```



or if it is on the right-hand side of `&&` or `||` and the proper check (regular or negative) is on the left-hand side:

```kotlin
// x is automatically cast to String on the right-hand side of `||`
if (x !is String || x.length == 0) return

// x is automatically cast to String on the right-hand side of `&&`
if (x is String && x.length > 0) {
    print(x.length) // x is automatically cast to String
}
```



Smart casts work for [`when` expressions](https://kotlinlang.org/docs/control-flow.html#when-expression) and [`while` loops](https://kotlinlang.org/docs/control-flow.html#while-loops) as well:

```kotlin
when (x) {
    is Int -> print(x + 1)
    is String -> print(x.length + 1)
    is IntArray -> print(x.sum())
}
```



Note that smart casts work only when the compiler can guarantee that the variable won't change between the check and the usage. More specifically, smart casts can be used under the following conditions:

- `val` local variables - always, with the exception of [local delegated properties](https://kotlinlang.org/docs/delegated-properties.html).
- `val` properties - if the property is private or internal or if the check is performed in the same [module](https://kotlinlang.org/docs/visibility-modifiers.html#modules) where the property is declared. <u>Smart casts cannot be used on open properties or properties that have custom getters.</u>
- `var` local variables - if the variable is not modified between the check and the usage, is not captured in a lambda that modifies it, and is not a local delegated property.
- `var` properties - never, because the variable can be modified at any time by other code.

### "Unsafe" cast operator﻿

Usually, the cast operator throws an exception if the cast isn't possible. And so, it's called *unsafe*. The unsafe cast in Kotlin is done by the infix operator `as`.

```kotlin
val x: String = y as String
```



Note that `null` cannot be cast to `String`, as this type is not [nullable](https://kotlinlang.org/docs/null-safety.html). If `y` is null, the code above throws an exception. To make code like this correct for null values, use the nullable type on the right-hand side of the cast:

```kotlin
val x: String? = y as String?
```



### "Safe" (nullable) cast operator﻿

To avoid exceptions, use the *safe* cast operator `as?`, which returns `null` on failure.

```kotlin
val x: String? = y as? String
```



Note that despite the fact that the right-hand side of `as?` is a non-null type `String`, the result of the cast is nullable.

### Generics type checks and casts﻿

Please see the corresponding section in the [generics documentation page](https://kotlinlang.org/docs/generics.html#generics-type-checks-and-casts) for information on which type checks and casts you can perform with generics.

# 二、Controlflow

## Conditions and loops﻿

### If expression﻿

In Kotlin, `if` is an expression: it returns a value. Therefore, there is no ternary operator (`condition ? then : else`) because ordinary `if` works fine in this role.

```kotlin
var max = a
if (a < b) max = b

// With else
var max: Int
if (a > b) {
    max = a
} else {
    max = b
}

// As expression
val max = if (a > b) a else b
```



Branches of an `if` expression can be blocks. In this case, the last expression is the value of a block:

```kotlin
val max = if (a > b) {
    print("Choose a")
    a
} else {
    print("Choose b")
    b
}
```



If you're using `if` as an expression, for example, for returning its value or assigning it to a variable, the `else` branch is mandatory.

### When expression﻿

`when` defines a conditional expression with multiple branches. It is similar to the `switch` statement in C-like languages. Its simple form looks like this.

```kotlin
when (x) {
    1 -> print("x == 1")
    2 -> print("x == 2")
    else -> {
        print("x is neither 1 nor 2")
    }
}
```



`when` matches its argument against all branches sequentially until some branch condition is satisfied.

`when` can be used either as an expression or as a statement. If it is used as an expression, the value of the first matching branch becomes the value of the overall expression. If it is used as a statement, the values of individual branches are ignored. Just like with `if`, each branch can be a block, and its value is the value of the last expression in the block.

The `else` branch is evaluated if none of the other branch conditions are satisfied.

If `when` is used as an *expression*, the `else` branch is mandatory, unless the compiler can prove that all possible cases are covered with branch conditions, for example, with [`enum` class](https://kotlinlang.org/docs/enum-classes.html) entries and [`sealed` class](https://kotlinlang.org/docs/sealed-classes.html) subtypes).

```kotlin
enum class Bit {
  ZERO, ONE
}

val numericValue = when (getRandomBit()) {
    Bit.ZERO -> 0
    Bit.ONE -> 1
    // 'else' is not required because all cases are covered
}
```



In `when` *statements*, the `else` branch is mandatory in the following conditions:

- `when` has a subject of an `Boolean`, [`enum`](https://kotlinlang.org/docs/enum-classes.html), or [`sealed`](https://kotlinlang.org/docs/sealed-classes.html) type, or their nullable counterparts.
- branches of `when` don't cover all possible cases for this subject.

```kotlin
enum class Color {
  RED, GREEN, BLUE
}

when (getColor()) {
    Color.RED -> println("red")
    Color.GREEN -> println("green")
    Color.BLUE -> println("blue")
    // 'else' is not required because all cases are covered
}

when (getColor()) {
  Color.RED -> println("red") // no branches for GREEN and BLUE
  else -> println("not red") // 'else' is required
}
```



To define a common behavior for multiple cases, combine their conditions in a single line with a comma:

```kotlin
when (x) {
    0, 1 -> print("x == 0 or x == 1")
    else -> print("otherwise")
}
```



You can use arbitrary expressions (not only constants) as branch conditions

```kotlin
when (x) {
    s.toInt() -> print("s encodes x")
    else -> print("s does not encode x")
}
```



You can also check a value for being `in` or `!in` a [range](https://kotlinlang.org/docs/ranges.html) or a collection:

```kotlin
when (x) {
    in 1..10 -> print("x is in the range")
    in validNumbers -> print("x is valid")
    !in 10..20 -> print("x is outside the range")
    else -> print("none of the above")
}
```



Another option is checking that a value `is` or `!is` of a particular type. Note that, due to [smart casts](https://kotlinlang.org/docs/typecasts.html#smart-casts), you can access the methods and properties of the type without any extra checks.

```kotlin
fun hasPrefix(x: Any) = when(x) {
    is String -> x.startsWith("prefix")
    else -> false
}
```



`when` can also be used as a replacement for an `if`-`else` `if` chain. If no argument is supplied, the branch conditions are simply boolean expressions, and a branch is executed when its condition is true:

```kotlin
when {
    x.isOdd() -> print("x is odd")
    y.isEven() -> print("y is even")
    else -> print("x+y is odd")
}
```



You can capture *when* subject in a variable using following syntax:

```kotlin
fun Request.getBody() =
    when (val response = executeRequest()) {
        is Success -> response.body
        is HttpError -> throw HttpException(response.status)
    }
```



The scope of variable introduced in *when* subject is restricted to the body of this *when*.

### For loops﻿

The `for` loop iterates through anything that provides an iterator. This is equivalent to the `foreach` loop in languages like C#. The syntax of `for` is the following:

```kotlin
for (item in collection) print(item)
```



The body of `for` can be a block.

```kotlin
for (item: Int in ints) {
    // ...
}
```



As mentioned before, `for` iterates through anything that provides an iterator. This means that it:

- has a member or an extension function `iterator()` that returns `Iterator<>`:
  - has a member or an extension function `next()`
  - has a member or an extension function `hasNext()` that returns `Boolean`.

All of these three functions need to be marked as `operator`.

To iterate over a range of numbers, use a [range expression](https://kotlinlang.org/docs/ranges.html):

```
for (i in 1..3) {
    println(i)
}
for (i in 6 downTo 0 step 2) {
    println(i)
}
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGSEAThoXhgRgIwB0XAzKRUy1hABwYEALgBsieYtVoBfBTXpMWbTADYMUCAHc0AFQgYADBgDOEmCIwAmASuEYxkmS3lCayqmkUgADQgEjgMAOYwEgAKUjgSalgIIABWOABuOEHgEFgieFIwDABqRZZ4EGjJ3AAcXGYgikA%3D%3D%3D)

Target: JVMRunning on v.1.8.0

A `for` loop over a range or an array is compiled to an index-based loop that does not create an iterator object.

If you want to iterate through an array or a list with an index, you can do it this way:

```
for (i in array.indices) {
    println(array[i])
}
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6aAbjgDYY4BOjOAnhgLwPNsDyShciBxCANBiEAjMRPBDilShmUYkERhkJ4MBbi1YA6AlDxgYAZ1IVMK2wAdGBAC60iTfQG08AXQU3lAL6KaAEgoiBOTADmME4ACrQ4TmqMWAggAFY4NGHgEFh2eLQwjABqJeZ4EGjpAIwGABwGAAwgAUA)

Target: JVMRunning on v.1.8.0

Alternatively, you can use the `withIndex` library function:

```
for ((index, value) in array.withIndex()) {
    println("the element at $index is $value")
}
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6mG1AbjgDYY4BOzOAnhgLxOscDySQuRA4RAGgwiARhKngRxSpWrUkEZhkKECsAB6S69FDFIFebdgDoA7ngAuACwCSafSVIUqq1QAdmBPb0RCJOMBgw9DBYMGj2TPEAJLowehh4AM4YiUYmiiqqAL7KaIUg4iD2LADmMPYACvQ49urMWAggAFY4dOXgEFi%2BeFHMAGowzBl4EGgdAIxWABxWAAwghUA)

Target: JVMRunning on v.1.8.0

### While loops﻿

`while` and `do-while` loops execute their body continuously while their condition is satisfied. The difference between them is the condition checking time:

- `while` checks the condition and, if it's satisfied, executes the body and then returns to the condition check.
- `do-while` executes the body and then checks the condition. If it's satisfied, the loop repeats. So, the body of `do-while` executes at least once regardless of the condition.

```kotlin
while (x > 0) {
    x--
}

do {
    val y = retrieveData()
} while (y != null) // y is visible here!
```



### Break and continue in loops﻿

Kotlin supports traditional `break` and `continue` operators in loops. See [Returns and jumps](https://kotlinlang.org/docs/returns.html).

## Nothing类

此类型没有值，用于标记永远无法访问的代码位置。在你自己的代码中，你可以使用 Nothing 来标记一个永远不会返回的函数：

```kotlin
fun fail(message: String): Nothing {
    throw IllegalArgumentException(message)
}
```

调用此函数时，编译器将知道执行不会在调用之后继续：

```kotlin
val s = person.name ?: fail("Name required")
println(s)     // 's' is known to be initialized at this point
```

在处理类型推断时，也可能会遇到此类型。此类型的可为 null 的变体 Nothing？，只有一个可能的值，即 null。如果使用 null 初始化推断类型的值，并且没有其他信息可用于确定更具体的类型，则编译器将推断 Nothing？类型：

```kotlin
val x = null           // 'x' has type `Nothing?`
val l = listOf(null)   // 'l' has type `List<Nothing?>
```

# 三、Packages and imports

## Packages and imports﻿

A source file may start with a package declaration:

```kotlin
package org.example

fun printMessage() { /*...*/ }
class Message { /*...*/ }

// ...
```



All the contents, such as classes and functions, of the source file are included in this package. So, in the example above, the full name of `printMessage()` is `org.example.printMessage`, and the full name of `Message` is `org.example.Message`.

If the package is not specified, the contents of such a file belong to the *default* package with no name.

### Default imports﻿

A number of packages are imported into every Kotlin file by default:

- [kotlin.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/index.html)
- [kotlin.annotation.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/index.html)
- [kotlin.collections.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/index.html)
- [kotlin.comparisons.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.comparisons/index.html)
- [kotlin.io.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/index.html)
- [kotlin.ranges.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/index.html)
- [kotlin.sequences.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/index.html)
- [kotlin.text.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/index.html)

Additional packages are imported depending on the target platform:

- JVM:
  - java.lang.*
  - [kotlin.jvm.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.jvm/index.html)
- JS:
  - [kotlin.js.*](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.js/index.html)

### Imports﻿

Apart from the default imports, each file may contain its own `import` directives.

You can import either a single name:

```kotlin
import org.example.Message // Message is now accessible without qualification
```



or all the accessible contents of a scope: package, class, object, and so on:

```kotlin
import org.example.* // everything in 'org.example' becomes accessible
```



If there is a name clash, you can disambiguate by using `as` keyword to locally rename the clashing entity:

```kotlin
import org.example.Message // Message is accessible
import org.test.Message as TestMessage // TestMessage stands for 'org.test.Message'
```



The `import` keyword is not restricted to importing classes; you can also use it to import other declarations:

- top-level functions and properties
- functions and properties declared in [object declarations](https://kotlinlang.org/docs/object-declarations.html#object-declarations-overview)
- [enum constants](https://kotlinlang.org/docs/enum-classes.html)

### Visibility of top-level declarations﻿

If a top-level declaration is marked `private`, it is private to the file it's declared in (see [Visibility modifiers](https://kotlinlang.org/docs/visibility-modifiers.html)).

# 四、Classes and objects

## Classes﻿

Classes in Kotlin are declared using the keyword `class`:

```kotlin
class Person { /*...*/ }
```

The class declaration consists of the class name, the class header (specifying its type parameters, the primary constructor, and some other things), and the class body surrounded by curly braces. Both the header and the body are optional; if the class has no body, the curly braces can be omitted.

```kotlin
class Empty
```

### Constructors﻿

A class in Kotlin can have a *primary constructor* and one or more *secondary constructors*. The primary constructor is a part of the class header, and it goes after the class name and optional type parameters.

```kotlin
class Person constructor(firstName: String) { /*...*/ }
```

If the primary constructor does not have any annotations or visibility modifiers, the `constructor` keyword can be omitted:

```kotlin
class Person(firstName: String) { /*...*/ }
```

The primary constructor cannot contain any code. Initialization code can be placed in *initializer blocks* prefixed with the `init` keyword.

During the initialization of an instance, the initializer blocks are executed in the same order as they appear in the class body, interleaved with the property initializers:

```
class InitOrderDemo(name: String) {
    val firstProperty = "First property: $name".also(::println)
    
    init {
        println("First initializer block that prints $name")
    }
    
    val secondProperty = "Second property: ${name.length}".also(::println)
    
    init {
        println("Second initializer block that prints ${name.length}")
    }
}
```

Primary constructor parameters can be used in the initializer blocks. They can also be used in property initializers declared in the class body:

```kotlin
class Customer(name: String) {
    val customerKey = name.uppercase()
}
```

Kotlin has a concise syntax for declaring properties and initializing them from the primary constructor:

```kotlin
class Person(val firstName: String, val lastName: String, var age: Int)
```

Such declarations can also include default values of the class properties:

```kotlin
class Person(val firstName: String, val lastName: String, var isEmployed: Boolean = true)
```

You can use a [trailing comma](https://kotlinlang.org/docs/coding-conventions.html#trailing-commas) when you declare class properties:

```kotlin
class Person(...................................
    val firstName: String,
    val lastName: String,
    var age: Int, // trailing comma
) { /*...*/ }
```

Much like regular properties, properties declared in the primary constructor can be mutable (`var`) or read-only (`val`).

If the constructor has annotations or visibility modifiers, the `constructor` keyword is required and the modifiers go before it:

```kotlin
class Customer public @Inject constructor(name: String) { /*...*/ }
```

Learn more about [visibility modifiers](https://kotlinlang.org/docs/visibility-modifiers.html#constructors).

#### Secondary constructors﻿

A class can also declare *secondary constructors*, which are prefixed with `constructor`:

```kotlin
class Person(val pets: MutableList<Pet> = mutableListOf())

class Pet {
    constructor(owner: Person) {
        owner.pets.add(this) // adds this pet to the list of its owner's pets
    }
}
```

If the class has a primary constructor, each secondary constructor needs to delegate to the primary constructor, either directly or indirectly through another secondary constructor(s). Delegation to another constructor of the same class is done using the `this` keyword:

```kotlin
class Person(val name: String) {
    val children: MutableList<Person> = mutableListOf()
    constructor(name: String, parent: Person) : this(name) {
        parent.children.add(this)
    }
}
```

Code in initialize blocks effectively becomes <u>part of the primary constructor</u>. Delegation to the primary constructor happens as the first statement of a secondary constructor, so the code in all initializer blocks and property initializers is executed before the body of the secondary constructor.

Even if the class has no primary constructor, the delegation still happens implicitly, and the initializer blocks are still executed:

```kotlin
class Constructors {
    init {
        println("Init block")
    }

    constructor(i: Int) {
        println("Constructor $i")
    }
}
```

If a non-abstract class does not declare any constructors (primary or secondary), it will have a generated primary constructor with <u>no arguments</u>. The visibility of the constructor will be <u>public</u>.

If you don't want your class to have a public constructor, declare an empty primary constructor with non-default visibility:

```kotlin
class DontCreateMe private constructor() { /*...*/ }
```

> On the JVM, if all of the primary constructor parameters have default values, the compiler will generate an additional parameterless constructor which will use the default values. This makes it easier to use Kotlin with libraries such as Jackson or JPA that create class instances through parameterless constructors.
>
> ```kotlin
>class Customer(val customerName: String = "")
> ```

### Creating instances of classes﻿

To create an instance of a class, call the constructor as if it were a regular function:

```kotlin
val invoice = Invoice()

val customer = Customer("Joe Smith")
```

> <u>Kotlin does not have a `new` keyword.</u>

The process of creating instances of nested, inner, and anonymous inner classes is described in [Nested classes](https://kotlinlang.org/docs/nested-classes.html).

### Class members﻿

Classes can contain:

- [Constructors and initializer blocks](https://kotlinlang.org/docs/classes.html#constructors)
- [Functions](https://kotlinlang.org/docs/functions.html)
- [Properties](https://kotlinlang.org/docs/properties.html)
- [Nested and inner classes](https://kotlinlang.org/docs/nested-classes.html)
- [Object declarations](https://kotlinlang.org/docs/object-declarations.html)

### Inheritance﻿

Classes can be derived from each other and form inheritance hierarchies. [Learn more about inheritance in Kotlin](https://kotlinlang.org/docs/inheritance.html).

### Abstract classes﻿

A class may be declared `abstract`, along with some or all of its members. An abstract member does not have an implementation in its class. You don't need to annotate abstract classes or functions with `open`.

```kotlin
abstract class Polygon {
    abstract fun draw()
}

class Rectangle : Polygon() {
    override fun draw() {
        // draw the rectangle
    }
}
```

You can override a non-abstract `open` member with an abstract one.

```kotlin
open class Polygon {
    open fun draw() {
        // some default polygon drawing method
    }
}

abstract class WildShape : Polygon() {
    // Classes that inherit WildShape need to provide their own
    // draw method instead of using the default on Polygon
    abstract override fun draw()
}
```

### Companion objects﻿

If you need to write a function that can be called without having a class instance but that needs access to the internals of a class (such as a factory method), you can write it as a member of an [object declaration](https://kotlinlang.org/docs/object-declarations.html) inside that class.

Even more specifically, if you declare a [companion object](https://kotlinlang.org/docs/object-declarations.html#companion-objects) inside your class, you can access its members using only the class name as a qualifier.

## Properties﻿

### Declaring properties﻿

Properties in Kotlin classes can be declared either as mutable, using the `var` keyword, or as read-only, using the `val` keyword.

```kotlin
class Address {
    var name: String = "Holmes, Sherlock"
    var street: String = "Baker"
    var city: String = "London"
    var state: String? = null
    var zip: String = "123456"
}
```



To use a property, simply refer to it by its name:

```kotlin
fun copyAddress(address: Address): Address {
    val result = Address() // there's no 'new' keyword in Kotlin
    result.name = address.name // accessors are called
    result.street = address.street
    // ...
    return result
}
```



### Getters and setters﻿

The full syntax for declaring a property is as follows:

```kotlin
var <propertyName>[: <PropertyType>] [= <property_initializer>]
    [<getter>]
    [<setter>]
```



The initializer, getter, and setter are optional. The property type is optional if it can be inferred from the initializer or the getter's return type, as shown below:

```kotlin
var initialized = 1 // has type Int, default getter and setter
// var allByDefault // ERROR: explicit initializer required, default getter and setter implied
```



The full syntax of a read-only property declaration differs from a mutable one in two ways: it starts with `val` instead of `var` and does not allow a setter:

```kotlin
val simple: Int? // has type Int, default getter, must be initialized in constructor
val inferredType = 1 // has type Int and a default getter
```



You can define custom accessors for a property. If you define a custom getter, it will be called every time you access the property (this way you can implement a computed property). Here's an example of a custom getter:

```kotlin
class Rectangle(val width: Int, val height: Int) {
    val area: Int // property type is optional since it can be inferred from the getter's return type
        get() = this.width * this.height
}
```



You can omit the property type if it can be inferred from the getter:

```kotlin
val area get() = this.width * this.height
```



If you define a custom setter, it will be called every time you assign a value to the property, except its initialization. A custom setter looks like this:

```kotlin
var stringRepresentation: String
    get() = this.toString()
    set(value) {
        setDataFromString(value) // parses the string and assigns values to other properties
    }
```



By convention, the name of the setter parameter is `value`, but you can choose a different name if you prefer.

If you need to annotate an accessor or change its visibility, but you don't need to change the default implementation, you can define the accessor without defining its body:

```kotlin
var setterVisibility: String = "abc"
    private set // the setter is private and has the default implementation

var setterWithAnnotation: Any? = null
    @Inject set // annotate the setter with Inject
```



#### Backing fields﻿

In Kotlin, a field is only used as a part of a property to hold its value in memory. Fields cannot be declared directly. However, when a property needs a backing field, Kotlin provides it automatically. This backing field can be referenced in the accessors using the `field` identifier:

```kotlin
var counter = 0 // the initializer assigns the backing field directly
    set(value) {
        if (value >= 0)
            field = value
            // counter = value // ERROR StackOverflow: Using actual name 'counter' would make setter recursive
    }
```



The `field` identifier can only be used in the accessors of the property.

A backing field will be generated for a property if it uses the default implementation of at least one of the accessors, or if a custom accessor references it through the `field` identifier.

For example, there would be no backing field in the following case:

```kotlin
val isEmpty: Boolean
    get() = this.size == 0
```



#### Backing properties﻿

If you want to do something that does not fit into this *implicit backing field* scheme, you can always fall back to having a *backing property*:

```kotlin
private var _table: Map<String, Int>? = null
public val table: Map<String, Int>
    get() {
        if (_table == null) {
            _table = HashMap() // Type parameters are inferred
        }
        return _table ?: throw AssertionError("Set to null by another thread")
    }
```



> On the JVM: Access to private properties with default getters and setters is optimized to avoid function call overhead.

### Compile-time constants﻿

If the value of a read-only property is known at compile time, mark it as a *compile time constant* using the `const` modifier. Such a property needs to fulfil the following requirements:

- It must be a top-level property, or a member of an [`object` declaration](https://kotlinlang.org/docs/object-declarations.html#object-declarations-overview) or a *[companion object](https://kotlinlang.org/docs/object-declarations.html#companion-objects)*.
- It must be initialized with a value of type `String` or a primitive type
- It cannot be a custom getter

The compiler will inline usages of the constant, replacing the reference to the constant with its actual value. However, the field will not be removed and therefore can be interacted with using [reflection](https://kotlinlang.org/docs/reflection.html).

Such properties can also be used in annotations:

```kotlin
const val SUBSYSTEM_DEPRECATED: String = "This subsystem is deprecated"

@Deprecated(SUBSYSTEM_DEPRECATED) fun foo() { ... }
```



### Late-initialized properties and variables﻿

Normally, properties declared as having a non-null type must be initialized in the constructor. However, it is often the case that doing so is not convenient. For example, properties can be initialized through dependency injection, or in the setup method of a unit test. In these cases, you cannot supply a non-null initializer in the constructor, but you still want to avoid null checks when referencing the property inside the body of a class.

To handle such cases, you can mark the property with the `lateinit` modifier:

```kotlin
public class MyTest {
    lateinit var subject: TestSubject

    @SetUp fun setup() {
        subject = TestSubject()
    }

    @Test fun test() {
        subject.method()  // dereference directly
    }
}
```



This modifier can be used on `var` properties declared inside the body of a class (not in the primary constructor, and only when the property does not have a custom getter or setter), as well as for top-level properties and local variables. The type of the property or variable must be non-null, and it must not be a primitive type.

Accessing a `lateinit` property before it has been initialized throws a special exception that clearly identifies the property being accessed and the fact that it hasn't been initialized.

#### Checking whether a lateinit var is initialized﻿

To check whether a `lateinit var` has already been initialized, use `.isInitialized` on the [reference to that property](https://kotlinlang.org/docs/reflection.html#property-references):

```kotlin
if (foo::bar.isInitialized) {
    println(foo.bar)
}
```



This check is only available for properties that are lexically accessible when declared in the same type, in one of the outer types, or at top level in the same file.

### Overriding properties﻿

See [Overriding properties](https://kotlinlang.org/docs/inheritance.html#overriding-properties)

### Delegated properties﻿

The most common kind of property simply reads from (and maybe writes to) a backing field, but custom getters and setters allow you to use properties so one can implement any sort of behavior of a property. Somewhere in between the simplicity of the first kind and variety of the second, there are common patterns for what properties can do. A few examples: lazy values, reading from a map by a given key, accessing a database, notifying a listener on access.

Such common behaviors can be implemented as libraries using [delegated properties](https://kotlinlang.org/docs/delegated-properties.html).

## Extensions﻿

Kotlin provides the ability to extend a class or an interface with new functionality without having to inherit from the class or use design patterns such as *Decorator*. This is done via special declarations called *extensions*.

For example, you can write new functions for a class or an interface from a third-party library that you can't modify. Such functions can be called in the usual way, as if they were methods of the original class. This mechanism is called an *extension function*. There are also *extension properties* that let you define new properties for existing classes.

### Extension functions﻿

To declare an extension function, prefix its name with a *receiver type*, which refers to the type being extended. The following adds a `swap` function to `MutableList<Int>`:

```kotlin
fun MutableList<Int>.swap(index1: Int, index2: Int) {
    val tmp = this[index1] // 'this' corresponds to the list
    this[index1] = this[index2]
    this[index2] = tmp
}
```



The `this` keyword inside an extension function corresponds to the receiver object (the one that is passed before the dot). Now, you can call such a function on any `MutableList<Int>`:

```kotlin
val list = mutableListOf(1, 2, 3)
list.swap(0, 2) // 'this' inside 'swap()' will hold the value of 'list'
```



This function makes sense for any `MutableList<T>`, and you can make it generic:

```kotlin
fun <T> MutableList<T>.swap(index1: Int, index2: Int) {
    val tmp = this[index1] // 'this' corresponds to the list
    this[index1] = this[index2]
    this[index2] = tmp
}
```



You need to declare the generic type parameter before the function name to make it available in the receiver type expression. For more information about generics, see [generic functions](https://kotlinlang.org/docs/generics.html).

### Extensions are resolved statically﻿

Extensions do not actually modify the classes they extend. By defining an extension, you are not inserting new members into a class, only making new functions callable with the dot-notation on variables of this type.

Extension functions are dispatched *statically*, which means they are not virtual by receiver type. An extension function being called is determined by the type of the expression on which the function is invoked, not by the type of the result from evaluating that expression at runtime. For example:

```kotlin
open class Shape
class Rectangle: Shape()

fun Shape.getName() = "Shape"
fun Rectangle.getName() = "Rectangle"

fun printClassName(s: Shape) {
    println(s.getName())
}

printClassName(Rectangle())
```

This example prints *Shape*, because the extension function called depends only on the declared type of the parameter `s`, which is the `Shape` class.

If a class has a member function, and an extension function is defined which has the same receiver type, the same name, and is applicable to given arguments, the *member always wins*. For example:

```kotlin
class Example {
    fun printFunctionType() { println("Class method") }
}

fun Example.printFunctionType() { println("Extension function") }

Example().printFunctionType()
```

This code prints *Class method*.

However, it's perfectly OK for extension functions to overload member functions that have the same name but a different signature:

```kotlin
class Example {
    fun printFunctionType() { println("Class method") }
}

fun Example.printFunctionType(i: Int) { println("Extension function #$i") }

Example().printFunctionType(1)
```

### Nullable receiver﻿

Note that extensions can be defined with a nullable receiver type. These extensions can be called on an object variable even if its value is null, and they can check for `this == null` inside the body.

This way, you can call `toString()` in Kotlin without checking for `null`, as the check happens inside the extension function:

```kotlin
fun Any?.toString(): String {
    if (this == null) return "null"
    // after the null check, 'this' is autocast to a non-null type, so the toString() below
    // resolves to the member function of the Any class
    return toString()
}
```



### Extension properties﻿

Kotlin supports extension properties much like it supports functions:

```kotlin
val <T> List<T>.lastIndex: Int
    get() = size - 1
```



> Since extensions do not actually insert members into classes, there's no efficient way for an extension property to have a [backing field](https://kotlinlang.org/docs/properties.html#backing-fields). This is why *initializers are not allowed for extension properties*. Their behavior can only be defined by explicitly providing getters/setters.

Example:

```kotlin
val House.number = 1 // error: initializers are not allowed for extension properties
```



### Companion object extensions﻿

If a class has a [companion object](https://kotlinlang.org/docs/object-declarations.html#companion-objects) defined, you can also define extension functions and properties for the companion object. Just like regular members of the companion object, they can be called using only the class name as the qualifier:

```kotlin
class MyClass {
    companion object { }  // will be called "Companion"
}

fun MyClass.Companion.printCompanion() { println("companion") }

fun main() {
    MyClass.printCompanion()
}
```

#### Scope of extensions﻿

In most cases, you define extensions on the top level, directly under packages:

```kotlin
package org.example.declarations

fun List<String>.getLongestString() { /*...*/}
```



To use an extension outside its declaring package, import it at the call site:

```kotlin
package org.example.usage

import org.example.declarations.getLongestString

fun main() {
    val list = listOf("red", "green", "blue")
    list.getLongestString()
}
```



See [Imports](https://kotlinlang.org/docs/packages.html#imports) for more information.

### Declaring extensions as members﻿

You can declare extensions for one class inside another class. Inside such an extension, there are multiple *implicit receivers* - objects whose members can be accessed without a qualifier. An instance of a class in which the extension is declared is called a *dispatch receiver*, and an instance of the receiver type of the extension method is called an *extension receiver*.

```kotlin
class Host(val hostname: String) {
    fun printHostname() { print(hostname) }
}

class Connection(val host: Host, val port: Int) {
    fun printPort() { print(port) }

    fun Host.printConnectionString() {
        printHostname()   // calls Host.printHostname()
        print(":")
        printPort()   // calls Connection.printPort()
    }

    fun connect() {
        /*...*/
        host.printConnectionString()   // calls the extension function
    }
}

fun main() {
    Connection(Host("kotl.in"), 443).connect()
    //Host("kotl.in").printConnectionString()  // error, the extension function is unavailable outside Connection
}
```



In the event of a name conflict between the members of a dispatch receiver and an extension receiver, the extension receiver takes precedence. To refer to the member of the dispatch receiver, you can use the [qualified `this` syntax](https://kotlinlang.org/docs/this-expressions.html#qualified-this).

```kotlin
class Connection {
    fun Host.getConnectionString() {
        toString()         // calls Host.toString()
        this@Connection.toString()  // calls Connection.toString()
    }
}
```



Extensions declared as members can be declared as `open` and overridden in subclasses. This means that the dispatch of such functions is virtual with regard to the dispatch receiver type, but static with regard to the extension receiver type.

```kotlin
open class Base { }

class Derived : Base() { }

open class BaseCaller {
    open fun Base.printFunctionInfo() {
        println("Base extension function in BaseCaller")
    }

    open fun Derived.printFunctionInfo() {
        println("Derived extension function in BaseCaller")
    }

    fun call(b: Base) {
        b.printFunctionInfo()   // call the extension function
    }
}

class DerivedCaller: BaseCaller() {
    override fun Base.printFunctionInfo() {
        println("Base extension function in DerivedCaller")
    }

    override fun Derived.printFunctionInfo() {
        println("Derived extension function in DerivedCaller")
    }
}

fun main() {
    BaseCaller().call(Base())   // "Base extension function in BaseCaller"
    DerivedCaller().call(Base())  // "Base extension function in DerivedCaller" - dispatch receiver is resolved virtually
    DerivedCaller().call(Derived())  // "Base extension function in DerivedCaller" - extension receiver is resolved statically
}
```



### Note on visibility﻿

Extensions utilize the same [visibility modifiers](https://kotlinlang.org/docs/visibility-modifiers.html) as regular functions declared in the same scope would. For example:

- An extension declared at the top level of a file has access to the other `private` top-level declarations in the same file.
- If an extension is declared outside its receiver type, it cannot access the receiver's `private` or `protected` members.





## Data classes﻿

It is not unusual to create classes whose main purpose is to hold data. In such classes, some standard functionality and some utility functions are often mechanically derivable from the data. In Kotlin, these are called *data classes* and are marked with `data`:

```kotlin
data class User(val name: String, val age: Int)
```



The compiler automatically derives the following members from all properties declared in the primary constructor:

- `equals()`/`hashCode()` pair
- `toString()` of the form `"User(name=John, age=42)"`
- [`componentN()` functions](https://kotlinlang.org/docs/destructuring-declarations.html) corresponding to the properties in their order of declaration.
- `copy()` function (see below).

To ensure consistency and meaningful behavior of the generated code, data classes have to fulfill the following requirements:

- The primary constructor needs to have at least one parameter.
- All primary constructor parameters need to be marked as `val` or `var`.
- Data classes <u>cannot be abstract, open, sealed, or inner.</u>

Additionally, the generation of data class members follows these rules with regard to the members' inheritance:

- If there are explicit implementations of `equals()`, `hashCode()`, or `toString()` in the data class body or `final` implementations in a superclass, then these functions are not generated, and the existing implementations are used.
- If a supertype has `componentN()` functions that are `open` and return compatible types, the corresponding functions are generated for the data class and override those of the supertype. If the functions of the supertype cannot be overridden due to incompatible signatures or due to their being final, an error is reported.
- Providing explicit implementations for the `componentN()` and `copy()` functions is not allowed.

Data classes may extend other classes (see [Sealed classes](https://kotlinlang.org/docs/sealed-classes.html) for examples).

> On the JVM, if the generated class needs to have a parameterless constructor, default values for the properties have to be specified (see [Constructors](https://kotlinlang.org/docs/classes.html#constructors)).

```kotlin
data class User(val name: String = "", val age: Int = 0)
```



### Properties declared in the class body﻿

The compiler only uses the properties defined inside the primary constructor for the automatically generated functions. To exclude a property from the generated implementations, declare it inside the class body:

```kotlin
data class Person(val name: String) {
    var age: Int = 0
}
```



Only the property `name` will be used inside the `toString()`, `equals()`, `hashCode()`, and `copy()` implementations, and there will only be one component function `component1()`. <u>While two `Person` objects can have different ages, they will be treated as equal.</u>

```
val person1 = Person("John")
val person2 = Person("John")
person1.age = 10
person2.age = 20
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIoEMAuyAEYA2yDOeGACjAE54QB2AFAG7LYaXIC2M8GAyqqQJaUBzAJQZgAHUoYpGeqQzIB7DAElKqDAF4MABgkBfCQDMArpJbJ%2B1EeMoTpMhhgAOZCpQCMm4q6rUxIACkIAAtbECE7aXpGF3IqACYvEjiafyDQ%2FwjJaVi3dwA6BRgvd11sqVyEwsUveLLIir41bFSQSo9NLXb4jgASYHbPDS6fSniDcIbnJtQWvzbRzwB3XlRg%2BRr%2BweqYPT6BxYms%2BycZuf9ujBW1jeKt0fidvYx7lPHM%2FRAAGhB0UkVUERcKhDBBSCwECAAFbIejfcAQFhOXjYMgANVcvCokIKAA58toQHogA%3D%3D%3D)

Target: JVMRunning on v.1.8.0

### Copying﻿

Use the `copy()` function to copy an object, allowing you to alter *some* of its properties while keeping the rest unchanged. The implementation of this function for the `User` class above would be as follows:

```kotlin
fun copy(name: String = this.name, age: Int = this.age) = User(name, age)
```



You can then write the following:

```kotlin
val jack = User(name = "Jack", age = 1)
val olderJack = jack.copy(age = 2)
```



### Data classes and destructuring declarations﻿

*Component functions* generated for data classes make it possible to use them in [destructuring declarations](https://kotlinlang.org/docs/destructuring-declarations.html):

```kotlin
val jane = User("Jane", 35)
val (name, age) = jane
println("$name, $age years of age") // prints "Jane, 35 years of age"
```



### Standard data classes﻿

The standard library provides the `Pair` and `Triple` classes. In most cases, though, named data classes are a better design choice because they make the code more readable by providing meaningful names for the properties.

## Sealed classes﻿

*Sealed* classes and interfaces represent restricted class hierarchies that provide more control over inheritance. All direct subclasses of a sealed class are known at compile time. No other subclasses may appear outside a module within which the sealed class is defined. For example, third-party clients can't extend your sealed class in their code. Thus, each instance of a sealed class has a type from a limited set that is known when this class is compiled.

The same works for sealed interfaces and their implementations: once a module with a sealed interface is compiled, no new implementations can appear.

In some sense, sealed classes are similar to [`enum`](https://kotlinlang.org/docs/enum-classes.html) classes: the set of values for an enum type is also restricted, but each enum constant exists only as a *single instance*, whereas a subclass of a sealed class can have *multiple* instances, each with its own state.

As an example, consider a library's API. It's likely to contain error classes to let the library users handle errors that it can throw. If the hierarchy of such error classes includes interfaces or abstract classes visible in the public API, then nothing prevents implementing or extending them in the client code. However, the library doesn't know about errors declared outside it, so it can't treat them consistently with its own classes. With a sealed hierarchy of error classes, library authors can be sure that they know all possible error types and no other ones can appear later.

To declare a sealed class or interface, put the `sealed` modifier before its name:

```kotlin
sealed interface Error

sealed class IOError(): Error

class FileReadError(val file: File): IOError()
class DatabaseError(val source: DataSource): IOError()

object RuntimeError : Error
```



A sealed class is [abstract](https://kotlinlang.org/docs/classes.html#abstract-classes) by itself, it cannot be instantiated directly and can have `abstract` members.

Constructors of sealed classes can have one of two [visibilities](https://kotlinlang.org/docs/visibility-modifiers.html): `protected` (by default) or `private`:

```kotlin
sealed class IOError {
    constructor() { /*...*/ } // protected by default
    private constructor(description: String): this() { /*...*/ } // private is OK
    // public constructor(code: Int): this() {} // Error: public and internal are not allowed
}
```

### Location of direct subclasses﻿

Direct subclasses of sealed classes and interfaces must be declared in the same package. They may be top-level or nested inside any number of other named classes, named interfaces, or named objects. Subclasses can have any [visibility](https://kotlinlang.org/docs/visibility-modifiers.html) as long as they are compatible with normal inheritance rules in Kotlin.

Subclasses of sealed classes must have a proper qualified name. They can't be local nor anonymous objects.

> `enum` classes can't extend a sealed class (as well as any other class), but they can implement sealed interfaces.

These restrictions don't apply to indirect subclasses. If a direct subclass of a sealed class is not marked as sealed, it can be extended in any way that its modifiers allow:

```kotlin
sealed interface Error // has implementations only in same package and module

sealed class IOError(): Error // extended only in same package and module
open class CustomError(): Error // can be extended wherever it's visible
```



#### Inheritance in multiplatform projects﻿

There is one more inheritance restriction in [multiplatform projects](https://kotlinlang.org/docs/multiplatform-get-started.html): direct subclasses of sealed classes must reside in the same source set. It applies to sealed classes without the [`expect` and `actual` modifiers](https://kotlinlang.org/docs/multiplatform-connect-to-apis.html).

If a sealed class is declared as `expect` in a common source set and have `actual` implementations in platform source sets, both `expect` and `actual` versions can have subclasses in their source sets. Moreover, if you use a [hierarchical structure](https://kotlinlang.org/docs/multiplatform-share-on-platforms.html#share-code-on-similar-platforms), you can create subclasses in any source set between the `expect` and `actual` declarations.

[Learn more about the hierarchical structure of multiplatform projects](https://kotlinlang.org/docs/multiplatform-share-on-platforms.html#share-code-on-similar-platforms).

### Sealed classes and when expression﻿

The key benefit of using sealed classes comes into play when you use them in a [`when`](https://kotlinlang.org/docs/control-flow.html#when-expression) expression. If it's possible to verify that the statement covers all cases, you don't need to add an `else` clause to the statement:

```kotlin
fun log(e: Error) = when(e) {
    is FileReadError -> { println("Error while reading file ${e.file}") }
    is DatabaseError -> { println("Error while reading from database ${e.source}") }
    is RuntimeError ->  { println("Runtime error") }
    // the `else` clause is not required because all the cases are covered
}
```

> `when` expressions on [`expect`](https://kotlinlang.org/docs/multiplatform-connect-to-apis.html) sealed classes in the common code of multiplatform projects still require an `else` branch. This happens because subclasses of `actual` platform implementations aren't known in the common code.

## Object expressions and declarations﻿

Sometimes you need to create an object that is a slight modification of some class, without explicitly declaring a new subclass for it. Kotlin can handle this with *object expressions* and *object declarations*.

### Object expressions﻿

*Object expressions* create objects of anonymous classes, that is, classes that aren't explicitly declared with the `class` declaration. Such classes are useful for one-time use. You can define them from scratch, inherit from existing classes, or implement interfaces. Instances of anonymous classes are also called *anonymous objects* because they are defined by an expression, not a name.

#### Creating anonymous objects from scratch﻿

Object expressions start with the `object` keyword.

If you just need an object that doesn't have any nontrivial supertypes, write its members in curly braces after `object`:

```
val helloWorld = object {
    val hello = "Hello"
    val world = "World"
    // object expressions extend Any, so `override` is required on `toString()`
    override fun toString() = "$hello $world"
}
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYYAWMjjEA6hAE6NQMAXgwQARgCsYYAC5lqtRQ2ZsOEYRnIgAEu05aFimsowB3PgI1ae%2FKAcxGaAeiejJ0uTAAeAB14wAZwC8CDQAjG8ZGDRBAEE0AE8AGgwA9QADCDoYXl48WHSMPHD%2FAEcUPH9BUIx0mQgAZRk8tABzEnTDIyycvNgMVEx6ppb20hEtABJVTgxJ81t7RQBfSi6%2FAhlCGe4LKGJKZZAkkBkcXlaYGQAFRhwZJD4sBBAJHAZj8AgsHzxGHIAajlgqEXgBGAB0AA4IWCAAwgZZAA)

Target: JVMRunning on v.1.8.10

#### Inheriting anonymous objects from supertypes﻿

To create an object of an anonymous class that inherits from some type (or types), specify this type after `object` and a colon (`:`). Then implement or override the members of this class as if you were [inheriting](https://kotlinlang.org/docs/inheritance.html) from it:

```kotlin
window.addMouseListener(object : MouseAdapter() {
    override fun mouseClicked(e: MouseEvent) { /*...*/ }

    override fun mouseEntered(e: MouseEvent) { /*...*/ }
})
```



If a supertype has a constructor, pass appropriate constructor parameters to it. Multiple supertypes can be specified as a comma-delimited list after the colon:

```kotlin
open class A(x: Int) {
    public open val y: Int = x
}

interface B { /*...*/ }

val ab: A = object : A(1), B {
    override val y = 15
}
```



#### Using anonymous objects as return and value types﻿

When an anonymous object is used as a type of a local or [private](https://kotlinlang.org/docs/visibility-modifiers.html#packages) but not [inline](https://kotlinlang.org/docs/inline-functions.html) declaration (function or property), all its members are accessible via this function or property:

```kotlin
class C {
    private fun getObject() = object {
        val x: String = "x"
    }

    fun printX() {
        println(getObject().x)
    }
}
```



If this function or property is public or private inline, its actual type is:

- `Any` if the anonymous object doesn't have a declared supertype
- The declared supertype of the anonymous object, if there is exactly one such type
- The explicitly declared type if there is more than one declared supertype

In all these cases, members added in the anonymous object are not accessible. Overridden members are accessible if they are declared in the actual type of the function or property:

```kotlin
interface A {
    fun funFromA() {}
}
interface B

class C {
    // The return type is Any. x is not accessible
    fun getObject() = object {
        val x: String = "x"
    }

    // The return type is A; x is not accessible
    fun getObjectA() = object: A {
        override fun funFromA() {}
        val x: String = "x"
    }

    // The return type is B; funFromA() and x are not accessible
    fun getObjectB(): B = object: A, B { // explicit return type is required
        override fun funFromA() {}
        val x: String = "x"
    }
}
```



#### Accessing variables from anonymous objects﻿

The code in object expressions can access variables from the enclosing scope:

```kotlin
fun countClicks(window: JComponent) {
    var clickCount = 0
    var enterCount = 0

    window.addMouseListener(object : MouseAdapter() {
        override fun mouseClicked(e: MouseEvent) {
            clickCount++
        }

        override fun mouseEntered(e: MouseEvent) {
            enterCount++
        }
    })
    // ...
}
```



### Object declarations﻿

The [Singleton](https://en.wikipedia.org/wiki/Singleton_pattern) pattern can be useful in several cases, and Kotlin makes it easy to declare singletons:

```kotlin
object DataProviderManager {
    fun registerDataProvider(provider: DataProvider) {
        // ...
    }

    val allDataProviders: Collection<DataProvider>
        get() = // ...
}
```



This is called an *object declaration*, and it always has a name following the `object` keyword. Just like a variable declaration, an object declaration is not an expression, and it cannot be used on the right-hand side of an assignment statement.

The initialization of an object declaration is thread-safe and done on first access.

To refer to the object, use its name directly:

```kotlin
DataProviderManager.registerDataProvider(...)
```



Such objects can have supertypes:

```kotlin
object DefaultListener : MouseAdapter() {
    override fun mouseClicked(e: MouseEvent) { ... }

    override fun mouseEntered(e: MouseEvent) { ... }
}
```



> ### 
>
> 
>
> Object declarations can't be local (that is, they can't be nested directly inside a function), but they can be nested into other object declarations or non-inner classes.

#### Data objects﻿

> ### 
>
> 
>
> Data object declarations is an [Experimental](https://kotlinlang.org/docs/components-stability.html) feature. It may be dropped or changed at any time. Opt-in is required with the `compilerOptions.languageVersion.set(KotlinVersion.KOTLIN_1_9)` [compiler option](https://kotlinlang.org/docs/gradle.html#compiler-options).

When printing a plain `object` declaration in Kotlin, you'll notice that its string representation contains both its name and the hash of the object:

```kotlin
object MyObject

fun main() {
    println(MyObject) // MyObject@1f32e575
}
```



Just like [data classes](https://kotlinlang.org/docs/data-classes.html), you can mark your `object` declaration with the `data` modifier to get a nicely formatted string representation without having to manually provide an implementation for its `toString` function:

```kotlin
data object MyObject

fun main() {
    println(MyObject) // MyObject
}
```



[Sealed class hierarchies](https://kotlinlang.org/docs/sealed-classes.html) are a particularly good fit for `data object` declarations, since they allow you to maintain symmetry with any data classes you might have defined alongside the object:

```kotlin
sealed class ReadResult {
    data class Number(val value: Int): ReadResult()
    data class Text(val value: String): ReadResult()
    data object EndOfFile: ReadResult()
}

fun main() {
    println(ReadResult.Number(1)) // Number(value=1)
    println(ReadResult.Text("Foo")) // Text(value=Foo)
    println(ReadResult.EndOfFile) // EndOfFile
}
```



#### Companion objects﻿

An object declaration inside a class can be marked with the `companion` keyword:

```kotlin
class MyClass {
    companion object Factory {
        fun create(): MyClass = MyClass()
    }
}
```



Members of the companion object can be called simply by using the class name as the qualifier:

```kotlin
val instance = MyClass.create()
```



The name of the companion object can be omitted, in which case the name `Companion` will be used:

```kotlin
class MyClass {
    companion object { }
}

val x = MyClass.Companion
```



Class members can access the private members of the corresponding companion object.

The name of a class used by itself (not as a qualifier to another name) acts as a reference to the companion object of the class (whether named or not):

```kotlin
class MyClass1 {
    companion object Named { }
}

val x = MyClass1

class MyClass2 {
    companion object { }
}

val y = MyClass2
```



Note that even though the members of companion objects look like static members in other languages, at runtime those are still instance members of real objects, and can, for example, implement interfaces:

```kotlin
interface Factory<T> {
    fun create(): T
}

class MyClass {
    companion object : Factory<MyClass> {
        override fun create(): MyClass = MyClass()
    }
}

val f: Factory<MyClass> = MyClass
```



However, on the JVM you can have members of companion objects generated as real static methods and fields if you use the `@JvmStatic` annotation. See the [Java interoperability](https://kotlinlang.org/docs/java-to-kotlin-interop.html#static-fields) section for more detail.

#### Semantic difference between object expressions and declarations﻿

There is one important semantic difference between object expressions and object declarations:

- Object expressions are executed (and initialized) *immediately*, where they are used.
- Object declarations are initialized *lazily*, when accessed for the first time.
- A companion object is initialized when the corresponding class is loaded (resolved) that matches the semantics of a Java static initializer.

# 04_Functions

## Functions

### 方法声明

一个具有两个Int类型的参数和一个Int类型的返回值的函数：

```Kotlin
fun sum(a: Int, b: Int): Int {
    return a + b
}
```

一个方法的主体也可以使用表达式，返回值程序自行推定：

```Kotlin
fun sum(a: Int, b: Int) = a + b
```

可以没有返回值也可以不定义返回值类型，直接省略到例子一中的":Int"

### 默认参数

方法参数可以指定默认值，调用方法的时候可以跳过有默认值的参数：

```kotlin
fun read(
    b: ByteArray,
    off: Int = 0,
    len: Int = b.size,
) { /*...*/ }
```

重写的方法始终使用基方法的默认参数，重写具有默认参数值的方法时，必须从签名中省略默认参数值：

```kotlin
open class A {
    open fun foo(i: Int = 10) { /*...*/ }
}

class B : A() {
    override fun foo(i: Int) { /*...*/ }  // No default value is allowed.
}
```

如果默认参数位于没有默认值的参数之前，则只能通过使用命名参数调用函数来使用默认值：

```kotlin
fun foo(
    bar: Int = 0,
    baz: Int,
) { /*...*/ }

foo(baz = 1) // The default value bar = 0 is used
```

如果默认参数后面的最后一个参数是 lambda，则可以将其作为命名参数传递或在括号外传递：？？？？？？？？？？？看不懂？？？？？？？？？？？？

```kotlin
fun foo(
    bar: Int = 0,
    baz: Int = 1,
    qux: () -> Unit,
) { /*...*/ }

foo(1) { println("hello") }     // Uses the default value baz = 1
foo(qux = { println("hello") }) // Uses both default values bar = 0 and baz = 1
foo { println("hello") }        // Uses both default values bar = 0 and baz = 1
```

### 空类型安全

#### 可以为空的类型和不可以为空的类型

Kotlin 中 NPE （NullPointerException）的唯一可能原因是：

- 直接调用 throw NullPointerException()
- 使用!!运算符
- 与初始化相关的数据不一致，例如：
  - 构造函数中可用的未初始化的this在某处传递和使用（“泄漏this”）。
  - 父类构造函数调用一个开放成员，该成员在派生类中未初始化。

- 与Java的交互操作：
  - 尝试访问平台类型的空引用的成员;
  - 用于 Java 互操作的泛型类型的可空性问题。例如，一段 Java 代码可能会将 null 添加到 Kotlin MutableList 中<String>，因此需要一个 MutableList<String？> 来处理它。
  - 外部 Java 代码导致的其他问题。

在 Kotlin 中，类型系统区分可以保存 null 的引用（可为空的引用）和不能保存 null 的引用（非空引用）。例如，字符串类型的常规变量不能保存 null：

```kotlin
var a: String = "abc" // Regular initialization means non-null by default
a = null // compilation error
```

要允许空值，您可以通过编写 String？：

```kotlin
var b: String? = "abc" // can be set to null
b = null // ok
print(b)
```

#### 安全调用

访问可为空变量的属性的第二个选项是使用安全调用运算符 ？.：

```kotlin
val a = "Kotlin"
val b: String? = null
println(b?.length)
println(a?.length) // Unnecessary safe call
```

Safe calls are useful in chains.

```kotlin
bob?.department?.head?.name
```

To perform a certain operation only for non-null values, you can use the safe call operator together with let:

```kotlin
val listWithNulls: List<String?> = listOf("Kotlin", null)
for (item in listWithNulls) {
    item?.let { println(it) } // prints Kotlin and ignores null
}
```

A safe call can also be placed on the left side of an assignment. Then, if one of the receivers in the safe calls chain is `null`, the assignment is skipped and the expression on the right is not evaluated at all:

```kotlin
// If either `person` or `person.department` is null, the function is not called:
person?.department?.head = managersPool.getManager()
```

## Lambdas

```kotlin
max(strings, { a, b -> a.length < b.length })
```

上面的表达式等同于

```kotlin
fun compare(a: String, b: String): Boolean = a.length < b.length
```

### **Lambda表达式的语法**

```kotlin
val sum: (Int, Int) -> Int = { x: Int, y: Int -> x + y }
```

- lambda 表达式始终由大括号括起来。
- 完整语法形式的参数声明位于大括号内，函数类型可选。
- 函数主体在 -> 之后。
- 如果 lambda 的推断返回类型不是 Unit，则 lambda 函数主体中的最后一个（或可能是单个）表达式将被视为返回值。

如果所有的可选项都不启用，那么lambda表达式会看起来像下面这样：

```kotlin
val sum = { x: Int, y: Int -> x + y }
```

### Passing trailing lambdas﻿

根据 Kotlin 约定，如果函数的最后一个参数是函数，那么作为相应参数传递的 lambda 表达式可以放在括号之外：

```kotlin
val product = items.fold(1) { acc, e -> acc * e }
```

如果 lambda 是该调用中的唯一参数，则可以完全省略括号：

```kotlin
run { println("...") }
```

### it：单个参数的隐式名称

lambda 表达式只有一个参数是很常见的。

如果编译器可以在没有任何参数的情况下解析签名，则不需要声明该参数，并且可以省略 ->。该参数将在名称 it 下隐式声明：

```kotlin
ints.filter { it > 0 } // this literal is of type '(it: Int) -> Boolean'
```

### lambda的返回值

您可以使用限定的返回语法从 lambda 显式返回值。否则，将隐式返回最后一个表达式的值。

因此，以下两个代码段是等效的：

```kotlin
ints.filter {
    val shouldFilter = it > 0
    shouldFilter
}

ints.filter {
    val shouldFilter = it > 0
    return@filter shouldFilter
}
```

此约定以及将 lambda 表达式传递到括号外，允许使用 LINQ 样式（链式调用）的代码：

```kotlin
strings.filter { it.length == 5 }.sortedBy { it }.map { it.uppercase() }
```

### 未使用变量的下划线

如果未使用 lambda 参数，则可以放置下划线而不是其名称：

```kotlin
map.forEach { (_, value) -> println("$value!") }
```

### Destructuring in lambdas﻿

Destructuring in lambdas is described as a part of [destructuring declarations](https://kotlinlang.org/docs/destructuring-declarations.html#destructuring-in-lambdas).

### 匿名函数

上面的 lambda 表达式语法缺少一件事 - 指定函数返回类型的能力。在大多数情况下，这是不必要的，因为可以自动推断返回类型。但是，如果确实需要显式指定它，则可以使用替代语法：匿名函数。

```kotlin
fun(x: Int, y: Int): Int = x + y
```

匿名函数看起来非常类似于常规函数声明，只是省略了它的名称。它的主体可以是表达式（如上所示）或块：

```kotlin
fun(x: Int, y: Int): Int {
    return x + y
}
```

参数和返回类型的指定方式与常规函数的指定方式相同，但如果可以从上下文中推断参数类型，则可以省略这些参数类型：

```kotlin
ints.filter(fun(item) = item > 0)
```

匿名函数的返回类型推断的工作方式与普通函数类似：对于具有表达式主体的匿名函数，返回类型是自动推断的，但对于具有块体的匿名函数，必须显式指定（或假定为 Unit）。

> 将匿名函数作为参数传递时，请将它们放在括号内。允许您将函数保留在括号外的速记语法仅适用于 lambda 表达式。

lambda 表达式和匿名函数之间的另一个区别是非本地返回的行为。不带标签的 return 语句始终从使用 fun 关键字声明的函数返回。这意味着 lambda 表达式中的返回将从封闭函数返回，而匿名函数内的返回将从匿名函数本身返回。

### 闭包

lambda 表达式或匿名函数（以及本地函数和对象表达式）可以访问其闭包，其中包括在外部作用域中声明的变量。闭包中捕获的变量可以在 lambda 中修改：

```kotlin
var sum = 0
ints.filter { it > 0 }.forEach {
    sum += it
}
print(sum)
```

### 带接收器的函数文本

带有接收器的函数类型，例如 A.（B） -> C，可以使用特殊形式的函数文字 - 带有接收器的函数文字进行实例化。

如上所述，Kotlin 提供了在提供接收器对象的同时调用带有接收器的函数类型的实例的能力。

在函数文本的主体中，传递给调用的接收器对象成为隐式 this，以便无需任何其他限定符即可访问该接收器对象的成员，或使用 this 表达式访问接收器对象。

此行为类似于扩展函数的行为，扩展函数还允许您访问函数体内接收器对象的成员。

下面是一个带有接收器及其类型的函数文本的示例，其中在接收器对象上调用 plus：

```kotlin
val sum: Int.(Int) -> Int = { other -> plus(other) }
```

匿名函数语法允许您直接指定函数文本的接收器类型。如果您需要使用 receiver 声明函数类型的变量，然后稍后使用它，这会很有用。

```kotlin
val sum = fun Int.(other: Int): Int = this + other
```

当可以从上下文推断接收器类型时，Lambda 表达式可以用作带有接收器的函数文本。它们使用的最重要示例之一是类型安全的构建器：

```kotlin
class HTML {
    fun body() { ... }
}

fun html(init: HTML.() -> Unit): HTML {
    val html = HTML()  // create the receiver object
    html.init()        // pass the receiver object to the lambda
    return html
}

html {       // lambda with receiver begins here
    body()   // calling a method on the receiver object
}
```

## Operator overloading﻿

Kotlin allows you to provide custom implementations for the predefined set of operators on types. These operators have predefined symbolic representation (like `+` or `*`) and precedence. To implement an operator, provide a [member function](https://kotlinlang.org/docs/functions.html#member-functions) or an [extension function](https://kotlinlang.org/docs/extensions.html) with a specific name for the corresponding type. This type becomes the left-hand side type for binary operations and the argument type for the unary ones.

To overload an operator, mark the corresponding function with the `operator` modifier:

```kotlin
interface IndexedContainer {
    operator fun get(index: Int)
}
```



When [overriding](https://kotlinlang.org/docs/inheritance.html#overriding-methods) your operator overloads, you can omit `operator`:

```kotlin
class OrdersList: IndexedContainer {
    override fun get(index: Int) { /*...*/ }
}
```



### Unary operations﻿

#### Unary prefix operators﻿

| Expression | Translated to    |
| ---------- | ---------------- |
| `+a`       | `a.unaryPlus()`  |
| `-a`       | `a.unaryMinus()` |
| `!a`       | `a.not()`        |

This table says that when the compiler processes, for example, an expression `+a`, it performs the following steps:

- Determines the type of `a`, let it be `T`.
- Looks up a function `unaryPlus()` with the `operator` modifier and no parameters for the receiver `T`, that means a member function or an extension function.
- If the function is absent or ambiguous, it is a compilation error.
- If the function is present and its return type is `R`, the expression `+a` has type `R`.



> These operations, as well as all the others, are optimized for [basic types](https://kotlinlang.org/docs/basic-types.html) and do not introduce overhead of function calls for them.

As an example, here's how you can overload the unary minus operator:

```kotlin
data class Point(val x: Int, val y: Int)

operator fun Point.unaryMinus() = Point(-x, -y)

val point = Point(10, 20)

fun main() {
   println(-point)  // prints "Point(x=-10, y=-20)"
}
```



#### Increments and decrements﻿

| Expression | Translated to         |
| ---------- | --------------------- |
| `a++`      | `a.inc()` + see below |
| `a--`      | `a.dec()` + see below |

The `inc()` and `dec()` functions must return a value, which will be assigned to the variable on which the `++` or `--` operation was used. They shouldn't mutate the object on which the `inc` or `dec` was invoked.

The compiler performs the following steps for resolution of an operator in the *postfix* form, for example `a++`:

- Determines the type of `a`, let it be `T`.
- Looks up a function `inc()` with the `operator` modifier and no parameters, applicable to the receiver of type `T`.
- Checks that the return type of the function is a subtype of `T`.

The effect of computing the expression is:

- Store the initial value of `a` to a temporary storage `a0`.
- Assign the result of `a0.inc()` to `a`.
- Return `a0` as the result of the expression.

For `a--` the steps are completely analogous.

For the *prefix* forms `++a` and `--a` resolution works the same way, and the effect is:

- Assign the result of `a.inc()` to `a`.
- Return the new value of `a` as a result of the expression.

### Binary operations﻿

#### Arithmetic operators﻿

| Expression | Translated to  |
| ---------- | -------------- |
| `a + b`    | `a.plus(b)`    |
| `a - b`    | `a.minus(b)`   |
| `a * b`    | `a.times(b)`   |
| `a / b`    | `a.div(b)`     |
| `a % b`    | `a.rem(b)`     |
| `a..b`     | `a.rangeTo(b)` |

For the operations in this table, the compiler just resolves the expression in the *Translated to* column.

Below is an example `Counter` class that starts at a given value and can be incremented using the overloaded `+` operator:

```kotlin
data class Counter(val dayIndex: Int) {
    operator fun plus(increment: Int): Counter {
        return Counter(dayIndex + increment)
    }
}
```



#### in operator﻿

| Expression | Translated to    |
| ---------- | ---------------- |
| `a in b`   | `b.contains(a)`  |
| `a !in b`  | `!b.contains(a)` |

For `in` and `!in` the procedure is the same, but the order of arguments is reversed.

#### Indexed access operator﻿

| Expression             | Translated to             |
| ---------------------- | ------------------------- |
| `a[i]`                 | `a.get(i)`                |
| `a[i, j]`              | `a.get(i, j)`             |
| `a[i_1, ..., i_n]`     | `a.get(i_1, ..., i_n)`    |
| `a[i] = b`             | `a.set(i, b)`             |
| `a[i, j] = b`          | `a.set(i, j, b)`          |
| `a[i_1, ..., i_n] = b` | `a.set(i_1, ..., i_n, b)` |

Square brackets are translated to calls to `get` and `set` with appropriate numbers of arguments.

#### invoke operator﻿

| Expression         | Translated to             |
| ------------------ | ------------------------- |
| `a()`              | `a.invoke()`              |
| `a(i)`             | `a.invoke(i)`             |
| `a(i, j)`          | `a.invoke(i, j)`          |
| `a(i_1, ..., i_n)` | `a.invoke(i_1, ..., i_n)` |

Parentheses are translated to calls to `invoke` with appropriate number of arguments.

#### Augmented assignments﻿

| Expression | Translated to      |
| ---------- | ------------------ |
| `a += b`   | `a.plusAssign(b)`  |
| `a -= b`   | `a.minusAssign(b)` |
| `a *= b`   | `a.timesAssign(b)` |
| `a /= b`   | `a.divAssign(b)`   |
| `a %= b`   | `a.remAssign(b)`   |

For the assignment operations, for example `a += b`, the compiler performs the following steps:

- If the function from the right column is available:
  - If the corresponding binary function (that means `plus()` for `plusAssign()`) is available too, `a` is a mutable variable, and the return type of `plus` is a subtype of the type of `a`, report an error (ambiguity).
  - Make sure its return type is `Unit`, and report an error otherwise.
  - Generate code for `a.plusAssign(b)`.
- Otherwise, try to generate code for `a = a + b` (this includes a type check: the type of `a + b` must be a subtype of `a`).

> ### 
>
> 
>
> Assignments are *NOT* expressions in Kotlin.

#### Equality and inequality operators﻿

| Expression | Translated to                     |
| ---------- | --------------------------------- |
| `a == b`   | `a?.equals(b) ?: (b === null)`    |
| `a != b`   | `!(a?.equals(b) ?: (b === null))` |

These operators only work with the function [`equals(other: Any?): Boolean`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/equals.html), which can be overridden to provide custom equality check implementation. Any other function with the same name (like `equals(other: Foo)`) will not be called.

> ### 
>
> 
>
> `===` and `!==` (identity checks) are not overloadable, so no conventions exist for them.

The `==` operation is special: it is translated to a complex expression that screens for `null`'s. `null == null` is always true, and `x == null` for a non-null `x` is always false and won't invoke `x.equals()`.

#### Comparison operators﻿

| Expression | Translated to         |
| ---------- | --------------------- |
| `a > b`    | `a.compareTo(b) > 0`  |
| `a < b`    | `a.compareTo(b) < 0`  |
| `a >= b`   | `a.compareTo(b) >= 0` |
| `a <= b`   | `a.compareTo(b) <= 0` |

All comparisons are translated into calls to `compareTo`, that is required to return `Int`.

#### Property delegation operators﻿

`provideDelegate`, `getValue` and `setValue` operator functions are described in [Delegated properties](https://kotlinlang.org/docs/delegated-properties.html).

### Infix calls for named functions﻿

You can simulate custom infix operations by using [infix function calls](https://kotlinlang.org/docs/functions.html#infix-notation).

# 05_StandardLibrary

## Collections

### Ranges and progressions﻿

Kotlin lets you easily create ranges of values using the [`rangeTo()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/range-to.html) function from the `kotlin.ranges` package and its operator form `..`. Usually, `rangeTo()` is complemented by `in` or `!in` functions.

```kotlin
if (i in 1..4) { // equivalent of i >= 1 && i <= 4
    print(i)
}
```

Integral type ranges ([`IntRange`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-int-range/index.html), [`LongRange`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-long-range/index.html), [`CharRange`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-char-range/index.html)) have an extra feature: they can be iterated over. These ranges are also [progressions](https://en.wikipedia.org/wiki/Arithmetic_progression) of the corresponding integral types.

Such ranges are generally used for iteration in `for` loops.

```kotlin
for (i in 1..4) print(i)
```

To iterate numbers in reverse order, use the [`downTo`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/down-to.html) function instead of `..`.

```kotlin
for (i in 4 downTo 1) print(i)
```

It is also possible to iterate over numbers with an arbitrary step (not necessarily 1). This is done via the [`step`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/step.html) function.

```kotlin
for (i in 1..8 step 2) print(i)
println()
for (i in 8 downTo 1 step 2) print(i)
```

To iterate a number range which does not include its end element, use the [`until`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/until.html) function:

```kotlin
for (i in 1 until 10) {       // i in 1 until 10, excluding 10
    print(i)
}
```

#### Range﻿

A range defines a closed interval in the mathematical sense: it is defined by its two endpoint values which are both included in the range. Ranges are defined for comparable types: having an order, you can define whether an arbitrary instance is in the range between two given instances.

The main operation on ranges is `contains`, which is usually used in the form of `in` and `!in` operators.

To create a range for your class, call the `rangeTo()` function on the range start value and provide the end value as an argument. `rangeTo()` is often called in its operator form `..`.

```kotlin
val versionRange = Version(1, 11)..Version(1, 30)
println(Version(0, 9) in versionRange)
println(Version(1, 20) in versionRange)
```

#### Progression﻿

As shown in the examples above, the ranges of integral types, such as `Int`, `Long`, and `Char`, can be treated as [arithmetic progressions](https://en.wikipedia.org/wiki/Arithmetic_progression) of them. In Kotlin, these progressions are defined by special types: [`IntProgression`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-int-progression/index.html), [`LongProgression`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-long-progression/index.html), and [`CharProgression`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-char-progression/index.html).

Progressions have three essential properties: the `first` element, the `last` element, and a non-zero `step`. The first element is `first`, subsequent elements are the previous element plus a `step`. Iteration over a progression with a positive step is equivalent to an indexed `for` loop in Java/JavaScript.

```java
for (int i = first; i <= last; i += step) {
  // ...
}
```

When you create a progression implicitly by iterating a range, this progression's `first` and `last` elements are the range's endpoints, and the `step` is 1.

```kotlin
for (i in 1..10) print(i)
```

To define a custom progression step, use the `step` function on a range.

```kotlin
for (i in 1..8 step 2) print(i)
```

The `last` element of the progression is calculated this way:

- For a positive step: the maximum value not greater than the end value such that `(last - first) % step == 0`.
- For a negative step: the minimum value not less than the end value such that `(last - first) % step == 0`.

Thus, the `last` element is not always the same as the specified end value.

```kotlin
for (i in 1..9 step 3) print(i) // the last element is 7
```

To create a progression for iterating in reverse order, use `downTo` instead of `..` when defining the range for it.

```kotlin
for (i in 4 downTo 1) print(i)
```

If you already have a progression, you can iterate it in reverse order with the [`reversed`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/reversed.html) function:

```kotlin
for (i in (1..4).reversed()) print(i)
```

Progressions implement `Iterable<N>`, where `N` is `Int`, `Long`, or `Char` respectively, so you can use them in various [collection functions](https://kotlinlang.org/docs/collection-operations.html) like `map`, `filter`, and other.

```kotlin
println((1..10).filter { it % 2 == 0 })
```

