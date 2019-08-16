#coding=utf-8
'''
Created on 2019年8月16日

@author: Administrator
'''
import unittest
from python_interfacetest_youyou.ddtTest.math_method import Math


class TestMath(unittest.TestCase):

    """Math的测试类"""
    """首先我们增加个初始化函数，传入两个相加的数及预期结果，
    并且用super()来调用父类的__init__()来初始化和传入用例名"""
    def __init__(self, a, b, expect, methodName):
        self.a = a
        self.b = b
        self.expect = expect
        super(TestMath, self).__init__(methodName)
 
    def test_add(self):
        """"然后将加法测试用例的参数改为动态传参"""
        result = Math(self.a, self.b).add()
        self.assertEqual(result, self.expect)
#         python2.7不支持f-string格式化字符串
#         print (f'{self.a}+{self.b}的结果是{self.expect}')
#         print ("%s+%s的结果是%s"%(self.a,self.b,self.expect))
        print ("{}+{}的结果是{}".format(self.a,self.b,self.expect))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()