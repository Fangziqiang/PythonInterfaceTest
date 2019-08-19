#coding=utf-8
################################################################
# 1、并行迭代
# 程序可以同时迭代两个序列。比如有下面两个列表：
names=['anne','beth','beth','beth','beth','beth','genorge','damon']
ages=[12,45,32,102,4,5,6,7]
# 如果想打印名字和对应的年龄，可以像下面这样做：
for i in range(len(names)):
    print names[i],'is',ages[i],'years old'
# 这里i是循环索引的标准变量名
# 而内建的zip函数可以用来进行并行迭代，可以把两个序列“压缩在一起，然后返回一个元组的列表：”
print zip(names,ages)
# 输出：[('anne', 12), ('beth', 45), ('genorge', 32), ('damon', 102)]
# 现在我们可以在循环中解包元组：
for name,age in zip(names,ages):
    print name,'is',age,'yers old'

# zip函数也可以作用于任意多的序列。关于它很重要的一点是zip可以对付不等长的序列：当最短的序列“用完”的时候就会停止：
print zip(range(5),xrange(10000))
# 输出：[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
# 不推荐使用range替换xrange，range会计算所有的数字，而使用xrange只计算前5个数字
# range函数一次创建整个序列，而xrange一次只创建一个数。当需要迭代一个巨大的序列时xrange会更高效

################################################################
# 2、编号迭代
# 在一个字符串列表中替换所有包含'xxx'的字符串
index=0
for string in names:
    if 'beth' in string:
        names[index]='[censored]'
        print names
        print "index=:%d" %index
    index +=1

# 另一种方法是使用内建的enumerate函数
for index,string in enumerate(names):
    if 'beth' in string:
        names[index]='[censored]'
# 这个函数可以在提供索引的地方迭代索引-值对。

# 3、翻转和排序迭代
# reversed和sorted:他们同列表的reverse和sort方法类似，但作用于任何序列或可迭代对象上，不是原地修改对象，
# 而是返回翻转或排序后的版本：
print sorted([4,3,6,8,3,5])
# [3, 3, 4, 5, 6, 8]
n=[1,4,56,7,8]
n.sort()
print n
# [1, 4, 7, 8, 56]

print sorted('Hello,world!')
# ['!', ',', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']

print list(reversed('Hello,world!'))
['!', 'd', 'l', 'r', 'o', 'w', ',', 'o', 'l', 'l', 'e', 'H']
# ''.join(iterable)使用''连接字符串列表
print ''.join(reversed('Hello,world!'))
# 输出：!dlrow,olleH




