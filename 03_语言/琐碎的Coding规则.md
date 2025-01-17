switch的case中请默认追加default语句即使是空语句，default也需要添加break

else需要写花括号

常量.equals(变量)

TextUtils.isEmpty(String变量)

用ArrayList.isEmpty() 而不是size(ArrayList) == 0

链式调用时每次调用新换一行

0~num-1的循环比 1~num的循环更有效率

在 CPU 级别，比较 i < num的指令（通常是 cmp 和 jl）比 i <= num 的指令（cmp 和 jle）稍微简单。

通过一个条件表达式标识2~12，2<=i <13更合理，1.刚好体现了下边界，13-2=11刚好为数字个数（循环次数）