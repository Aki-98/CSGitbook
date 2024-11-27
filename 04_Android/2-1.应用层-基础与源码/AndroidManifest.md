# meta-data

**基本用法：存储全局信息**

定义在<activity>等标签外部，在<application>标签内部

可以保存boolean、int、String、float

AndroidManifest.xml中

```xml
<manifest>
	<application
		android:icon="@drawable/icon"
		android:label="@string/app_name">
		<meta-data android:name="my_test_metagadata" android:value="testValue"/>
		<activity
			android:name=".MainActivity"
			android:label="@string/app_name">
			<intent-filter>
				<action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity >
	</application >
</manifest>
```

读取

```java
Application ai = getPackageManager().getApplicationInfo(getPackageName(),PackageManager.GET_META_DATA);
Bundle bundle = ai.metaData;
String myApiKey = bundle.getString("my_test_metagadata");
```

**Lib和API的使用**

有时使用库或者api的时候需要定义meta-data

比如使用GooglePlayService的时候需要定义版本才能使用

```xml
<meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version"/>
```

**配置Activity**

有时Activity需要传递参数以正确配置

这种情况meta-data标签需要被放置在<activity>内部

```xml
<manifest>
	<application
		android:icon="@drawable/icon"
		android:label="@string/app_name">
		<activity
			android:name=".MainActivity"
			android:label="@string/app_name">
			<intent-filter>
				<action android:name="android.intent.action.MAIN"/>
				<category android:name="android.intent.category.LAUNCHER"/>
		</activity>
		<activity android:name=".SearchableActivity" >
			<intent-filter>
				<action android:name="android.intent.action.SEARCH"/>
	        </intent-filter>
			<meta-data android:name="android.app.searchable"
        	           android:resource="@xml/searchable"/>
		</activity >
	</application >
</manifest>
```

```java
try{
    ActivityInfo ai = getPackageManager().getActivityInfo(this.getComponentName(),PackageManager.GET_META_DATA);
    Bundle bundle = ai.metaData;
    if(bundle!=null){
        String apiKey = bundle.getString("apikey");
        Log.d(this.getClass().getSimpleName(),"apiKey = "+apiKey);
    }
}catch(PackageManager.NameNotFoundException e){
    Utilties.log(this.getClass().getSimpleName(),"Fail to load meta-data, NameNotFound: "+e.getMessage());
}catch(NullPointerException e){
    Log.e(this.getClass().getSimpleName(),"Failed to load meta-data,Null Pointer: "+e.getMessage());
}
```

**Android usage:**

Intents are great example for that - If you want to pass data in intents it has to be primitive because Android only have pre-build metadata about those kind of objects. (String and integer have different binary structure that the system know how to work with).

Intents also allow you to build your own metadata to your custom objects via the Parcel class (this process of manually build you own metadata called marshalling)

