# Repo

## 初始化

```
$ git init
```

git init命令只做一件事，就是在项目根目录下创建一个.git子目录，用来保存版本信息。

```
$ ls .git

branches/
config
description
HEAD
hooks/
info/
objects/
refs/
```

## 配置

查看版本

```
git --version
```



配置全局用户名和邮箱

```
git config —global user.name “name”
git config —global user.email “email address”
```



配置当前仓库用户名和邮箱

```
git config user.name “name”
git config user.email “email address”
```



找到.gitconfig文件

```
git config --list --show-origin
```



查看远程仓库

```shell
git remote -v
```



关联远程仓库

```bash
git remote add origin git@github.com:sony-netapp/SearchApp4China.git
```



删除远程仓库

```shell
git remote rm <repo-name>
```



修改远程 Git 仓库的地址

```
git remote set-url <remote-name> <new-url>
```

# WorkZone

## 快照

放弃工作区中全部的修改
````
git checkout .
````

放弃工作区中某个文件的修改：

```
git checkout -- filename
```

列出缓存区中文件与上一次提交的区别（新增、更改、删除）

```
git status
```

生成快照

```
git commit -m "commit message"
```

切换快照

```
git checkout {snapchat-hash}
```

展示某个快照的所有代码改动

```
git show {snapchat-hash}
```

查看本地提交历史

```
git log
```

显示可引用的本地历史版本记录

```
git reflog
```

强制跳转回退到某个版本

```
git reset --hard <snapshot-hashcode>
```

## 缓存区

### add

会提交当前工作区中当前目录(包括子目录)下所有的文件改动。

注意：在Git Version 1.x中：会将当前工作区中当前目录(包括子目录)下的所有新文件和对已有文件的改动提交至暂存区，但不包括被删除的文件。

```
git add .
```



只会监控当前整个工作区中之前已被 `add` 的文件，即已被跟踪(tracked)的文件，也就是只会将当前整个工作区中被修改和被删除的文件提交至暂存区。而新文件因为未被跟踪(untracked)，所以不会被提交至暂存区。

```
git add -u
git add --update
```



它会将当前整个工作区中所有的文件改动提交至暂存区，包括新增、修改和被删除的文件，不受当前所在目录限制

注意： `git add -A` 不属于 `git add .` 和 `git add -u` 。因为 `git add .` 只会提交当前目录(包括子目录)下的新文件和对已有文件的改动，而 `git add -A` 不受当前目录限制。也就是说，`git add .` 和 `git add -u` 功能的合集只能属于 `git add -A` 功能的子集。

```
git add -A
git add --all
```



添加单个文件

```
git add <file-name>
```



表示添加当前目录(包括子目录)下的所有文件改动，但不包括文件名以 `.` 符号开头的文件的改动

```
git add *
```



### reset

从暂存区中删除文件，相当于git add 的撤销操作

```
git reset .
```

回退到某次commit但不修改本地文件

```
git reset --soft <commit_hash>
```



### rm

从缓存区中删除的意思是不再跟踪此文件的修改

不删除物理文件，仅将该文件从缓存中删除

```
git rm --cached <文件路径/文件名>
```



不仅将该文件从缓存中删除，还会将物理文件删除（不会回收到垃圾桶）

```
git rm --f <文件路径/文件名>
```





### clean

删除不在缓存区的文件

```
git clean -f #删除文件
git clean -fd #删除文件和目录
git clean -xfd #不会连 gitignore 的untrack 文件/目录也一起删掉 (慎用,一般这个是用来删掉编译出来的 .o之类的文件用的)  
git clean -nxfd # 在用上述 git clean 前,墙裂建议加上 -n 参数来先看看会删掉哪些文件,防止重要文件被误删
```



## 提交

将本地git记录添加到远程

```
git commit -m "modify DownloadUri from PRD to DEV"
git commit 后在vim编辑提交说明，shift+zz保存退出
```



如果当前分支与多个主机存在追踪关系，则可以使用 -u 参数指定一个默认主机，这样后面就可以不加任何参数使用git push

```
git push -u <remote-name> <branch-name>
```



强制提交，回退版本时使用

```
git push -f
```



# Branch

## 本地

查看本地分支

```bash
git branch
```



在本地创建新分支

```
git branch <local-branch-name> 
```



creates a new branch from the current HEAD, and switches the working directory to the new branch

```
git checkout -b <local-branch-name>
```



拉取远程分支并merge到本地

```
git pull origin <local-branch-name>:<remote-branch-name>
```



删除本地分支

```
git branch -d <local-branch-name> 
```



查看所有分支

```
git branch -a
```



修改分支名字

```
git branch -m <old-name> <new-name>
```



合并两个分支，处于哪个分支，就合并到哪个分支上

```
git merge A //将A分支合并到当前分支上
git merge A B //将A分支和B分支合并到当前分支上
```



## 远程

创建远程分支

```
git push origin origin_branch:local_branch
```

查看远程分支的提交

```
git log origin/branch-name
git log HEAD...origin/branch-name
```

切换到远程分支

```
git checkout -b new-branch-name remote-branch-name
git checkout -b sony/banko/s-develop-01 origin/sony/banko/s-develop-01
```

删除远程分支

```
git push origin --delete pullrequest_Valhalla2_dev
```

拉取远程仓库最新更新

```
git pull origin
```



# Commit

修改上一次的commit-msg，后面不要接新的message，进入vim修改

```java
git commit --amend
```



# Tag

本地创建

```shell
git tag v0.1
```

本地删除（不会删除远程的标签）

```shell
git tag -d v0.1
```

推送本地标签到远程

```shell
git push origin v0.1
```

一次性推送全部尚未推送到远程的本地标签

```shell
git push origin --tags
```

从远程删除标签

```shell
git push origin :refs/tags/v0.1
```



# Merge

列出冲突的文件

```shell
git diff --name-only --diff-filter=U
```



# Patch的使用

打patch

```shell
//将暂存区的文件与上一次Commit生成patch包
git diff --cached > changes.patch 
```

使用补丁

```shell
git apply changes.patch
```



# Rebase的使用

1.可以修改Commit-msg和commit内的文件内容

```shell
git rebase -i HEAD~N
```

2.在弹出的界面中pick -- > edit修改commit消息

3.输入下面的命令开始修改

```shell
git commit --amend
```

4.输入下面的命令保存

```shell
git rebase --continue
```

5.回到第三步继续修改
