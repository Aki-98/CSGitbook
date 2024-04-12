Float设计的初衷：实现文字环绕效果

包裹：

   收缩

   坚挺

   隔绝（BFC-块级格式化上下文）

具有包裹性的：

   display:inline-block/table-cell/...

   position:absolute(近亲)/fixed/sticky

   overflow:hidden/scroll

具有破坏性，浮动后使父元素高度塌陷：

   display:none

   position:absolute(近亲)/fixed/sticky

   浮动使父元素高度塌陷是标准，当父元素高度塌陷后，置于父元素下的元素没有限制会在空间允许的条件下浮动上来，这就是文字环绕图片的原因；

   或者是图片位于文字之间，图片的浮动会使其突破父元素向左或右浮动后文字拼接呈环绕效果（浮动的破坏性只是为了实现文字环绕效果

清除浮动（带来的影响）：

   法1：脚底插入clear:both;

   法2：父元素BEC（IE8+)或haslayout（IE6/IE7）

Clear常用形式：

1. HTML block水平元素底部走起<div...></div>
2. CSS after伪元素底部生成  .clearfix:after{}(不兼容IE6/IE7)

父元素BFC(IE8+)或haslayout(IE6/IE7)

   float:left/right

   position:absolute/fixed

   overflow:hidden/scroll(IE7+)

   display:inline-block/table-cell(IE8+)

   width/height/zoom:1/...(IE7/IE7)

权衡后的策略

```css
.clearfix:after{content:";display:block;height:0;overflow:hidden;clear:both;}

.clearfix{*zoom:1;}

.fix:after{}

.fix{}
```

更好的方法：

```css
.clearfix:after{content:";display:table;clear:both;}

.clearfix{*zoom:1;}
```

.clearfix应用在包含浮动子元素的父级元素上

haslayout（浮动也会触发）在IE6/IE7下不合适