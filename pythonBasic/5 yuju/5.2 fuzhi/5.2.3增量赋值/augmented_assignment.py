#coding=utf-8

x=2
x+=1
x*=2
print x
# 6

# 对于其他数据类型也适用(只要二元运算符本身适用于这些数据类型即可)：
# 增量赋值可以让代码更加紧凑和简练，很多情况下更易读
fnord ='foo'
fnord +='bar'
fnord *=2
print fnord
# foobarfoobar