#coding=utf-8

# 使用星号就可以从转换元组中读出字段宽度
# %xyz
# x：符号对齐方式，0表示数字将会用0填充，负号(-)用来左对齐数值
# 可以使用*作为字段宽度或者精度(或者两者都是用*),此时数值会从元组参数中读出
# y:宽度
# z:精度，如果是*，那么精度将会从元组中读出
# 使用给定的宽度打印格式化后的价格列表
width=input("Please enter width:")
price_width=10
item_width=width-price_width
header_format='%-*s%*s'
format='%-*s%*.2f'

print '='*width
print header_format %(item_width,'Item',price_width,'Price')
print '='*width


print format %(item_width,'Apples',price_width,0.4)
print format %(item_width,'Pears',price_width,0.5)
print format %(item_width,'Cantaloupes',price_width,1.92)
print format %(item_width,'Dried Apricots(16 oz)',price_width,8)
print format %(item_width,'prunes(4 lbs)',price_width,12)

print '='*width