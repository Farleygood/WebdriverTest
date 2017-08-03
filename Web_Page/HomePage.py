#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium.webdriver.common.by import By
from BasePage1 import WebUI
# from MessageCount import Message_Count

class LoginHomePage(WebUI):


    click_loc = (By.XPATH,'//*[@id="login-form"]/div[3]/input')
    userName_loc = (By.ID,"loginform-username")
    password_loc = (By.ID,"loginform-password")
    clickButton_loc = (By.XPATH,'//*[@id="login-form"]/div[3]/input')
    error_loc = (By.XPATH,'//*[@id="login-form"]/div[2]/div/div')

    def Click(self):
        self.wait
        self.findElement(*self.click_loc).click()

    def getUserTextField(self,username):
        self.wait
        self.findElement(*self.userName_loc).send_keys(username)

    def getPasswordField(self,password):
        self.wait
        self.findElement(*self.password_loc).send_keys(password)

    def getSubmitButton(self):
        self.wait
        self.findElement(*self.clickButton_loc).click()

    # 获取登录错误的提示信息
    def GetErrorText(self):
        self.wait
        self.findElement(*self.error_loc).text

    # 登录函数,登录成功后返回消息总数
    def Login(self,username,password):
        self.wait
        self.doLogin(username, password)
        # self.Message_Count(self.driver)

    def doLogin(self,username,password):
        self.wait
        self.getUserTextField(username)
        self.getPasswordField(password)
        self.getSubmitButton()
