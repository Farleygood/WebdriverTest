#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from appium import webdriver
import unittest
import os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class BaseTestCase(unittest.TestCase):
    
    def Setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.51cto.com/')
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()
        
class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4.4'
        desired_caps['deviceName']='m2'
        # desired_caps['appPackage']='com.taobao.mobile.dipei'
        # desired_caps['appActivity']='com.taobao.ecoupon.activity.PortalActivity'
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        desired_caps['app'] = PATH('C:\\ddandroid_206200.apk')
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def tearDown(self):
        self.driver.quit()  
        
        
        
        
          