#coding=utf-8

string1='Hello'

# 因为字符串不能像列表一样被修改，所以有时候根据字符串创建列表会很有用。list函数可以实现这个操作
# list函数适用于所有类型的序列，而不只是字符串
list1=list(string1)

# 可以使用下面的表达式将一个由字符组成的列表转换成为字符串：
string2=''.join(list1)

print list1
print string2




