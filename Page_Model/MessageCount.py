#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium.webdriver.common.by import By
from BasePage import WebUI
import logging

class Message_Count(WebUI):
    logging.info(u'增加日志模块…….')
    message_loc = (By.XPATH,'//*[@id="login_status"]/div/a[2]')
    
    def GetMessageCount(self):
        self.wait
        logging.info(u'打印未读消息数')
        msg = self.driver.find_element(*self.message_loc).text
        print msg