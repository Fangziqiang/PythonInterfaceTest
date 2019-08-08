#coding=utf-8
import requests
import unittest

host="http://192.168.10.6:8080"

class login(unittest.TestCase):
    def setUp(self):
        print("start")
    
    def sendCode(self):
        sendCode_path="/owner/v1/share/code"
        sendCode_url=host+sendCode_path
        print sendCode_url
        payload = {"phone":"17610831883","password":"111111"}
        r = requests.post(sendCode_url,json=payload,verify=False)
        print r.text
        print r.status_code
        self.assertEqual(r.code, "success")
        
    def test_login(self):
        login_path="/auth/login"
        login_path=host+login_path 
        payload = {"phone":"17610831883","password":"111111"}
        r = requests.post(login_path,json=payload)
        print r.status_code
        print r.text
        
    def tearDown(self):
        print("end")

if __name__=="__main__":
    unittest.main()
