#coding=utf-8

import unittest

class Unittest_case(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")
    
    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")
    
    def setUp(self):
        print("这个是case的前置条件")
    
    def tearDown(self):
        print("这个是case的后置条件")
    
    def testfirst01(self):
        u'''测试登录用例，账号：xx 密码 123456'''
        print("这个是第一条case")
        self.assertEqual(3, 4)

    def testfirst02(self):
        u'''测试登搜索用例，关键词：xxx'''
        print("这个是第二条case")

if __name__=="__main__":
#     运行所有case
    #unittest.main()
    
#     创建unittest容器
    suite = unittest.TestSuite()
#     将testfirst02添加到容器
    suite.addTest(Unittest_case("testfirst02"))
    unittest.TextTestRunner().run(suite)