#coding=utf-8

# lower方法返回字符串的小写字母版
print 'Trondheim Hammer Dance'.lower()
# 输出：trondheim hammer dance

# 如果存储的是'Gumby'而用户输入'gumby'甚至是'GUMBY',结果也是一样。解决方法就是在存储和搜索时把所有名字都转换为小写
name='Gumby'
names=['gumby','smith','jones']
if name.lower() in names:
    print 'Found it!'

# title方法会将字符串转换为标题——也就是所有单词的首字母大写，而其他字母小写。
print "that's all folks".title()
# 输出结果：That'S All Folks