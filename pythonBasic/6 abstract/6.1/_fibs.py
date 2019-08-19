#coding=utf-8
# -*- coding:utf-8 -*-

#斐波那契数列（任一个数都是前两数之和的数字序列）：
def fibs(num):
    '这里是函数注释：在def语句后面，以及模块和类的开头，添加这样的字符串，即可为函数添加文档注释'
    result=[0,1]
    for i in range(int(num)-2):
        result.append(result[-1]+result[-2])
    return result
    
num=input("How many fibonacci numbers dou you want?")
print (fibs(num))
'打印函数注释文档'
print ("打印函数注释文档：")
print (fibs.__doc__)

'特殊的内置函数help很有用，可以获取有关函数的信息'
print ("打印函数有关信息：")
print (help(fibs))
