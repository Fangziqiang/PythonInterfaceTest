#coding=utf-8

name=list('Perl')
print name
# 输出：['P', 'e', 'r', 'l']

name[2:]=list('ar')
print name
# 输出：['P', 'e', 'a', 'r']

# 使用分片赋值时，可以使用与原序列不等长的序列将分片替换
name2=list('Lilei')
name2[1:]=list('python2.7')
print name2

# 分片赋值语句可以不需要替换原有元素的情况下插入新的元素
numbers=[1,5]
numbers[1:1]=[2,3,4]
print numbers
# 输出：[1, 2, 3, 4, 5]

# 通过分片赋值来删除元素也是可行的
numbers2=[1,2,3,4,5]
numbers2[1:4]=[]
print numbers2
# 输出：[1, 5]



