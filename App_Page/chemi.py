#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

from selenium import webdriver
from appium import webdriver as aw
from selenium.webdriver.common.by import By
from Web_Page.BasePage1 import AppUI
import time as t

class CheMi(AppUI):

    banler_loc = (By.ID,'com.android.systemui:id/chargingViewSubTree')
    username_loc = (By.ID, 'com.chemi:id/et_tel_number')
    passwd_loc = (By.ID, 'com.chemi:id/et_login_pwd')
    loginButton_loc = (By.ID, 'com.chemi:id/bt_login_submit')

    def getUserName(self,username):

        self.wait
        self.findElement(*self.username_loc).send_keys(username)

    def clearUserName(self):
        self.wait
        self.findElement(*self.username_loc).clear

    def getPasswd(self,password):

        self.wait
        self.findElement(*self.passwd_loc).send_keys(password)
        # 隐藏键盘
        # self.driver.hide_keyboard()

    def getLoginBt(self):

        self.wait
        self.findElement(*self.loginButton_loc).click()

    def Login(self,username,password):

        # self.clearUserName()
        self.getUserName(username)
        self.getPasswd(password)
        self.getLoginBt()
        t.sleep(5)

    def get_banler(self):
        self.wait
        self.findElement(*self.banler_loc).click()
