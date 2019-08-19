#coding=utf-8

x=1
while x<=100:
    print x
    x += 1
    
name=''
# while not name:
#     name=raw_input("Please enter your name:")
# print "Hello,%s!"%name

# 如果输入一个空格，程序也会接受这个名字，可以这样修改程序：
while not name or name.isspace():
    name=raw_input("Please enter your name:")
print "Hello,%s!"%name
# 或者使用while not name.strip()