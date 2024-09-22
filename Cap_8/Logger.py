# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:20:59 2021

@author: MBI
"""
import os,time
from datetime import datetime


class LogLevel():
    OFF = 0
    Minimum = 1
    Normal = 2
    Debug = 3

class Logger():
    def __init__(self,fullTestName,loglevel=LogLevel.Debug):
        testname = os.path.splitext(os.path.basename(fullTestName))[0]
        logName = testname + '.log'
        
        logsFolder = 'Logs'
        if not os.path.exists(logsFolder):
            os.makedirs(logsFolder,exist_ok = True)
        
        self.log = os.path.join(logsFolder,logName)
        self.createLog()
        self.loggingLevel = loglevel
        self.startTime = time.perf_counter()
    
    def createLog(self):
        with open (self.log,mode='w',encoding='utf-8') as logFile:
            logFile.write(self.getDataTime() + '\t\t*** Starting Test ***\n')
        
        logFile.close()
    
    def writeTolog(self,msg='',loglevel=LogLevel.Debug):
        if loglevel > self.loggingLevel:
            return
        with open(self.log,mode='a',encoding='utf-8') as logFile:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
            
            logFile.write(self.getDataTime() + '\t\t' + msg + '\n')
        
        logFile.close()
    
    def getDataTime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def writeTestRunTime(self):
        elapsed = time.perf_counter() - self.startTime
        self.writeTolog('\nElapsed Test Time (seconds): {0:.2f}'.format(elapsed),LogLevel.OFF)
    
    def setLogginLevel(self,level):
        self.loggingLevel = level
                
                
                
                
                
                
                
        