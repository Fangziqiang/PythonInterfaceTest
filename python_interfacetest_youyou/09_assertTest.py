#coding=utf-8
import unittest

class AssertTest(unittest.TestCase):
    def test01(self):
#        判断a==b
        a=1
        b=1
        self.assertEqual(a, b)
    
    def test02(self):
#         判断a in b
        a = 'hello'
        b = 'hello world'
        self.assertIn(a, b)
    
    def test03(self):
#         判断a is True
        a = True
        self.assertTrue(a)
    
    def test04(self):
        a = "方自强"
        b = "fangziqiang"
#         self.assertEqual(a,b) 
#         AssertionError: '\xe6\x96\xb9\xe8\x87\xaa\xe5\xbc\xba' != 'fangziqiang'
# 可以自定义异常
        self.assertEqual(a, b, msg="失败原因：%s != %s"%(a,b))


if __name__=="__main__":
    unittest.main()
    
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
