#coding=utf-8
numbers=[1,2,3,4,5,6,7,8,9,10]
tag='<a href="http://www.python.org">Python web site</a>'
# 分片操作的实现需要提供两个索引作为边界，第一个索引包含在分片内，第二个索引不包含在分片内。
print tag[3:9]

# 如果分片所得部分包括序列结尾的元素，那么，只需置空最后一个索引即可：
print numbers[-3:]

# 这种方法同样适用于序列开始的元素：
print numbers[:3]

# 如果需要复制整个序列，可以将两个索引都置空
print numbers[:]

# 对http://www.something.com的URL进行分割
url=raw_input("Please input the URL:")
domain=url[11:-4]
print "Domain name:"+domain