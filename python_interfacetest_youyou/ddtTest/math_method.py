#coding=utf-8

class Math():
    """数学类"""
    def __init__(self, a, b):  # 初始化
        self.a = a
        self.b = b
 
    def add(self):  # 加法
        result = self.a + self.b
        return result
 
    def sub(self):  # 减法
        result = self.a - self.b
        return result
 
    def multiply(self):  # 乘法
        result = self.a * self.b
        return result
 
    def divide(self):  # 除法  注意：b传参不要为0
        result = self.a / self.b
        return result
