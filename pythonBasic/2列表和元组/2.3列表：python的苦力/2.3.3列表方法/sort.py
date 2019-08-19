#coding=utf-8

# sort方法用于在原位置对列表进行排序。
x=[4,6,2,1,7,9]
x.sort()
print x

# 当用户需要一个排好序的列表副本，同时又保留原有列表不变的时候，需要先
# 把a的副本赋值给b，然后对b进行排序。如下例所示：
a=[4,6,2,1,7,9]
b=a[:]
b.sort()
print "排序后a：",a
print "排序后b：",b
# 运行结果：
# 排序后a： [4, 6, 2, 1, 7, 9]
# 排序后b： [1, 2, 4, 6, 7, 9]

# a[:]得到的是包含了a所有元素的分片，这是一种很有效率的赋值整个列表
# 的方法。只是简单的把a赋值给b是没用的，因为这样做就让a和b都指向同一个列表了。
c=[4,6,2,1,7,9]
d=c
d.sort()
print "排序后c：",c
print "排序后d：",d
# 运行结果：
# 排序后c： [1, 2, 4, 6, 7, 9]
# 排序后d： [1, 2, 4, 6, 7, 9]

# 另一种获取已排序列表副本的方法是使用sorted函数
x1=[4, 6, 2, 1, 7, 9]
y1=sorted(x1)
print "排序后x1：",x1
print "排序后y1：",y1
# 运行结果：
# 排序后x1： [4, 6, 2, 1, 7, 9]
# 排序后y1： [1, 2, 4, 6, 7, 9]

# 这个函数实际上可以用于任何序列，却总是返回一个列表：
print sorted('python')
# 如果想把一些元素按相反的顺序排列，可以先使用sort（或者sorted），然后
# 再调用reverse方法。
greeting='hellohowareyou'
greeting2=sorted(greeting)
greeting2.reverse()
print greeting2
print greeting


