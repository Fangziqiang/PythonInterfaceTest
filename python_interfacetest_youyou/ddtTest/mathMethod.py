#coding=utf-8
'''
Created on 2019年8月16日

@author: Administrator
'''

class Math(object):
    '''
    classdocs
    '''

    def __init__(self, a,b):
        '''
        Constructor
        '''
        self.a=a
        self.b=b
    def add(self):
        result=self.a+self.b
        return  result
    
    def sub(self):
        result=self.a-self.b
        return result
    
    def mutiply(self):
        result=self.a * self.b
        return result
    
    def divide(self):
        result=self.a / self.b
        return result