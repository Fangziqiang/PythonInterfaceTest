# encoding:utf8

import unittest
from test_case.test_add import AddCase

# 加载测试类中的用例
# loadTestsFromTestCase(self, testCaseClass)

# 使用loadTestsFromTestCase这个方法，需传入unittest测试类的类名
# 以项目为例子，传入 testCaseClass ：AddCase
cases = unittest.TestLoader().loadTestsFromTestCase(AddCase)

# unittest.TextTestRunner(verbosity=2).run(suite)运行用例，TextTestRunner类将用例执行的结果以text形式输出，
# verbosity默认值为1，不限制完整结果，即单个用例成功输出’.’,失败输出’F’,错误输出’E’;
# verbosity=2将输出完整的信息， verbosity=2是指测试结果的输出的详细程度，
# 有0-6级，具体代码实现可看Python27\Lib\unittest\runner.py源代码


runner = unittest.TextTestRunner(verbosity=2)
# runner = unittest.TextTestRunner()
runner.run(cases)
