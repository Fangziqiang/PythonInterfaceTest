#coding=utf-8

# fromkeys方法使用给定的键建立新的字典，每个键默认对应的值应为None。
print {}.fromkeys(['name','phone'])
# 输出结果：{'phone': None, 'name': None}

# 也可以直接给在所有字典的类型dict上面调用方法
dict.fromkeys(['name','phone'])
# 如果不想使用None作为默认值，也可以自己提供默认值。
print dict.fromkeys(['name','phone'],'(unknown)')