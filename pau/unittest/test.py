#coding=utf-8

# 测试用例的名称要以 test 开头
# unittest.main()是运行主函数

# 前置和后置 setUp:执行用例的前置条件
# tearDown:执行测试用例的后置条件，前置和后置都是非必要的条件，如果没有也可以写pass

import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        pass    #如果没有可以不写，或者pass代替

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
        
    def testAdd(self):  ## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
    
if __name__ == '__main__':
    unittest.main()