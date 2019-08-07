# coding=utf-8
import unittest
import requests

# 1、unittest.skip()方法
# 跳过测试和预期失败的功能，是python3.1版本开始，出现的新功能。unittest支持跳过单个测试用例甚至整个测试类。
# skip()的各个方法说明如下：
# @unittest.skip(reason) 无条件跳过被装饰的测试方法；reason：理由，描述为什么跳过测试用例
# @unittest.skipIf(condition,reason)    如果条件为真，则继续执行执行，否则跳过被装饰的测试用例；reason：理由，描述为什么跳过测试用例
# @unittest.skipUnless(condition,reason)  除非条件为真，否则跳过被装饰的测试用例
# @unittest.expectedFailure    将测试用例标记为“预期失败”：如果测试执行时失败，则测试结果不计为失败；
# unittest.Skip(reason)    如引发某种定义的异常，则跳过该测试；一般可以使用TestCase.skip()或者一个跳过装饰器，而不是直接使用
#  官方文档：https://docs.python.org/3.6/library/unittest.html


class DemoTest(unittest.TestCase):
    status = 200
    def setUp(self):
        self.url = 'http://www.cnblogs.com/imyalost/'

    @unittest.skip(u"无条件跳过该测试")
    def test_blog1(self):
        # 无条件跳过
        r1 = requests.get(self.url)

    @unittest.skipIf(status > 200, u"状态码大于200，就跳过该测试")
    def test_blog2(self):
        # 如果断言结果为真，则继续执行，否则跳过测试
        r2 = requests.get(self.url)
        status2 = r2.status_code
        self.assertTrue(status2 > self.status)

    @unittest.skipUnless(status == 404, u"状态码为200，则跳过")
    def test_blog3(self):
        # 除非结果为真，否则跳过该测试
        r3 = requests.get(self.url)
        status3 = r3.status_code
        self.assertTrue(status3 > self.status)

    @unittest.expectedFailure
    def test_blog4(self):
        # 将测试用例标记为“预期失败”，如果测试执行时失败，则测试结果不计为失败
        r4 = requests.get(self.url+'/test4')
        status4 = r4.status_code
        self.assertTrue(status4 ==self.status)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()