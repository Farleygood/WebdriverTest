#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
import time as t

class Page_Loc(object):
    
    def __init__(self,driver):
        self.driver = driver
    
    def find_element(self,*loc):
        try:
            return self.driver.find_element(*loc)
        except(NoSuchElementException,ValueError,KeyError,Exception),e:
            print 'Error details: %S' %(e.args(0))
            
    @property
    def wait(self):
        t.sleep(3)
    
        
        

