#coding=utf-8

'''
Created on 2019年8月13日

@author: Administrator
'''
import unittest
import xlrd

# 安装xlrd模块    pip install xlrd
# excel基本操作方法：
# 打开excel表格，参数是文件路径
data=xlrd.open_workbook("test.xlsx")
table=data.sheets()[0]  #通过索引顺序获取
table=data.sheet_by_index(0)  #通过索引顺序获取
table = data.sheet_by_name(u'Sheet1') # 通过名称获取
nrows = table.nrows # 获取总行数
ncols = table.ncols # 获取总列数
# 获取一行或一列的值，参数是第几行
print table.row_values(0) # 获取第一行值
print table.col_values(0) # 获取第一列值

#.在 excel 中存放数据，第一行为标题，也就是对应字典里面的 key 值，如：username，password
# 如果 excel 数据中有纯数字的一定要右键》设置单元格格式》文本格式，要不然读取的数据是浮点数
# （先设置单元格格式后编辑，编辑成功左上角有个小三角图标）



class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()