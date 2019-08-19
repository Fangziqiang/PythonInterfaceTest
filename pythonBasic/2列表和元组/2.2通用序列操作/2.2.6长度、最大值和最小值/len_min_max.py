#coding=utf-8
import string

# 内建函数len、min和max非常有用。
# len函数返回序列中所包含元素的数量
# min函数和max函数则分别返回序列中最大和最小的元素

numbers=[100,55,689,556,689,689]
print len(numbers)
print min(numbers)
print max(numbers)

for i in range(len(numbers)):
    if numbers[i]==689:
        print "689第一次出现的位置是从左向右第",i+1,"个"
        break
    