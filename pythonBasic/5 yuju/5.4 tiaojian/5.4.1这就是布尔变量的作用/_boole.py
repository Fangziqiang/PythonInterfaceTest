#coding=utf-8

# 下面的值作为布尔表达式的时候，会被解释器看做假(false):
# False None 0 "" () [] {}
# 换句话说，也就是标准值False和None、所有类型的数字0(包括浮点型、长整型和其他类型)、空序列(比如空字符串、元组和
# 列表)以及空的字典都为假。其他的一切都被解释为真，包括特殊值True。
print True==0
# False
print False==0
# True
print True+False+20
# 21

# 布尔值True和False属于布尔类型，bool函数可以用来(和list、str以及tuple一样)转换其他值。
print bool('I think,therefore I am')
# True
print bool("")
# False
print bool(42)
# True
print bool(0)
# False

# 因为所有值都可以用作布尔值，所以几乎不需要对他们进行显示转换(可以说Python会自动转换这些值)