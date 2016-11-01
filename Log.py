#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging.handlers

 
class FinalLogger():
 
    logger = None
   
    
    levels = {"n" : logging.NOTSET,
    "d" : logging.DEBUG,
    "i" : logging.INFO,
    "w" : logging.WARN,
    "e" : logging.ERROR,
    "c" : logging.CRITICAL}
     
    log_level = "d"
    log_file = "final_logger.log"
    log_max_byte = 10 * 1024 * 1024;
    log_backup_count = 5
    
    @staticmethod
    def getLogger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger
        log_file = "./FinalLogger.log_file"
        logging.basicConfig(filename = log_file,level = logging.DEBUG)

        FinalLogger.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename = FinalLogger.log_file,\
        maxBytes = FinalLogger.log_max_byte,\
        backupCount = FinalLogger.log_backup_count)
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
        return FinalLogger.logger
    
# 把日志输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.INFO)
FinalLogger.getLogger().addHandler(console)
      
        
        
        
    