#coding=utf-8
import getpathInfo
import HTMLTestRunner
import unittest
import os
path = getpathInfo.get_Path()
def all_case():
#         os.getcwd()获取当前目录，方法一
    case_dir=os.path.join((os.getcwd()),'testcase')
#     case_dir = os.path.join(path, "baidu")
#     case_dir="E:\eclipse\workspace\PythonInterfaceTest\python_interfacetest_youyou\youyoutest"

#       方法二
#       case_path=os.path.dirname(os.path.abspath(__file__))
#       case_dir:待执行用例的目录；-pattern：这个是匹配脚本名称的规则，test*.py 意思是匹配 test 开头的所有脚本。
#       -top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了
    print (case_dir)
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='test_*.py',top_level_dir=None)
    testcase.addTests(discover)

    print testcase
    return testcase
    
if __name__=="__main__":
#     unittest.main()
#     返回实例
#     runner=unittest.TextTestRunner()
    # run所有用例
#     runner.run(all_case())
    # stream 测试报告写入文件的存储区域
    # title 测试报告主题
    # description：测试报告的描述
    report_path=os.path.join(path, "report\\result.html")
    print report_path
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u"这是我的接口自动化测试报告",
                                         description=u"用例执行情况")
    runner.run(all_case())
    fp.close()