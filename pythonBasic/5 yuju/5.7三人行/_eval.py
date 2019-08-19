#coding=utf-8

print eval(raw_input("Enter an arithmetic expression:"))
scope={}
scope['x']=2
scope['y']=3
print eval('x*y',scope)