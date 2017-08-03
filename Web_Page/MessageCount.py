#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium.webdriver.common.by import By
from BasePage1 import WebUI
import logging, sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Message_Count(WebUI):
    message_loc = (By.XPATH,'//*[@id="login_status"]/div/a[3]')

    def GetMessageCount(self):
        self.wait
        msg = self.driver.find_element(*self.message_loc).text
        logging.info(u'未读消息数为:' + msg[3])
        print '你有' + msg[3] + '条未读消息!'