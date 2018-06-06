#!/usr/bin/env python
# -*- coding=utf-8 -*-
#获取配置文件参数
import thread 
import time 

from com.wyyw.iGuard.config.Config import Config
from com.wyyw.iGuard.core.Core import start_watch
from com.wyyw.iGuard.polling.polling import runpolling


class Main:
    def init(self):
        pass
    def menu(self):
        
        print '1.替代发布'
        print '2.检测目标程序'
        print '3.运行防篡改工具'
        str = input("请输入菜单编号:")
        print str
        
    def watch(self):
        # 事件驱动机制
        start_watch(Config.FOLDERPATH,None)
    def pollingThread(self):
        # 轮询机制
        runpolling()
if __name__ == '__main__':
    print "监控文件  : ",Config.FOLDERPATH
    main = Main()
    try:
        print "启动轮询机制"
        thread.start_new_thread(main.pollingThread, ())
        print "启动事件驱动"
        thread.start_new_thread(main.watch,())
        # 增加线程阻塞
        while 1:
            time.sleep(0.1)
    except Exception ,ex:
        print ex.message
        pass
    
