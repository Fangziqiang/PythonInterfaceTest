#coding=utf-8

# 字典的基本操作在很多方面与序列(sequence)类似：
# len(d)返回d中项(键-值对)的数量;
# d[k]返回关联到键k上的值
# d[k]=v将值v关联到键k上；
# del d[k]删除键为k的项；
# k in d检查d中是否含有键为k的项

# 尽管字典和列表有很多特性相同，但也有下面一些重要的区别。
#     键类型:字典的键不一定为整型数据,也可能是其他不可变类型,比如浮点型\字符串或者元组。
#     自动添加：即使那个键起初在字典中并不存在，也可以为它分配一个值，这样字典就会建立新的项.
# 而（在不使用append方法或者其他类似操作的情况下）不能将值关联到列表范围之外的索引上
#     成员资格：表达式k in d（d为字典），查找的是键，而不是值。表达式v in l(l为列表)，则用来查找值，而不是索引。

