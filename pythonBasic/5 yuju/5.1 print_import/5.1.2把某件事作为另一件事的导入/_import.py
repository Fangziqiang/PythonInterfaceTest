#coding=utf-8

# 从模块导入函数的时候，可以使用
import somemodule
# 或者
from somemodule import somefunction
# 或者
from somemodule import somefunction,anotherfunction,yetanotherfunction
# 或者
from somemodule import *

# 如果两个模块都有open函数，只需要使用第一种方式，然后像下面这样使用函数：
module1.open()
module2.open()
# 但还有另外的选择，可以在语句末尾增加一个as子句，在该子句后给出名字，或为整个模块提供别名：
import math as foobar
print foobar.sqrt(4)
# 也可以为函数提供别名：
from module1 import open as open1
from module2 import open as open2

