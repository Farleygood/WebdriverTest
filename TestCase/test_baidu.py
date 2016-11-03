
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from BaseTestPage import BaseTestCase
from HomePage import LoginHomePage
from BasePage import Page_Loc
from MessageCount import Message_Count
import time as t
import unittest,logging

#这里为什么不导入LogConfig模块，直接使用logging也可以，其他地方就一定要导入LogConfig模块呢？没搞明白
class MyCtoBlog():

    logging.info(u'logging info: 运行测试用例')
    RunSetup = BaseTestCase()
    RunSetup.Setup(self.drvier)
    
    '''测试51cto登录成功后返回消息总数'''
    def test_001(self,username = 'zshzx@126.com',password='XXXXX'):
        
        LoginHomePage.login(self.driver,username,password)
    RunSetup.tearDown()
           
    logging.info(u'运行测试用例完毕') 
    logging.info('testabcccccc56598465')
    
    
# '''
# 忽略打开浏览器时提示 ignore-certificate-errors
# '''
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# driver = webdriver.Chrome(chrome_options=options)
# 
# driver.maximize_window()
# driver.implicitly_wait(15)
# driver.get('http://www.51cto.com/')
# t.sleep(5)
# driver.quit()