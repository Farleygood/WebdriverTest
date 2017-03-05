#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from Page_Model.HomePage import LoginHomePage
import logging,unittest
from Page_Model.BaseTestPage import BaseTestCase
import time as t
from Page_Model.MessageCount import Message_Count

class MyCtoBlog(BaseTestCase, LoginHomePage):

    logging.info(u'logging info: 运行测试用例')
    def test_001(self, username ='zshzx@126.com',password='xxxxx'):
        ''' 测试51cto登录成功后返回消息总数 '''
        self.doLogin(username, password)
        t.sleep(8)
        Message_Count(self.driver).GetMessageCount()
    logging.info(u'运行测试用例完毕')

if __name__ == '__main__':
    unittest.main(verbosity=2)


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
