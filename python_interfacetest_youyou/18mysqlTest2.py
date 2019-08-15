#coding=utf-8

import pymysql

db = pymysql.connect(host='192.168.10.6', user="root", passwd="Hzcx_root", db='pau_dev', port=3306, charset='utf8')
cursor = db.cursor()

sql = """select status from t_owner_staff where phone='17610831886'; """

cursor.execute(sql)

desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来

cursor.close()

db.close()

print(data_dict)