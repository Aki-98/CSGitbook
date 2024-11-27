# 介绍

JaCoCo is a free code coverage library for Java, which has been created by the EclEmma team based on the lessons learned from using and integration existing libraries for many years.

important features:

- Coverage analysis of instructions (C0), branches (C1), lines, methods, types and cyclomatic complexity.

- Based on Java byte code and therefore works also without source files.

JaCoCo supports two ways class instrumentation: on the fly with using Java Agent and offline when classes are prepared during build phase.

wiki：

https://www.jacoco.org/jacoco/trunk/doc/



# 使用

## 配置

android studio gradle jacoco config:

for instrumented unit test, you can only add the following option into build.gradle to enable jacoco codecovarage;

```
buildTypes {
	debug {
		testCoverageEnabled true
	}
}
```

then you can run the gradle task'createDebugCoverageReport' to generate the code coverage report after resync the project.

for local unit test:

- add “apply plugin: "jacoco" into build.gradle

- add the gradle task which type is 'JacocoReport' to generate the local unit test code coverage

## JacocoReport Task(gradle task)

after exec local unit test, the code coverage data will be collected into *.exec files

then we can call JacocoReport to generate the code coverage report(html)



the exec file location:

module/build/jacoco/testDebugUnitTest.exec

module/jacoco.exec // the unit test didn't generate this somtimes, now we didn't now why



About the samples please refer to the p20,p21



following is on the fly mode jacoco config:

![image-20230329142814075](Jacoco_imgs\image-20230329142814075.png)



following is on the offline mode jacoco config: 

the mainSrc,javDebugTree,kotlinDebugTree is same as on the fly mode config

![image-20230329142829931](Jacoco_imgs\image-20230329142829931.png)



## jacoco instrumentation types

### On-the-fly instrumentation: 

用一个新的class loader，然后在执行class文件的过程中加入类似的输出代码。

在应用启动时加入jacoco agent进行插桩，在开发、测试人员使用应用期间实时地进行代码覆盖率分析。相信很多的java项目开发人员并不会去写单元测试代码的，因此覆盖率统计就要把手工测试或接口测试覆盖的情况作为重要依据，显然在线模式更符合实际需求。

One of the main benefits of JaCoCo is the Java agent, which instruments classes on-the-fly. This simplifies code coverage analysis a lot as no pre-instrumentation and classpath tweaking is required. However, there can be situations where on-the-fly instrumentation is not suitable, for example:

- Runtime environments that do not support Java agents.

- Deployments where it is not possible to configure JVM options.

- Bytecode needs to be converted for another VM like the Android Dalvik VM.

- Conflicts with other agents that do dynamic classfile transformation.

So there is a big issue when test some powermock test. PowerMock instruments classes and Javassist is used to modify classes. The main issue is that Javassist reads classes from disk and all JaCoCo changes are disappeared. As result zero code coverage for classes which are loaded by PowerMock class loader.

refer uri:https://github.com/powermock/powermock/wiki/Code-coverage-with-JaCoCo

### Offline Instrumentation:

先对class文件加入代码再运行

in this mode, you must pre-instruments classes in build process.

At runtime the pre-instrumented classes needs be on the classpath instead of the original classes. In addition jacocoagent.jar must be put on the classpath.

refer uri:https://www.jacoco.org/jacoco/trunk/doc/offline.html

In this mode, it can solve the conflict with PowerMock