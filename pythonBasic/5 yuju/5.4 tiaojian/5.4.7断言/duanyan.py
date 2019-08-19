#coding=utf-8

# 断言使用的关键字是assert
# 如果需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert语句就有用了，它可以在程序中置入检查点
# 条件后可以添加字符串，用来解释断言：
age=10
assert 0<age<100

age=-1
assert 0<age<100,'The age must be realistic'
# 报错信息：AssertionError: The age must be realistic