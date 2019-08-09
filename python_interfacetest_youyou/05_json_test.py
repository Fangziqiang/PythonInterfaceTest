#coding=utf-8
import requests
import json
import unittest
from StringIO import  StringIO

# Encode (python->json)   
#  json.dumps（）
# -------------------------------
# python的数据类，经过encode成json的数据类型，对应的表：
# ---PYTHON---     ---JSON---
# dict---              object
# list,tuple           array
# str,unicode          string
# int,long,float       number
# True                 true
# False                false
# None                 null
# ------------------------------

# decode (json->python)   
#  
# -------------------------------
# json数据转化成python可识别的数据，对应的表关闭如下：
# ---JSON---        ---PYTHON---     
# object               dict
# array                list,tuple           
# string               str,unicode          
# number(int)          int,long     
# number(real)         float
# true                 True                 
# false                False                
# null                 None                 
# ------------------------------
# 83页
class json_test(unittest.TestCase):
    def test01(self):
        s1=json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
        print "s1:",s1     
    def test02(self):
        print (json.dumps("\foo\bar"))
    
    def test03(self):
        print (json.dumps(u'\u1234'))
    
    def test04(self):
        print (json.dumps("\\"))
    
    def test05(self):
        print (json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

    def test06(self):
        io=StringIO()
        json.dumps(['streamingAPI'],io)
        io.getvalue()
    
suite= unittest.TestSuite()
suite.addTest(json_test("test01"))
suite.addTest(json_test("test02"))
suite.addTest(json_test("test03"))
suite.addTest(json_test("test04"))
suite.addTest(json_test("test05"))
suite.addTest(json_test("test06"))

if __name__=="__main__":
    #运行测试用例方法一
    unittest.main()
    
    #方法二
    run = unittest.TextTestRunner()
    run.run(suite)