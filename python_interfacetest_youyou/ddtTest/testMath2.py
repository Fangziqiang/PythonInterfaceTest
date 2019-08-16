#coding=utf-8
'''
Created on 2019年8月16日

@author: Administrator
'''
import unittest
import mathMethod

class Test_math(unittest.TestCase):

    def __init__(self,a,b,expect,method):
        self.a=a
        self.b=b
        self.expect=expect
#         用super()来调用父类的__init__()来初始化和传入用例名"""
        super(Test_math,self).__init__(method)

    def test_add(self):
#         pass
        result=mathMethod.Math(self.a,self.b).add()
        self.assertEqual(result, self.expect)
        print ("({})+({})的结果是{}".format(self.a,self.b,self.expect))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()