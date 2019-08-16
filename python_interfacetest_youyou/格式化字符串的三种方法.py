# 博客地址：https://www.cnblogs.com/c-x-a/p/9333826.html
1、Option #1: %-formatting
使用示例：
name = "Eric"
age = 74
"Hello, %s. You are %s." % (name, age) 

2、Option #2: str.format()

例
"Hello, {}. You are {}.".format(name, age) 

您可以通过引用其索引来以任何顺序引用变量
name = "Eric"
age = 74
"Hello, {1}. You are {0}-{0}.".format(age, name) 

person = {'name': 'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']) 

也可以使用**来用字典来完成这个巧妙的技巧：

"Hello, {name}. You are {age}.".format(**person) 
'Hello, Eric. You are 74.'

3、f-Strings：一种改进Python格式字符串的新方法
name = "Eric"
age = 74
f"Hello, {name}. You are {age}." 
使用大写字母F也同样有效

放置表达式
f"{2 * 37}" 
调用函数
f"{name.lower()} is funny." 

使用带有f字符串的类创建对象。想象一下你有以下类：
class Comedian:    
    def __init__(self, first_name, last_name, age):        
        self.first_name = first_name        
        self.last_name = last_name        
        self.age = age    
    def __str__(self):        
        return f"{self.first_name} {self.last_name} is {self.age}."    
    def __repr__(self):        
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!" 

new_comedian = Comedian("Eric", "Idle", "74")
f"{new_comedian}" 

多行f-string
message = (f"Hi {name}. "        
           "You are a {profession}. "        
           "You were in {affiliation}.")
message 


