#coding=utf-8
from math import sqrt
# 使用exec和eval执行和求值字符串
# 执行一个字符串的语句是exec
exec "print 'Hello,world'"
scope={}
exec "sqrt=1" in scope 
print sqrt(4)
print scope['sqrt']

print scope.keys()
# 输出：['__builtins__', 'sqrt']