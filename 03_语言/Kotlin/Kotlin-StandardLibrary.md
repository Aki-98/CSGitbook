# Collections

## Overview

The Kotlin Standard Library provides a comprehensive set of tools for managing *collections* – groups of a variable number of items (possibly zero) that are significant to the problem being solved and are commonly operated on.

Collections are a common concept for most programming languages, so if you're familiar with, for example, Java or Python collections, you can skip this introduction and proceed to the detailed sections.

A collection usually contains a number of objects (this number may also be zero) of the same type. Objects in a collection are called *elements* or *items*. For example, all the students in a department form a collection that can be used to calculate their average age.

The following collection types are relevant for Kotlin:

- *List* is an ordered collection with access to elements by indices – integer numbers that reflect their position. Elements can occur more than once in a list. An example of a list is a telephone number: it's a group of digits, their order is important, and they can repeat.
- *Set* is a collection of unique elements. It reflects the mathematical abstraction of set: a group of objects without repetitions. Generally, the order of set elements has no significance. For example, the numbers on lottery tickets form a set: they are unique, and their order is not important.
- *Map* (or *dictionary*) is a set of key-value pairs. Keys are unique, and each of them maps to exactly one value. The values can be duplicates. Maps are useful for storing logical connections between objects, for example, an employee's ID and their position.

Kotlin lets you manipulate collections independently of the exact type of objects stored in them. In other words, you add a `String` to a list of `String`s the same way as you would do with `Int`s or a user-defined class. So, the Kotlin Standard Library offers generic interfaces, classes, and functions for creating, populating, and managing collections of any type.

The collection interfaces and related functions are located in the `kotlin.collections` package. Let's get an overview of its contents.

### Collection types﻿

The Kotlin Standard Library provides implementations for basic collection types: sets, lists, and maps. A pair of interfaces represent each collection type:

- A *read-only* interface that provides operations for accessing collection elements.
- A *mutable* interface that extends the corresponding read-only interface with write operations: adding, removing, and updating its elements.

Note that altering a mutable collection doesn't require it to be a [`var`](https://kotlinlang.org/docs/basic-syntax.html#variables): write operations modify the same mutable collection object, so the reference doesn't change. Although, if you try to reassign a `val` collection, you'll get a compilation error.

```kotlin
val numbers = mutableListOf("one", "two", "three", "four")
numbers.add("five")   // this is OK
println(numbers)
//numbers = mutableListOf("six", "seven")      // compilation error
```

The read-only collection types are [covariant](https://kotlinlang.org/docs/generics.html#variance). This means that, if a `Rectangle` class inherits from `Shape`, you can use a `List<Rectangle>` anywhere the `List<Shape>` is required. In other words, the collection types have the same subtyping relationship as the element types. Maps are covariant on the value type, but not on the key type.

In turn, mutable collections aren't covariant; otherwise, this would lead to runtime failures. If `MutableList<Rectangle>` was a subtype of `MutableList<Shape>`, you could insert other `Shape` inheritors (for example, `Circle`) into it, thus violating its `Rectangle` type argument.

Below is a diagram of the Kotlin collection interfaces:

![Collection interfaces hierarchy](Kotlin-StandardLibrary_imgs\dwTVGQn1CIR.png)

Let's walk through the interfaces and their implementations. To learn about `Collection`, read the section below. To learn about `List`, `Set`, and `Map`, you can either read the corresponding sections or watch a video by Sebastian Aigner, Kotlin Developer Advocate:

#### Collection﻿

[`Collection`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html) is the root of the collection hierarchy. This interface represents the common behavior of a read-only collection: retrieving size, checking item membership, and so on. `Collection` inherits from the `Iterable<T>` interface that defines the operations for iterating elements. You can use `Collection` as a parameter of a function that applies to different collection types. For more specific cases, use the `Collection`'s inheritors: [`List`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html) and [`Set`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html).

```kotlin
fun printAll(strings: Collection<String>) {
    for(s in strings) print("$s ")
    println()
}
    
fun main() {
    val stringList = listOf("one", "two", "one")
    printAll(stringList)
    
    val stringSet = setOf("one", "two", "three")
    printAll(stringSet)
}
```

[`MutableCollection`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html) is a `Collection` with write operations, such as `add` and `remove`.

```kotlin
fun List<String>.getShortWordsTo(shortWords: MutableList<String>, maxLength: Int) {
    this.filterTo(shortWords) { it.length <= maxLength }
    // throwing away the articles
    val articles = setOf("a", "A", "an", "An", "the", "The")
    shortWords -= articles
}

fun main() {
    val words = "A long time ago in a galaxy far far away".split(" ")
    val shortWords = mutableListOf<String>()
    words.getShortWordsTo(shortWords, 3)
    println(shortWords)
}
```

#### List﻿

[`List`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html) stores elements in a specified order and provides indexed access to them. Indices start from zero – the index of the first element – and go to `lastIndex` which is the `(list.size - 1)`.

```kotlin
val numbers = listOf("one", "two", "three", "four")
println("Number of elements: ${numbers.size}")
println("Third element: ${numbers.get(2)}")
println("Fourth element: ${numbers[3]}")
println("Index of element \"two\" ${numbers.indexOf("two")}")
```

List elements (including nulls) can duplicate: a list can contain any number of equal objects or occurrences of a single object. Two lists are considered equal if they have the same sizes and [structurally equal](https://kotlinlang.org/docs/equality.html#structural-equality) elements at the same positions.

```kotlin
val bob = Person("Bob", 31)
val people = listOf(Person("Adam", 20), bob, bob)
val people2 = listOf(Person("Adam", 20), Person("Bob", 31), bob)
println(people == people2)
bob.age = 32
println(people == people2)
```

[`MutableList`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html) is a `List` with list-specific write operations, for example, to add or remove an element at a specific position.

```kotlin
val numbers = mutableListOf(1, 2, 3, 4)
numbers.add(5)
numbers.removeAt(1)
numbers[0] = 0
numbers.shuffle()
println(numbers)
```

As you see, in some aspects lists are very similar to arrays. However, there is one important difference: an array's size is defined upon initialization and is never changed; in turn, a list doesn't have a predefined size; a list's size can be changed as a result of write operations: adding, updating, or removing elements.

In Kotlin, the default implementation of `MutableList` is [`ArrayList`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-array-list/index.html) which you can think of as a resizable array.

#### Set﻿

[`Set`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html) stores unique elements; their order is generally undefined. `null` elements are unique as well: a `Set` can contain only one `null`. Two sets are equal if they have the same size, and for each element of a set there is an equal element in the other set.

```kotlin
val numbers = setOf(1, 2, 3, 4)
println("Number of elements: ${numbers.size}")
if (numbers.contains(1)) println("1 is in the set")

val numbersBackwards = setOf(4, 3, 2, 1)
println("The sets are equal: ${numbers == numbersBackwards}")
```

[`MutableSet`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html) is a `Set` with write operations from `MutableCollection`.

The default implementation of `MutableSet` – [`LinkedHashSet`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-linked-hash-set/index.html) – preserves the order of elements insertion. Hence, the functions that rely on the order, such as `first()` or `last()`, return predictable results on such sets.

```kotlin
val numbers = setOf(1, 2, 3, 4)  // LinkedHashSet is the default implementation
val numbersBackwards = setOf(4, 3, 2, 1)

println(numbers.first() == numbersBackwards.first())
println(numbers.first() == numbersBackwards.last())
```

An alternative implementation – [`HashSet`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-hash-set/index.html) – says nothing about the elements order, so calling such functions on it returns unpredictable results. However, `HashSet` requires less memory to store the same number of elements.

#### Map﻿

[`Map`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html) is not an inheritor of the `Collection` interface; however, it's a Kotlin collection type as well. A `Map` stores *key-value* pairs (or *entries*); keys are unique, but different keys can be paired with equal values. The `Map` interface provides specific functions, such as access to value by key, searching keys and values, and so on.

```kotlin
val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key4" to 1)

println("All keys: ${numbersMap.keys}")
println("All values: ${numbersMap.values}")
if ("key2" in numbersMap) println("Value by key \"key2\": ${numbersMap["key2"]}")    
if (1 in numbersMap.values) println("The value 1 is in the map")
if (numbersMap.containsValue(1)) println("The value 1 is in the map") // same as previous
```

Two maps containing the equal pairs are equal regardless of the pair order.

```kotlin
val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key4" to 1)    
val anotherMap = mapOf("key2" to 2, "key1" to 1, "key4" to 1, "key3" to 3)

println("The maps are equal: ${numbersMap == anotherMap}")
```

[`MutableMap`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html) is a `Map` with map write operations, for example, you can add a new key-value pair or update the value associated with the given key.

```kotlin
val numbersMap = mutableMapOf("one" to 1, "two" to 2)
numbersMap.put("three", 3)
numbersMap["one"] = 11

println(numbersMap)
```

The default implementation of `MutableMap` – [`LinkedHashMap`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-linked-hash-map/index.html) – preserves the order of elements insertion when iterating the map. In turn, an alternative implementation – [`HashMap`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-hash-map/index.html) – says nothing about the elements order.

### Collection operations overview﻿

The Kotlin standard library offers a broad variety of functions for performing operations on collections. This includes simple operations, such as getting or adding elements, as well as more complex ones including search, sorting, filtering, transformations, and so on.

#### Extension and member functions﻿

Collection operations are declared in the standard library in two ways: [member functions](https://kotlinlang.org/docs/classes.html#class-members) of collection interfaces and [extension functions](https://kotlinlang.org/docs/extensions.html#extension-functions).

Member functions define operations that are essential for a collection type. For example, [`Collection`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html) contains the function [`isEmpty()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/is-empty.html) for checking its emptiness; [`List`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html) contains [`get()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/get.html) for index access to elements, and so on.

When you create your own implementations of collection interfaces, you must implement their member functions. To make the creation of new implementations easier, use the skeletal implementations of collection interfaces from the standard library: [`AbstractCollection`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-abstract-collection/index.html), [`AbstractList`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-abstract-list/index.html), [`AbstractSet`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-abstract-set/index.html), [`AbstractMap`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-abstract-map/index.html), and their mutable counterparts.

Other collection operations are declared as extension functions. These are filtering, transformation, ordering, and other collection processing functions.

#### Common operations﻿

Common operations are available for both [read-only and mutable collections](https://kotlinlang.org/docs/collections-overview.html#collection-types). Common operations fall into these groups:

- [Transformations](https://kotlinlang.org/docs/collection-transformations.html)
- [Filtering](https://kotlinlang.org/docs/collection-filtering.html)
- [`plus` and `minus` operators](https://kotlinlang.org/docs/collection-plus-minus.html)
- [Grouping](https://kotlinlang.org/docs/collection-grouping.html)
- [Retrieving collection parts](https://kotlinlang.org/docs/collection-parts.html)
- [Retrieving single elements](https://kotlinlang.org/docs/collection-elements.html)
- [Ordering](https://kotlinlang.org/docs/collection-ordering.html)
- [Aggregate operations](https://kotlinlang.org/docs/collection-aggregate.html)

Operations described on these pages return their results without affecting the original collection. For example, a filtering operation produces a *new collection* that contains all the elements matching the filtering predicate. Results of such operations should be either stored in variables, or used in some other way, for example, passed in other functions.

```kotlin
val numbers = listOf("one", "two", "three", "four")  
numbers.filter { it.length > 3 }  // nothing happens with `numbers`, result is lost
println("numbers are still $numbers")
val longerThan3 = numbers.filter { it.length > 3 } // result is stored in `longerThan3`
println("numbers longer than 3 chars are $longerThan3")
```

For certain collection operations, there is an option to specify the *destination* object. Destination is a mutable collection to which the function appends its resulting items instead of returning them in a new object. For performing operations with destinations, there are separate functions with the `To` postfix in their names, for example, [`filterTo()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter-to.html) instead of [`filter()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter.html) or [`associateTo()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate-to.html) instead of [`associate()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate.html). These functions take the destination collection as an additional parameter.

```kotlin
val numbers = listOf("one", "two", "three", "four")
val filterResults = mutableListOf<String>()  //destination object
numbers.filterTo(filterResults) { it.length > 3 }
numbers.filterIndexedTo(filterResults) { index, _ -> index == 0 }
println(filterResults) // contains results of both operations
```

For convenience, these functions return the destination collection back, so you can create it right in the corresponding argument of the function call:

```kotlin
// filter numbers right into a new hash set, 
// thus eliminating duplicates in the result
val result = numbers.mapTo(HashSet()) { it.length }
println("distinct item lengths are $result")
```

Functions with destination are available for filtering, association, grouping, flattening, and other operations. For the complete list of destination operations see the [Kotlin collections reference](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/index.html).

#### Write operations﻿

For mutable collections, there are also *write operations* that change the collection state. Such operations include adding, removing, and updating elements. Write operations are listed in the [Write operations](https://kotlinlang.org/docs/collection-write.html) and corresponding sections of [List-specific operations](https://kotlinlang.org/docs/list-operations.html#list-write-operations) and [Map specific operations](https://kotlinlang.org/docs/map-operations.html#map-write-operations).

For certain operations, there are pairs of functions for performing the same operation: one applies the operation in-place and the other returns the result as a separate collection. For example, [`sort()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sort.html) sorts a mutable collection in-place, so its state changes; [`sorted()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sorted.html) creates a new collection that contains the same elements in the sorted order.

```kotlin
val numbers = mutableListOf("one", "two", "three", "four")
val sortedNumbers = numbers.sorted()
println(numbers == sortedNumbers)  // false
numbers.sort()
println(numbers == sortedNumbers)  // true
```

### Collection transformation operations﻿

The Kotlin standard library provides a set of extension functions for collection *transformations*. These functions build new collections from existing ones based on the transformation rules provided. In this page, we'll give an overview of the available collection transformation functions.

#### Map﻿

The *mapping* transformation creates a collection from the results of a function on the elements of another collection. The basic mapping function is [`map()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map.html). It applies the given lambda function to each subsequent element and returns the list of the lambda results. The order of results is the same as the original order of elements. To apply a transformation that additionally uses the element index as an argument, use [`mapIndexed()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map-indexed.html).

```kotlin
val numbers = setOf(1, 2, 3)
println(numbers.map { it * 3 })
println(numbers.mapIndexed { idx, value -> value * idx })
```

If the transformation produces `null` on certain elements, you can filter out the `null`s from the result collection by calling the [`mapNotNull()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map-not-null.html) function instead of `map()`, or [`mapIndexedNotNull()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map-indexed-not-null.html) instead of `mapIndexed()`.

```kotlin
val numbers = setOf(1, 2, 3)
println(numbers.mapNotNull { if ( it == 2) null else it * 3 })
println(numbers.mapIndexedNotNull { idx, value -> if (idx == 0) null else value * idx })
```

When transforming maps, you have two options: transform keys leaving values unchanged and vice versa. To apply a given transformation to keys, use [`mapKeys()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map-keys.html); in turn, [`mapValues()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map-values.html) transforms values. Both functions use the transformations that take a map entry as an argument, so you can operate both its key and value.

```kotlin
val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key11" to 11)
println(numbersMap.mapKeys { it.key.uppercase() })
println(numbersMap.mapValues { it.value + it.key.length })
```

#### Zip﻿

*Zipping* transformation is building pairs from elements with the same positions in both collections. In the Kotlin standard library, this is done by the [`zip()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/zip.html) extension function.

When called on a collection or an array with another collection (or array) as an argument, `zip()` returns the `List` of `Pair` objects. The elements of the receiver collection are the first elements in these pairs.

If the collections have different sizes, the result of the `zip()` is the smaller size; the last elements of the larger collection are not included in the result.

`zip()` can also be called in the infix form `a zip b`.

```kotlin
val colors = listOf("red", "brown", "grey")
val animals = listOf("fox", "bear", "wolf")
println(colors zip animals)

val twoAnimals = listOf("fox", "bear")
println(colors.zip(twoAnimals))

--------------------------------------------------------------------

[(red, fox), (brown, bear), (grey, wolf)]
[(red, fox), (brown, bear)]
```

You can also call `zip()` with a transformation function that takes two parameters: the receiver element and the argument element. In this case, the result `List` contains the return values of the transformation function called on pairs of the receiver and the argument elements with the same positions.

```kotlin
val colors = listOf("red", "brown", "grey")
val animals = listOf("fox", "bear", "wolf")

println(colors.zip(animals) { color, animal -> "The ${animal.replaceFirstChar { it.uppercase() }} is $color"})

-----------------------------------------------------------------

[The Fox is red, The Bear is brown, The Wolf is grey]
```

When you have a `List` of `Pair`s, you can do the reverse transformation – *unzipping* – that builds two lists from these pairs:

- The first list contains the first elements of each `Pair` in the original list.
- The second list contains the second elements.

To unzip a list of pairs, call [`unzip()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/unzip.html).

```kotlin
val numberPairs = listOf("one" to 1, "two" to 2, "three" to 3, "four" to 4)
println(numberPairs.unzip())

---------------------------------------------------------------

([one, two, three, four], [1, 2, 3, 4])
```

#### Associate﻿

*Association* transformations allow building maps from the collection elements and certain values associated with them. In different association types, the elements can be either keys or values in the association map.

The basic association function [`associateWith()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate-with.html) creates a `Map` in which the elements of the original collection are keys, and values are produced from them by the given transformation function. If two elements are equal, only the last one remains in the map.

```kotlin
val numbers = listOf("one", "two", "three", "four")
println(numbers.associateWith { it.length })

---------------------------------------------------
{one=3, two=3, three=5, four=4}
```

For building maps with collection elements as values, there is the function [`associateBy()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate-by.html). It takes a function that returns a key based on an element's value. If two elements' keys are equal, only the last one remains in the map.

`associateBy()` can also be called with a value transformation function.

```kotlin
val numbers = listOf("one", "two", "three", "four")

println(numbers.associateBy { it.first().uppercaseChar() })
println(numbers.associateBy(keySelector = { it.first().uppercaseChar() }, valueTransform = { it.length }))

-------------------------------------------------------------
{O=one, T=three, F=four}
{O=3, T=5, F=4}
```

Another way to build maps in which both keys and values are somehow produced from collection elements is the function [`associate()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate.html). It takes a lambda function that returns a `Pair`: the key and the value of the corresponding map entry.

Note that `associate()` produces short-living `Pair` objects which may affect the performance. Thus, `associate()` should be used when the performance isn't critical or it's more preferable than other options.

An example of the latter is when a key and the corresponding value are produced from an element together.

```kotlin
val names = listOf("Alice Adams", "Brian Brown", "Clara Campbell")
println(names.associate { name -> parseFullName(name).let { it.lastName to it.firstName } })  

-----------------------------------------------------------------
{Adams=Alice, Brown=Brian, Campbell=Clara}
```

Here we call a transform function on an element first, and then build a pair from the properties of that function's result.

#### Flatten﻿

If you operate nested collections, you may find the standard library functions that provide flat access to nested collection elements useful.

The first function is [`flatten()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/flatten.html). You can call it on a collection of collections, for example, a `List` of `Set`s. The function returns a single `List` of all the elements of the nested collections.

```kotlin
val numberSets = listOf(setOf(1, 2, 3), setOf(4, 5, 6), setOf(1, 2))
println(numberSets.flatten())

----------------------------------------
[1, 2, 3, 4, 5, 6, 1, 2]
```

Another function – [`flatMap()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/flat-map.html) provides a flexible way to process nested collections. It takes a function that maps a collection element to another collection. As a result, `flatMap()` returns a single list of its return values on all the elements. So, `flatMap()` behaves as a subsequent call of `map()` (with a collection as a mapping result) and `flatten()`.

```kotlin
val containers = listOf(
    StringContainer(listOf("one", "two", "three")),
    StringContainer(listOf("four", "five", "six")),
    StringContainer(listOf("seven", "eight"))
)
println(containers.flatMap { it.values })
-----------------------------------------------
[one, two, three, four, five, six, seven, eight]
```

#### String representation﻿

If you need to retrieve the collection content in a readable format, use functions that transform the collections to strings: [`joinToString()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/join-to-string.html) and [`joinTo()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/join-to.html).

`joinToString()` builds a single `String` from the collection elements based on the provided arguments. `joinTo()` does the same but appends the result to the given [`Appendable`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/-appendable/index.html) object.

When called with the default arguments, the functions return the result similar to calling `toString()` on the collection: a `String` of elements' string representations separated by commas with spaces.

```kotlin
val numbers = listOf("one", "two", "three", "four")

println(numbers)         
println(numbers.joinToString())

val listString = StringBuffer("The list of numbers: ")
numbers.joinTo(listString)
println(listString)

------------------------------------------------------------
[one, two, three, four]
one, two, three, four
The list of numbers: one, two, three, four
```

To build a custom string representation, you can specify its parameters in function arguments `separator`, `prefix`, and `postfix`. The resulting string will start with the `prefix` and end with the `postfix`. The `separator` will come after each element except the last.

```kotlin
val numbers = listOf("one", "two", "three", "four")    
println(numbers.joinToString(separator = " | ", prefix = "start: ", postfix = ": end"))

-----------------------------------------------
start: one | two | three | four: end
```

For bigger collections, you may want to specify the `limit` – a number of elements that will be included into result. If the collection size exceeds the `limit`, all the other elements will be replaced with a single value of the `truncated` argument.

```kotlin
val numbers = (1..100).toList()
println(numbers.joinToString(limit = 10, truncated = "<...>"))

----------------------------------------------------------
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, <...>

```

Finally, to customize the representation of elements themselves, provide the `transform` function.

```kotlin
val numbers = listOf("one", "two", "three", "four")
println(numbers.joinToString { "Element: ${it.uppercase()}"})

--------------------------------------------------------------
Element: ONE, Element: TWO, Element: THREE, Element: FOUR
```



# Filtering collections﻿

[Edit page](https://github.com/JetBrains/kotlin-web-site/edit/master/docs/topics/collection-filtering.md)

Last modified: 15 February 2023

Filtering is one of the most popular tasks in collection processing. In Kotlin, filtering conditions are defined by *predicates* – lambda functions that take a collection element and return a boolean value: `true` means that the given element matches the predicate, `false` means the opposite.

The standard library contains a group of extension functions that let you filter collections in a single call. These functions leave the original collection unchanged, so they are available for both [mutable and read-only](https://kotlinlang.org/docs/collections-overview.html#collection-types) collections. To operate the filtering result, you should assign it to a variable or chain the functions after filtering.

## Filter by predicate﻿

The basic filtering function is [`filter()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter.html). When called with a predicate, `filter()` returns the collection elements that match it. For both `List` and `Set`, the resulting collection is a `List`, for `Map` it's a `Map` as well.

```
val numbers = listOf("one", "two", "three", "four")  
val longerThan3 = numbers.filter { it.length > 3 }
println(longerThan3)

val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key11" to 11)
val filteredMap = numbersMap.filter { (key, value) -> key.endsWith("1") && value > 10}
println(filteredMap)
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJC5EBDQwZAGgwzRAdwhKVIUQAsuMBSGUykEFFxmkVmWg2aM5Ac24AVXTjQBmASzadeADokPEZRbjIMPFFAxhg0Jz0MAD4MHwBfaloABy4CUUYiRwS3D29iSiyaez8Obh4AWRxs31xsyWkQAGsYAE8ARhkMUQgMfpNuvoAmIZGMKYme3q9Z0a9Fvv7BkGHRrYrbaqYMELDuGCgmlsFWOt4r4NDwrkjCJeV7FBhSAFpUpcC8SgPAA6tFdJ1tqQAGTQ%2BhML4pMYABkyhwwuXyhUIp2eFyuB0o6WMOhwXBcogACowcKIzFwsAgQAArHAMEmQLDZULcABq9TwciZ%2FUCAA5Av1kSB0kA%3D%3D)

Target: JVMRunning on v.1.8.10

The predicates in `filter()` can only check the values of the elements. If you want to use element positions in the filter, use [`filterIndexed()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter-indexed.html). It takes a predicate with two arguments: the index and the value of an element.

To filter collections by negative conditions, use [`filterNot()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter-not.html). It returns a list of elements for which the predicate yields `false`.

```
val numbers = listOf("one", "two", "three", "four")

val filteredIdx = numbers.filterIndexed { index, s -> (index != 0) && (s.length < 5)  }
val filteredNot = numbers.filterNot { it.length <= 3 }

println(filteredIdx)
println(filteredNot)
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJC5EBDQwZAGgwzRAdwhKVIUQAsuMBSGUykEFFxnFqtGzQbMkeRqO4woASSgAPASzacvAB0Ti7cHmiw3u5kGARRynwAtAB8GITxML4AhIIADKQAZIXpPEGMMGgA5noYADwYAKykGAC%2BdvRMGKGuBlAAchCifqwc3GU93IPDwHGi5ZU1uvWCAMxtlB0ADlwEooxEk31e3taYtDt7B4RH7tNnlK3GOjhcVTCiAAqMOKJmXFgECAAFY4BjPSBYLbObgANXGeDkQIAjEEABxBZF5ECtIA)

Target: JVMRunning on v.1.8.10

There are also functions that narrow the element type by filtering elements of a given type:

- [`filterIsInstance()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter-is-instance.html) returns collection elements of a given type. Being called on a `List<Any>`, `filterIsInstance<T>()` returns a `List<T>`, thus allowing you to call functions of the `T` type on its items.

  ```
  val numbers = listOf(null, 1, "two", 3.0, "four")
  ```

  ```
  println("All String elements in upper case:")
  ```

  ```
  numbers.filterIsInstance<String>().forEach {
  ```

  ```
      println(it.uppercase())
  ```

  ```
  }
  ```

  [Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJCrRowA0GAIwLyIUQHcIqhQGYAdAAYVyCCi6ri1WgAcuBUYyKqAgrIwBlUXbQBzDDEYYLBg0UT4CDBRra24MMBweGHgLKxpWDm4ePSQ8RlFuAEkeArQxHDQwGAAeT28fAD4SbIguAFEcMAALMlTaGlt7R0I8UT0omK54xJJLTFoAX0pKeZA5NRwuHxhRAAVGHFEkFqwEEAArHAZV8Agsa1zuADVMvAg0U8U9AA49RQMQeZAA)

  Target: JVMRunning on v.1.8.10

- [`filterNotNull()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter-not-null.html) returns all non-null elements. Being called on a `List<T?>`, `filterNotNull()` returns a `List<T: Any>`, thus allowing you to treat the elements as non-null objects.

  ```
  val numbers = listOf(null, "one", "two", null)
  ```

  ```
  numbers.filterNotNull().forEach {
  ```

  ```
      println(it.length)   // length is unavailable for nullable Strings
  ```

  ```
  }
  ```

  [Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJCrRowA0GciAhoYShUtEB3COpYpZxarVYduPAHRI8jUdwByEUfYOMSViFwCiOMAAsyY1paAAcuAlFGIjxRC0YYNABzUT9SGgB6dKEE5ICRDHQcBhscdniMJE99WVLygGVRcKSeIIwAX0pKNpA5EFEcLkSYUQAFRhxRSq4sBBAAKyKcHvAILBCbbgA1czwVWYBGCwAOC32ABhA2oA)

  Target: JVMRunning on v.1.8.10

## Partition﻿

Another filtering function – [`partition()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/partition.html) – filters a collection by a predicate and keeps the elements that don't match it in a separate list. So, you have a `Pair` of `List`s as a return value: the first list containing elements that match the predicate and the second one containing everything else from the original collection.

```
val numbers = listOf("one", "two", "three", "four")
val (match, rest) = numbers.partition { it.length > 3 }

println(match)
println(rest)
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJC5EBDQwZAGgwzRAdwhKVIUQAsuMBSGUykEFFxnFqtBs0K5RYXcoNjSg1h248AdAAccLlE8ELkyDFDfRhg0AHM9DAA%2BDABmDABfShsafy4CUUYiR2drTFo8gqLCN1EyygzjHSC4mFEABUYcUTMuLAQQACscBibILH88GK4ANR88OQGARl8ADl8lgAYQDKA%3D%3D)

Target: JVMRunning on v.1.8.10

## Test predicates﻿

Finally, there are functions that simply test a predicate against collection elements:

- [`any()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/any.html) returns `true` if at least one element matches the given predicate.
- [`none()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/none.html) returns `true` if none of the elements match the given predicate.
- [`all()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/all.html) returns `true` if all elements match the given predicate. Note that `all()` returns `true` when called with any valid predicate on an empty collection. Such behavior is known in logic as *[vacuous truth](https://en.wikipedia.org/wiki/Vacuous_truth)*.

```
val numbers = listOf("one", "two", "three", "four")

println(numbers.any { it.endsWith("e") })
println(numbers.none { it.endsWith("a") })
println(numbers.all { it.endsWith("e") })

println(emptyList<Int>().all { it > 5 })   // vacuous truth
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJC5EBDQwZAGgwzRAdwhKVIUQAsuMBSGUykEFFxnFK1WgAcuBUYyKsO3HgDocaAJ5kMPFFPGDQoHgB1IN1pECNSAF9rTHtHNGdXNk5eTzQ5GACgkLDI6NicKwwk2xoHJxdCN2yvJmZgQODQ8Ki9WPiq5JqMOvSGmCw7UV8AGRFRAB4ASXSAPhJvRjaOjBWMAFYB2gB6I%2FocMBRzPlEuFD0bNATjHRwuAHMYUQAFRhxRMy4WAQIAAVjgGM9IBM8IxuAA1Dx4OTAgCMngAHJ4UQAGEAJIA%3D)

Target: JVMRunning on v.1.8.10

`any()` and `none()` can also be used without a predicate: in this case they just check the collection emptiness. `any()` returns `true` if there are elements and `false` if there aren't; `none()` does the opposite.

```
val numbers = listOf("one", "two", "three", "four")
val empty = emptyList<String>()

println(numbers.any())
println(empty.any())

println(numbers.none())
println(empty.none())
```

[Open in Playground →](https://play.kotlinlang.org/editor/v1/N4Igxg9gJgpiBcIBmBXAdgAgLYEMCWaAFAJQbAA6alGNGAbjgDYZopYBGMATgM4YC8GRnh4AXAPJJC5EBDQwZAGgwzRAdwhKVIUQAsuMBSGUykEFFxnFqtBsxhYADqICeAjA%2BcuAMiNEAeAGVRLgIAcwA%2BEkobGkdQtFFGIlYObh4AOhw0FxJrTFp4giSiT1csnLzYlQK4hJLCVM5eDLQ5GCrajCLE5MIyl1b2zsoAX2MdHC4wmFEABUYcUTMuLAQQACscBgnIJzxGbgA1dLw5dYBGDIAODIuABhBRoA)

### Ordering﻿

The order of elements is an important aspect of certain collection types. For example, two lists of the same elements are not equal if their elements are ordered differently.

In Kotlin, the orders of objects can be defined in several ways.

First, there is *natural* order. It is defined for implementations of the [`Comparable`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-comparable/index.html) interface. Natural order is used for sorting them when no other order is specified.

Most built-in types are comparable:

- Numeric types use the traditional numerical order: `1` is greater than `0`; `-3.4f` is greater than `-5f`, and so on.
- `Char` and `String` use the [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order): `b` is greater than `a`; `world` is greater than `hello`.

To define a natural order for a user-defined type, make the type an implementer of `Comparable`. This requires implementing the `compareTo()` function. `compareTo()` must take another object of the same type as an argument and return an integer value showing which object is greater:

- Positive values show that the receiver object is greater.
- Negative values show that it's less than the argument.
- Zero shows that the objects are equal.

Below is a class for ordering versions that consist of the major and the minor part.

```kotlin
class Version(val major: Int, val minor: Int): Comparable<Version> {
    override fun compareTo(other: Version): Int = when {
        this.major != other.major -> this.major compareTo other.major // compareTo() in the infix form 
        this.minor != other.minor -> this.minor compareTo other.minor
        else -> 0
    }
}

fun main() {    
    println(Version(1, 2) > Version(1, 3))
    println(Version(2, 0) > Version(1, 5))
}
```

*Custom* orders let you sort instances of any type in a way you like. Particularly, you can define an order for non-comparable objects or define an order other than natural for a comparable type. To define a custom order for a type, create a [`Comparator`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-comparator/index.html) for it. `Comparator` contains the `compare()` function: it takes two instances of a class and returns the integer result of the comparison between them. The result is interpreted in the same way as the result of a `compareTo()` as is described above.

```kotlin
val lengthComparator = Comparator { str1: String, str2: String -> str1.length - str2.length }
println(listOf("aaa", "bb", "c").sortedWith(lengthComparator))
```

Having the `lengthComparator`, you are able to arrange strings by their length instead of the default corder.

A shorter way to define a `Comparator` is the [`compareBy()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.comparisons/compare-by.html) function from the standard library. `compareBy()` takes a lambda function that produces a `Comparable` value from an instance and defines the custom order as the natural order of the produced values.

With `compareBy()`, the length comparator from the example above looks like this:

```kotlin
println(listOf("aaa", "bb", "c").sortedWith(compareBy { it.length }))
```

The Kotlin collections package provides functions for sorting collections in natural, custom, and even random orders. On this page, we'll describe sorting functions that apply to [read-only](https://kotlinlang.org/docs/collections-overview.html#collection-types) collections. These functions return their result as a new collection containing the elements of the original collection in the requested order. To learn about functions for sorting [mutable](https://kotlinlang.org/docs/collections-overview.html#collection-types) collections in place, see the [List-specific operations](https://kotlinlang.org/docs/list-operations.html#sort).

#### Natural order﻿

The basic functions [`sorted()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sorted.html) and [`sortedDescending()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sorted-descending.html) return elements of a collection sorted into ascending and descending sequence according to their natural order. These functions apply to collections of `Comparable` elements.

```kotlin
val numbers = listOf("one", "two", "three", "four")

println("Sorted ascending: ${numbers.sorted()}")
println("Sorted descending: ${numbers.sortedDescending()}")
```

#### Custom orders﻿

For sorting in custom orders or sorting non-comparable objects, there are the functions [`sortedBy()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sorted-by.html) and [`sortedByDescending()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sorted-by-descending.html). They take a selector function that maps collection elements to `Comparable` values and sort the collection in natural order of that values.

```kotlin
val numbers = listOf("one", "two", "three", "four")

val sortedNumbers = numbers.sortedBy { it.length }
println("Sorted by length ascending: $sortedNumbers")
val sortedByLast = numbers.sortedByDescending { it.last() }
println("Sorted by the last letter descending: $sortedByLast")
```

To define a custom order for the collection sorting, you can provide your own `Comparator`. To do this, call the [`sortedWith()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sorted-with.html) function passing in your `Comparator`. With this function, sorting strings by their length looks like this:

```kotlin
val numbers = listOf("one", "two", "three", "four")
println("Sorted by length ascending: ${numbers.sortedWith(compareBy { it.length })}")
```

#### Reverse order﻿

You can retrieve the collection in the reversed order using the [`reversed()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/reversed.html) function.

```kotlin
val numbers = listOf("one", "two", "three", "four")
println(numbers.reversed())
```

`reversed()` returns a new collection with the copies of the elements. So, if you change the original collection later, this won't affect the previously obtained results of `reversed()`.

Another reversing function - [`asReversed()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/as-reversed.html)

- returns a reversed view of the same collection instance, so it may be more lightweight and preferable than `reversed()` if the original list is not going to change.

```kotlin
val numbers = listOf("one", "two", "three", "four")
val reversedNumbers = numbers.asReversed()
println(reversedNumbers)
```

If the original list is mutable, all its changes reflect in its reversed views and vice versa.

```kotlin
val numbers = mutableListOf("one", "two", "three", "four")
val reversedNumbers = numbers.asReversed()
println(reversedNumbers)
numbers.add("five")
println(reversedNumbers)
```

However, if the mutability of the list is unknown or the source is not a list at all, `reversed()` is more preferable since its result is a copy that won't change in the future.

#### Random order﻿

Finally, there is a function that returns a new `List` containing the collection elements in a random order - [`shuffled()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/shuffled.html). You can call it without arguments or with a [`Random`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.random/-random/index.html) object.

```kotlin
val numbers = listOf("one", "two", "three", "four")
println(numbers.shuffled())
```