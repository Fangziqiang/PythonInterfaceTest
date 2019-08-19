#coding=utf-8
# str、repr、和反引号是将Python值转换为字符串的3种方法。
# str函数会把值转换为合理形式的字符串
# 而repr会创建一个字符串，它以合法的Python表达式的形式来表示值
# 例：
print repr("Hello world!")
# 输出：'Hello world!'

print str("Hello world!")
# 输出：Hello world!

# repr(x)的功能也可以使用`x`实现（注意，`是反引号，而不是单引号）。
# 在python3.0中，已经不再使用反引号。
# 如果希望打印一个包含数字的句子，那么反引号就很有用了。比如：
temp=5
# 下面这个语句会报错：
# print "The temperature is"+temp

# 这个就可以正常打印：
print "The temperature is "+`temp`
print "The temperature is "+repr(temp)
print "The temperature is "+str(temp)



