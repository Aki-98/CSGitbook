# Branch

一个快照构成的连续的单向链表称作分支，每个分支有一个指向该分支快照的指针

在git中路径也被当做文件夹处理

每次提交会创建一个子版本，子版本来自于上一个父版本

这一系列的版本称为branch/stream。在git中main stream称作HEAD

所谓分支（branch）就是指向某个快照的指针，分支名就是指针名。

分支会自动更新，如果当前分支有新的快照，指针就会自动指向它。

Git 有一个特殊指针HEAD， 总是指向当前分支的最近一次快照。Git 还提供简写方式，HEAD^指向 HEAD的前一个快照（父节点），HEAD~6则是HEAD之前的第6个快照。

每一个分支指针都是一个文本文件，保存在.git/refs/heads/目录，该文件的内容就是它所指向的快照的二进制对象名（哈希值）。

# Merge

合并拥有同一父节点的分支

![image-20220315112026957](Git-操作原理_imgs\image-20220315112026957.png)

git merge –abort

There are changes in both branches, but they conflict. In this case, the conflicting result is left in the working directory for the user to fix and commit, or to abort the merge with git merge –abort.

# Rebase

重定向分支指针

![image-20220315111450866](Git-操作原理_imgs\image-20220315111450866.png)

## CherryPick

选一个分支中一个或者几个commit来应用提交到另外一个分支

![image-20220315112009109](Git-操作原理_imgs\image-20220315112009109.png)

# Revert

![image-20220315112501885](Git-操作原理_imgs\image-20220315112501885.png)