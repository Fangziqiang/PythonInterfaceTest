#coding=utf-8

# 1、比较运算符
'''
表达式                             描述
x==y        x等于y
x<y         x小于y
x>y         x大于y
x>=y        。。。
x<=y        。。。
x!=y        。。。
x is y      x和y是同一个对象
x is not y  x和y是不同的对象
x in y      x是y容器(例如，序列)的成员
x not in y  x不是y容器(例如，序列)的成员
'''
#####################################################
# 2、相等运算符
# 如果想要知道两个东西是否相等，应该使用相等运算符，即两个等号==：
print 'foo'=='foo'
# True
print 'foo'=='bar'
# False
# 单个运算符是赋值运算符，是用来改变值得，而不能用来比较。
####################################################
# 3、is:同一性运算符
# 这个运算符比较有趣。它看起来和==一样，事实却不同：
x=y=[1,2,3]
z=[1,2,3]
print x==y
# True
print x==z
# True
print x is y
# True
print x is z
# False
# 最后一个为False是因为is运算符是判定同一性而不是相等性的。变量x和y都被绑定到同一个列表上，而变量z被绑定在另外一个
# 具有相同数值和顺序的列表上。他们的值可能相等，但却不是同一个对象。
####################################################
# 4、in:成员资格运算符
# in运算符可以像其他运算符一样在条件语句中使用。
name=raw_input("What's your name?")
if 's' in name:
    print "Your name contains the letter 's'."
else:
    print "Your name contains the letter 's'."
########################################################
# 5、字符串和序列比较
# 字符串可以按照字母顺序排列进行比较。
print 'alpha'<'beta'

# 如果要忽略大小写字母的区别，可以使用upper和lower
print 'FnOrD'.lower()=='Fnord'.lower()

# 6、布尔运算符
number=input("Enter a number between 1 and 10:")
if number>=1 and number<=10:
    print 'Great'
else:
    print 'Wrong'
# and运算符就是所谓的布尔运算符。他连接两个布尔值，并且两者都为真发回真，否则返回假。与它同类的还有两个运算符
# or和not，使用这3个运算符就可以随意结合真值。
if ((cash>price) or customer_has_good_credit) and not out_of_stock:
    give_goods()