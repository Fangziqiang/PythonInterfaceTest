#coding=utf-8

items=[('name','Gumby'),('age',42)]
d=dict(items)
print d
# 输出：{'age': 42, 'name': 'Gumby'}

print d['name']
# 输出：Gumby

# dict函数还可以通过关键字参数来创建字典，如下例所示：
d2=dict(name='Gumby',age=42)
print d2
# 输出：{'age': 42, 'name': 'Gumby'}