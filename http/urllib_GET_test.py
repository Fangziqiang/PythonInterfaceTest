#coding=utf-8
'''
Created on 2019��3��20��

@author: Administrator
'''
import urllib.request
import requests

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='test',
                          uri='http://localhost:8081/jenkins',
                          user='admin',
                          passwd='admin')
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)

response = urllib.request.urlopen('http://localhost:8081/jenkins/api/json?pretty=true')
print (response.read())