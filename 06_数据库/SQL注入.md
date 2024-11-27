SQL注入（SQL Injection）是一种代码注入攻击技术，攻击者通过在应用程序的输入字段中插入或“注入”恶意的SQL代码，从而改变预期的SQL查询。这样，攻击者可以绕过应用程序的安全检查，执行未经授权的操作，比如读取、修改、删除数据库中的数据，甚至获取系统权限。

### SQL注入的工作原理

当应用程序直接将用户输入的数据嵌入到SQL查询中，而不进行适当的校验和处理时，就会导致SQL注入。例如，假设有一个登录系统，用户输入用户名和密码，这些输入被直接拼接到SQL查询中：

```sql
SELECT * FROM users WHERE username = 'user_input' AND password = 'user_password';
```

如果攻击者在用户名字段中输入`' OR '1'='1`，密码字段中输入`' OR '1'='1`，则查询将变为：

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '' OR '1'='1';
```

由于`'1'='1'`始终为真，SQL查询将返回所有用户，攻击者因此能够绕过身份验证。

### SQL注入的危害

1. **数据泄露**：攻击者可以读取数据库中的敏感信息。
2. **数据篡改**：攻击者可以修改或删除数据库中的数据。
3. **权限提升**：攻击者可能通过SQL注入获取更高的权限，控制整个系统。
4. **持久后门**：攻击者可以在数据库中插入恶意代码，建立持久的后门。

### 防御SQL注入的方法

1. **使用参数化查询（Prepared Statements）**：避免直接拼接SQL查询字符串，使用占位符和绑定变量来传递用户输入。

   ```java
   String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
   PreparedStatement statement = connection.prepareStatement(sql);
   statement.setString(1, username);
   statement.setString(2, password);
   ResultSet resultSet = statement.executeQuery();
   ```

2. **使用存储过程**：将SQL逻辑放在数据库中，通过调用存储过程来执行查询。

3. **输入验证**：严格验证和过滤用户输入，拒绝或转义包含特殊字符的输入。

4. **最小权限原则**：限制应用程序对数据库的权限，仅授予执行所需操作的最低权限。

5. **安全框架**：使用安全框架和ORM（对象关系映射）工具，它们内置了防SQL注入的机制。

通过以上方法，可以有效防止SQL注入攻击，保护应用程序和数据的安全。