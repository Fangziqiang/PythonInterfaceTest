#coding=utf-8

'python接口测试练习'
# 需要使用python2.7版本

import urllib
# import httplib

http_client=None

# http_client = httplib.HTTPConnection('localhost',8081,timeout=30)
http_client.request('GET', '/jenkins/api/json')

response =http_client.getresponse()
print (response.status)
print (response.read())
