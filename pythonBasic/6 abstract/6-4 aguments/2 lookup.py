#coding=utf-8

'初始化数据结构的函数'
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

'存储人员姓名的函数'
def lookup(data,lable,name):
    return data[lable].get(name)

Lie = 'Magnus Lie Hetland'
storage={}
init(storage)
print (storage)
# {'middle': {}, 'last': {}, 'first': {}}

lookup(storage, 'middle', 'Lie')
print (storage)