#coding=utf-8
'''
Created on 2019年9月11日

@author: Administrator
'''

from selenium import webdriver


# browser = webdriver.Firefox()
# browser = webdriver.Ie()
browser = webdriver.Chrome()
browser.get('https://www.aiinp.com/') 

browser.close()