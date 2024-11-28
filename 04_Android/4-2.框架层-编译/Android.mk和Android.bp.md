# Android.mk

编写 `Android.mk` 文件是 Android 工程中配置构建系统的关键部分，主要用于描述如何编译本地代码（如 C/C++ 代码）。以下是 `Android.mk` 文件的基本结构和常用指令的详细介绍。

------

### **1. `Android.mk` 的基本结构**

```makefile
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# 定义模块名称
LOCAL_MODULE := your_module_name

# 指定源文件
LOCAL_SRC_FILES := file1.c file2.cpp

# 指定头文件路径（可选）
LOCAL_C_INCLUDES := $(LOCAL_PATH)/include

# 指定库依赖（可选）
LOCAL_LDLIBS := -llog -landroid

# 指定目标库类型（可选）
LOCAL_MODULE_TAGS := optional  # 可以是 "optional", "debug", 或 "tests"

# 编译为共享库或可执行文件
include $(BUILD_SHARED_LIBRARY)  # 共享库
#include $(BUILD_EXECUTABLE)     # 可执行文件
```

------

### **2. 常用指令**

#### **1) `LOCAL_PATH`**

定义当前 `Android.mk` 文件的目录：

```makefile
LOCAL_PATH := $(call my-dir)
```

#### **2) `include $(CLEAR_VARS)`**

清除之前的变量定义，避免变量污染。此命令必须包含在每个模块定义的开头。

#### **3) `LOCAL_MODULE`**

定义模块名称：

```makefile
LOCAL_MODULE := my_library
```

#### **4) `LOCAL_SRC_FILES`**

定义源码文件路径，可以是相对于 `LOCAL_PATH` 的路径：

```makefile
LOCAL_SRC_FILES := main.cpp helper.c
```

#### **5) `LOCAL_C_INCLUDES`**

定义头文件路径，支持绝对路径和相对路径：

```makefile
LOCAL_C_INCLUDES := $(LOCAL_PATH)/include
```

#### **6) `LOCAL_LDLIBS`**

定义链接的系统库，例如 `-llog` 用于 Android 日志库：

```makefile
LOCAL_LDLIBS := -llog -lz
```

#### **7) 编译目标**

- **共享库：**

  ```makefile
  include $(BUILD_SHARED_LIBRARY)
  ```

  会生成一个以 `.so` 为后缀的共享库文件。

- **静态库：**

  ```makefile
  include $(BUILD_STATIC_LIBRARY)
  ```

  会生成一个以 `.a` 为后缀的静态库文件。

- **可执行文件：**

  ```makefile
  include $(BUILD_EXECUTABLE)
  ```

------

### **3. 示例**

```makefile
LOCAL_PATH := $(call my-dir) # 当前 Android.mk 文件所在的路径，表示当前目录为基准，控制本目录下的编译。
##############################
include $(CLEAR_VARS) # 清除之前的变量定义，避免变量污染，确保每个模块的定义互不干扰。

LOCAL_MODULE := ChinaHome # 模块名称为 ChinaHome，编译输出的目标文件将以此名称命名。
LOCAL_SRC_FILES := ChinaHome.apk # 指定模块的源文件，这里是当前目录下的 ChinaHome.apk。
LOCAL_MODULE_CLASS := APPS # 指定模块类型为 APPS，表示这是一个应用程序模块。
LOCAL_PRIVILEGED_MODULE := true # 声明模块为特权应用，安装到系统分区并拥有额外权限。
LOCAL_SYSTEM_EXT_MODULE := true # 指定模块安装在 system_ext 分区，用于特定系统扩展功能。
LOCAL_CERTIFICATE := PRESIGNED # 指定 APK 已经预签名，构建系统不会对其重新签名。
LOCAL_OPTIONAL_USES_LIBRARIES := \ # 声明可选使用的库，模块运行时可以选择性依赖这些库。'\'为换行语法
    org.apache.http.legacy # 使用 Apache HTTP 库，通常用于兼容老旧的网络请求接口。
LOCAL_NOTICE_FILE := $(LOCAL_PATH)/NOTICE.ChinaHome.json # 指定模块的许可证文件路径，用于开源合规。

include $(BUILD_PREBUILT) # 使用预构建模块规则，表示直接打包现有的 ChinaHome.apk，而不重新编译源代码。
##############################
include $(CLEAR_VARS) # 清除之前的变量定义，避免变量污染。

LOCAL_MODULE := AccountApp # 模块名称为 AccountApp，编译输出的目标文件将以此名称命名。
LOCAL_SRC_FILES := AccountApp.apk # 指定模块的源文件，这里是当前目录下的 AccountApp.apk。
LOCAL_MODULE_CLASS := APPS # 指定模块类型为 APPS，表示这是一个应用程序模块。
LOCAL_PRIVILEGED_MODULE := true # 声明模块为特权应用，安装到系统分区并拥有额外权限。
LOCAL_CERTIFICATE := sony-general-app # 指定 APK 使用 `sony-general-app` 的证书进行签名。
LOCAL_PRODUCT_MODULE := true # 指定模块安装到产品分区，用于设备的产品特定功能。

include $(BUILD_PREBUILT) # 使用预构建模块规则，表示直接打包现有的 AccountApp.apk，而不重新编译源代码。
##############################
```



# Android.bp

`Android.bp` 基于 Soong 构建系统，使用 JSON 类似的结构（基于 Blueprint 语法）来配置模块的构建规则。

### **1. `Android.bp` 的基本结构**

一个典型的 `Android.bp` 文件：

```bp
cc_library_shared {
    name: "your_module_name",       // 模块名称
    srcs: ["file1.c", "file2.cpp"], // 源文件列表
    include_dirs: ["include"],      // 头文件路径
    shared_libs: ["liblog"],        // 依赖的共享库
    static_libs: ["libutils"],      // 依赖的静态库
    cflags: ["-DMY_DEFINE=1"],      // 自定义编译宏
    ldflags: ["-Wl,--no-undefined"],// 链接选项
}
```

------

### **2. 常用模块类型**

#### **1) `cc_library_shared`**

构建共享库（`.so`）：

```
cc_library_shared {
    name: "my_shared_lib",
    srcs: ["src/main.c", "src/helper.c"],
    include_dirs: ["include"],
    shared_libs: ["liblog"],
}
```

#### **2) `cc_library_static`**

构建静态库（`.a`）：

```
cc_library_static {
    name: "my_static_lib",
    srcs: ["src/main.c", "src/helper.c"],
    include_dirs: ["include"],
}
```

#### **3) `cc_binary`**

构建可执行文件：

```
cc_binary {
    name: "my_executable",
    srcs: ["main.cpp"],
    static_libs: ["my_static_lib"],
    shared_libs: ["liblog"],
}
```

#### **4) `filegroup`**

定义文件组，便于复用：

```
filegroup {
    name: "common_headers",
    srcs: ["include/*.h"],
}
```

#### **5) `prebuilt_shared_library`**

预构建的共享库：

```bp
prebuilt_shared_library {
    name: "prebuilt_lib",
    srcs: ["libs/libprebuilt.so"],
    export_include_dirs: ["include"],
}
```

------

### **3. 关键字段说明**

#### **1) `name`**

模块的唯一标识符。

#### **2) `srcs`**

源文件列表，支持通配符：

```bp
srcs: ["src/*.c"],
```

#### **3) `include_dirs`**

指定头文件路径，相对于当前模块的路径：

```bp
include_dirs: ["include"],
```

#### **4) `shared_libs` 和 `static_libs`**

- **`shared_libs`**：依赖的共享库模块。
- **`static_libs`**：依赖的静态库模块。

例如：

```
shared_libs: ["liblog"],
static_libs: ["libutils"],
```

#### **5) `cflags` 和 `ldflags`**

- **`cflags`**：C/C++ 编译选项。
- **`ldflags`**：链接选项。

```
cflags: ["-DMY_DEFINE=1", "-Wall"],
ldflags: ["-Wl,--no-undefined"],
```

#### **6) `target`**

指定针对不同平台的配置：

```
target: {
    android: {
        cflags: ["-DANDROID"],
    },
    linux_glibc: {
        cflags: ["-DLINUX"],
    },
},
```

#### **7) `compile_multilib`**

指定构建单个架构还是多架构：

```
compile_multilib: "both",  // 可选 "32", "64", 或 "both"
```

------

### **4. 示例**

```
android_library { # 定义一个 Android 库模块，构建结果为 `.jar` 文件。
    name: "...", # 模块的唯一名称，生成的目标文件也将以此命名。

    platform_apis: true, # 允许使用 Android 平台私有 API，通常需要特权权限。

    static_libs: [ # 声明此模块依赖的静态库（编译时依赖）。这些库会被链接到此模块中。
        ...
        "guava", # Guava 是一个广泛使用的 Java 工具库，提供集合、字符串处理等功能。
    ],

    # Requires uses-library in manifest
    libs: [ # 声明运行时依赖的动态库，通常需要在 `AndroidManifest.xml` 中添加 uses-library。
    ],

    aidl: { # 配置 AIDL（Android 接口定义语言）相关的目录和文件。
        local_include_dirs: ["src"], # 本地 AIDL 文件所在的路径。
        include_dirs: ["frameworks/base/core/java/android/service"], # 引入外部 AIDL 文件的路径（例如系统服务接口）。
    },

    srcs: [ # 声明模块的源文件，包括 Java 和 AIDL 文件。
        "src/**/*.java", 
        "src/....aidl",
    ],

    resource_dirs: [ # 声明模块的资源目录，用于存放资源文件（XML、图片等）。
        "res", 
    ],

    manifest: "AndroidManifest.xml", # 指定模块的 AndroidManifest 文件路径。

    java_version: "1.8", # 指定 Java 的编译版本为 1.8，确保与模块代码兼容。
}
```

