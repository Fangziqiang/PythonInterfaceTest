#coding=utf-8

import unittest

def all_case():
    #待执行用例的目录
    case_dir="E:\\eclipse\\workspace\\PythonInterfaceTest\\pau\\case"
    testcase=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
#     discover筛选出来的用例，循环添加到测试套件中
#     for test_suit in discover:
#         for test_case in test_suit:
#             testunit.addTests(test_case)
#             print(testunit)
    testcase.addTests(discover)
    print(testcase)
    return testcase
if __name__=="__main__":
#     返回实例
    runner = unittest.TextTestRunner()
#     run所有用例
    runner.run(all_case())