#coding=utf-8

# compare(x,y)函数会在x<y时返回负数，在x>y时返回正数，x=y时返回0（根据你的定义）
# 内建函数cmp提供了比较函数的默认实现方式：
print cmp(42,32)
# 输出：1
print cmp(99,100)
# 输出：-1
print cmp(10,10)
# 输出：0

x=[4,6,2,1,7,9]
x.sort(cmp=None, key=None, reverse=False)
print x