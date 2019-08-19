#coding=utf-8

# strip方法返回去除两侧(不包括内部)空格的字符串
print '    internal whitespace is kept     '.strip()
# 输出结果：internal whitespace is kept

name='gumby '
names=['gumby','smith','jones']
if name in names:
    print 'Found it!'

if name.strip() in names:
    print 'Found it!'

# 也可以指定需要去除的字符，将他们列为参数即可
print '**** SPAM * for * everyone!!!***'.strip(' *!')
# 输出解果：SPAM * for * everyone
# 这个方法只会去处两侧的字符，所以字符串中的星号没有被去掉