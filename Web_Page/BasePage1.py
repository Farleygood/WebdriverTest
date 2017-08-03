#! /usr/bin/env python
# coding:utf-8

__author__ = 'Farley'

from selenium.webdriver.support.expected_conditions import NoSuchElementException
import time as t

class Factory(object):
    def __init__(self, driver):
        self.driver = driver

    # # 工厂方法
    # def createWebDdriver(self, webDdriver):
    #     if webDdriver == 'web':
    #         return WebUI(self.driver)
    #     elif webDdriver == 'app':
    #         return AppUI(self.driver)

    def findElement(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException, e:
            print 'Error details :%s' % (e.args[0])

    def findElements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException, e:
            print 'Error details :%s' % (e.args[0])

    def getScreenshot(self, name, form='png'):
        t.sleep(2)
        self.driver.get_screenshot_as_file('E:/Git/WebdriverTest/img/' + name + "." + form)

    @property
    def wait(self):
        t.sleep(3)

    def __str__(self):
        return 'webDdriver'

class WebUI(Factory):
    def __str__(self):
        return 'web'


class AppUI(Factory):
    def __str__(self):
        return 'app'
