Android使用repo来管理多个Git项目。它需要一个manifest XML文件来指示这些git项目的属性。

# Manifest

repo manifest XML可以包含下面的元素。
以如下，manifest片段为例：https://github.com/CyanogenMod/android

```xml
<?xml version="1.0" encoding="UTF-8"?>

<manifest>

<remote name="github"
fetch=".."
review="review.cyanogenmod.org" />
<remote name="private"
fetch="ssh://git@github.com" />
<remote name="aosp"
fetch="https://android.googlesource.com"
review="android-review.googlesource.com"
revision="refs/tags/android-7.1.1_r6" />
<default revision="refs/heads/cm-14.1"
remote="github"
sync-c="true"
sync-j="4" />
    
<!-- AOSP Projects -->
<project path="build" name="CyanogenMod/android_build" groups="pdk,tradefed">
<copyfile src="core/root.mk" dest="Makefile" />
</project>
<project path="build/blueprint" name="platform/build/blueprint" groups="pdk,tradefed" remote="aosp" />
<project path="build/kati" name="CyanogenMod/android_build_kati" groups="pdk,tradefed" />
<project path="build/soong" name="platform/build/soong" groups="pdk,tradefed" remote="aosp" >
<linkfile src="root.bp" dest="Android.bp" />
<linkfile src="bootstrap.bash" dest="bootstrap.bash" />
</project>
<project path="abi/cpp" name="platform/abi/cpp" groups="pdk" remote="aosp" />
<project path="art" name="CyanogenMod/android_art" groups="pdk" />
    
</manifest>
```

## Manifest元素

最顶层的XML元素

## remote元素

设置远程git服务器的属性，包括下面的属性：

- name: 远程git服务器的名字，直接用于git fetch, git remote 等操作
- alias: 远程git服务器的别名，如果指定了，则会覆盖name的设定。在一个manifest中， 
- name不能重名，但alias可以重名。
- fetch: 所有projects的git URL 前缀
- review: 指定Gerrit的服务器名，用于repo upload操作。如果没有指定，则repo upload没有效果。

一个manifest文件中可以配置多个remote元素，用于配置不同的project默认下载指向。

## default元素

设定所有projects的默认属性值，如果在project元素里没有指定一个属性，则使用default元素的属性值。

- remote: 之前定义的某一个remote元素中name属性值，用于指定使用哪一个远程git服务器。
- revision: git分支的名字，例如master或者refs/heads/master
- sync_j: 在repo sync中默认并行的数目。
- sync_c: 如果设置为true，则只同步指定的分支(revision 属性指定)，而不是所有的ref内容。
- sync_s: 如果设置为true，则会同步git的子项目

Example:

    <default remote="main" revision="platform/main"/>

## project元素

指定一个需要clone的git仓库。

- name: 唯一的名字标识project，同时也用于生成git仓库的URL。格式如下：
        ${remote_fetch}/${project_name}.git
- path: 可选的路径。指定git clone出来的代码存放在本地的子目录。如果没有指定，则以name作为子目录名。
- remote: 指定之前在某个remote元素中的name。
- revision: 指定需要获取的git提交点，可以是master, refs/heads/master, tag或者SHA-1值。如果不设置的话，默认下载当前project，当前分支上的最新代码。
- groups: 列出project所属的组，以空格或者逗号分隔多个组名。所有的project都自动属于"all"组。每一个project自动属于name:'name' 和path:'path'组。
  例如<project name="monkeys" path="barrel-of"/>，它自动属于default, name:monkeys, and path:barrel-of组。如果一个project属于notdefault组，则，repo sync时不会下载。
- sync_c: 如果设置为true，则只同步指定的分支(revision 属性指定)，而不是所有的ref内容。
- sync_s: 如果设置为true，则会同步git的子项目。
- upstream: 在哪个git分支可以找到一个SHA1。用于同步revision锁定的manifest(-c 模式)。该模式可以避免同步整个ref空间。
- annotation: 可以有多个annotation，格式为name-value pair。在repo forall 命令中这些值会导入到环境变量中。
- remove-project: 从内部的manifest表中删除指定的project。经常用于本地的manifest文件，用户可以替换一个project的定义。

### 子元素

Project元素下面会有两个子元素。Copyfile和linkfile

```xml
<copyfile src="core/root.mk" dest="Makefile" />
<linkfile src="root.bp" dest="Android.bp" />
```

- Copefile:复制，cp src dest

- Linkfile：软链接 ，ln -s src dest

# Repo

## 安装repo

在ubuntu中可以通过命令进行repo的安装：

```shell
Sudo apt-get install repo
```

也可以直接下载repo文件，然后将路径配置到环境变量里面。

```shell
$ mkdir ~/bin
$ PATH=~/bin:$PATH
$ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
$ chmod a+x ~/bin/repo
```

## Repo help

安装 Repo 后，您可以通过运行以下命令找到最新文档（开头是包含所有命令的摘要）：

```shell
repo help
```

您可以通过在 Repo 树中运行以下命令来获取有关某个命令的信息：

```shell
repo help <COMMAND>
```


例如，以下命令会生成 Repo init 参数的说明和选项列表，该参数会在当前目录中初始化 Repo。（要了解详情，请参阅 init。）

```shell
repo help init
```

## Repo init

Usage

```shell
repo init –u URL [OPTIONS]
```


在当前目录中安装 Repo。这会创建一个 .repo/ 目录，其中包含用于 Repo 源代码和标准 Android 清单文件的 Git 代码库。该 .repo/ 目录中还包含 manifest.xml，这是一个指向 .repo/manifests/ 目录中所选清单的符号链接。

Options:

- u：指定一个URL，其连接到一个manifest仓库
- m：在manifest仓库中选择一个xml文件，如果未选择，默认指向default.xml
- b：选择一个maniest仓库中的一个特殊的分支
- --mirror：下一步和源同步的时候，本地按照源的版本库组织方式进行组织
- --reference=<path>：path为一个镜像地址，从镜像同步代码。
- --repo-url=<url>：url为repo 库的位置，用于修改repo文件中REPO-URL参数的指向。

命令repo init 要完成如下操作：

- 完成repo工具的完整下载，执行的repo脚本只是引导程序
- 克隆清单库manifest.git (地址来自于-u 参数)
- 克隆的清单库位于manifest.git中，克隆到本地.repo/manifests.清单.repo/manifest.xml只是符号链接，它指.repo/manifests/default.xml
- 如果manifests中有多个xml文件，repo init 可以任意选择其中一个，默认选择是default.xml

## Repo sync

Usage

```shell
repo sync [<PROJECT_LIST>]
```

下载新的更改并更新本地环境中的工作文件。如果您在未使用任何参数的情况下运行 repo sync，则该操作会同步所有项目的文件。
运行 repo sync 后，将出现以下情况：

- 如果目标项目从未同步过，则 repo sync 相当于 git clone。远程代码库中的所有分支都会复制到本地项目目录中。
- 如果目标项目已同步过，则 repo sync 相当于以下命令：

```shell
git remote update
git rebase origin/<BRANCH>
```


其中 <BRANCH> 是本地项目目录中当前已检出的分支。如果本地分支没有在跟踪远程代码库中的分支，则相应项目不会发生任何同步。

如果 git rebase 操作导致合并冲突，那么您需要使用普通 Git 命令（例如 git rebase --continue）来解决冲突。repo sync 运行成功后，指定项目中的代码会与远程代码库中的代码保持同步。

Option:

- d：将指定项目切换回清单修订版本。如果项目当前属于某个主题分支，但只是临时需要清单修订版本，则此选项会有所帮助。
- s：同步到当前清单中清单服务器元素指定的一个已知的良好版本。
- f：即使某个项目同步失败，系统也会继续同步其他项目。

## Repo start

Usage

```shell
repo start <BRANCH_NAME> [<PROJECT_LIST>]
```


从清单中指定的修订版本开始，创建一个新的分支进行开发。

- <BRANCH_NAME> 参数应简要说明您尝试对项目进行的更改。如果您不知道，则不妨考虑使用默认名称。

- <PROJECT_LIST> 指定了将参与此主题分支的项目。

## Repo diff

Usage

```shell
repo diff [<PROJECT_LIST>]
```


使用 git diff 显示提交与工作树之间的明显更改。

## Repo prune

Usage

```shell
repo prune [<PROJECT_LIST>]
```

删减（删除）已合并的主题。

## Repo status

Usage

```shell
repo status [<PROJECT_LIST>]
```

对于每个指定的项目，将工作树与临时区域（索引）以及此分支 (HEAD) 上的最近一次提交进行比较。在这三种状态存在差异之处显示每个文件的摘要行。

要仅查看当前分支的状态，请运行 repo status。系统会按项目列出状态信息。对于项目中的每个文件，系统使用两个字母的代码来表示：

在第一列中，大写字母表示临时区域与上次提交状态之间的不同之处。

```shell
{|
| 字母 || 含义 || 说明
|-
| - || 无更改 || HEAD 与索引中相同
|-
| A || 已添加 || 不存在于 HEAD 中，但存在于索引中
|-
| M || 已修改 || 存在于 HEAD 中，但索引中的文件已修改
|-
| D || 已删除 || 存在于 HEAD 中，但不存在于索引中
|-
| R || 已重命名 || 不存在于 HEAD 中，但索引中的文件的路径已更改
|-
| C || 已复制 || 不存在于 HEAD 中，已从索引中的另一个文件复制
|-
| T || 模式已更改|| HEAD 与索引中的内容相同，但模式已更改
|-
| U || 未合并 || HEAD 与索引之间存在冲突；需要解决方案
|}
```

在第二列中，小写字母表示工作目录与索引之间的不同之处。

```
{|
| 字母 | 含义 | 说明
|-
| - | 新/未知 | 不存在于索引中，但存在于工作树中
|-
| m | 已修改 | 存在于索引中，也存在于工作树中（但已修改）
|-
| d | 已删除 | 存在于索引中，不存在于工作树中
|}
```

## Repo forall

Usage

```shell
repo forall [<PROJECT_LIST>] -c <COMMAND>
```


在每个项目中运行指定的 shell 命令。通过 repo forall 可使用下列额外的环境变量：

- REPO_PROJECT 可设为项目的具有唯一性的名称。
- REPO_PATH 是客户端根目录的相对路径。
- REPO_REMOTE 是清单中远程系统的名称。
- REPO_LREV 是清单中修订版本的名称，已转换为本地跟踪分支。如果您需要将清单修订版本传递到某个本地运行的 Git 命令，则可使用此变量。
- REPO_RREV 是清单中修订版本的名称，与清单中显示的名称完全一致。

Option：

- c：要运行的命令和参数。此命令会通过 /bin/sh 进行求值，它之后的任何参数都将作为 shell 位置参数传递。
- p：在指定命令输出结果之前显示项目标头。这通过以下方式实现：将管道绑定到命令的 stdin、stdout 和 sterr 流，然后通过管道将所有输出结果传输到一个页面调度会话中显示的连续流中。
- v：显示该命令向 stderr 写入的消息。