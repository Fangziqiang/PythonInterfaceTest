#coding=utf-8

# find方法可以在一个较长的字符串中查找子字符串。它返回子字符串所在位置的最左端索引。如果没有找到则返回-1
s1='With a moo-moo here,and a moo-moo there'
print s1.find('moo')
print s1[7:10]

subject="$$$ Get rich now!!! $$$"
print subject.find('$$$')
# 输出：0
print subject.find('$$$',1)   #只提供起点
# 输出：20

print subject.find('!!!',1)   
# 输出：16
print subject.find('!!!',0,16)#提供起始点和结束点
# 输出：-1
# 注意：由起始和终止值指定的范围（第二和第三个参数）包含第一个索引，但不包含第二个索引。