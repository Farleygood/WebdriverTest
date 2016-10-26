#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
import time as t
'''
忽略打开浏览器时提示 ignore-certificate-errors
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()
driver.implicitly_wait(15)
driver.get('http://www.51cto.com/')
t.sleep(5)
driver.quit()