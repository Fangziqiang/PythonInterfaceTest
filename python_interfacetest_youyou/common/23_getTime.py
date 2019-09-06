# -*- coding:utf-8 -*-
import time
#Python 获取时间戳
#Python 默认获取的时间是一个具有时间的元组，asctime()  是接受时间元祖，返回一个时间字符串


TimeTuple=time.localtime(time.time())   #获取当前的时间返回一个时间元组
print '获取当前的时间戳(元组)：',TimeTuple
fmt='%Y-%m-%d %a %H:%M:%S'      #格式化时间
test=time.strftime(fmt,TimeTuple)       #把传入的元组按照格式，输出字符串
print '获取当前的时间(字符串)：',test


TimeStr = time.asctime(time.localtime(time.time()))     #根据获取的元组输出一个时间字符串
print '当前时间为(字符串)：',TimeStr
fmt2='%a %b %d  %H:%M:%S %Y'        #格式化时间
test2=time.strptime(TimeStr,fmt2)       #接受字符串按照格式，输出元组
print '当前的时间戳(元组)',test2


fmt='%Y-%m-%d %a %H:%M:%S'      #定义时间显示格式
Date=time.strftime(fmt,time.localtime(time.time()))     #把传入的元组按照格式，输出字符串
print '获取当前的时间：',Date

# 定义：时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数。时间戳（timestamp），通常是一个字符序列，唯一地标识某一刻的时间。
now = time.time()  # 1s = 1000ms
now = (int(now * 1000))  # 获得13位时间戳
print(now)

'''
python中时间日期格式化符号： 
%y 两位数的年份表示（00-99） 
%Y 四位数的年份表示（0000-9999） 
%m 月份（01-12） 
%d 月内中的一天（0-31） 
%H 24小时制小时数（0-23） 
%I 12小时制小时数（01-12） 
%M 分钟数（00-59） 
%S 秒（00-59） 
%a 本地简化星期名称 
%A 本地完整星期名称 
%b 本地简化的月份名称 
%B 本地完整的月份名称 
%c 本地相应的日期表示和时间表示 
%j 年内的一天（001-366） 
%p 本地A.M.或P.M.的等价符 
%U 一年中的星期数（00-53）星期天为星期的开始 
%w 星期（0-6），星期天为星期的开始 
%W 一年中的星期数（00-53）星期一为星期的开始 
%x 本地相应的日期表示 
%X 本地相应的时间表示 
%Z 当前时区的名称 
%% %号本身
'''