#coding=utf-8
# 如果需要检查多个条件，就可以使用elif，它是“else if”的缩写，也是if和else子句的联合使用——
# 也就是具有条件的else子句

num=input("Enter a number:")

if num>0:
    print "The number is positive"
elif num<0:
    print "The number is nagative"
else:
    print "The number is zero"