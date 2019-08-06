#coding=utf-8

import unittest
import os

class assert_test(unittest.TestCase):
    def test_case01(self):
#         os.getcwd()获取当前目录
        case_path=os.path.dirname(os.path.abspath(__file__))
        print case_path
    
if __name__=="__main__":
    unittest.main()
    