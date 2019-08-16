#coding=utf-8
import requests
import unittest
import json
from _random import Random

class json_test2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("所有case执行之前的前置")
        self.url="http://192.168.10.6:8080/user/orders"
        self.h={
                 "Accept": "application/json",
                 "Accept-Encoding": "gzip, deflate",
                 "Accept-Language": "zh-CN,zh",
                 "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiJ5OWJtZTQiLCJzdWIiOiIxMzI3MTU3MDUwMSIsImV4cCI6MTU2NTc2NTIyMiwiZGV2aWNlSWQiOiIxMTUxNjc2MDA1MTA3MTA5ODg5MTU2MzQxNTkzMTg3N3RuayIsImlhdCI6MTU2NTE2MDQyMn0.Jx4nnrm_eZFYvtULgHmxxpRLCRzPlTxxDarDwnREMFWflrCssWS0mymQcesEiY8vo_Nh7T7cm4a-zN3gKo3U1A",
                 "Connection": "keep-alive",
                 "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                 "User-Agent": "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; SM-G955F Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1",
                 "Host": "192.168.10.6:8080"
                 }
        self.par={"status":"confirmed","owner":"16d0a4b0dcd411e8b2e187bf6b98e5cd","page":"1"}
    
    @classmethod
    def tearDownClass(self):
        print("所有case执行之后的后置")
    
    def setUp(self):
        print("这个是case的前置条件")
       
    def get_confirme_order(self):
        
#         print ("start")
        r=requests.get(self.url,headers=self.h,params=self.par)
#         print(r.text)
        print (r.status_code)
        
        self.assertEqual(r.status_code, "300", msg="失败原因：%s != 300"%(r.status_code))
        
#         print (r.content)
        print("---------------json解析---------------------")
        result=r.json()
#         获取orders里面的内容
        orders=result["orders"]

        print ("-------------orders-----------")
        print orders
        print ("-------------orders列表最上面一个-----------")
        print orders[0]     #获取orders里面最上面一个
        print ("-------------goods-----------")
        print orders[0]["goods"]    #获取goods列表
        print orders[0]["phone"]
        
        for i in range(len(orders)):
            print orders[i]["phone"]
              
        
    def tearDown(self):
        print("这个是case的后置条件")
        
    
    
        
if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(json_test2("get_confirme_order"))
    unittest.TextTestRunner().run(suite)
    
        
        