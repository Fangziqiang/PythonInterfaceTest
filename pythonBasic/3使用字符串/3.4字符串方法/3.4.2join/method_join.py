#coding=utf-8

# join方法是非常重要的方法，它是split方法的逆方法，用来在队列中添加元素
seq1=[1,2,3,4,5]
sep='+'
# print sep1.join(seq1)
# 连接数字列表，会报错：TypeError: sequence item 0: expected string, int found

#连接字符串列表
seq2=['1','2','3','4','5']
print sep.join(seq2)
# 输出：1+2+3+4+5

dirs='','usr','bin','env'
print '/'.join(dirs)
# 输出：/usr/bin/env

print 'C:'+'/'.join(dirs)
# 输出：C:/usr/bin/env