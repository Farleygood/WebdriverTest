#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from appium import webdriver as aw
import unittest,os

PATH=lambda p:os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 忽略google浏览器打开时的提示信息
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # self.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.get('http://home.51cto.com/index?reback=http://www.51cto.com/')
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Galaxy A8'
        desired_caps['appPackage'] = 'com.chemi'
        desired_caps['appActivity'] = 'com.chemi.ui.activity.StartActivity'
        # 屏蔽手机自带的默认输入法，使用appium自带的输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['app'] = PATH('C:/Users/Administrator/Desktop/1.8.6.1.apk')
        cls.driver = aw.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)