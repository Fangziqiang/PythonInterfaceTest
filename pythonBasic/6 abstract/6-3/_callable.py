#coding=utf-8
# -*- coding:utf-8 -*-

# 一般而言，要判断某个对象是否可调用，可使用内置函数callable

import math
x = 1
y = math.sqrt

print callable(x)
print callable(y)
print y(2)

#使用def定义函数
def hello(name):
    return "Hello,"+name+"!"
print hello("python")
print hello("testor")