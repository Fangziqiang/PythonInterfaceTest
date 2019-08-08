#coding=utf-8

import requests
import unittest
import re

url="http://192.168.10.6:7001/j_acegi_security_check"

headers={
         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
         }

d={"j_username":"fzq","j_password":"123456","from":"/","Submit":"Sign in"}

s = requests.session()
r = s.post(url, headers=headers,data=d)
# r = requests.post(url, headers=headers,data=d)
# 正则表达式提取账号好登录按钮

# <b>这是一个加粗文本</b>
t=re.findall(r'<b>(.+?)</b>',r.content)
print t[0]
print t[1]
# print r.content