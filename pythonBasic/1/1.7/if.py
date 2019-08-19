#coding=utf-8
import time

if 1==2:
    print "one equals two"
else:
    print "one donot equals two"

x=input("x:")
y=input("y:")
if x==y:
    print "x equals y"
else:
    print "x donot equals y"

# 获取时间
now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
now2 = time.strftime("%M",time.localtime())

now3 = int(now2)
print int(now2)
if now3%60 == 0:
    print "Time is on the hour"
else:
    print "Time is not on  the hour"
