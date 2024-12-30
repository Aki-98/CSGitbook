# 【同一个电脑上添加两个github仓库】

https://blog.csdn.net/qq_34634812/article/details/90168486



# 【windows下启动git bash每次启动自动添加ssh-agent和ssh-add密钥】

https://blog.csdn.net/wobofan2006/article/details/126505622



# 【Git: ‘LF will be replaced by CRLF the next time Git touches it‘ 问题解决与思考】

[Git: ‘LF will be replaced by CRLF the next time Git touches it‘ 问题解决与思考-CSDN博客](https://blog.csdn.net/Babylonxun/article/details/126598477)



# 【push 大文件时可能遇到的问题，网络缓存不够】

```
## 设置http缓存为1000M（大小可以根据需要自行更改）
git config --global http.postBuffer 1048576000 
## 设置https缓存为1000M
git config --global https.postBuffer 1048576000
```



# 【修改了`.gitignore`文件中的规则，之前的commit有需要忽略的文件，可以清除缓存区后重新提交】

清空缓存区：

```
git rm -r --cached .
```



# 【比较同一分支两个提交之间的差别】

https://github.com/sony-netapp/HomeAccount4China/compare/a90579c3f95667aff72cd0f630db42dd72d5ade3...bb95b720cbf7ef2acb7d14c8f816e7bd194c2c54



# 【删除本地不存在于远程的分支】

```
git fetch --prune

git branch -vv | grep ': gone]' | awk '{print $1}' | xargs -r git branch -d
```



# 【修改Commit-msg】

```
git commit --amend //长消息
git commit --amend -m "" //短消息
git push --force
```



# 【怎样解决不小心将修改提交到本地的主分支无法触发PR的问题】

1.将本地的主分支重命名为PR分支名称

```shell
git branch -m Main PR
```

2.将本地的PR分支Push到远程的同时，重新设置upstream分支

原本upsteam分支应该设置为了主分支，如果不重新设置会push到主分支上

```shell
git push origin --set-upstream origin PR
```

3.重新从远程拉取开发分支

```shell
git checkout Main
```

4.创建PR



# 【怎样解决不小心将修改提交到远程的主分支无法触发PR的问题】

1.将本地的主分支重命名为PR分支名称

```shell
git branch -m Main PR
```

2.将本地的PR分支Push到远程的同时，重新设置upstream分支

原本upsteam分支应该设置为了主分支，如果不重新设置会push到主分支上

```shell
git push origin --set-upstream origin PR
```

3.重新从远程拉取开发分支

```shell
git checkout Main
```

4.将commit reset 到修改前的节点，并push --force到远程

```shell
git reset --hard 107d523a2fa7540421a65476c28313de44c3da4c
```

5.创建PR



# 【删除本地不存在于远程的分支】

```shell
git fetch --prune

git branch -vv | grep ': gone]' | awk '{print $1}' | xargs -r git branch -d
```



# 【在Commit中删除新加入gitignore的文件】

```
git rm --cached <文件路径>
然后正常commit即可
```



# 【替换Commit历史记录中的AuthorEmail，删除Remote】

```
//可能要多次执行
git filter-branch --env-filter 'OLD_EMAIL="aki_98@163.com"; CORRECT_NAME="5109U25854"; CORRECT_EMAIL="qingqiu.li@sony.com"; if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then export GIT_COMMITTER_NAME="$CORRECT_NAME"; export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"; fi; if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then export GIT_AUTHOR_NAME="$CORRECT_NAME"; export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"; fi;' --tag-name-filter cat -- --branches --tags

```

执行完后删除.git\refs\original 和 .git\refs\remote下的文件



# 【如何排除gitignore的文件后打包整个仓库？】

```shell
git clone D:\\temp\\Automation D:\\temp\\Automation_LQQ_OnTracked
```

打包temp仓库



# 【修改远程分支的名字】

要修改 Git 远程分支的名字，可以按照以下步骤进行：

1. 重命名本地分支

首先，将本地的分支名称修改为新的名称。

```
# 切换到你想要重命名的分支
git checkout old-branch-name

# 重命名本地分支
git branch -m new-branch-name
```

2. 删除远程的旧分支

将旧的远程分支删除：

```
# 删除远程的旧分支
git push origin --delete old-branch-name
```

3. 推送新分支到远程仓库

将新命名的本地分支推送到远程仓库：

```
git push origin new-branch-name
```

4. 设置新的远程追踪分支（可选）

推送新分支后，Git 不会自动将它设置为追踪分支。你可以通过以下命令让本地分支追踪新的远程分支：

```
git branch --set-upstream-to=origin/new-branch-name
```

5. 清理旧的本地远程分支引用（可选）

最后，你可以清理掉对旧的远程分支的本地引用：

```
git fetch --prune
```
