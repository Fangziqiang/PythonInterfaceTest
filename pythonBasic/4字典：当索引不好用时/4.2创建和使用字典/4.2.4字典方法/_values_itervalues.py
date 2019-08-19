#coding=utf-8

# values方法以列表的形式返回字典中的值(itervalues返回值得迭代器)。与返回键的列表不同的是，
# 返回值的列表中可以包含重复的元素：
d={}
d[1]=1
d[2]=2
d[3]=3
d[4]=1
print d.values()
# [1, 2, 3, 1]