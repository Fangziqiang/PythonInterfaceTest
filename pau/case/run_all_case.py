#coding=utf-8

import unittest

def all_case():
    #待执行用例的目录
    case_dir="E:\\eclipse\\workspace\\PythonInterfaceTest\\pau\\case"
    testcase=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
    