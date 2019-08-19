#coding=utf-8
numbers=[1,2,3,4,5,6,7,8,9,10]

print numbers[0:10:1]
# 输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print numbers[0:10:2]
# 输出：[1, 3, 5, 7, 9]

print numbers[::4]
# 输出：[1, 5, 9]

print numbers[3:6:3]
# 输出：[4]

# 步长不能为0，但步长可以是负数，即从右到左提取元素：
# 当使用一个负数作为步长时，必须让开始点（开始索引）大于结束点。
print numbers[8:3:-1]
# 输出：[9, 8, 7, 6, 5]

print numbers[10:0:-2]
# 输出：[10, 8, 6, 4, 2]

print numbers[0:10:-2]
# 输出：[]

print numbers[::-2]
# 输出：[10, 8, 6, 4, 2]

print numbers[5::-2]
# 输出：[6, 4, 2]

print numbers[:5:-2]
# 输出：[10, 8]

