#coding=utf-8
# import报错：cannot import name Template
# 原因：python脚本的同级目录有个string.py文件
from string import Template
from time import sleep

# string模块提供另外一种格式化值得方法：模板字符串。他的工作方式
# 类似于很多Unix shell里的变量替换。substitute这个模板方法
# 会用传递进来的关键字参数foo替换字符串中的$foo。如下所示：
s=Template('$x,glorious $x!')
# sleep(3)
print s.substitute(x='slurm')
# 输出： slurm,glorious slurm!

# 如果替换字段是单词的一部分，那么参数名就必须用括号括起来，从而准确指明结尾：
s=Template("It's ${x}tastic!")
print s.substitute(x='slurm')
# 输出：It's slurmtastic!

# 可以使用$$插入美元符号
s2=Template("Make $$ selling $x!")
print s2.substitute(x='slurm')
# 输出：Make $ selling slurm!

# 除了关键字参数外，还可以使用字典变量提供值/名称对
s2=Template("A $thing must nerver $action.")
d={}
d['thing']='gentleman'
d['action']='show his socks'
print s2.substitute(d)
# 输出结果：A gentleman must nerver show his socks.
# 方法safe_substitute不会因缺少值或者不正确使用$字符而出错。

