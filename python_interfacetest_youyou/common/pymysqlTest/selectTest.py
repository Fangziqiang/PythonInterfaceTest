#coding=utf-8
'''
Created on 2019年8月26日

@author: Administrator
'''

import pymysql

# 打开数据库连接
db = pymysql.connect(host="192.168.10.6",user="root",password="Hzcx_root",db="pau_dev",port=3306)

#使用cursor()方法获取操作游标
cur = db.cursor() 

#查询操作
sql = "select * from t_goods limit 100"

try:
    cur.execute(sql)
    results = cur.fetchall()    #获取查询的所有记录
    print("id","name","code","price")
    # 遍历结果
    for row in results:
        id = row[0]
        name= row[1]
        code = row[2]
        price= row[3]
        print(id,name,code,price)
except Exception as e:
    raise e
finally:
    db.close()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
