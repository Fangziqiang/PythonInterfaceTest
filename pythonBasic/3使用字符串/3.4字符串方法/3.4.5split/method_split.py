#coding=utf-8

# 这是一个很重要的字符串方法，他是join的逆方法，用来将字符串分割成序列
# 如果不提供任何分隔符，程序就会把所有空格作为分隔符(空格、制表、换行等)
s1='1+2+3+4+5'
print s1.split('+')
# 输出结果：['1', '2', '3', '4', '5']

s2='/usr/bin/env'
print s2.split('/')
# 输出：['', 'usr', 'bin', 'env']

s3='Using the default'
print s3.split()
# 输出结果：['Using', 'the', 'default']