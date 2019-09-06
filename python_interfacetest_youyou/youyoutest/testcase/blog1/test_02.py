#coding=utf-8

import unittest

class Unittest_case2(unittest.TestCase):
    
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
    
    @unittest.skip("不执行第一条")
    def testfirst01(self):
        print("这个是第一条case")

    def testfirst02(self):
        print("这个是第二条case")
    
    def testfirst03(self):
        print("这个是第3条case")

if __name__=="__main__":
#     运行所有case，case运行顺序根据case名称升序执行
    #unittest.main()
    
#     创建unittest容器
    suite = unittest.TestSuite()
#     将case添加到容器，执行顺序根据添加顺序执行
    suite.addTest(Unittest_case2("testfirst02"))
    suite.addTest(Unittest_case2("testfirst01"))
    suite.addTest(Unittest_case2("testfirst03"))
    unittest.TextTestRunner().run(suite)