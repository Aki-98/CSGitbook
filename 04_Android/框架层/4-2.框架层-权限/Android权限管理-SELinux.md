**SELinux运行的三种状态**

| 状态       | 解析                                          |
| ---------- | --------------------------------------------- |
| Enforcing  | SELinux security policy is enforced.          |
| Permissive | SELinux prints warnings instead of enforcing. |
| Disabled   | SELinux is fully disabled.                    |

**查看SELinux运行状态**

```shell
getenforce 
```

**切换到Permissive状态**

```shell
setenforce 0
```

**切换到Enforcing状态**

```shell
setenforce 1
```

这种切换方式不用重启机器，但是该命令只能将SELinux在enforcing、permissive这两种模式之间切换，重启服务器后，又会恢复到etc/selinux/config下，也就是说setenforce的修改不能持久

另外就是修改/etc/selinux/config，如下所示，可以配置SELinux为enforcing、permissive、disabled三个值，修改后必须重启系统才能生效。

```vim
[root@DB-Server ~]# more /etc/selinux/config
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#       enforcing - SELinux security policy is enforced.
#       permissive - SELinux prints warnings instead of enforcing.
#       disabled - SELinux is fully disabled.
SELINUX=enforcing
# SELINUXTYPE= type of policy in use. Possible values are:
#       targeted - Only targeted network daemons are protected.
#       strict - Full SELinux protection.
SELINUXTYPE=targeted
You have new mail in /var/spool/mail/root
```

如果由 enforcing 或 permissive 改成 disabled，或由 disabled 改成其他两个，那也必须要重新开机。这是因为 SELinux 是整合到核心里面去的，你只可以在SELinux 运作下切换成为强制 (enforcing) 或宽容 (permissive) 模式，不能够直接关闭 SELinux 的！同时，由 SELinux 关闭 (disable) 的状态到开启的状态也需要重新开机啦。

**查看avc log**

```shell
logcat | grep avc
$ sudo grep "avc:" /var/log/audit/audit.log
```

**查看文件的安全上下文**

```
ls -Z
```

**查看进程的安全上下文**

```
ps -Z
```
