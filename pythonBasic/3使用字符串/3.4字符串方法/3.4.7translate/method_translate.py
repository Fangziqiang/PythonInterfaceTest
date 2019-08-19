#coding=utf-8
from string import maketrans
# translate方法和replace方法一样，可以替换字符串中的某些部分，但是和replace不同的是，
# translate方法只处理单个字符。他的优势在于可以同时进行多个替换，有些时候比replace效率高得多

# 在使用tranclate转换之前，需要先完成一张转换表。转换表中是以某字符替换某字符的对应关系。
# 因为这个表有多达256个项目，我们还是不要自己写了，使用string模块里面的maketrans函数就行

table=maketrans('cs', 'kz')
print len(table)
# 输出：256

print table[97:123]
# 输出：abkdefghijklmnopqrztuvwxyz

# 创建这个表后，可以将它作为translate方法的参数，进行字符串的转换如下
print 'this is an incredible test'.translate(table)
# 输出：thiz iz an inkredible tezt

# translate的第二个参数是可选的，这个参数是用来指定需要删除的字符。例如，如果想要模拟
# 一句语速超快的德国语，可以删除所有空格。
print 'this is an incredible test'.translate(table,' ')
# 输出：thizizaninkredibletezt

##########非英语字符串的问题#######################










