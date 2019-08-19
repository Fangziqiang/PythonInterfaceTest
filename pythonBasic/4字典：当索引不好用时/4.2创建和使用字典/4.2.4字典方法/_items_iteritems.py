#coding=utf-8

# items方法将所有的字典项以列表方式返回，这些列表项中的每一项都来自于(键，值),但是项在返回时并没有特殊的顺序
d={'title':'Python Web Site','url':'http://www.python.org',
   'spam':0}
print d.items()

# iteritems方法的作用大致形同，但是会返回一个迭代器对象而不是列表：
it=d.iteritems()
print it
# 输出：<dictionary-itemiterator object at 0x00000000026D7408>

# Convert the iterator to a list
print list(it)
# 输出：[('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')]