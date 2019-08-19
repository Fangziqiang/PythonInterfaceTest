#coding=utf-8

# 列表推导式是利用其他列表创建新列表的一种方法

print [x*x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 只打印能被3整除的平方数
print [x*x for x in range(10) if x%3==0]
# [0, 9, 36, 81]

# 也可以增加更多for语句的部分：
print [(x,y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 作为对比，下面的代码使用两个for语句创建了相同的列表：
result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
        
        
################################
# 也可以结合if子句联合使用，
girls=['alice','bernice','clarice']
boys=['chris','arrnold','bob']
print [b+'+'+g for b in boys for g in girls if b[0]==g[0]]
# ['chris+clarice', 'arrnold+alice', 'bob+bernice']
# 这样就得到了那些名字首字母相同的男孩和女孩

###更优方案
# 这个程序建造了一个叫做letterGirl的字典，其中每一项都把单字母作为键，以女孩名字组成的列表作为值。
letterGirls={}
for girl in girls:
#     如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
    letterGirls.setdefault(girl[0],[]).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]

    
    
    
    






