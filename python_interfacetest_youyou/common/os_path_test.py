#coding=utf-8

'''
Created on 2019年8月17日

@author: Administrator
'''

import os
import unittest

class MyClass(unittest.TestCase):
    '''
    classdocs
    '''


#     def __init__(self, params):
#         '''
#         Constructor
#         '''
    def test_os_path_01abspath(self):
        # 返回path规范化的绝对路径
        print ("--------test_os_path_01abspath----------")
#         os.path.abspath(path)
        path = os.path.abspath("config.ini")
        print ("os.path.abspath 返回规范化的绝对路径:%s"%path)
        print os.path.abspath("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        print os.path.abspath("./report\\2019_08_16.log")
        
    def test_os_path_02split(self):
        # 将path分割成目录和文件名二元组返回。
        print ("--------test_os_path_02split----------")
        # ('E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common', '19_Log.py')
        print os.path.split("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        
        # ('E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common', '')
        print os.path.split("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\")
    
    def test_os_path_03dirname(self):
        # 返回path的目录。其实就是os.path.split(path)的第一个元素
        print ("--------test_os_path_03dirname----------")
        print os.path.dirname("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        print os.path.dirname('c:\\csv\\') 
    
    def test_os_path_04basename(self):
        # 返回path最后的文件名，如果path以/或者\结果，就返回空值
        # 返回19_Log.py
        print ("--------test_os_path_04basename----------")
        print os.path.basename("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        print os.path.basename("E:\\eclipse\\workspace\\")
        print ("----------")
    def test_os_path_05commonprefix(self):
        # 返回list中，所有path共有的最长的路径
        print ("--------test_os_path_05commonprefix----------")
        print os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff'])
    
    def test_os_path_06exists(self):
        # 如果path存在，则返回True， 如果path不存在，则返回False
        print ("--------test_os_path_06exists----------")
        print os.path.exists("c:\\")
        print os.path.exists("c:\\hello.py")
    
    def test_os_path_07isabs(self):
        # 如果path是绝对路径，返回True
        print ("--------test_os_path_07isabs----------")
        print os.path.isabs("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        print os.path.isabs("\\19_Log1.py1")
        
    def test_os_path_08isfile(self):
        # 如果path是一个存在的文件，返回True，否则返回False
        print ("--------test_os_path_08isfile----------")
        print os.path.isfile("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        print os.path.isfile("E:\\file.txt")
    
    def test_os_path_09isdir(self):
        # 如果path是一个存在的目录，返回True，否则返回False
        print ("--------test_os_path_09isdir----------")
        print os.path.isdir("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
        print os.path.isdir("E:\\")
    
    def test_os_path_10join(self):
        # os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
        print ("--------test_os_path_10join----------")
        print os.path.join('c:\\', 'csv', 'test.csv') 
        'c:\\csv\\test.csv' 
        print os.path.join('windows\temp', 'c:\\', 'csv', 'test.csv') 
        'c:\\csv\\test.csv' 
        print os.path.join('/home/aa','/home/aa/bb','/home/aa/bb/c') 
        '/home/aa/bb/c' 

    def test_os_path_11normcase(self):
        #在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。 
        print("-------------test_os_path_11normcase-------------")
        print os.path.normcase('c:/windows\\system32\\') 
        'c:\\windows\\system32\\' 
    
    def test_os_path_12normpath(self):
        # 规范化路径
        print("-------------test_os_path_12normpath-------------")
        os.path.normpath('c://windows\\System32\\../Temp/') 
        'c:\\windows\\Temp' 
    def test_os_path_13splitdriver(self):
        #返回(drivername,fpath)元组
        print os.path.splitdrive('c:\\windows\\system32\\test.txt') 
        ('c:', '\\windows\\system32\\test.txt') 
        
    def test_os_path_14splitext(self):
    #os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作 
 
        print os.path.splitext('c:\\csv\\test.csv') 
        ('c:\\csv\\test', '.csv') 
 
    def test_os_path_15getsize(self):
        #os.path.getsize(path) 返回path的文件的大小（字节）。 
 
        print os.path.getsize('E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py') 
        299L 
    
    def test_os_path_16getatime(self):
        # os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间。 
        print os.path.getatime("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")
    def test_os_path_17getmtime(self):
        #os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间
        print os.path.getmtime("E:\\eclipse\\workspace\\PythonInterfaceTest\\python_interfacetest_youyou\\common\\19_Log.py")



# MyClass().os_path_test()
if __name__=="__main__":
    unittest.main()
    
    
    
    
    