### okio框架

#### ByteString

```java
String str = "This is a string" ;
System.out.println(str.length());

ByteString bytestring = ByteString.encodeutf8(str);
System.out.printin(byteString);

//编码
String base64 = byteString.base64();
System.out.printin(base64);

ByteString md5 = byteString.md5();
System.out.printin(md5);//获得md5字符串
System.out.printin(md5.hex());//获得md516进制字符串

//解码
ByteString bytestring1 = Bytestring.decodeBase64("YWj");
System.out.print1n(bytestring1);//abc

//获得SH1校验值
String hex = bytestring1.sha1( ).hex( );
System.out.println(hex);

FileInputStream in = new FileInputStream("in.png");
ByteString read = ByteString.read(in,in.available());
System.out.println(read);


FileOutputStream out = new FileOutputStream("out.png");
read.write(out);

in.close();
out.close();

```

#### Buffer

```java
Buffer buffer = new Buffer();
System.out.println(buffer);//[size=0]

buffer.writeUTF8("abc" ) ;
System.out.println(buffer);//[text=abc]

while(!buffer.exhausted()){
	System.out.println(buffer.readUTF8(1));
    //a  --> buffer:[text:bc]
    //b  --> buffer:[text:c]
    //c  --> buffer:[size:0]
}

BufferedSource source = okio.buffer(okio.source(new File( pathname: "in.txt")));
BufferedSink sink = okio.buffer(Okio.sink(new File( pathname: "out.txt")));
source.readAl1(sink) ;
source.close();
sink.close();

```

