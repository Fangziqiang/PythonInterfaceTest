# -*- coding: utf-8 -*-

import pymysql.cursors
# 连接数据库
db = pymysql.Connect(
    host='localhost',
    port=3310,
    user='user',
    passwd='123',
    db='test',
    charset='utf8'
)
cursor = db.cursor()
# 事务处理
sql_1 = "UPDATE staff SET saving = saving + 1000 WHERE user_id = '1001' "
sql_2 = "UPDATE staff SET expend = expend + 1000 WHERE user_id = '1001' "
sql_3 = "UPDATE staff SET income = income + 2000 WHERE user_id = '1001' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    db.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    db.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
db.close()
