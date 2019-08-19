#coding=utf-8

# tuple函数的功能与list函数基本上是一样的：以一个序列作为参数并把它转换
# 为元组。如果参数就是元组，那么该参数就会被原样返回
print tuple([1,2,3])
# 输出：(1, 2, 3)

print tuple('abc')
# 输出： ('a', 'b', 'c')

print tuple((1,2,3))
# 输出：(1, 2, 3)