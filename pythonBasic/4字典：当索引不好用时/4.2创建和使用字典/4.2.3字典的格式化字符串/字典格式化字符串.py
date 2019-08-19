#coding=utf-8

phonebook={'Alice':'2341','Beth':'9102','Cecil':'3158'}
print "Cecil's phone number is %(Cecil)s." %phonebook
# 输出结果:Cecil's phone number is 3158.

template='''<html>
<head><title>%(title)s</title></head>
    <body>
        <h1>%(title)s</h1>
        <p>%(text)s</p>
    </body>
'''

data={'title':'My Home Page','text':'Welcome to my home page!'}
print template %data