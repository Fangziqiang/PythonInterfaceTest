#coding=utf-8

# keys方法将字典中的键以列表形式返回，而iterkeys则返回针对键的迭代器
d={'title':'Python Web Site','url':'http://www.python.org',
   'spam':0}
print d.keys()
# ['url', 'spam', 'title']

print d.iterkeys()
# <dictionary-keyiterator object at 0x00000000027B7408>