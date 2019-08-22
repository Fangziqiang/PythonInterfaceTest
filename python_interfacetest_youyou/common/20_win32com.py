#coding=utf-8

# https://blog.csdn.net/lakerszhy/article/details/50485576

# 文章地址：
# https://blog.csdn.net/qq404766692/article/details/8365542
import win32com.client
from win32com.client import Dispatch,constants

w = win32com.client.Dispatch("Word.Application")

# 使用下面的方法，启动独立的进程：
# w = win32com.client.DispatchEx("Word.Application")

# 后台运行，不显示，不警告
w.Visible = 0
w.DisplayAlerts = 0

# 打开新的文件
doc = w.Documents.Open(FileName = filenamein)
# 创建新的文档


