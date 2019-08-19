#coding=utf-8
# 有时候程序什么事情都不用做，这种情况不多，但是一旦出现，就应该让pass语句出马了:

# 例：
name=raw_input("Please enter your name:")
if name=="Ralph Auldus Melish":
    print 'Welcome!'
elif name=='Enid':
    #还没完.....
#     如果不加pass，这块代码是不会执行的，因为Python中空代码块是非法的
    pass
elif name=='Bill Gates':
    print 'Access Denied'