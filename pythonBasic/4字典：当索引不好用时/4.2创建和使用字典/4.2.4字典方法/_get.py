#coding=utf-8

# get方法是个更宽松的访问字典项的方法。一般来说，如果试图访问字典中不存在的项时会出错，而用get就不会
d={}
# print d['name']
# KeyError: 'name'

# 而用get就不会：
print d.get('name')
# None
# 可以自定义“默认”值，替换None
print d.get('name','N/A')

# 如果建存在，get用起来就像普通的字典查询一样：
d['name']='Eric'
print d.get('name')
#######################################
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

# 使用正确的键：
key=request
if  request=='p':
    key='phone'
if  request=='a':
    key='addr'
person=people.get(name,{})
label=labels.get(key,key)
result=person.get(key,'not available')

print "%s's %s is %s." %(name,label,result)










