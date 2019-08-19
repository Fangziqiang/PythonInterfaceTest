#coding=utf-8
from math import sqrt

# 1、break
for n in range(99,0,-1):
#     -1为步长，表示每对相邻数字之间的差别。
    root=sqrt(n)
    if root==int(root):
        print n
        break
    

# 2、continue
# continue语句比break语句用的少很多，它会让当前的迭代结束，跳到下一轮循环的开始
for x in seq:
    if codition1:continue
    if codition2:continue
    if codition3:continue
    
    do_something()
    do_something_else()
    do_another_thing()
    etc()
# 很多时候，只要使用if语句就可以了：
for x in seq:
    if not (codition1 or codition2 or codition3):   
        do_something()
        do_something_else()
        do_another_thing()
        etc()


