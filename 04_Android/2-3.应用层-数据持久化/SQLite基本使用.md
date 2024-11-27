## SQLite

SQLite数据库是个轻量级的数据库，本质上是个二进制文件。

![image-20220303170613410](SQLite基本使用_imgs\image-20220303170613410.png)

**SQLiteExpert工具**

**SQLiteOpenHelper**

**SQLiteDatabase**

rawQuery();查询

execSQL();添加、删除、修改、创建

API函数

```java
/**1.添加**/
//参数1：所要操作的数据库表的名称
//参数2：可以为空的列
//参数3：添加的参数
ContentValues values = new ContentValues();
values.put("name",name);
values.put("age",age);
values.put("sex",sex);
long id = db.insert("test_db",null,values);

/**2.查询**/
//参数1：所要操作的数据库表的名称
//参数2：要查询的列，传入null代表查询所有列
//参数3：条件语句
//参数4：条件参数
//参数5：group by 分组
//参数6：having 去除不符合条件的组
//参数7：order by 按……排序
Cursor c = db.query("test_db",null,"name=? and age=? and sex=?",new String[]{"李清秋","23","女"},null,null);
Cursor c2 = db.query("test_db",null,null,null,null,"group by (age)","having sex='女'");

```

**数据库更新、升级、降级**

https://www.jianshu.com/p/65923fa3e3dc

