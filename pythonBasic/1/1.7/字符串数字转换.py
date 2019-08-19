#coding=utf-8
'''数字转成字符串'''
# 方法一：
#     使用格式化字符串：
# 例：
tt=322
temp='%d'%tt
# temp即为tt转换成的字符串

# 方法二：
str(5)

'''字符串转换成数字'''
# 方法一：
#     int(str)
# 例：
str='60'
a=int(str)
# 方法二：
import string
tt='55'
ts=string.atoi(tt)
# ts即为tt转换成的数字