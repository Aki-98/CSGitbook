上面我们针对 Groovy 语言进行简单的学习，接下来就是 Gradle DSL 语言的学习。Gradle 是 Android Studio 中采用的全新项目构建方式。

> Gradle 是一个开源的自动化构建工具，提供更高的灵活和体验。Gradle 脚本采用 Groovy 或 Kotlin 进行编写。

官方文档：https://docs.gradle.org/current/dsl/index.html

# 基本概念

Gradle 是一种脚本配置，所以当它执行的时候，它需要跟对应的类型相对应。在 Gradle 中存在以下三种类型：

| 脚本类型        | 委托的实例 |
| --------------- | ---------- |
| Build script    | Project    |
| Init script     | Gradle     |
| Settings script | Settings   |

Gradle 围绕项目 Project，所以 Project 是我们最重要的接口,通过 Project 接口，我们可以获取整个 Gradle 的属性。通常我们的项目在 Project 模式的下结构是：



```java
├── app #Android App目录
│   ├── app.iml
│   ├── build #构建输出目录
│   ├── build.gradle #构建脚本
│   ├── libs #so相关库
│   ├── proguard-rules.pro #proguard混淆配置
│   └── src #源代码，资源等
├── build
│   └── intermediates
├── build.gradle #工程构建文件
├── gradle
│   └── wrapper
├── gradle.properties #gradle的配置
├── gradlew #gradle wrapper linux shell脚本
├── gradlew.bat
├── LibSqlite.iml
├── local.properties #配置Androod SDK位置文件
└── settings.gradle #工程配置
```

# Project

## 1.生命周期 Lifecycle

Project 与 build.gradle 文件是一对一的关系，在初始化脚本构建的过程中，Gradle 为每一个项目创建 Project对象。步骤如下：

**初始化阶段**

在初始化阶段，构建工具根据每个 build.gradle 文件创建出每个项目对应的 Project，同时会执行项目根目录下的 settings.gradle 分析需要参与编译的项目。

比如我们常见的 settings.gradle 配置文件：

```groovy
include ':app', ':groovydemo'
```

指明了需要编译的项目。

**配置阶段**

配置阶段为每个 Project 创建并配置 Task，配置阶段会去加载所有参与构建项目的 build.gradle 文件，将每个 build.gradle 文件转换为一个 Gradle 的 Project 对象，分析依赖关系，下载依赖。

**执行阶段**

Gradle 根据 Task 之间的依赖关系，决定哪些 Task 需要执行，以及 Task 之间的先后顺序。

# Task

Task 是 Gradle 中的最小执行单元，所有的构建、编译、打包、debug、test 等都是执行了某一个 task，一个 Project 可以有多个 Task，Task 之间可以互相依赖。例如我有两个 Task，TaskA 和 TaskB，指定 TaskA 依赖 TaskB，然后执行 TaskA，这时会先去执行 TaskB，TaskB 执行完毕后在执行 TaskA。

同时，我们也可以自定义 Task，也可以查找 Task 是否存在。站在编程的角度来看 Task 同样是一个类，核心方法：

- String getName()：获取任务名称
- Project getProject()：获取任务所在的 Project 对象
- List<Action<? super Task>> getActions()：获取 Action
- TaskDependency getTaskDependencies()：获取任务依赖
- Task dependsOn(Object... var1)：任务依赖关系函数
- void onlyIf(Closure var1)
- TaskState getState()：获取任务的状态
- Task doFirst(Closure var1)：任务先执行..
- Task doLast(Closure var1)：任务后执行..
- String getDescription()：获取任务描述
- String getGroup()：获取任务分组

## 1. 任务的创建

Task 是 Gradle 中最小执行基本单元，创建任务的方式有以下几种：

- Project.task(String name)
- Project.task(String name, Closure configureClosure)
- Project.task(Map<String, ?> args, String name, Closure configureClosure)
- Project.task(Map<String, ?> args, String name)
- TaskContainer.create(String name)
- TaskContainer.create(Map<String,?> options)

前面三种都是基于 Project 提供的 task 重载方法进行创建。这里需要着重介绍下里面的 Map 参数，Map 参数选项用于控制 Task 的创建以及属性。

| 配置项      | 描述                 | 默认值      |
| ----------- | -------------------- | ----------- |
| type        | 任务创建的类型       | DefaultTask |
| overwrite   | 是否重写已存在的任务 | false       |
| dependsOn   | 添加任务的依赖       | []          |
| action      | 添加任务中的 Action  | null        |
| description | 任务的描述           | null        |
| group       | 配置任务的分组       | null        |

第一种：直接以任务名称创建任务

```groovy
Task copyTask = task("copyTask")
copyTask.description = "Copy Task"
copyTask.group = "custom"
copyTask.doLast {
    print("Copy Task Create")
}
```

这种方式跟 Java 中的创建对象的方式非常相似，这种方式的本质是调用 Project 类中的 task(String name) 方法进行对象的创建。

第二种：task + 闭包的方式

```groovy
Task taskClosure = project.task("taskClosure"){
    print("Task Closure")
}
```

这种写法利用闭包是最后一个参数的时候，可以抽取到外部写。上面的这种写法也可以精简：

```groovy
task taskClousre {
    print("Task Closure")
}
```

这种形式的在 .gradle 脚本文件中用的非常多，所以大家也写这种吧！

第三种：task + Map

```groovy
Task mapTask = project.task(dependsOn: copyTask,description: "mapTask",group: "mapTask",
        "mapTask"){
    println("Map Task Create")
}
```

这里通过 Map 进行 Task 的一些设置，这里我们可以同样以方式一一样，单独进行设置。

第四种：TaskContainer 创建任务

```groovy
project.tasks.create("TaskContainer") {
    description "TaskContainer"
    group "TaskContainer"
    doLast {
        println("TaskContainer")
    }
}
```

在上面的演示例子中，我们也介绍了任务的分组和描述的使用，可以在 Gradle Pojects 栏中进行查看任务的分组和描述。

## 2. 任务之间的关系

1. dependsOn(Task task) 任务依赖,通过 dependsOn 可以建立任务之间的执行依赖关系，先执行依赖的任务。

   ```groovy
   def name = "Hello World from"
   
   task checkName {
       if (name.length() > 0){
           name = name.replace("from", "")
       }
   }
   
   task printName() {
       println(name)
   }
   
   printName.dependsOn(checkName)
   ```

2. mustRunAfter(Task task) 必须在添加的任务之后执行。

   ```groovy
   def name = "Hello World from"
   
   task checkName {
       if (name.length() > 0){
           name = name.concat(" China")
       }
   }
   
   task printName() {
       println(name)
   }
   
   printName.mustRunAfter(checkName)
   ```

## 3. 任务类型

在 1 节中，我们提到了创建任务时可以通过 Map 配置任务的依赖属性关系，里面涉及到 任务类型（type），默认值是 DefaultTask 类型，关于 type，我的理解是 Groovy 系统的 Task 类型，我们查看官方文档，可以看到有很多 Task 类的子类，这些应该都可以作为 type 值进行设置？那么常见的任务类型有哪些呢？

官方 Task API：https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html

1. Copy 类型 Task，Copy 任务的方法：

- eachFile：遍历文件
- exclude(Closure excludeSpec)：去除包含的内容
- filter(Closure closure)：过滤
- from(Object... sourcePaths)：源目录
- include(Closure includeSpec)：包含内容
- into(Object destDir)：目标目录
- rename(Closure closure)：重命名
- with(CopySpec... sourceSpecs)

通过 Copy 任务，我们可以更方面实现文件的拷贝复制类操作，因为它提供了一些封装好的方法，不需要我们在通过 File 的操作进行。常见的就是创建的 makeJar 任务,拷贝系统编译的 jar 包到指定目录。

```groovy
task makeJar(type: Copy) {
    def jarName = 'SensorsAnalytics-Android-SDK-Release-' + version + '.jar';
    delete 'build/libs/' + jarName
    from('build/intermediates/bundles/release/')
    into('build/libs/')
    include('classes.jar')
    rename('classes.jar', jarName)
}
```

makeJar 的任务执行步骤：首先设置 type 是 Copy 类型任务，定义拷贝目标的 jar 名称，接着删除 目标目录已存在的 jar 文件，from 从源目录拷贝到 into 的目标目录，包含 include 的 classes.jar，最后给文件重命名。

> 在 Android Studio 的 2.X 版本中自动生成的 jar 包路径在：build/intermediates/bundles/release/ 目录，在 3.X 中目录：build/intermediates/packaged-classes/release/。

1. Jar 类型 Task

```groovy
task makeJar(type: Jar, dependsOn: build) {
    delete 'build/libs/sensorsdata.jar'
    from('build/intermediates/classes/release')
    into('build/libs/')
    exclude('android/', 'androidx/','BuildConfig.class', 'R.class')
    exclude {
        it.name.startsWith('R$')
    }
}
```

Jar 任务的作用就是打包 jar 包，比如我们通过 from 指定工程目录中的源码进行打包，这样我们就可以实现高度的定制化，不像通过 Copy 任务复制系统根据整个目录生成的 Jar 包一样。比如下面的 task 生成 Jar 包。

```groovy
task makeJars(type: org.gradle.jvm.tasks.Jar) {
    from(android.sourceSets.main.java.srcDirs)
}
```

在 Gradle 中提供了很多常见的任务：

![img](Gradle-DSL语言_imgs\mmqcSXGGctq.png)

Gradle System Tasks

# 常见脚本块

Gradle 支持 Groovy 语言进行编写，非常灵活支持各种插件。比如你想在脚本中使用一些第三方的插件、类库等，就需要自己手动添加对这些插件、类库的引用，而这些插件、类库又不是直接服务于项目的，而是支持其它 build 脚本的运行，所以你应当将这部分的引用放置在 buildscript 代码块中。 gradle 在执行脚本时，会优先执行buildscript代码块中的内容，然后才会执行剩余的build脚本。所以需要我们了解常见的脚本块配置。

## 1. allprojects { }

配置整个 Project 和子项目的配置。

```groovy
allprojects {
    repositories {
        google()
        jcenter()
    }
}
```

比如我们在 allprojects 内部定义的 Task 任务，就会用于根目录和子项目。比如下面的例子，我们执行：./gradlew print 任务，打印的结果如下：

```groovy
allprojects {
    task print {
        println project.name
    }
}

输出结果：
GradlePlugin(根目录)
app
groovydemo
sensorsdatalibrary
```

## 2. buildscript { }

buildscript 中的声明是 gradle 脚本自身需要使用的资源。

```groovy
buildscript {
    
    repositories {
        google()
        jcenter()
        mavenCentral()
    }
    //格式为-->group:module:version
    dependencies {
        classpath 'com.android.tools.build:gradle:3.1.2'
        classpath 'com.qihoo360.replugin:replugin-plugin-gradle:2.2.4'
    }
}
```

## 3. configurations { }

配置整个 Project 的 dependency 属性，与之对应的是 ConfigurationContainer，在 Project 项目中可以通过以下方法获取 ConfigurationContainer 对象：

- Project.getConfigurations()
- configurations

通常使用最多的就是去除依赖，比如我们添加的依赖中也依赖某个库，这种间接依赖的冲突，transitive dependencies 被称为依赖的依赖，称为“间接依赖”比较合适。

```groovy
configurations {
    compile.exclude module: 'commons'
    all*.exclude group: 'org.gradle.test.excludes', module: 'reports'
}
```

## 4. dependencies { }

配置项目的依赖库，与之对应的是 DependencyHandler 类。
 在 dependencies{} 脚本块中有不同的依赖方式，这里在 Android Studio 的 2.X 版本与 3.X 版本中差别还是挺大的，Android Studio3.0 中，compile 依赖关系已被弃用，被 implementation 和 api 替代，provided 被 compile only 替代，apk 被 runtime only 替代。为了比较方便，前面写是 3.X 版本，括号是 2.X。

- implementation：依赖的库只能在本项目使用，外部无法使用。比如我在一个 library 中使用 implementation 依赖了 gson 库，然后我的主项目依赖了 library，那么，我的主项目就无法访问 gson 库中的方法。这样的好处是编译速度会加快，推荐使用 implementation 的方式去依赖，如果你需要提供给外部访问，那么就使用 api 依赖即可
- api(compile)：使用该方式依赖的库将会参与编译和打包
- testImplementation(testCompile)：只在单元测试代码的编译以及最终打包测试 Apk 时有效
- debugImplementation(debugCompile)：只在 debug 模式的编译和最终的 debug Apk 打包时有效
- releaseImplementation(releaseCompile)：仅仅针对 Release 模式的编译和最终的 Release Apk 打包
- compileOnly(provided)：只在编译时有效，不会参与打包，可以在自己的moudle中使用该方式依赖。比如 com.android.support，gson 这些使用者常用的库，避免冲突。
- runtimeOnly(apk)：只在生成 Apk 的时候参与打包，编译时不会参与，很少用。

下面是一些常见的依赖使用方式：

```groovy
apply plugin: 'java'
//so that we can use 'compile', 'testCompile' for dependencies

dependencies {
  //for dependencies found in artifact repositories you can use
  //the group:name:version notation
  compile 'commons-lang:commons-lang:2.6'
  testCompile 'org.mockito:mockito:1.9.0-rc1'

  //map-style notation:
  compile group: 'com.google.code.guice', name: 'guice', version: '1.0'

  //declaring arbitrary files as dependencies
  compile files('hibernate.jar', 'libs/spring.jar')

  //putting all jars from 'libs' onto compile classpath
  compile fileTree('libs')
}
```

在实际项目开发中，我们会引入很多第三方开源库，自然就会造成依赖冲突，这里就涉及到在 dependencies 提供的配置字段：

- force = true：即使在有依赖库版本冲突的情况下坚持使用被标注的这个依赖库版本
- transitive = true：依赖的依赖是否可用，举个例子，使用的三方库中可能也依赖别的库，我们称之为“间接依赖”
- exclude：用于排除指定版本库，通常用于排除冲突依赖库

```groovy
dependencies {
  compile('com.sensorsdata.analytics.android:SensorsAnalyticsSDK:2.0.2') {
    //强制使用我们依赖的 2.0.2 版本库
    force = true

    //剔除间接依赖的库,可以通过这三种方式，后面再讲解自定义插件的时候就能看懂这三种方式了。
    exclude module: 'cglib' //by artifact name
    exclude group: 'org.jmock' //by group
    exclude group: 'org.unwanted', module: 'iAmBuggy' //by both name and group

    //禁用所有的间接依赖库
    transitive = false
  }
}
```

## 5. repositories { }

配置 Project 项目所需的仓库地址，Gradle 必须知道从哪里下载外部依赖，这是由仓库配置来指定的，比如 google()、jcenter() 或 mavenCentral()。通常在 buildscript 脚本块中也能看到配置的 repositories 属性，buildscript 中的声明是 gradle 脚本自身需要使用的资源，可以声明的资源包括依赖项、 第三方插件、 maven 仓库地址等。而在 build.gradle 文件中直接声明的依赖项、仓库地址等信息是项目自身需要的资源。

```groovy
repositories {
    //Maven本地仓库，寻找本地仓库的逻辑与Maven相同
    mavenLocal()
    //Maven中心仓库
    mavenCentral()
    //JCenter仓库
    jcenter()
    //其它Maven远程仓库
    maven {
        //可以指定身份验证信息
        credentials {
            username 'user'
            password 'password'
        }
        url "http://repo.mycompany.com/maven2"
        //如果上面的URL找不到构件，则在下面找
        artifactUrls "http://repo.mycompany.com/jars"
    }
    //Ivy远程仓库
    ivy {
        url "http://repo.mycompany.com/repo"
    }
    //Ivy本地仓库
    ivy {
        url "../local-repo"
    }
    //扁平布局的文件系统仓库
    flatDir {
        dirs 'lib'
    }
    flatDir {
        dirs 'lib1', 'lib2'
    }
}
```

## 6. sourceSets { }

配置项目的源码目录结构。

```groovy
sourceSets {
    main {
        java {
            srcDirs = ['src/java']
        }
        resources {
            srcDirs = ['src/resources']
        }
    }
}
```

## 7. subprojects { }

用于配置子项目的脚本块。比如我们在 subprojects 中配置 print 任务，则只会作用于子目录。

```groovy
subprojects {
    task print {
        println project.name
    }
}

输出结果：
app
groovydemo
sensorsdatalibrary
```

## 8. publishing { }

用于发布构建。



```groovy
publishing {
  publications {
    myPublication(MavenPublication) {
      from components.java
      artifact sourceJar
      pom {
        name = "Demo"
        description = "A demonstration of Maven POM customization"
        url = "http://www.example.com/project"
        licenses {
          license {
            name = "The Apache License, Version 2.0"
            url = "http://www.apache.org/licenses/LICENSE-2.0.txt"
          }
        }
        developers {
          developer {
            id = "johnd"
            name = "John Doe"
            email = "john.doe@example.com"
          }
        }
        scm {
          connection = "scm:svn:http://subversion.example.com/svn/project/trunk/"
          developerConnection = "scm:svn:https://subversion.example.com/svn/project/trunk/"
          url = "http://subversion.example.com/svn/project/trunk/"
        }
      }
    }
  }
}
```

