#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'

import unittest,os,sys,HTMLTestRunner,time
import LogConfig,logging

reload(sys)
sys.setdefaultencoding('utf-8')

def suite():
    logging.info(u'运行suite……')
    dir_case = unittest.defaultTestLoader.discover('F:/Git/WebdriverTest/TestCase',\
                            pattern = 'test_*.py', \
                            top_level_dir = None
                        )
    logging.info(u'suite运行完毕……')
    return dir_case
def getNowTime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
    
def runAutomation():
    filename = 'F:/Git/WebdriverTest/Report/' + getNowTime() + 'TestReport.html'
    
    #打印日志级别为info
    logging.info(u'loginfo: 文件创建成功！......')

    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = u'自动化测试报告',
            description = u'自动化测试详细信息'
        )
    runner.run(suite())

if __name__ == '__main__':
    runAutomation()
    
    
