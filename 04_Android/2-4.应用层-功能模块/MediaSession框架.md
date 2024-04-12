**MediaSession框架：**

- C/S架构
- 规范了音视频应用中界面与播放器之间的通信接口，实现界面与播放器之间的完全解耦。

![img](MediaSession框架_imgs\v2-e1f6747dab51b11d1d6b2656452b6953_720w.webp)



**MediaSession媒体会话（Server）**

- 负责与MediaPlayer播放器的所有通信，对应用的其它部分隐藏播放器的API，系统只能从控制播放器的MediaSession中调用播放器。
- 维持的信息：PlaybackState-播放器状态（播放/暂停），MetaData-播放内容的相关信息（标题/音乐家）。
- MediaSession可以接收来自一个或多个MediaController的回调，响应回调的逻辑必须保持一致，无论哪个客户端应用发起了回调，对回调的响应都是相同的。



**MediaController媒体控制器（Client）**

- 界面的代码只与MediaController通信，MediaController会将传输控制操作转换为对媒体会话的回调。每当会话状态发生变化时，它也会接收来自媒体会话的回调，这时便可以更新界面。
- MediaController一次只能连接到一个MediaSession
- MediaController 创建时需要受控端的配对令牌，因此需要在浏览器连接成功后才进行 MediaController 的创建。



**MediaBrowser媒体浏览器（Client）**

- 用来连接媒体服务MediaBrowserService和订阅数据，在注册的回调接口中可以获取到Service的连接状态、获取音乐数据，一般在客户端中创建。



**MediaBrowserService媒体服务（Server）**

- 它有两个关键的回调函数，onGetRoot（控制客户端MediaBrowser的连接请求，返回值中决定是否允许连接）,onLoadChildren（MediaBrowser向服务器发送数据订阅请求时会被调用，一般在这里执行异步获取数据的操作，然后在将数据发送回MediaBrowser注册的接口中）。

