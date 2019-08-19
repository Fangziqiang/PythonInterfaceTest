#coding=utf-8

# 所有标准的序列操作（索引、分片、乘法、判断成员资格、求长度、取最小值和
# 最大值）对字符串同样适用，但是，字符串都是不可变的。因此类似以下的分片
# 赋值是不合法的：
website='http://www.python.org'
website[-3:]='com'
print website
# 输出会报错：TypeError: 'str' object does not support item assignment
