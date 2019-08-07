#coding=utf-8

import unittest
import os

# 三、unittest 常用的断言方法
# 1.assertEqual(self, first, second, msg=None)
# --判断两个参数相等：first == second

# 2.assertNotEqual(self, first, second, msg=None)
# --判断两个参数不相等：first ！= second

# 3.assertIn(self, member, container, msg=None)
# --判断是字符串是否包含：member in container

# 4.assertNotIn(self, member, container, msg=None)
# --判断是字符串是否不包含：member not in container

# 5.assertTrue(self, expr, msg=None)
# --判断是否为真：expr is True

# 6.assertFalse(self, expr, msg=None)
# --判断是否为假：expr is False

# 7.assertIsNone(self, obj, msg=None)
# --判断是否为 None：obj is None

# 8.assertIsNotNone(self, obj, msg=None)
# --判断是否不为 None：obj is not None

# 可以自定义异常
#         self.assertEqual(a, b, msg="失败原因：%s != %s"%(a,b))


class assert_test(unittest.TestCase):
   
    def test_case01(self):
#         os.getcwd()获取当前目录
        case_path=os.path.dirname(os.path.abspath(__file__))
#         print case_path

    def testAdd(self):  ## test method names begin 'test*'
        a='1+1'
        b=3
        self.assertEqual(a, b,msg="失败原因:%s != %s"%(a,b))
        try:
            self.assertNotEqual((1+2), 3)
        except AssertionError as e:
            print (e)
            raise

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
        
        self.assertEqual(0 + 1, 1)
if __name__=="__main__":
    unittest.main()
    