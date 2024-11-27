#  Android 中的 AIDL（Android Interface Definition Language）

AIDL（Android Interface Definition Language）是 Android 提供的一种用于在应用组件间进行 IPC（进程间通信）的机制。通过 AIDL，开发者可以定义一个接口，然后在不同的应用组件之间进行通信，例如在应用与服务之间。

**1. AIDL 基本概念：**

- **接口定义**：使用 AIDL 定义一个接口，该接口定义了可供其他组件调用的方法。
- **跨进程通信**：AIDL 允许应用组件（例如 Activity、Service）与其他进程中的组件进行通信。

**2. AIDL 数据类型：**

AIDL 支持以下数据类型：

- 基本数据类型（如 int、long、boolean 等）
- String
- CharSequence
- List
- Map
- 自定义的 Parcelable 对象

**3. AIDL 文件结构：**

AIDL 文件通常具有 `.aidl` 扩展名，并且其内容类似于 Java 接口。

```
aidlCopy code// IMyAidlInterface.aidl
package com.example;

// 定义接口
interface IMyAidlInterface {
    int add(int num1, int num2);
    String concatenate(String str1, String str2);
}
```

**4. AIDL 用法：**

1. **定义 AIDL 接口**：创建 `.aidl` 文件，并在其中定义接口。
2. **实现 AIDL 接口**：在服务（Service）中实现定义的 AIDL 接口。
3. **绑定服务**：在客户端（通常是 Activity 或其他服务）中绑定到该 AIDL 服务，并调用其方法。

**5. 示例：**

**a. 定义 AIDL 接口：**

```java
aidlCopy code// IMyAidlInterface.aidl
package com.example;

// 定义接口
interface IMyAidlInterface {
    int add(int num1, int num2);
    String concatenate(String str1, String str2);
}
```

**b. 实现 AIDL 接口：**

```java
javaCopy code// MyAidlService.java
public class MyAidlService extends Service {

    private final IMyAidlInterface.Stub mBinder = new IMyAidlInterface.Stub() {
        @Override
        public int add(int num1, int num2) throws RemoteException {
            return num1 + num2;
        }

        @Override
        public String concatenate(String str1, String str2) throws RemoteException {
            return str1 + str2;
        }
    };

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }
}
```

**c. 绑定 AIDL 服务：**

```java
javaCopy code// MainActivity.java
public class MainActivity extends AppCompatActivity {

    private IMyAidlInterface mService;

    private final ServiceConnection mConnection = new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName className, IBinder service) {
            mService = IMyAidlInterface.Stub.asInterface(service);
            try {
                int result = mService.add(5, 3);
                String concatenatedStr = mService.concatenate("Hello, ", "World!");
                Log.d("MainActivity", "Add Result: " + result);
                Log.d("MainActivity", "Concatenated String: " + concatenatedStr);
            } catch (RemoteException e) {
                e.printStackTrace();
            }
        }

        @Override
        public void onServiceDisconnected(ComponentName className) {
            mService = null;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Intent intent = new Intent();
        intent.setComponent(new ComponentName("com.example", "com.example.MyAidlService"));
        bindService(intent, mConnection, Context.BIND_AUTO_CREATE);
    }

    @Override
    protected void onDestroy() {
        unbindService(mConnection);
        super.onDestroy();
    }
}
```

**6. 注意事项：**

- **线程安全**：由于 AIDL 方法在 IPC 通信时运行在服务进程中，因此需要确保 AIDL 接口的实现是线程安全的。
- **数据传输**：当传输自定义对象或列表时，需要确保对象实现了 `Parcelable` 接口。

# AIDL 跨进程抛出异常

来源：https://blog.csdn.net/LVXIANGAN/article/details/103441176

1、跨进程通讯中，从一端到另外一端，只支持传递以下9种异常:

- SecurityException
- BadParcelableException
- IllegalArgumentException
- NullPointerException
- IllegalStateException
- NetworkOnMainThreadException
- UnsupportedOperationException
- ServiceSpecificException
- Parcelable的异常
  

2、对于不支持的异常，会在程序内部处理，可能导致崩溃，但不会传递给对方。常见的不支持的异常，

- 运行时异常：RuntimeException
- 算术异常类：ArithmeticExecption
- 类型强制转换异常：ClassCastException
- 数组下标越界异常：ArrayIndexOutOfBoundsException
- 文件未找到异常：FileNotFoundException
- 字符串转换为数字异常：NumberFormatException
- 输入输出异常：IOException
- 方法未找到异常：NoSuchMethodException

 

 报错：

```

01-01 05:49:46.770 19937 19937 E testtest: RemoteException
01-01 05:49:46.770 19937 19937 E testtest: java.lang.UnsupportedOperationException: TestException
01-01 05:49:46.770 19937 19937 E testtest:      at android.os.Parcel.readException(Parcel.java:1728)
01-01 05:49:46.770 19937 19937 E testtest:      at android.os.Parcel.readException(Parcel.java:1669)
01-01 05:49:46.770 19937 19937 E testtest:      at me.linjw.demo.ipcdemo.ITestExceptionAidl$Stub$Proxy.testThrowException(ITestExceptionAidl.java:77)
01-01 05:49:46.770 19937 19937 E testtest:      at me.linjw.demo.ipcdemo.MainActivity$3.onServiceConnected(MainActivity.java:132)
01-01 05:49:46.770 19937 19937 E testtest:      at android.app.LoadedApk$ServiceDispatcher.doConnected(LoadedApk.java:1465)
01-01 05:49:46.770 19937 19937 E testtest:      at android.app.LoadedApk$ServiceDispatcher$RunConnection.run(LoadedApk.java:1482)
01-01 05:49:46.770 19937 19937 E testtest:      at android.os.Handler.handleCallback(Handler.java:751)
01-01 05:49:46.770 19937 19937 E testtest:      at android.os.Handler.dispatchMessage(Handler.java:95)
01-01 05:49:46.770 19937 19937 E testtest:      at android.os.Looper.loop(Looper.java:154)
01-01 05:49:46.770 19937 19937 E testtest:      at android.app.ActivityThread.main(ActivityThread.java:6097)
01-01 05:49:46.770 19937 19937 E testtest:      at java.lang.reflect.Method.invoke(Native Method)
01-01 05:49:46.770 19937 19937 E testtest:      at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:1052)
01-01 05:49:46.770 19937 19937 E testtest:      at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:942)
 
```

# `RemoteCallbackList` 类注释

## 为什么需要RemoteCallbackList？

在 Android 中，服务和客户端可能运行在不同的进程中。直接使用普通的列表来管理回调接口时，如果某个客户端进程崩溃，可能会导致服务端引用了无效的回调接口，从而引发 `RemoteException`。`RemoteCallbackList` 能自动处理进程间通信的细节，确保回调接口的可靠性和安全性。这也减少了服务端开发者手动管理和清理无效回调的复杂性，避免了内存泄漏和资源浪费。

## **有什么功能？**

Func List：

- **跟踪注册的 `IInterface` 回调**：通过它们的底层唯一的 `IBinder` 进行识别（通过调用 `IInterface.asBinder()`）。
- **为每个注册的接口附加 `IBinder.DeathRecipient`**：这样，如果其进程消失，它可以从列表中清除。
- **执行底层接口列表的锁定**：以处理多线程的传入调用，并以线程安全的方式迭代列表的快照，而不持有其锁。

API List：

- `register(E callback)`: 注册回调接口。
- `unregister(E callback)`: 反注册回调接口。
- `beginBroadcast()`: 准备回调广播，返回当前注册的回调数量。
- `getBroadcastItem(int index)`: 获取特定位置的回调接口。
- `finishBroadcast()`: 完成回调广播。

## 如何使用？

要使用这个类，只需在您的服务（`Service`）中创建一个实例，并在客户端注册和注销时调用其 `register` 和 `unregister` 方法。要回调注册的客户端，使用 `beginBroadcast`、`getBroadcastItem` 和 `finishBroadcast` 方法。

**注意事项：**

如果注册的回调的进程消失，这个类会自动从列表中删除它。如果您想在这种情况下进行额外的工作，您可以创建一个子类来实现 `onCallbackDied` 方法。

# AIDL跨进程 最大传输大小 < 1M - 8k
