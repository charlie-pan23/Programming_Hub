# Java Programming
-----
## Lab 2

%	modulo/remainder 取模/取余         

| 1/0 | 1.0/0.0 |
|---|---|
|java.lang.ArithmeticException|结果是Infinity（无穷大）|
|报错：整数运算遵循严格的算术规则，而在这些规则中，除以零是没有定义的，因此Java选择通过抛出异常来指示这种错误的操作。|这是因为浮点数运算在Java中遵循IEEE 754标准，该标准允许浮点数运算产生正无穷大（Infinity）、负无穷大（-Infinity）和非数（NaN，即Not a Number）这些特殊的结果。|

√负数->	NaN

### 逻辑运算符

|符号|表示|用法|含义|
|---|---|---|---|
|&&|逻辑与（AND）|expression1 && expression2|当expression1和expression2都为true时，整个表达式的结果为true；否则为false。|
|\|\||逻辑或（OR）|expression1 \|\| expression2|当expression1和expression2中至少有一个为true时，整个表达式的结果为true；当两者都为false时，结果为false。|
|!|逻辑非（NOT）|!expression|如果expression为true，则整个表达式的结果为false；如果expression为false，则结果为true。|
|^（在某些情况下用作布尔运算符）|逻辑异或（XOR）|expression1 ^ expression2|当expression1和expression2中有且仅有一个为true时，整个表达式的结果为true；如果两者都为true或都为false，结果为false。|
|&（也可用于布尔运算）|条件AND|expression1 & expression2|与逻辑与&&类似，但不同之处在于，无论expression1的结果如何，expression2都会被评估。|
|\|（也可用于布尔运算）|条件OR|expression1 \| expression2|与逻辑或||类似，但不同之处在于，无论expression1的结果如何，expression2都会被评估。|


### 当一个表达式中包含多个运算符时，高优先级的运算符会先被计算。以下是一些常见运算符的优先级，从高到低排列（部分）：

|符号|备注|
|---|---|
|一元运算符|如逻辑非!、正号+、负号-、自增++、自减--等|
|乘性运算符|乘法*、除法/、取模%|
|加性运算符|加法+、减法-|
|移位运算符|左移<<、右移>>、无符号右移>>>|
|关系运算符|大于>、小于<、大于等于>=、小于等于<=、实例测试instanceof|
|相等性运算符|等于==、不等于!=|
|按位与|&|
|按位异或|^|
|按位或|\||
|逻辑与|&&|
|逻辑或|\|\||
|条件运算符（三元运算符）|? :|
|赋值运算符|=、+=、-=、*=、/=等|