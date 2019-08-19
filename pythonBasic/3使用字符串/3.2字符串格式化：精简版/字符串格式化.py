#coding=utf-8

# 字符串格式化适用字符串格式化操作符即百分号%来实现
format="Hello,%s,%s enough for ya?"
values=('world','Hot')
print format %values
# 输出：Hello,world,Hot enough for ya?

# 注意：如果使用列表或者其他序列代替元组，那么序列就会被解释为一个值。
# 只有元组和字典可以格式化一个以上的值。例如下面这个例子：
values2=['world','Hot']
# print format %values2
# 上面的打印语句会报错，报错信息：TypeError: not enough arguments for format string

# 格式化字符串的%s部分称为转换说明符，他们标记了需要插入转换值的位置。
# s表示值会被格式化为字符串---如果不是字符串，则会用str将其转换为字符串。
# ----如果要在格式化字符串里面包括百分号，那么必须使用%%，这样python就不会将百分号误以为是转换说明符了。
