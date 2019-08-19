#coding=utf-8
# 下面的语句中加入了一些不必要的内容，if语句里面可以嵌套使用if语句，就像下面这样：
name=raw_input("What's your name:")
if name.lower().endswith("fang"):
    if name.startswith("Mr."):
        print "Hello,Mr.Fang"
    elif name.startswith("Mrs."):
        print "Hello,Mrs.Fang"
    else:
        print "Hello,Fang"
else:
    print "Hello,stranger"