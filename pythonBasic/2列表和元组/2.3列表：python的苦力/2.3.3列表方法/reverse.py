#coding=utf-8

# reverse方法将列表中的元素反向存放
x=[1,2,3,4,5]
x.reverse()
print x

# 如果需要对一个序列进行反向迭代，那么可以使用reversed函数，
# 这个函数并不返回一个列表，二是返回一个迭代器对象
# 使用list函数把返回的而对象转换成列表也是可行的：
y=['h','e','l','l','o']
print list(reversed(y))
# 输出：['o', 'l', 'l', 'e', 'h']