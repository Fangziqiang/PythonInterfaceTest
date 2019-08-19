#coding=utf-8
from math import sqrt
for n in range(99,81,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
else:
    print "Didn't find it!"
# for和while循环中都可以使用continue、break语句和else子句