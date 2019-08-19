#coding=utf-8
from selenium.webdriver.common.actions.interaction import KEY

# 多个赋值操作可以同时进行
x,y,z=1,2,3
print x,y,z
# 1 2 3

# 交换两个(或更多个)变量
x,y=y,x
print x,y,z
# 2 1 3

# 事实上，这里所做的事情叫做序列解包或可选代解包——将多个值的序列解开，然后放到变量的序列中：
values=1,2,3
print values
# (1, 2, 3)
x,y,z=values
print ("x=%d"%x)
# 1

# 假设需要获取字典中任意的键值对，可以使用popitem方法，这个方法将键值对作为元组返回，那么这个元组就可以直接赋值到两个变量中：
scoundrel={'name':'Robin','girlfriend':'Marion'}
key,value=scoundrel.popitem()
print key,value
# girlfriend Marion







