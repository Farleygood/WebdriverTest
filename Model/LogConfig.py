#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import logging
import time
# 配置日志信息
# log_file = "F:/Git/WebdriverTest/logs/Webdriver.log"
# 打印年月日，每天存储一个日志文件
time = time.strftime('%Y%m%d',time.localtime(time.time()))

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] [%(funcName)s] [%(asctime)s]%(message)s',
                    datefmt='%m-%d %H:%M',
                    # 每天存储一个日志文件,如果想覆盖log改filemode='w'
                    filename='F:/GitHub/GitHib_Project/WebdriverTest/logs/WebdriverTest_%s.log'%time,
                    filemode='a+')

# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 设置日志打印格式
formatter = logging.Formatter('[%(levelname)s] [%(funcName)s] [%(asctime)s]%(message)s')

console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)
