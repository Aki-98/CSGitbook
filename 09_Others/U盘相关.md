Q1：能刷和不能刷的U盘有什么区别？
- 无关：文件系统，已测：exFAT、FAT32、NTFS
- 无关：柱面头也没有关系，1或者0都可能能刷也可能刷不了。
- 未知：和每个扇区的大小有没有关系？
- 无关：完全没有坏道的U盘也可能刷不了。
- 无关：u盘里的system volume information文件夹，这只是个backup的缓存文件。
	- https://zhidao.baidu.com/question/1049972701400525059.html
- 未知：Model，VendorCoProductCode（Val&Amaebi可刷）、KingstonDataTraveler3.0（Amaebi可刷）、SanDiskCruzerGlide3.0（Val可刷）
- 可能有关：USB2.0端口供电不足。

Q2：怎么格式化写保护的U盘？
- 无效：修改注册表项目https://zhidao.baidu.com/question/23062716.html?si=1
- 无效：用diskpart 输入attributes disk clear readonly
- 无效：DiskGenius、系统修改U盘属性
- 无效：利用cmd将U盘格式转换为NTFS convert L: /fs:ntfs /nosecurity/x

其它：
1.U盘的Attribute
- A代表All，可读可写
- R代表Read，只可读
2.不要整理U盘的碎片，会影响U盘寿命。