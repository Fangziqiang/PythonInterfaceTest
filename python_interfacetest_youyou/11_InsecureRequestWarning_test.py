#coding=utf-8
import unittest
import requests
import urllib3


# 禁用安全请求警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 上面的方法报错，可以使用urllib3
urllib3.disable_warnings()

class Blog_login(unittest.TestCase):
    def login(self,username,pw,reme=True):
        url="https://passport.cnblogs.com/user/signin"
        header={
                }
        json_data={"input1":username,
                   "input2":pw,
                   "remember":reme}
        res=requests.post(url,headers=header,json=json_data,verify=False)
        
        result=res.content
        print result
        return res.json()