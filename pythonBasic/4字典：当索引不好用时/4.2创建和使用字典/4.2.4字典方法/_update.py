#coding=utf-8

# update方法可以利用一个字典项更新另一个字典：
# 提供的字典项会被添加到旧的字典中，若有相同的键则会进行覆盖
d={'title':'Python Web Site',
   'url':'http://www.python.org',
   'changed':'Mar 14 22:09:15 MET 2008'}
x={'title2':'Python language Website'}
d.update(x)
print d
