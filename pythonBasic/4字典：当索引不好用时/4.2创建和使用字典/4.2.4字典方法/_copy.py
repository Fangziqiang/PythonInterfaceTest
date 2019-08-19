#coding=utf-8
from copy import deepcopy

# copy方法返回一个具有相同键值对的新字典
x={'username':'admin','machines':['foo','bar','baz']}
y=x.copy()
y['username']='mlh'
y['machines'].remove('bar')
print y
# 运行结果：{'username': 'mlh', 'machines': ['foo', 'baz']}

print x
# 运行结果：{'username': 'admin', 'machines': ['foo', 'baz']}
# 可以看到，当在副本中替换值的时候，原始字典不受影响，但是，如果修改了某个值(原地修改，而不是替换)，
# 原始的字典也会改变，因为同样的值也存储在原字典中
# 避免这个问题的一种方法就是使用深复制(deep copy),复制其包含所有的值，可以使用copy模块的deepcopy函数来完成操作

d={}
d['names']=['Alfred','Bertrand']
c=d.copy()
dc=deepcopy(d)
d['names'].append('Clive')

print c
# {'names': ['Alfred', 'Bertrand', 'Clive']}
print dc
# {'names': ['Alfred', 'Bertrand']}



