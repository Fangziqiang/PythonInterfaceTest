#coding=utf-8

# 一个简单的for语句就能循环字典的所有键，就像处理序列一样：
d={'x':1,'y':2,'z':3}
# for key in d:
#     print key,'corresponds to',d[key]
#     
for key,value in d.items():
    print key,'corresponds to',value