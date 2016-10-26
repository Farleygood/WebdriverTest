#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from Page.baiduHq import login
from selenium import webdriver

'''
忽略打开浏览器时提示 ignore-certificate-errors
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://www.baidu.com')
login(driver, 'xxxxx', 'xxxxx')
driver.quit()