#coding=utf-8

scoundrel={'age':42,'first name':'Robin','last name':'of locksley'}
robin=scoundrel
scoundrel=None
print scoundrel
# 输出：None
print robin
# 输出：{'last name': 'of locksley', 'first name': 'Robin', 'age': 42}
robin=None
# 首先robin和scoundrel都被绑定到同一个字典上，所以当  scoundrel被设置为None时，字典通过robin还是可用的。但是
# 当把robin也设置为None的时候，字典就漂在内存里面了，没有任何名字绑到它上面，没有办法获取和使用它，所以Python解释器直接删除
# 了那个字典。也可以使用None之外的其他值，字典同样会消失不见。

# 另一个方法是使用del语句，它不仅会移除一个对象的引用，也会移除那个名字本身。
x=['Hello','world']
y=x
y[1]='Python'
print x
# ['Hello', 'Python']
del x 
print y
# ['Hello', 'Python']
# x和y都指向同一个列表，但是删除x并不会影响y,原因就是删除的只是名称，而不是列表本身








