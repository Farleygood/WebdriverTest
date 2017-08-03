#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import time as t
import unittest
from Web_Page.BaseTestPage import AppTestCase
from App_Page.chemi import CheMi
from App_Page.swipetest import Swipetest

class CheMiTest(AppTestCase, Swipetest, CheMi):

    def test_001(self):
        '''获取手机分辨率'''
        # print u'手机分辨率为：',self.driver.get_window_size()
        print 'phone PIXEL is', self.getSize()
        t.sleep(5)

    def test_002(self):
        '''登录车米app'''
        for i in range(3):
            t.sleep(3)
            self.driver.swipe(955, 977, 100, 977, 800)
            # self.swipeLift(1000)
            if i < 2:
                # print u'滑动到了第%s页' %(i+2)
                print 'Swipe to page No.%s ' % (i + 2)
            else:
                continue
            # self.driver.back()
            t.sleep(3)
        self.Login('13538152630', '123456')
        self.driver.get_screenshot_as_file(
            'E:/Git/WebdriverTest/image/chemi1.png'
        )
        t.sleep(3)
        self.driver.find_element_by_name(u'我').click()
        self.driver.find_element_by_id('com.chemi:id/rl_car').click()
        print 'into my car page'
        t.sleep(5)
        self.swipeRight(1000)
        t.sleep(3)
        self.driver.find_element_by_id('com.chemi:id/rl_qu').click()
        print 'into FAQ'
        t.sleep(3)
        self.swipeRight(1000)
        t.sleep(3)
        print 'return my page'
        self.driver.find_element_by_id('com.chemi:id/rl_se').click()
        self.driver.find_element_by_id('com.chemi:id/logout').click()
        self.driver.find_element_by_id('com.chemi:id/tv_dialog_ok').click()
        print 'logout'
        t.sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
