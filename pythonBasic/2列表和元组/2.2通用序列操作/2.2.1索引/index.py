#coding=utf-8

greeting='Hello'
print greeting[0]
print greeting[-1]

fourth=raw_input("Years:")[3]
print fourth
months = [
    'January',
    'February',
    'March',\
    'April',\
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]
#以1~31的数字作为结尾的列表
endings = ['st','nd','rd']+17*['th']\
+['st','nd','rd']+7*['th']\
+['st']

year = raw_input('Year:')
month=raw_input('Month(1-12):')
day=raw_input('Day(1-31):')
# if (month>=1 and month<=12):
#     month_number=int(month)
# else:
#     print u'请输入1-12之间的整数'
# 
# 
# if (day>=1 and day<=31):
#     day_number=int(day)
# else:
#     print u'请输入1-31之间的整数'

month_number=int(month)
day_number=int(day)

month_name=months[month_number-1]
ordinal=day+endings[day_number-1]

print month_name+' '+ordinal+'.'+year
