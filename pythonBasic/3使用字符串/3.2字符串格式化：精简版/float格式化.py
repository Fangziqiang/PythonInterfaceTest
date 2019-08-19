#coding=utf-8
from math import pi

# 如果要格式化实数(浮点数)，可以使用f说明符类型，同时提供所需要的精度：
# ---一个句点再加上希望保留的小数位数。
# 例：
format="P1 with three decimals:%.3f"
print format % pi
# 输出结果：P1 with three decimals:3.142