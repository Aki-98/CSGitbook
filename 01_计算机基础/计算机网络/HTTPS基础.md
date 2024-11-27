### <span id="head1">HTTP存在的问题</span>

#### <span id="head2">可能被窃听</span>

1. HTTP本身不具备加密的功能，HTTP报文使用明文方式发送
2. 由于互联网是由联通世界各个地方的网络设施组成，所有发送和接收经过某些设备的数据都可能被截获或窥视。

#### <span id="head3">认证问题</span>

1. 无法确认你发送到的服务器就是真正的目标服务器，可能服务器是伪装的
2. 无法确定返回的客户端是否是按照真实意图接收的客户端，可能是伪装的客户端
3. 无法确定正在通信的对方是否具备访问权限，Web服务器上某些重要的信息，只想发给特定用户即使是无意义的请求也会照单全收。无法阻止海量请求下的dos攻击（拒绝服务攻击）

#### <span id="head4">可能被篡改</span>

请求或响应在传输途中，遭攻击者拦截并篡改内容的攻击被称为中间人攻击。

### <span id="head5">HTTPS定义</span>

HTTP over SSL的简称，即工作在SSL（或TLS）上的HTTP。就是加密通信的HTTP。

### <span id="head6">工作原理</span>

在客户端和服务器之间协商出一套对称密钥，每次发送信息之前将内容加密，收到之后解密，达到内容的加密传输。

### <span id="head7">为什么不直接用非对称加密？</span>

非对称加密由于使用了复杂的数学原理，因此计算想当复杂，如果完全使用非对称加密来加密通信内容，会严重影响网络通信的性能。

### <span id="head8">HTTPS 连接建立的过程</span>

HTTPS的整体思路很简单，它其实就是做了三件事：**认证、密钥协商、数据加密**

- 通信双方身份的验证
- 通信双方协商出一个安全的会话密钥，注意中间人攻击的问题
- 使用会话密钥对称加密通信内容

下面是具体过程

1. ClientHello： 建立TCP连接之后，客户端率先发出Client Hello消息
2. ServerHello：服务端在收到Client Hello之后，根据客户端发来的消息内容作出回应，在这一步协商：密钥协商算法、身份验证算法、对称加密算法、摘要算法
3. 服务器证书信任建立（Certificate） ：服务端在发送ServerHello之后会立马发送服务器的证书链信息，其实 Certificate 和 Server Hello 是在同一个数据包里面的，以降低延迟
4. Pre-masterSecret ： pre-master-secret由client产生，在产生该secret之前，client和server已经交换了`client_random`和`server_random`。然后client和server会使用一个PRF(Pseudo-Random Function)来产生master-secret
5. 客户端通知:将使用加密通信 ：通知对方我已经准备好加密通信了
6. 客户端发送:Finished ： 握手消息的完整性校验
7. 服务器通知:将使用加密通信 
8. 服务器发送:Finished
