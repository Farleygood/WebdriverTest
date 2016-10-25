#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import time
def wait():
	time.sleep(3)

def login(driver, username, password):
	wait()
	driver.find_element_by_id('u1').find_element_by_class_name('lb').click()
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('xxxxx')
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('xxxxx')
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
	wait()

	assert driver.find_element_by_xpath(".//*[@id='s_username_top']/span")
	print u'登录成功！'