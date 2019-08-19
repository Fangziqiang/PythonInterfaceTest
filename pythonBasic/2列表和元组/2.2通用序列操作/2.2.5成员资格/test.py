#coding=utf-8

permissions='rw'
if ('rwq' in permissions):
    print True
else:
    print False
    
# 检查用户名和PIN码
database=[
    ['albert','1234'],
    ['dilbert','4242'],
    ['smith','7524'],
    ['jones','9843'],
    ]
username=raw_input("User name:")
pin=raw_input("PIN code:")
if [username,pin] in database:
    print "Acess granted"
else: print False