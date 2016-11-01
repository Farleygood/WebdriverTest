#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from Page.BaseTestPage import BaseTestCase
from Page.HomePage import LoginHomePage
from Page.BasePage import Page_Loc
from Page.MessageCount import Message_Count
import time as t
import unittest
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

class MyCtoBlog(LoginHomePage,Page_Loc,BaseTestCase):
    
    # 测试51cto登录成功后返回消息总数
    def test_001(self,username,password):
        self.Login('username','password')
        
    
    
    