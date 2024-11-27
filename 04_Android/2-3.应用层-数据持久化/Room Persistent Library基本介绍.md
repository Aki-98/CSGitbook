> refs: https://www.geeksforgeeks.org/introduction-to-room-persistent-library-in-android/



**背景：**

Room是谷歌提供的用于数据库存储访问的Lib，包含在jetpack project之中。



**依赖：**

```groovy
dependencies {
  implementation "androidx.room:room-runtime:2.2.5"
  kapt "androidx.room:room-compiler:2.2.5"
}
```



**好处：**

1. 查询在编译时进行验证。
   - 这意味着在编译代码时，Room会检查你的查询语句是否正确，这有助于减少在运行时出现的错误。
2. 减少样板代码。
   - Room提供了简洁的API，使得开发者在编写数据库相关代码时不需要编写大量重复的代码。
3. 简单易懂，容易应用。
   - Room的设计理念简单，使得开发者可以更容易地理解和使用它。
4. 与RxJava、LiveData和Kotlin协程的集成简单。



**组件：**

- **数据库（Database）**：这包含了数据库持有者，并作为应用程序持久化、关系型数据的主要访问点。
- **实体（Entity）**：数据库中的一个表，由一个实体表示。
- **DAO（Data Access Object）**：这个类包含了访问数据库的方法。

**Room数据库**：您的应用程序使用Room数据库来检索与数据库相关的数据访问对象（DAOs）。然后，每个DAO被应用程序用于从数据库检索实体并保存任何对这些实体的更改。最后，应用程序使用一个实体来检索和设置与数据库中表列对应的值。



**Database：**

```java
@Database(entities = arrayOf(User::class), version = 1)
abstract class courseDB: RoomDatabase() {
  abstract fun courseName(): courseDB
}
```

1. 继承自抽象类RoomDatabase
2. 注解中包含所有的Entity
3. 包含一个无参数的抽象方法，用于返回@Dao注解的实例
4. 设计模式为单例



**Entity：**

```java
@Entity
data class User(
  @PrimaryKey val uid: Int,
  @ColumnInfo(name = "courseName") val firstName: String?,
  @ColumnInfo(name = "courseHolder") val lastName: String?
)
```

1. 此类用@Entity注解，代表一张表
2. 每个成员变量代表一列，所有域必须都为public并且有getter and setter方法.
3. 如果所有的域都可访问，采用空的构造函数，或者采用含参构造函数。Room也可以使用部分构造函数。
4. 每个实体类至少需要有一个主键。要定义单个字段的主键，可以使用 @PrimaryKey注解，或者在 @Entity注解的 primaryKeys属性中为多个字段定义主键。还可以使用 @PrimaryKey注解的 autoGenerate属性自动分配主键。

```java
@Entity(indices = arrayOf(Index(value = ["courseHolder", "address"])))@Entity(indices = arrayOf(Index(value = ["courseName", "courseHolder"],
        unique = true)))
```

1. 使用 @Entity注解的 indices 属性可以为实体添加索引。
2. 使用 @Index注解并将 unique属性设置为 true 可以创建唯一索引。



**Data Access Object (DAO)：**

```java
@Dao
interface courseDAO{
  @Query("SELECT * FROM course")
  fun getAll(): List<GFG>
  
  @Query("SELECT * FROM course WHERE uid IN (:userIds)")
  fun loadAllByIds(userIds: IntArray): List<GFG>
  
  @Insert
  fun insertAll(vararg courses: User)
  
  @Delete
  fun delete(course: Courses)
}
```

1. DAO（数据访问对象）提供了与数据库交互的API。
2. DAO 是一个带有 @Dao 注解的接口。
3. 这个接口的方法用于从数据库检索数据或对数据库进行更改。
4. 通过注解如 @Query、@Insert 和 @Delete来标识这些方法。



**Converting Types：**

```java
class GFG {
  @TypeConverter
  fun fromTimestamp(value: Long?): Date? {
  return value?.let { Date(it) }
  }

  @TypeConverter
  fun dateToTimestamp(date: Date?): Long? {
  return date?.time?.toLong()
  }
}
```

将自定义数据类型持久化到单个数据库列中，可以使用类型转换器（Type converters）