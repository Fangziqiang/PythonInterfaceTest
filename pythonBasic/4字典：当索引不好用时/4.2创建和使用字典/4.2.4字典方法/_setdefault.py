#coding=utf-8

# setdefault方法在某种程序上类似于get方法，就是能够获得与给定键相关连的值，除此之外，setdefault还能在字典中不含有给定键的情况下设定相应的键值。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# 可以看到，当键不存在的时候，setdefault返回默认值并且相应地更新字典。如果建存在，那么就返回其对应的值，但不改变字典
# 默认值是可选的，这点和get一样。如果不设定，会默认是None。
d={}
print d.setdefault('name','N/A')
# N/A

print d
# {'name': 'N/A'}

d['name']='Gumby'
print d.setdefault('name','N/A')
# Gumby

print d
# {'name': 'Gumby'}

e={}
print e.setdefault('name')
# None
print e
# {'name': None}

