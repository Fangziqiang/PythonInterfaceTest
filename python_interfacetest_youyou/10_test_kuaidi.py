#coding=utf-8
import unittest
import requests
import urllib3
# 禁用安全警告
urllib3.disable_warnings()

class test_kuaidi(unittest.TestCase):
    def setUp(self):
        self.url='https://www.kuaidi100.com/query'
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    def chaxun_kuaidi(self,postid,type,temp,phone):
        '''三个参数：单号、快递名称、快递中文名'''
        payload={"postid":postid,"type":type,"temp":temp,"phone":phone}
        r = requests.get(self.url,headers=self.headers,params=payload,verify=False)
        print r.text
    def test_kuaidi(self):
        postid='71082372878114'
        type='huitongkuaidi'
        temp="0.544461645783288"
        phone=""
        self.chaxun_kuaidi(postid, type,temp,phone)
if __name__=="__main__":
    unittest.main()