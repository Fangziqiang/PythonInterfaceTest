#coding=utf-8

# popitem方法类似于list.pop,后者会弹出列表的最后一个元素。但不同的是popitem弹出随机的项，因为字典并没有
# “最后的元素”或者其他有关顺序的概念。要向一个接一个地移除并处理项，这个方法就非常有效了（因为不用首先获取键的列表）。
d={'title':'Python Web Site','url':'http://www.python.org',
   'spam':0}
print d.popitem()

print d