#coding=utf-8

# 1、用字符串做参数
def try_to_change(n):
    n='Mr.Gumby'
name='Mrs.Entity'
try_to_change(name)
print ()
print ('用字符串做参数调用函数后变量name的值为：'+name)
# Mrs.Entity
'同样，当在函数内部重新关联参数即给他赋值时，函数外部的变量不会受到影响'
#################################
# 2、将可变的数据结构用作参数
# 将同一个列表赋给两个变量时，这两个变量将同时指向这个列表。
def change(n):
    n[0]='Mr.Gumby'
names=['Mrs.Entity','Mr.Thing']
change(names)
print (names)
# 输出：['Mr.Gumby', 'Mr.Thing']
# 可以使用下面的表达式复制整个列表的切片，将会得到一个副本
# name = ['Mrs.Entity','Mr.Thing']
# n=names[:]




