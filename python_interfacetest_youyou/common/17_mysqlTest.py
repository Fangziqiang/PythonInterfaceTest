#coding=utf-8

'''
Created on 2019年8月15日

@author: Administrator
'''
# 安装mysql驱动
# 到https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python 
# 下载MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl 
# cmd到该目录下
# pip install MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl ##安装
# 安装成功 
# cmd命令行下执行：
# pip install mysql
# --------------------- 

import MySQLdb

mysql_info={"host":"192.168.10.6",
            #port 端口号是整数，不能加引号
            "port":3306,
            "user":"root",
            "passwd":"Hzcx_root",
            "db":"pau_dev",
            "charset":"utf8"
            }


class MysqlUtil():
    '''
    mysql 数据库相关操作
        连接数据库信息：mysql_info
        创建游标：mysql_execute
        查询某个字段对应的字符串：mysql_getstring
        查询一组数据：mysql_getrows
        关闭 mysql 连接：mysql_close
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.db_info=mysql_info
        u'''连接池方式'''
        self.conn=MysqlUtil.__getConnect(self.db_info)
        
    @staticmethod
    def __getConnect(db_info):
        try:
        # 建立数据库连接  MySQLdb.connect()
            conn=MySQLdb.connect(host=db_info['host'],
                                port=db_info['port'],
                                user=db_info['user'],
                                passwd=db_info['passwd'],
                                db=db_info['db'],
                                charset=db_info['charset']
                                )
            return conn
        except Exception as a:
            print("数据库连接异常:%s"%a)
        
        
    def mysql_execute(self,sql):
        '''执行sql语句'''
        #  cur=conn.cursor() 通过获取到的数据库连接conn下的 cursor()来创建游标
        cur=self.conn.cursor()
        try:
            #通过游标 cur 操作 execute()方法可以写入纯 sql 语句。通过 execute()方法中写入 sql语句来对数据进行操作
            cur.execute(sql)
        except Exception as a:
            self.conn.rollback()    #sql执行异常后回滚
            print ("执行sql语句出现异常：%s"%a)
        else:
            cur.close() # cur.close() 关闭游标
            self.conn.commit()      #提交事务
            
    def mysql_getrows(self,sql):
        '''返回查询结果'''
        cur=self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            print ("执行sql语句出现异常：%s"%a)
        else:
            rows=cur.fetchall()
            cur.close()
            return rows
    
    def mysql_getstring(self,sql):
        '''查询某个字段的对应值'''
        rows=self.mysql_getrows(sql)
        
        if rows != None:
            for row in rows:
                for i in row:
                    return i
    
    def mysql_close(self):
        '''关闭mysql'''
        try:
            self.conn.close()
        except Exception as a:
            print ("执行sql语句出现异常：%s"%a)      
        
if __name__=="__main__":
    mysql=MysqlUtil()
    
    sql= "select * from t_owner_staff where phone='17610831886';"
    
    
    mysql.mysql_execute(sql)
    print mysql.mysql_getrows(sql)
    
    print mysql.mysql_getstring(sql)
    mysql.mysql_close()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        