#coding=utf-8

import unittest
import time

# 测试unittest用例执行顺序
# 结论：
# 1、unittest执行测试用例是根据用例名称来顺序执行的
# 2、只执行test开头的用例
class Test(unittest.TestCase):
    def setUp(self):
        print ("start!")
    def tearDown(self):
        time.sleep(1)
        print("end!")
    def test01(self):
        print ("执行测试用例01")
    def test03(self):
        print ("执行测试用例03")
    def test02(self):
        print ("执行测试用例02")
    def addtest(self):
        print("add方法")

if __name__=="__main__":
    unittest.main()

# 执行结果：
''' 
start!
执行测试用例01
end!
.start!
执行测试用例02
end!
.start!
执行测试用例03
end!
.
'''