### **Ueventd Overview**

`ueventd` 是负责管理 `/dev` 目录中的设备节点、设置 `/sys` 文件的权限，并处理固件 uevents 的 Android 系统服务。它提供了默认行为，并且可以通过自定义脚本语言进行扩展和调整。这些脚本语言的解析器与 `init` 相同，允许开发者根据需要修改其行为。

### **主要功能**

1. **管理 /dev 设备节点：** `ueventd` 监听内核的 uevent 套接字，并基于接收到的 `add` 或 `remove` uevent 来创建或删除设备节点。默认情况下，设备节点会以模式 `0600` 创建，用户和组都为 `root`，并会根据当前加载的 SELinux 策略设置 SELabel。

2. **设置设备权限：** `ueventd` 允许在 `/dev` 目录下为设备节点设置不同的权限。通过配置脚本，开发者可以指定设备节点的权限、用户和组。例如，使用以下配置可以为 `/dev/null` 设置权限：

   ```
   bash
   
   
   复制代码
   /dev/null 0666 root root
   ```

3. **设备路径与设备名设置：** 默认情况下，`ueventd` 会根据设备类型来创建设备路径：

   - **块设备：** 创建为 `/dev/block/<basename>`，并在不同的路径下创建符号链接。
   - **USB 设备：** 根据 uevent 中提供的 `DEVNAME`，创建 `/dev/<DEVNAME>`，否则创建 `/dev/bus/usb/<bus_id>/<device_id>`。
   - **其他设备：** 根据设备的 `DEVPATH` 创建设备。

4. **子系统和路径配置：** 可以通过 `subsystem` 配置段来设置特定子系统（如 `sound`）的设备节点路径和目录：

   ```
   bash复制代码subsystem sound
     devname uevent_devpath
     dirname /dev/snd
   ```

   这样所有 `SUBSYSTEM=sound` 的设备将被创建在 `/dev/snd/` 目录下。

### **/sys 目录管理**

`ueventd` 默认情况下不对 `/sys` 目录进行任何操作，但它可以根据匹配的 uevent 来设置 `/sys` 中文件的权限。通过 `ueventd.rc` 配置文件，可以为 `/sys` 中的特定文件设置权限和用户/组。例如：

```
bash


复制代码
/sys/devices/system/cpu/cpu* cpufreq/scaling_max_freq 0664 system system
```

这表示当匹配 `/sys/devices/system/cpu/cpu*` 路径的 uevent 发送时，`cpufreq/scaling_max_freq` 文件将被设置为 `0664` 权限，用户和组为 `system`。

### **固件加载**

`ueventd` 负责加载内核固件。它默认会在多个固件目录中查找与 uevent 中的 `FIRMWARE` 名称匹配的文件，然后为内核提供固件。固件目录可以通过 `firmware_directories` 配置进行扩展。还可以通过 `external_firmware_handler` 配置，运行外部程序来处理固件请求。例如：

```
bash


复制代码
external_firmware_handler /devices/leds/red/firmware/coeffs.bin system /vendor/bin/led_coeffs.bin
```

这会运行 `/vendor/bin/led_coeffs.bin` 程序而不是直接加载默认的固件。

### **冷启动（Coldboot）**

当 `ueventd` 启动时，它会执行所谓的“冷启动”，即通过向 `/sys/class`、`/sys/block` 和 `/sys/devices` 中的每个 uevent 文件写入 `add`，让内核重新生成这些路径的 uevents，从而触发设备节点的创建。为了加速启动过程，这一过程会并行化。

### **配置选项**

1. **`uevent_socket_rcvbuf_size`**：用来设置 ueventd 套接字的接收缓冲区大小。例如：

   ```
   bash
   
   
   复制代码
   uevent_socket_rcvbuf_size 16M
   ```

   这会将接收缓冲区大小设置为 16MB。

2. **导入配置文件：**
   可以使用 `import` 命令导入其他配置文件，扩展当前的配置。例如：

   ```
   bash
   
   
   复制代码
   import /path/to/another/config.rc
   ```

   如果指定的是目录，`ueventd` 会解析目录下的所有文件，但不会递归解析子目录。

3. **路径匹配：** 对于 `/dev` 或 `/sys` 条目的路径，`ueventd` 支持使用通配符 `*` 进行匹配。当通配符出现在路径结尾时，`ueventd` 会使用 `fnmatch(entry_path, incoming_path, 0)` 进行匹配，否则使用 `fnmatch(entry_path, incoming_path, FNM_PATHNAME)` 进行路径匹配。