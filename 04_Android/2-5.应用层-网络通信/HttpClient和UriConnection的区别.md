# HttpClient和URLConnection的区别

区别

1、HttpURLConnection是java的标准类，没有做封装，用起来比较原始

2、HttpClient是开源框架，封装了访问HTTP的请求头、参数、内容体、响应等；HttpURLConnection中的输入输出流操作，在这个接口中被统一封装成了HttpPost（HttpGet）和HttpResponse。这样，减少了操作的繁琐性。

下面分别给出HttpURLConnection和HttpClient实现GET、POST请求示例，作为学习。

（1）HttpURLConnection实现GET

```java
package com.jingchenyong.test;
 
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
 
public class Test_HttpURLConnection_GET
{
    public static void main(String[] args) throws Exception
    {
        String urlString="http://15.6.46.35:8080/platform/index.html";
        URL url=new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection)url.openConnection();
        conn.setRequestProperty("Accept-Charset", "UTF-8");
        conn.setRequestProperty("connection", "keep-Alive");
        conn.setRequestMethod("GET");
        conn.connect();
        
        int code=conn.getResponseCode();
        System.out.println(code);
        //把流转为字符串方式一
        //String  result=IOUtils.toString(conn.getInputStream(),"UTF-8");
        //把流转为字符串方式二
        BufferedReader br=new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
        String result="";
        String tmp="";
        while((tmp=br.readLine())!=null){
            result=result+tmp;
        }
        System.out.println(result);
        //关闭流和连接    
    }   
}
```

HttpURLConnection实现POST

```java
package com.jingchenyong.test;
 
import java.io.BufferedOutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
 
import org.apache.commons.io.IOUtils;
import org.apache.commons.lang.StringUtils;
 
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
 
public class Test_HttpURLConnection_POST
{
    
    public static void main(String[] args)
        throws Exception
    {
        //设置连接
        String urlString = "http://15.6.46.37:9200//henry/henry/_search";
        URL url = new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection)url.openConnection();
        conn.setRequestProperty("Accept-Charset", "UTF-8");
        conn.setRequestProperty("connection", "keep-Alive");
        conn.setRequestMethod("POST");
        conn.setDoInput(true);
        conn.setDoOutput(true);
        conn.connect();
        String jsonstring = getJOSNString();
        if (StringUtils.isNotBlank(jsonstring))
        {
            /**
             * post提交方式一
             */
           /* OutputStream os = conn.getOutputStream();
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os));
            writer.write(jsonstring);
            writer.flush();
            writer.close();*/
            BufferedOutputStream out = new BufferedOutputStream(conn.getOutputStream());
            out.write(jsonstring.getBytes());
            out.flush();
            out.close();
            //流转字符串的另一种方式见GET方式
            String  result=IOUtils.toString(conn.getInputStream(),"UTF-8");
            System.out.println(result);
            //注意关闭流和连接，这里省略
        }
    }
    
    public static String getJOSNString()
    {
        JSONObject jsonobject = new JSONObject();
        JSONObject jsonobject1 = new JSONObject();
        JSONObject jsonobject2 = new JSONObject();
        jsonobject2.put("name", "jingchenyong");
        jsonobject1.put("match", jsonobject2);
        jsonobject.put("query", jsonobject1);
        String jsonstring = JSON.toJSONString(jsonobject);
        return jsonstring;
    }
}
```

HttpClient实现GET

```java
package com.jingchenyong.test;
 
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
 
import org.apache.commons.collections.MapUtils;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
 
public class Test_HttpClient_GET
{
    
    public static void main(String[] args) throws Exception
    {
        String url="http://15.6.46.35:8080/platform/index.html";
        URIBuilder builder = new URIBuilder(url);
        CloseableHttpClient httpClient = HttpClients.createDefault();
        Map<String,Object> map=getMap();
        if(MapUtils.isNotEmpty(map)){
            for(Entry<String,Object> entry:map.entrySet()){
                builder.addParameter(entry.getKey(), String.valueOf(entry.getValue()));
            }
            url=builder.build().toString();
        }
        HttpGet get=new HttpGet(url);
        // 增加超时设置
        RequestConfig requestConfig = RequestConfig.custom().setConnectTimeout(1000).build();
        get.setConfig(requestConfig);
        
        //发送GET请求
        CloseableHttpResponse response=httpClient.execute(get);
        //获取状态码
        System.out.println(response.getStatusLine().getStatusCode());
        //把结果流转为字符串方式一
        /*
        String result=IOUtils.toString(response.getEntity().getContent());
        System.out.println(result);
        */
        //把结果流转为字符串方式二
        StringBuilder reMsgBuider = new StringBuilder();
        InputStream in = response.getEntity().getContent();
        BufferedReader reader = new BufferedReader(new InputStreamReader(in, "UTF-8"));
        String msg = null;
        // 读取返回消息体
        while ((msg = reader.readLine()) != null) {
            reMsgBuider.append(msg);
        }
        String result = reMsgBuider.toString();
        System.out.println(result);
        //关闭流和连接
        
    }
    public static Map<String,Object> getMap(){
        Map<String,Object> map=new HashMap<String,Object>();
        //map.put("name", "jingchenyong");
        //map.put("age", 26);
        return map;
    }
}
```

HttpClient实现POST

```java
package com.jingchenyong.test;
 
import org.apache.commons.io.IOUtils;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
 
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
 
public class Test_HttpClient_POST
{
    
    public static void main(String[] args) throws Exception{
        String jsonstring=getJOSNString();
        RequestConfig config = RequestConfig.custom().setSocketTimeout(30000).setConnectTimeout(30000).build();
        CloseableHttpClient client = HttpClients.custom().setDefaultRequestConfig(config).build();
        HttpPost post = new HttpPost("http://15.6.46.37:9200//henry/henry/_search");
        //填充post体
        post.setEntity(new StringEntity(jsonstring,"UTF-8"));
        CloseableHttpResponse response = client.execute(post);
        System.out.println("状态码为："+response.getStatusLine().getStatusCode());
        //方式一
        //System.out.println("获取的结果为(获取方式一)："+IOUtils.toString(response.getEntity().getContent()));
        //方式二 见GET
        //方式三
        System.out.println("获取的结果为(获取方式二)："+EntityUtils.toString(response.getEntity(), "UTF-8"));
    }
    
    public static String getJOSNString()
    {
        JSONObject jsonobject = new JSONObject();
        JSONObject jsonobject1 = new JSONObject();
        JSONObject jsonobject2 = new JSONObject();
        jsonobject2.put("name", "jingchenyong");
        jsonobject1.put("match", jsonobject2);
        jsonobject.put("query", jsonobject1);
        String jsonstring = JSON.toJSONString(jsonobject);
        return jsonstring;
    }
}
```

性能方面：
HttpURLConnection的访问速度比HttpClient要快。