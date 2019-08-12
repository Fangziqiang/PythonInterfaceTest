#coding=utf-8

import unittest
import requests

# 重定向状态码
# --301 代表永久性转移
# --302 代表暂时性转移

# 禁止重定向
# allow_redirects = False
class location_test(unittest.TestCase):
    
    def setUp(self):
#         腾讯云控制台网址，打开时会重定向到登录页面
        self.url="https://console.cloud.tencent.com/apigateway/service-detail?rid=8&id=service-94vz3buz&tab=api&apiType=tsf"
        self.headers ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    def test1(self):
        r= requests.get(self.url,allow_redirects=False,verify=False)
        # 打印状态码，自动处理重定向请求
        print r.status_code
        print r.text

    def test2(self):
        
        s=requests.session()
        r=s.get(self.url,headers=self.headers,allow_redirects=False,verify=False)
        print r.status_code
#         print r.text
        new_url=r.headers["Location"]
        print r.headers["Content-Type"]
        print r.headers["Connection"]
        print new_url
        print r.headers
        
if __name__=="__main__":
#     unittest.main()
    
    suite= unittest.TestSuite()
    suite.addTest(location_test("test1"))
    suite.addTest(location_test("test2"))
    unittest.TextTestRunner().run(suite)
        
