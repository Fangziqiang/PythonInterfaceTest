#coding=utf-8
import unittest  # 导入单元测试框架
import HTMLTestRunnerCN  # 导入测试报告模版
from testMath import TestMath  # 导入测试类
from testMath2 import  Test_math
 
if __name__ == "__main__":
    """首先将我们要测试数据添加到list中,
        list中每个元素中都包含了[a, b, expect],然后用for循环来传入参数，
        并用每个元素生成一条测试用例后加载到测试套件suite中，
        最后执行用例，生成测试报告！"""
    test_date = [[0, 0, 0],  #  0 0 相加
                 [5, 5, 10],  # 正正相加
                 [-5, -5, -10],  # 负负相加
                 [5, -5, 0]]  # 正负相加
    suite = unittest.TestSuite()
    for item in test_date:
        suite.addTest(TestMath(item[0], item[1], item[2], 'test_add'))
        suite.addTest(Test_math(item[0], item[1], item[2], 'test_add'))
 
    with open('test_result.html', 'wb') as file:  # html文件必须以二进制方式写入
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=file,
                                                  title='测试报告',
                                                  description='这是第一次执行用例的测试报告！',
                                                  verbosity=2,
                                                  tester='C大调')
        runner.run(suite)
