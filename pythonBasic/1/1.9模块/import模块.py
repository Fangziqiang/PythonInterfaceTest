#coding=utf-8
import math
x=input("请输入年纪:")
# floor函数将一个数取整为小于等于该数的最小的整数
# 与floor相对的函数是ceil，可以将给定的数值转换成为大于或者等于它的最小整数
age=int(math.floor(x))
print (u"年龄最小是%d" %age)
age2=math.ceil(x)
print (u"年龄最大是%d" %age2)

# 在确定不会导入多个同名函数（从不同模块导入）的情况下，可以使用import
# 的另外一种形式：
from math import sqrt
print sqrt(9)