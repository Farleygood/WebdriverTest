#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from selenium.webdriver.common.by import By
from Page.BasePage import Page_Loc

class Message_Count(Page_Loc):
    
    message_loc = (By.XPATH,'//*[@id="login_status"]/div/a[2]')
    
    def GetMessageCount(self):
        self.wait
        return self.find_element(*self.message_loc).text
    