#coding=utf-8
from math import pi

# 简单转换只需要写出转换类型，使用起来很方便

print 'Price of eggs:$%d' % 42
# 输出结果：Price of eggs:$42

print 'Hexadecimal price of eggs:%x' % 42
# Hexadecimal:意思是十六进制
# decimal：十进制
# 输出结果：Hexadecimal price of eggs:2a

print "Pi:%f..." %pi
# 输出结果:Pi:3.141593...

print "Very inexact estimate of Pi:%i" %pi
# 输出结果：Very inexact estimate of Pi:3

print "Using str:%s" %42L
# 输出结果：Using str:42

print "Using repr:%r" %42L
# 输出结果：Using repr:42L