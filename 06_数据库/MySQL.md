# 一、基础概念

DB（database）

DBMS（database management system）DB是通过DBMS创建和操作的容器

常见的DBMS：MySQL Oracle（贵） DB2（处理海量的数据） SqlServer（微软公司，只能安装在Windows操作系统下）

# 二、DQL语句

## 基础查询

**语法:**

```
select <查询列表> from <表名>；
```

类似于:System.out,printIn(打印东西)；

**特点：**

1. 查询列表可以是：表中的字段、常量值、表达式、函数

2. 查询的结果是一个虚拟的表格

**用例：**

```SQL
#查询表中的单个字段
select last_name from employees;
#查询表中的多个字段
select last_name,salary,email from employees;
#查询表中的所有字段
select * from employees;
#查询常量值
select 100; 
select 'john';
#查询表达式
select 100%98;
#查询函数
select version();
#起别名
/*    用处：
        1.便于理解；
        2.如果要查询的字段有重名的情况，使用别名可以区分开来。
*/
select 100%98 as 别名
select last_name as 姓, first_name as 名 from employees;
select last_name 姓, first_name 名 from employees;
#eg.查询salary,显示结果为out put
select salary as out put from employees;#out被识别为关键字，出现错误
select salary as "out put" from employees;
#去重
#eg.查询员工表中涉及到的所有部分编号
select department_id from employees;//会有重复信息
select distinct department_id from employees;
#+号的作用
/*用法：
	只能作为运算符使用。
	如果有字符型，尝试转换成数值型，再进行运算（“1”->1）;如果转换失败，则转换成0，再进行运行。
	只要其中一方为null，结果肯定为null
*/
#eg.查询员工名和员工的姓，连接成一个字段，并显示为 姓名
select 
	concat(last_name,first_name) as 姓名 
from 
	employees;  
#eg.查询出表employees的全部列，各个列之间用逗号连接，列头显示成out_put
select 
	concat('first_name', ',' , 'last_name', ',' ,'job_id', ',',IFNULL(commission_pct,0)) as out_put
from
	employees;
```

## 条件查询

语法：

```sql
select 
	查询列表 
from
	表名
where
	筛选条件;
```

分类：

- 按条件表达式筛选
  - 条件运算符 > < = != <> >= <=
- 按逻辑表达式筛选
  - 逻辑运算符 && || ! 
  - and or not
- 模糊查询
  - like
  - between and
  - in
  - is null

用例：

### 1.按条件表达式筛选

```sql
#eg. 查询工资>12000的员工信息
SELECT
	*
FROM
	employees
WHERE 
	salary>12000;
#eg. 查询部门编号不等于90号的员工名和部门编号
SELECT 
	last_name,
	department_id
FROM
	employees
WHERE
	department_id!=90;//不标准，最好是department_id<>90;
```

### 2.按逻辑表达式筛选

```sql
#eg.查询工资z在10000到20000之间的员工名，工资和奖金
SELECT
    last_name,
    salary,
    commission_pct
FROM
	employees
WHERE
	salary>=10000 AND salary<=20000;
#eg.查询部门编号不是在90到110之间，或者工资高于15000的员工信息
SELECT
	*
FROM
	employees
WHERE
	department_id<90 OR department_id>110 OR salary>15000;
```

### 3.模糊查询

#### 3.1 like

特点：

- \- 一般和通配符搭配使用
- %任意多个字符，包含0个字符
- _任意单个字符

```sql
#eg. 查询员工名共包含字符a的员工信息
SELECT
	*
FROM
	employees
WHERE
	last_name LIKE '%a%';//默认大小写a是一回事
#eg.查询员工名中第三个字符为e，第五个字符为a的员工名和工资
SELECT
	last_name
FROM
	employees
WHERE
	last_name LIKE '___e_a%';
#eg. 查询员工名中第二个字符为下划线的员工名
SELECT
	last_name
FROM
	employees
WHERE
	last_name LIKE '_\_%';
SELECT
	last_name
FROM
	employees
WHERE
	last_name LIKE '_$_%' ESCAPE '$';
```

#### 3.2 between and 

注意：

- 使用 between and 可以提高语句的简洁度

- 包含临界值

- 两个临界值不要调换顺序

```sql
#eg. 查询员工编号在100到120之间的员工信息
SELECT
	*
FROM
	employees
WHERE
	employee_id BETWEEN 100 AND 120;
```

#### 3.3 in关键字

含义：判断某字符的值是否属于in列表中的某一项

特点：

- 使用in提高语句简洁度

- in列表的值必须是同样的类型，或者可以兼容的类型，即可以隐式转换

```sql
#eg. 查询员工的公众编号是 IT_PROG、AD_VP、AD_PRES中的一个的员工名和工种编号
SELECT
	last_name,
	job_id
FROM
	employees
WHERE
	job_id IN ('IT_PROG','AD_VP','AD_PRES');
```

#### 3.4 is null 关键字

= 或 <> 不能用于判断null值

is null 或 is not null 可以判断null值

```sql
#eg. 查询没有奖金的员工名和奖金率
SELECT
	last_name,
	commission_pct
FROM
	employees
WHERE
	commission_pct IS NULL;
```

### 4.安全等于<=>

特点：可读性差

```sql
#eg. 查询没有奖金的员工名和奖金率
SELECT
	last_name,
	commission_pct
FROM
	employees
WHERE
	commission_pct <=>  NULL;
#eg. 查询工资为12000的员工信息
SELECT
*
FROM
	employees
WHERE
	salary  <=>  12000;
```

Tips：

- IS NULL：仅仅可以判断NULL值，可读性较高，建议使用

- <=>:  既可以判断NULL，又可以判断普通的数值， 可读性较低

## 排序查询

语法：

```sql
SELECT
	查询列表
FROM
	表
(WHERE
 	筛选条件）
ORDER BY
 	排序列表
```

特点：

- ASC 代表升序，DESC代表降序，不写默认升序

- ORDER BY 子句中可以支持单个字段、多个字段、表达式、函数、别名

- ORDER BY 子句一般是放在查询语句的最后面，LIMIT子句除外

```sql
#eg.查询员工信息，要求工资从高到低排序
SELECT * FROM employees ORDER BY salary DESC;(降序排序)
SELECT * FROM employees ORDER BY salary ASC;(升序排序)
SELECT * FROM employees ORDER BY salary ;(默认为升序排序)
#eg.查询部门编号>=90的员工信息，要求按入职时间排序
SELECT 
*
FROM 
	employees
WHERE
	department_id >= 90
ORDER BY 
	hiredate ASC;
#eg.按年薪的高低显示员工信息和年薪【按别名排序】
SELECT
	*,salary*12*(1+IFNULL(commission_pct,0)) 年薪
FROM
	employees
ORDER BY 
	salary*12*(1+IFNULL(commission_pct,0)) DESC;
#eg.按姓名的长度显示员工的姓名和工资【按函数排序】
SELECT
	LENGTH(last_name) 字节长度，last_name,salary
FROM
	employees
ORDER BY
	LENGTH(last_name) DESC;
#eg.查询员工信息，要求先按工资排序，再按员工编号排序【按多个字段排序】
SELECT
	*
FROM
	employees
ORDER BY
	salary ASC，employee_id DESC;
```

## 常见函数

语法：

```sql
SELECT 
	函数名(实参列表) 
(from 
 	表)
```

分类：

- 单行函数：做处理使用
  - 如 concat、length、ifnull等
  - 又分为 字符函数、数学函数、日期函数、其他函数、流程控制函数

- 分组函数：做统计使用、又称为统计函数、聚合函数、组函数

### 1.单行函数

### 1.1 字符函数

#### 1.1.1 length

```sql
select length(‘john’); #4
select length('张三丰hahaha'); #15 uft8 一个中文字占3个字节，一个英文字占1个字节
```

#### 1.1.2 concat

链接字符串

```sql
select concat(first_name,'_',last_name) from employees;
```

#### 1.1.3 upper lower

upper：英文字母变大写；lower：英文字母变小写。

```sql
#eg. 姓变大写，名变小写，然后拼接
select concat(upper(last_name),lower(first_name)) 姓名 from employees;
```

#### 1.1.4 substr substring

注意：索引从1开始

```sql
select substr('李莫愁爱上了陆展元',7) out_put; #李莫愁爱上了
select substr('李莫愁爱上了陆展元',1,3) out_put; #李莫愁
#eg.姓名中首字符大写，其他字符小写然后用_拼接，显示出来
select concat(upper(substr(last_name,1,1)),'_',lower(substr(last_name,2))) out_put from employees;
```

#### 1.1.5 instr

返回子串第一次出现的索引，如果找不到返回0

```sql
select instr('杨不悔爱上了殷六侠','殷六侠') as out_put; #7
```

#### 1.1.6 trim

去掉前后的空格

```sql
select length(trim('    张翠山    ')) as out_put; #9
select length(trim('a' from 'aaaaaa张aa翠山aaaaa')) as out_put;#张aa翠山 11 
```

#### 1.1.7 rpad lpad

rpad：用指定的字符实现右填充指定长度；lpad：用指定的字符实现左填充指定长度

```sql
select rpad('殷素素',10,'*') as out_put;#殷素素*******
select lpad('殷素素',10,'*') as out_put;#*******殷素素
```

1.1.9 replace

替换

```sql
select replace('张无忌爱上了周芷若','周芷若','赵敏') as out_put;
```

### 1.2 数学函数

#### 1.2.1 round

四舍五入

```sql
select round(1.65);#2
select round(-1.65);#-2
select round(-1.45);#-1
select round(1.567,2);#1.57
```

#### 1.2.2 ceil

向上取整（更大的数）

```sql
select ceil(1.002);#2
select ceil(1.00);#1
```

#### 1.2.3 floor

向下取整（更小的数

```sql
select ceil(1.002);#1
select ceil(0.99);#0
select ceil(9.99);#9
select ceil(-9.99);#-10
```

#### 1.2.4 truncate

截断

```sql
select truncate(1.65,1);#1.6
```

1.2.5 mod

取余

```sql
select mod(10,3); #1
select 10%3;#1
select mod(-10,-3);#-1 被除数为正，结果为正，被除数为负，结果为负
select mod(-10,3);#-1
select mod(10,-3);#1
select mod(10,3);#1
```

### 1.3 日期函数

#### 1.3.1 now 

返回当前系统日期+时间

```sql
select now();
```

#### 1.3.2 curdate 

返回当前系统日期，不包含时间

```sql
select curdate();
```

#### 1.3.3 curtime 

返回当前系统时间，不包含日期

```sql
select curtime();
```

#### 1.3.4 year month monthname...

可以获取指定的部分、年、月、日、小时、分钟、秒

```sql
select year(now()) 年;
select year(now('1998-1-1')) 年;
select year(hiredate) 年 from employees;
select month(now()) 月; #8
select monthname(now()) 月; #August
```

#### 1.3.5 str_to_date 

将日期格式的字符转换成指定格式的日期

```sql
select str_to_date('1998-3-2','%Y-%c-%d') as out_put; #1990-03-02
#eg.查询入职日期为1992-4-3的员工信息
select * from employees where hiredate = str_to_date('1992-4-3','%c-%d %Y');
```

![clipboard.png](MySQL_imgs\g6B5JSMFzjm.png)

#### 1.3.6 date_format

将日期转换成字符

```sql
select date_format('2018/6/6','%Y年%m月%d日') #2018年06月06日
#eg.查询有奖金的员工名和入职日期(**月/**日 **年)
select 
	last_name,date_format(hiredate,'%m月/%d日 %y年') 入职日期 
from 
    employees 
where 
    commission_pct is not null;
```

### 1.4 其他函数

```sql
select version();#查看版本
select database();#查看当前数据库
select user();#查看当前用户
```

### 1.5 流程控制函数

#### 1.5.1 if函数

```sql
select if(10>5,'大','小'); #大

select last_name,commission_pct,if(commision_pct is null,'没奖金，哈哈','有奖金，嘻嘻') 备注 from employees;
```

#### 1.5.2 case函数

##### (1) switch case 的效果

语法：

```sql
case 要判断的字段或表达式
	when 常量1 then 要显示的值或语句
	when 常量2 then 要显示的值2或语句2
	···
	else 要显示的值n或语句n
end
```

用例：

```sql
#eg.查询员工的工资，要求部门号为30，显示的工资为1.1倍；部门号为40，显示的工资为1.2倍；部门号为50，显示的工资为1.3倍；其他部分，显示的工资为原工资。

select salary 原始工资,department_id,
    case department_id
        when 30 then salary*1.1
        when 40 then salary*1.2
        when 50 then salary*1.3
        else salary
    end as 新工资
from employees;
```

##### (2)类似于多重if

语法：

```sql
case
	when 条件1 then 要显示的值或语句
	when 条件2 then 要显示的值2或语句2
	···
	else 要显示的值n或语句n
end
```

用例：

```sql
#eg.查询员工的工资的情况，如果工资>20000,显示A级别；如果工资>15000,显示B级别；如果工作>10000,显示C级别；否则，显示D级别。
select salary,
	case 
		when salary>20000 then 'A'
		when salary>15000 then 'B'
		when salary>10000 then 'C'
		else 'D'
	end as 工资级别
from employees;
```

### 2. 分组函数

sum 求和 avg 平均值 max 最大值 min 最小值 count 计算个数

1.简单使用

```sql
select sum(salary) from employees;
select round(avg(salary),2) from employees;
select min(salary),max(salary) from employees;
```

2.参数支持哪些类型

sum,avg字符型，但没有意义

```sql
select max(last_name),min(last_name) from employees;#支持，也有意义
select max(hiredate),min(hiredate) from employees;#支持，也有意义
count 都支持，也有意义，会忽略null值
```

3.是否忽略null值

会忽略null值:sum、avg、max、min、count

```sql
select avg(commisssion_pct),sum(commisssion_pct)/35,sum(commisssion_pct)/127 from employees;
```

4.和distinct搭配(去重)

```sql
select sum(distinct salary) from employees;
```

5.count函数介绍

```sql
select count(*) from employees; #统计行数，效率一般更高
select count(1) from employees; #统计行数 写1 写2都行 写啥都一样，除了null
```

6.和分组函数一同查询的字段有限制，要求是group by 之后的字段

```sql
select avg(salary),employee_id from employees;#没有任何意义
```

## 分组查询

语法：

```sql
select 分组函数、列（要求出现在group by的后面）

from 表

【where 筛选条件】

group by 分组的列表

【order by 子句】
```

注意：查询列表必须特殊，要求是分组函数和group by后出现的字段

特点：

- 分组查询中的筛选条件分为
  - 数据源  位置
  - 分组前筛选 原始表  where
  - 分组后筛选 分组后的结果集 having
  - tips:分组函数做条件肯定是在having语句之中；能用分组前筛选的，优先考虑使用分组前筛选
- group by子句支持单个字段分组、多个字段分组（没有顺序要求）、表达式分组、函数分组

- 也可以添加排序（排序放在整个分组查询的最后）

### 1.简单分组查询

```sql
#eg.查询每个部门的平均工资
select avg(salary) from employees;
#eg.查询每个工种的最高工资
select max(salary),job_id
from employees
group by job_id;
#eg.查询每个位置上的部门个数
select count(*),location_id
from departments
group by location_id;
```

### 2.添加筛选条件

```sql
#eg.查询邮箱中包含a字符的每个部门的平均工资
select avg(salary),department_id
from employees
where email like '%a%'
group by department_id
#eg.查询有奖金的每个部门的每个领导手下员工的最高工资
select max(salary),manager_id,
from employees
where commission_pct is not null
group by manager_id;
```

### 3.添加复杂筛选条件

```sql
#eg.查询哪个部门的员工个数>2
#tips:1.查询每个部门的员工个数；2.根据1的结果进行筛选，查询哪个部门的员工个数>2
select count(*),department_id
from employees
group by department_id
having count(*)>2;
#eg.查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资
select job_id,max(salary)
from employees
where commission_pct is not null
group by job_id
having max(salary)>12000;
#eg.查询领导编号>102的每个领导手下的最低工资>5000的领导编号是哪个，以及其最低工资
select min(salary),manager_id
from employees
where manager_id>192
group by manager_id
having min(salary)>5000
```

### 4.按表达式或函数分组

```sql
#eg.按员工姓名的长度分组，查询每一组的员工个数，筛选员工个数>5的有哪些
select count(*),length(last_name)
from employees
group by length(last_name)
having count(*)>5;

```

### 5.按多个字段分组

```sql
#eg.查询每个部门每个工种的员工的平均工资
select avg(salary),department_id,job_id
from employees
group by job_id,department_id;
```

### 6.添加排序

```sql
#eg.查询每个部门每个工种的员工的平均工资，并且按平均工资的高低显示
select avg(salary),department_id,job_id
from employees
where department_id is not null
group by job_id,department_id
order by avg(salary) desc;
```

## 连接查询

按年代分类：

- sql92标准：仅仅支持内连接

- sql99标准：【推荐】支持内连接+外连接+交叉连接

按功能分类：

- 内连接：等值连接、非等值连接、自连接

- 外连接：左外连接、右外连接、全外连接

- 交叉连接：

### 1. sql92标准

#### 1.1 等值连接

- 多表等值连接的结果为多表的交集部分
- n表连接，至少需要n-1个连接条件

- 多表的顺序没有要求

- 一般需要为表起别名

- 可以搭配前面介绍的所有子句使用，比如排序、分组、筛选

```sql
#eg.查询女神名和对应的男神名
select name,boyname
from bos,beauty
where beauty.boyfriend_id=boys.id;
#eg.查询员工名和对应的部门名
select last_name,department_name
from employees,departments
where employees.department_id=departments.department_id;
```

1. 可以为表起别名（如果为表起了别名，则查询的字段不能使用原来的表名去限定）

```sql
#eg.查询员工名、工种号、工种名
select last_name,e.job_id,title
from employees as e,jobs 
where e.job_id=jobs.job_id
```

2. 表名顺序可以替换

3. 可以加筛选

```sql
#eg.查询有奖金的员工名、部门名
select last_name,department_name
from employees e,departments d
where e.department_id=d.department_id
and e.commission_pct is not null
#eg.查询城市名中第二个字符为o的部门名和城市名
select department_name,city
from departments d,location l
where d.location_id = l.location_id
and city like '_o%';
```

4. 可以加分组

```sql
#eg.查询每个城市的部门个数
select count(*) 个数,city
from departments d,locations l
where d.location_id=l.location_id
group by city;
#eg.查询有奖金的每个部门的部门名和部门的领导编号和该部门的最低工资
select department_name,manager_id,min(salary)
from departments d,employees e
where d.department_id=e.department_id
and commission_pct is not null
group by department_name,d.manager_id
```

5. 可以加排序

```sql
#eg.查询每个工种的工种名和员工个数，并且按员工个数降序
select job_title,count(*)
from employees e,jobs j
where e.job_id=j.job_id
group by job_title
order by count(*) desc;
```

6. 可以实现三表连接

```sql
#eg.查询员工名、部门名、所在的城市
select last_name,department_name,city
from employees e,departments d,location l
where e.department_id=d.department_id
and d.location_id=l.location_id;
```

#### 1.2 非等值连接

```sql
#eg.查询员工的工资和工资级别
select salary,grade_level
from employees e,job_grades g
where salary between g.lowest_sal and g.highest_sal;
```

#### 1.3 自连接

```sql
#eg.查询员工名和上级的名称
select employees_id,last_name,employee_id,last_name
from employees e,employees m
where e.manager_id=m.employee_id;
```

### 2. sql99语法

语法：

```sql
select 查询列表
from 表1 别名 【连接类型】
join 表2 别名 
on 连接条件
【where 筛选条件】
【group by 分组】
【order by 排序列表】
```

类型：

- 内连接：inner

- 外连接

  - 左外：left【outer】

  - 右外：right【outer】

  - 全外：full【outer】
  - 交叉连接：cross

#### 2.1 内连接

语法：

```sql
select 查询列表
from 表1，别名
inner join 表2，别名
on 连接条件
```

特点：

- 添加排序、分组、筛选

- inner可以省略

- 筛选条件放在where后面，连接条件放在on后面，提高分离性，便于阅读

- inner join连接和sql92语法中的等值连接效果是一样的，都是查询多表的交集

#####  2.1.1 等值连接

```sql
#eg.查询员工名、部门名
select last_name,department_name
from employee e
inner join departments d
on e.department_id=d.department_id;
#eg.查询名字中包含e的员工名和工种名（添加筛选）
select last_name,job_title
from employee e
inner join jobs j
on e.job_id=j.job_id
where e.last_name like "%e%";
#eg.查询部门个数>3的城市名和部门个数（添加分组+筛选）
select city,count(*) 部门个数
from departments d
inner join locations l
on d.location_id=l.location_id
group by city
having count(*)>3;
#eg.查询哪个部门的部门员工个数>3的部门名和员工个数，并按个数排序
select count(*),department_name
from employees e
inner join departments d
on e.department_id=d.department_id
group by department_name
having count(*)>3
order by count(*);
#eg.查询员工名，部门名，工种名，并按部门名降序
select last_name,department_name,job_title
from employees e
inner join departments d
on e.department_id = d.department_id
inner join jobs j
on e.job_id = j.job_id
order by department_name desc;
```

##### 2.1.2 非等值连接

```sql
#eg.查询员工的工资级别
select salary,grade_level
from employees e
join job_grades g
on e.salary between g.lowest_sal and g.highest_sal
#eg.查询工资级别的个数>20的个数，并且按工资级别降序
select count(*),grade_level
from employees e
join job_grades g
on e.salary between g.lowest_sal and g.highest_sal
group by grade_level
having count(*)>20
order by grade_level desc;
```

##### 2.1.3 自连接

```sql
#eg.查询员工的名字、上级的名字
select e.last_name,m.last_name
from employees e
join employees m
on e.manager_id = m.employee_id;
#eg.查询姓名中包含字符K的员工的名字、上级的名字
select e.last_name,m.last_name
from employees e
join employees m
on e.manager_id = m.employee_id;
where e.last_name like '%k%';
```

#### 2.2 外连接

应用场景：用于查询一个表中有，另一个表没有的记录

特点：

- 外连接的查询结果为主表中的所有记录

  - 如果从表中有和它匹配的，则显示匹配的值

  - 如果从表中没有和它匹配的，则显示null

  - 外连接查询结果=内连接结果+主表中有而从表没有的记录

- 左外连接，left join 左边的是主表（from后是主表）

  右外连接，right join 右边的是主表（join后是主表）

- 左外和右外交换两个表的顺序，可以实现同样的效果

- 全外连接=内连接的结果+表1中有但表2没有的+表2中有单表1没有的

```sql
#eg.查询男朋友不在男神表的女神名
#右外连接
select b.name,bo.*
from beauty b
left outer join boys bo
on b.boyfriend_id = bo.id
where bo.id is null;
#左外连接
select b.name,bo.*
from boys bo
right outer join beauty b
on b.boyfriend_id = bo.id
where bo.id is null;
#eg.查询哪个部门没有员工
#左外连接
select d.*,e.employee_id
from departments d
left outer join employees e
on d.department_id = e.department_id
where e.employee_id is null
#右外连接
select d.*,e.employee_id
from employees e
right outer join departments d
on d.department_id = e.department_id
where e.employee_id is null;
#全外连接
select b.*,bo.*
from beauty b
full outer join boys bo
on b.boyfriend_id = bo.id;
#交叉连接（笛卡尔乘积）
select b.*,bo.*
from beauty b
cross join boys bo;
```

![image-20230320174549282](MySQL_imgs\fO9HYNQ4G3J.png)



![image-20230320174604532](MySQL_imgs\cXR3ZzPT8oU.png)

#### 2.3 子查询

含义：出现在其他语句中的select语句，称为子查询或内查询；内部嵌套其他select语句的查询，称为外查询或主查询

分类：

- 按子查询出现的位置：

  - select 后面：仅仅支持标量子查询

  - from 后面：支持表子查询

  - where或having后面：标量子查询（单行）、列子查询（多行）、行子查询

  - exists后面（相关子查询）

- 按结果集的行列数不同：

  - 标量子查询（结果集只有一行一列）

  - 列子查询（结果集只有一列多行）

  - 行子查询（结果集有一行多列）

  - 表子查询（结果集一般为多行多列）

#####  2.3.1 where或having后面

特点：

- 子查询放在小括号内

- 子查询一般放在条件的右侧



###### 2.3.1.1 标量子查询

标量子查询，一般搭配着单行操作符使用

\> < >= <= = <>

```sql
#eg.谁的工资比Abel高？
select *
from employees
where salary > (
    select salary
    from employees
    where last_name = 'Abel'
);
#eg.返回job_id与141号员工相同，salary比143号员工多的员工 姓名，job_id和工资
select last_name,job_id,salary
from employees
where job_id = (
    select job_id
    from employees
    where employee_id = 141
) and salary > (
    select salary
    from employees
    where employee_id = 143
);
#eg.返回公司工资最少的员工的last_name,job_id和salary
select last_name,job_id,salary
from employees
where salary = (
    select min(salary)
    from employees
);
#eg.查询最低工资大于50号部门最低工资的部门id和其最低工资
select min(salary),department_id
from employees
group by department_id
having min(salary) > (
    select min(salary)
    from employees
    where department_id = 50
)
#非法使用标量子查询
select min(salary),department_id
from employees
group by department_id
having min(salary) > (
    select salary #得到的就不是一个值了 
    from employees
    where department_id = 50
)
```

###### 2.3.1.2 列子查询（多行子查询）

列子查询，一般搭配着多行操作符使用

| 操作符      | 含义                       |
| ----------- | -------------------------- |
| IN / NOT IN | 等于列表中的任意一个       |
| ANY / SOME  | 和子查询返回的某一个值比较 |
| ALL         | 和子查询返回的所有值比较   |

```sql
#eg.返回location_id是1400或1700的部门中所有员工姓名
select last_name
from employees
where department_id in(
    select distinct department_id
    from departments
    where location_id in (1400,1700)
);
#eg.返回其他部门中比job_id为‘IT_PROG’部门任一工资低(<最高工资就行)的员工的员工号、姓名、job_id以及salary
select employee_id,last_name,job_id,salary
from employees
where  salary < any (
    select distinct salary
    from employees
    where job_id = 'IT_PROG'
) and job_id <>'IT_PROG';
#eg.返回其它部门中比job_id为'IT_PROG'部门所有工资都低的员工的员工号、姓名、job_id以及salary
select employee_id,last_name,job_id,salary
from employees
where salary < all (
    select distinct salary
    from employees
    where job_id = 'IT_PROG'
) and job_id <>'IT_PROG';
```

###### 2.3.1.3 行子查询（结果集一行多列或多行多列）

```sql
#eg.查询员工编号最小并且工资最高的员工信息
select *
from employees
where employee_id = (
    select min(employee_id)
    from employees
) and salary = (
    select max(salary)
    from employees
);
select *
from employees
where(employee_id,salary)=(
    select min(employee_id),max(salary)
    from employees
);
```

##### 2.3.2 select后面

只支持标量子查询

###### 2.3.2.1 标量子查询

```sql
#eg.查询每个部门的员工个数
select d.*,(
    select count(*)
    from employees e
    where e.department_id=d.department_id
) 个数
from departments d;
#eg.查询员工号=102的部门名
select (
    select department_name
    from departments d
    inner join employees e
    on d.department_id=e.department_id
    where e.employee_id=102
) 部门名;
```

##### 2.3.3 from后面的子查询

###### 2.3.3.1 表子查询

```sql
#eg.查询每个部门的平均工资的工资等级
select ag_dep.*,g.grade_level
from (
    select avg(salary) ag,department_id
    from employees
    group by department_id
) ag_dep
inner join job_grades g
on ag_dep.ag between lowest_sal and highest_sal;
```

##### 2.3.4 exists后面

###### 2.3.4.1 相关子查询

语法：

exists（完整的查询语句）

结果：

1或0

```sql
#eg.查询有员工名的部门名
select department_name
from departments
where exists (
    select * 
    from employees e
    where d.department_id = e.department_id
);
select department_name
from departments d
where d.department_id in (
    select department_id
    from employees
);
#eg.查询没有女朋友的男神信息
select bo.*
from boys bo
where bo.id not in (
    select boyfriend_id
    from beauty
);
select bo.*
from boys bo
where not exists(
    select boyfriend_id
    from beauty b
    where bo.id=b.boyfriend_id
);
```

## 分页查询

应用场景：当要显示的数据、一页显示不全、需要分页提交sql请求

语法：

```sql
select 查询列表
from 表
【join type join 表2
on 连接条件
where 筛选条件
group by 分组字段
having 分组后的筛选
order by 排序的字段】
limit 【offset,】size;
```

- offset 要显示条目的起始索引（从0开始）

- size要显示的条目个数

特点：

- limit语句放在查询语句的最后

- 公式：要显示的页数 page，每页的条目数 size

```sql
#eg.查询前五条员工信息
select * from employees limit 0,4;
select * from employees limit 5;
#eg.查询第11条-第25条
select * from employees limit 10,15;
#eg.有奖金的员工信息，并且工资较高的前10名显示出来
select * from employees where commission_pct is not null order by salary desc limit 10;
```

## 联合查询

union：将多条查询语句的结果合并成一个结果

应用场景：要查询的结果来自多个表，且多个表没有直接的连接关系，但查询的信息一致时

特点：两个表的列数必须一样；多条查询语句的每一列的类型和顺序最好一致；使用union时会自动去重，使用union all 会包含重复项

```sql
#eg.查询部门编号>90或邮箱包含a的员工信息
select * from employees where email like '%a%' or department_id > 90;
select * from employees where email like '%a%'
union
select * from employees where department_id > 90;
#eg.查询中国用户中男性的信息>以及外国用户中男性的信息
select id,cname,csex from t_ca where csex='男'
union
select t_id,tName,tGender from t_ua where tGender='male'
```

# 三、DML语言

数据操作语言

##  1.插入语句

语法：

```sql
insert into 表名(列名...) values(值1,...)
#法一：支持插入多行，支持子查询
insert into beauty(id,name,sex,borndate,phone,photo,boyfriend_id)
values(13,'唐艺昕','女','1990-4-23','18988888888',null,2);
#法二：不支持插入多行，不支持子查询
insert into beauty(id,name,sex,phone)
values(14,'金星','女','13988888888');
```

特点：

- 插入的项目和列项目必须同类型或可兼容

- 可以为NULL的列如何插入值：

- 列的顺序可以调换

- 列数和值的个数必须一致（就算插入的数据为null，也不可以省略）

- 省略列名，默认所有列，而且列的顺序和表中列的顺序一致

## 2.修改语句

语法：

```sql
update 表名
set 列 = 新值，列 = 新值，...
where 筛选条件
#sql92
update 表1 别名，表2别名
set 列 = 值，列 = 值
where 连接条件
and 筛选条件
#sql99
update 表1 别名
inner | left | right join 表2 别名
on 连接条件
set 列 = 值，列 = 值
where 筛选条件
```

## 3.删除语句

### delete

语法：

```sql
#1.单表的删除
delete from 表名 where 筛选条件 
#2.多表的删除
#sql92
delete 别名
from 表1 别名，表2，别名
where 连接条件
and 筛选条件
#sql99
delete 表1的别名，表2的别名
from 表1 别名
inner | left | right join 表2 别名
on连接条件
where 筛选条件
```

用例：

```sql
#eg.删除张无忌的女朋友的信息
delete b
from beauty b
inner join boys bo
on b.boyfriend_id = bo.id
where bo.boyName='张无忌';
```

### truncate 

不允许加where，也叫做清空数据

语法：

```sql
truncate table 表名
```

特点：

- delete可以加where条件，truncate不能加

- truncate删除效率高一点

- 加入要删除的表中有自增长列，用delete删除后，再插入数据，自增长列的值从断点开始；而truncate删除后，再插入数据，自增长列的值从1开始

- truncate删除没有返回值，delete删除有返回值

- truncate删除不能回滚，而delete删除可以回滚

# 四、DDL语言

## 1.库的管理

创建

```sql
create database 库名;
```

修改

```sql
rename database <库名> to <新库名>
alter database <库名> character set gbk
```

删除

```sql
drop database <库名>
#通用的写法：
DROP DATABASE IF EXISTS <旧库名>;
```

## 2.表的管理

创建

```sql
create table <> 表名(
	列名 列的类型【(长度) 约束】,
	列名 列的类型【(长度) 约束】,
	列名 列的类型【(长度) 约束】,
);
```

修改

```sql
#1.修改列名
ALTER TABLE <表名> CHANGE COLUMN <原列名> <新列名> <新类型>;
#2.修改列的类型或约束
ALTER TABLE <表名> MODIFY COLUMN <列名> <新类型>;
#3.添加新列
ALTER TABLE <表名> ADD COLUMN <新列名> <类型>;
#4.删除列
ALTER TABLE <表名> DROP COLUMN <列名>
#5.修改表名
ALTER TABLE <表名> RENAME TO <新表名>;
```

删除

```sql
DROP TABLE <表名>;
```

表的复制

```sql
#1.仅仅复制表的结构
CREATE TABLE <新表> LIKE <旧表>;
#2.复制表的结构+数据
CREATE TABLE <新表>
SELECT * FROM <旧表>;
#3.只复制部分数据
CREATE TABLE <新表>
SELECT <列名1>,<列名2>,...
FROM <旧表>
WHERE <筛选条件>;
#4.仅仅复制某些字段
CREATE TABLE <新表>
SELECT <列名1>,<列名2>,...
FROM <旧表>
WHERE 0;
```

## 3.数据类型

### 3.1数值型

#### 3.1.1整型

| 整数类型     | 字节 | 范围                                                         |
| ------------ | ---- | ------------------------------------------------------------ |
| TinyInt      | 1    | 有符号：-128~127<br/>无符号：0~255                           |
| SmallInt     | 2    | 有符号：-32768~32767<br/>无符号：0~65535                     |
| MediumInt    | 3    | 有符号：-8388608~8388607<br/>无符号：0~1677215               |
| Int、Integer | 4    | 有符号：-2147483648~2147483647<br/>无符号：0~4294967295      |
| BigInt       | 8    | 有符号：-9223372036854775808~9223372036854775807<br/>无符号：0~9223372036854775807*2+1 |

特点：

- 如果不设置无符号还是有符号，默认是有符号，如果想设置无符号，添加unsigned关键字
- 如果插入的数值超出了范围，会报错
- 如果不设置长度，会有默认的长度
- 长度代表了显示的最大宽度，如果不够会用0在左边填充

#### 3.1.2小数

浮点数

| 浮点数类型 | 字节 | 范围 |
| ---------- | ---- | ---- |
| float      | 4    |      |
| double     | 8    |      |

定点数

| 定点数类型                | 字节 | 范围                                                         |
| ------------------------- | ---- | ------------------------------------------------------------ |
| DEC(M,D)<br/>DECIMAL(M,D) | M+2  | 最大取值范围与double相同，给定decimal的有效取值范围由M和D决定 |

特点：

- M：整数部位+小数部位；D：小数部位；如果超过范围，则插入临界值

- M和D都可以省略，如果是decimal，则M默认为10，D默认为0；如果是float和double，则会根据插入的数值的精度来决定精度

- 定点型的精确度较高，如果要求插入数值的精度较高如货币运算等则考虑使用

原则：

- 所选择的类型越简单越好，保存的数值的类型越小越好

### 3.2字符型

#### 较短的文本：char、varchar

| 字符串类型 | 最多字符数 | 描述及存储需求       |
| ---------- | ---------- | -------------------- |
| char(M)    | M          | M为0-255之间的整数   |
| varchar(M) | M          | M为0-65535之间的证书 |

特点：char固定长度，varchar可变长度；char比较耗空间，varchar比较节省，char效率高，varchar效率低。

应用场景：性别 char(1)，

#### 较长的文本：text、blob（较长的二进制数据）

其他：

#### enum 

不区分大小写

又称为枚举类型，要求插入的值必须属于列表中指定的值之一

如果列表成员为1-255，则需要1个字节存储

如果列表成员为255-65535，则需要2个字节存储

最多需要65535个成员

#### set

不区分大小写

和enum类型类似，里面可以保存0-64个成员。和enum类型最大的区别是：set类型一次可以选取多个成员，而enum只能选一个，根据成员个数不同，存储所占的字节也不同。

binary和varbinary用于保存较短的二进制

### 3.3日期型

![image-20230321170232595](MySQL_imgs\wMMMLJmhs5h.png)

![image-20230321170243481](MySQL_imgs\lmTWwEqpBDg.png)

## 4.常见约束

含义：一种限制，用于限制表中的数据，为了保证表的数据的准确和可靠性

分类：六大约束

**NOT NULL**：非空，用于保证该字段的值不能为空，比如姓名、学号等

**DEFAULT**：默认，用于保证该字段有默认值，比如性别

**PRIMARY KEY**：主键，用于保证该字段的值具有唯一性，并且非空，一个表只能有一个，允许但不推荐，比如学号、员工编号等

**UNIQUE**：唯一，用于保证该字段的值具有唯一性，可以为空，一个表可以有多个，允许但不推荐比如座位号

**CHECK**：检查约束【mysql中不支持】，比如年龄、性别

**FOREIGN KEY**：外键，用于限制两个表的关系，用于保证该字段的值必须来自于主表的关联列的值。在从表添加外键约束，用于引用主表中某列的值。比如学生表的专业编号，员工表的部门编号，员工表的工种编号。

特点：1.要求在从表设置外键关系；2.从表的外键列的类型和主表的关联列的类型一致或兼容；

添加约束的时机；3.主表的关联列必须是一个key（一般是主键或唯一）；4.插入数据是，先插入主表，再插入从表；删除数据是，先删除从表，再删除主表

### 4.1.创建表时

必须在数据添加之前添加约束

约束的添加分类：

**列级约束**：六大约束语法上都支持，但外键约束没有效果

```sql
create table stuinfo (
    id int primary key,
    stuName varchar(20) not null,
    gener char(1) check(gender='男' or gender='女'),
    seat int unique,
    age int default 18,
    majorId int foreign key references major(id)
);
```

**表级约束**：除了非空、默认、其他都支持

语法 【constraint 约束名】 约束类型（字段名）

```sql
create table stuinfo (
    id int ,
    stuName varchar(20) ,
    gener char(1) ,
    seat int ,
    age int ,
    majorId int ,
    constraint pk primary key(id),
    constraint uq unique(seat),
    constraint ck check(gender = '男' or gender = '女'),
    constraint fk_stuinfo_major foreign key(majorid) references major(id)
);
```

**通用的写法**

```sql
create table if exists stuinfo(
    if int primary key,
    stuname varchar(20) not null,
    sex char(1),
    age int default 18,
    seat int unique,
    majorid int,
    constraint fk_stuinfo_major foreign key(majorid) references major(id)
)
```

### 4.2修改表时

```SQL
#1.添加非空约束
alter table stuinfo modify column stuname varchar(20) not null;
#2.添加默认约束
alter table stuinfo modify column age int deafult 18
#3.添加主键
alter table stuinfo modify column id int primary key;
alter table stuinfo add primary key(id);
#4.添加唯一
alter table stuinfo modift column seat int unique;
alter table stuinfo add unique(seat);
#5.添加外键
alter table stuinfo add constraint foreign key(majorid) references major(id);
```

### 4.3修改表时删除约束

```SQL
#1.删除非空约束
alter table stuinfo modify column stuname varchar(20) null;
#2.删除默认约束
alter table stuinfo modify column age int;
#3.删除主键
alter table stuinfo drop index <主键名>;
show index from <表名>;
#4.删除唯一
alter table stuinfo drop index <唯一键名>;
#5.删除外键
alter table stuinfo drop foreign key<外键名>;
```

**标识列**

又称为自增长列

含义：可以不用手动的插入值，系统提供默认的序列值

特点：1.标识列必须和主键搭配吗？不一定，但要求是一个key；2.一个表可以有几个标识列？至多一个！；3.标识列的类型只能是数值型；4.标识列可以通过set auto_increment_increment=3设置

```SQL
#1.创建表时设置标识列
create table tab_identity (
    id int primary key auto_increment,
    name varchar(20)
);
insert into tab_identity values(1,'john');
#2.修改表时设置标识列
alter table tab_identity modify column id int primary key auto_incremnet;
#3.修改表时删除标识列
alter table tab_identity modift column id int;
```

#  五、TCL语言

transaction control language 事务控制语言

事务：一个或一组sql语句组成一个执行单元，这个执行单元要么全部执行，要么全部不执行。

案例：转账

存储引擎：

1. 在mysql中的数据用各种不同的计数存储在文件（或内存）中

2. 通过show engines来查看mysql支持的存储引擎

3. 在mysql中用的最多的存储引擎有：innodb，myisam，memory等。其中innodb支持事务，而myisam，memory等不支持事务。

事务的ACID属性

1. 原子性：Atomicity：原子性是指事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生

2. 一致性：Consistency：事务必须使数据库从一个一致性状态到另一个一致性的状态。

3. 隔离性：Isolation：事务的隔离性是指一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。

4. 持久性：Durability：持久性是指一个事务一旦被提交，它对数据库中的数据的改变就是永久性的，接下来的其他操作和数据库故障都不应该对其有任何影响。

事务的创建：

- 隐式事务：事务没有明显的开启和结束的标记。
  - 比如：insert、update、delete

- 显示事务：事务具有明显的开启和结束的标记。

  - 前提：比如先把自动提交功能关闭

  - set autocomit=0;

开启事务的语句：

```SQL
#步骤1：开启事务
set autocommit=0;
start transaction;可选的
#步骤2：编写事务中的sql语句(select insert update delete)
语句1；
语句2；
……
#步骤3：结束事务
commit；提交事务
rollback；回滚事务
savepoint;保存点，只搭配rollback使用
```

当多个事务同时访问数据库中相同的数据时，如果没有采取必要的隔离机制，就会导致各种并发的问题

- **脏读**：对于两个事务T1，T2，T1读取了已经被T2更新但还没有被提交的字段之后，若T2回滚，T1读取的内容就是临时且无效的。

- **不可重复读**：对于两个事务T1，T2，T1读取了一个字段，然后T2更新了该字段之后，T1再次读取他一字段，值就不同了。

- **幻读**：对于两个事务T1，T2，T1从一个表中读取了一个字段，然后T2在该表中插入了一些新行。之后，如果T1再次读取同一个表，就会多出几行。

数据库提供的4种事务隔离级别

![image-20230321173431178](MySQL_imgs\g1naHmDPu5P.png)

Oracle支持的2种事务隔离级别：read commited，serializable。Oracle默认的事务隔离级别为：read commited。

mysql支持4种事务隔离级别。Mysql默认的事务隔离级别为：repeatable read。

#  六、视图

含义：虚拟表，和普通表一样使用

特点：动态生成，只保存了sql逻辑，不保存查询结果

语法：

```sql
#1.创建
CREATE VIEW <视图名>
AS
SELECT……
#2.使用（当正常的表一样使用）
SELECT <视图名>.<列名> FROM <视图名>
#3.修改
ALTER VIEW <视图名>
AS
SELECT……
#4.删除
DROP VIEW <视图名>,<视图名>,……
#5.查看
DESC <视图名>; 
```

