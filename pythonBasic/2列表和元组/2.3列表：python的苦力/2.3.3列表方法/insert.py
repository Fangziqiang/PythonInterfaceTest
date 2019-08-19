#coding=utf-8

# insert方法用于将对象插入到列表中：
numbers=[1,2,3,5,6,7]
numbers.insert(3, 'four')
print numbers

numbers2=[1,2,3,5,6,7]
# insert方法的操作也可以用分片赋值来实现
numbers2[3:3]=['four']
print numbers2