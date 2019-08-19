#coding=utf-8

storage={}
storage['first']={}
storage['middle']={}
storage['last']={}
me='Magnus Lie Hetland'
storage['first']['Magnus']=[me]
storage['middle']['Lie']=[me]
storage['last']['Hetland']=[me]
print storage
# 输出：{'middle': {'Lie': ['Magnus Lie Hetland']}, 'last': {'Hetland': ['Magnus Lie Hetland']}, 'first': {'Magnus': ['Magnus Lie Hetland']}}
my_sister='Anne Lie Hetland'
storage['first'].setdefault('Anne',[]).append(my_sister)
storage['middle'].setdefault('Lie',[]).append(my_sister)
storage['last'].setdefault('Hetland',[]).append(my_sister)
print storage
