#coding=utf-8
import requests
import unittest

host="http://192.168.10.6:8080"

class login(unittest.TestCase):
    def setUp(self):
        print("start")
        self.sendCode_path="/owner/v1/share/code"
        self.sendCode_url=host+self.sendCode_path
        
        self.login_path="/auth/login"
        self.login_path=host+self.login_path
        
        self.payload = {"phone":"17610831883","password":"111111"}
        
    def sendCode(self):
        
        r = requests.post(self.sendCode_url,json=self.payload,verify=False)
        print r.text
        print r.status_code
        self.assertEqual(r.code, "success")
        
    def test_login(self):
        
        r = requests.post(self.login_path,json=self.payload)
        print r.status_code
        print r.text
        
    def tearDown(self):
        print("end")

if __name__=="__main__":
    unittest.main()
