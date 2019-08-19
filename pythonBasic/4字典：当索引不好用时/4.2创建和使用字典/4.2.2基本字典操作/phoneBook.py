#coding=utf-8


people={
   
    'Alice':{
        'phone':'2341',
        'addr':'Foo driver 23'
    },
        
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
        
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }
}

# 针对电话号码和地址使用的描述性标签
labels={'phone':'phone number',
        'addr':'address'
        }
name=raw_input('Name:')
request=raw_input("Phone number(p) or address(a)?:")
# 查找电话号码还是地址？使用正确的键：
if request == 'p':
    key='phone'
if request == 'a':
    key='addr'

# 如果名字是字典中的有效键才打印信息：
if name in people:print "%s's %s is %s." %\
(name,labels[key],people[name][key])


