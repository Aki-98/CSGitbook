# **MediaSession-CS框架**

- C/S架构
- 规范了音视频应用中界面与播放器之间的通信接口，实现界面与播放器之间的完全解耦。

![img](MediaSession框架_imgs\v2-e1f6747dab51b11d1d6b2656452b6953_720w.webp)

## **MediaSession媒体会话（Server）**

- 负责与MediaPlayer播放器的所有通信，对应用的其它部分隐藏播放器的API，系统只能从控制播放器的MediaSession中调用播放器。
- 维持的信息：PlaybackState-播放器状态（播放/暂停），MetaData-播放内容的相关信息（标题/音乐家）。
- MediaSession可以接收来自一个或多个MediaController的回调，响应回调的逻辑必须保持一致，无论哪个客户端应用发起了回调，对回调的响应都是相同的。



## **MediaController媒体控制器（Client）**

- 界面的代码只与MediaController通信，MediaController会将传输控制操作转换为对媒体会话的回调。每当会话状态发生变化时，它也会接收来自媒体会话的回调，这时便可以更新界面。
- MediaController一次只能连接到一个MediaSession
- MediaController 创建时需要受控端的配对令牌，因此需要在浏览器连接成功后才进行 MediaController 的创建。

# MediaSession-授权框架

![image-20240920155216578](E:\.personal\CSGitbook\04_Android\2-4.应用层-功能模块\MediaSession框架_imgs\image-20240920155216578.png)

## **MediaBrowser媒体浏览器（Client）**

- 用来连接媒体服务MediaBrowserService和订阅数据，在注册的回调接口中可以获取到Service的连接状态、获取音乐数据，一般在客户端中创建。



## **MediaBrowserService媒体服务（Server）**

- 它有两个关键的回调函数，onGetRoot（控制客户端MediaBrowser的连接请求，返回值中决定是否允许连接）,onLoadChildren（MediaBrowser向服务器发送数据订阅请求时会被调用，一般在这里执行异步获取数据的操作，然后在将数据发送回MediaBrowser注册的接口中）。



# 命令传递

客户端调用服务器

| 意义           | MediaController.TransportControls | MediaSession.Callback             |
| -------------- | --------------------------------- | --------------------------------- |
| 播放           | play()                            | onPlay()                          |
| 暂停           | pause()                           | onPause()                         |
| 停止           | stop()                            | onStop()                          |
| 指定播放位置   | seekTo(long)                      | onSeekTo(long)                    |
| 快进           | fastForward()                     | onFastForward()                   |
| 回倒           | rewind()                          | onRewind()                        |
| 下一首         | skipToNext()                      | onSkipToNext()                    |
| 上一首         | skipToPrevious()                  | onSkipToPrevious()                |
| 设置播放速度   | setPlaybackSpeed(float)           | onSetPlaybackSpeed(float)         |
| 打分           | setRating(Rating)                 | onSetRating(Rating)               |
| 发送自定义动作 | sendCustomAction(String,Bundle)   | onSendCustomAction(String,Bundle) |

# 支持判断

**议题1：SearchApp能否通过代码知道播放器是否支持某些操作指令**
**结论：可以知道非自定义的指令是否支持，但自定义指令不可以**

自定义指令比如单曲循环/顺序播放、切换全屏/半屏等，无法通过代码判断播放器是否支持
代码示例：

```java
MediaController mediaController = getMediaController(context);
if (null != mediaController) {
    // 获取当前的 PlaybackState
    PlaybackState playbackState = mediaController.getPlaybackState();

    if (playbackState != null) {
    // 获取支持的操作
    long actions = playbackState.getActions();

        // 检查播放器是否支持播放
        if ((actions & PlaybackState.ACTION_PLAY) != 0) {
        Log.d("MediaSession", "播放器支持播放操作");
        }

        // 检查播放器是否支持暂停
        if ((actions & PlaybackState.ACTION_PAUSE) != 0) {
        Log.d("MediaSession", "播放器支持暂停操作");
        }

        // 检查播放器是否支持快进
        if ((actions & PlaybackState.ACTION_FAST_FORWARD) != 0) {
        Log.d("MediaSession", "播放器支持快进操作");
       }
    }
}
  
```

 

**议题2：SearchApp能否通过代码知道播放器是否成功完成了指令**
**结论：只能知道部分指令是否成功执行**

暂停\继续播放等可以通过PlaybackState判断，但上一首\下一首等没有相应的Callback
代码示例：

```java
// 假设已经有一个 MediaController 实例
MediaController mediaController = ...;

// 创建并注册一个 Callback 来监听播放状态的变化
MediaController.Callback callback = new MediaController.Callback() {
    @Override
    public void onPlaybackStateChanged(PlaybackState state) {
        super.onPlaybackStateChanged(state);
        if (state != null) {
            int playbackState = state.getState();
            switch (playbackState) {
                case PlaybackState.STATE_PLAYING:
                    Log.d("MediaController", "Playback started successfully.");
                    break;
                case PlaybackState.STATE_PAUSED:
                    Log.d("MediaController", "Playback is paused.");
                    break;
                case PlaybackState.STATE_STOPPED:
                    Log.d("MediaController", "Playback stopped.");
                    break;
                case PlaybackState.STATE_ERROR:
                    Log.e("MediaController", "Playback encountered an error: " + state.getErrorMessage());
                    break;
                // 其他状态可以根据需要处理
                default:
                    Log.d("MediaController", "Playback state changed: " + playbackState);
                    break;
            }
        }
    }
};

// 注册 Callback
mediaController.registerCallback(callback);

// 执行播放操作
mediaController.getTransportControls().play();

// 在适当的时候注销 Callback
// mediaController.unregisterCallback(callback); 
```

 

