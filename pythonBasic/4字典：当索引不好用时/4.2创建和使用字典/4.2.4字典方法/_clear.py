#coding=utf-8
# clear方法清除字典中所有的值。这个是原地操作，类似于list.sort,所以无返回值。

d={}
d['name']='Gumby'
d['age']=42

print d
# 运行结果：{'age': 42, 'name': 'Gumby'}

returned_value=d.clear()

print d
# 运行结果：{}
print returned_value
# 运行结果：None

x1={}
y1=x1
x1['key']='value'
print y1
# 输出：{'key': 'value'}
x1={}
print y1
# 输出：{'key': 'value'}

x2={}
y2=x2
x2['key']='value'
print y2
# 输出：{'key': 'value'}
x2.clear()
print y2
# 输出：{}



