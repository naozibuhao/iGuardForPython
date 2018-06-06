#!/usr/bin/env python
# -*- coding=utf-8 -*-
#获取配置文件参数

'''
Created on 2017年1月4日
网站防篡改核心类
@author: wyyw
'''


import os, sys, time, subprocess
import shutil

from com.wyyw.iGuard.File.FileDev import FileDev
from com.wyyw.iGuard.config.Config import Config
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyFileSystemEventHander(FileSystemEventHandler):
    
    
    fileDev = FileDev()
    '''
    event.is_directory 
            该事件是否由一个目录触发
            
    event.src_path 
            触发该事件的文件或目录路径
            
    event.event_type 
            事件类型，为moved、deleted、created或modified的其中之一
            
    event.key 
            返回元组(event_type, src_path, is_directory)
    '''
    
    
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn
    # 时间处理集合
    def on_any_event(self, event):
        pass
#         print "any_event"
#         print event.src_path
    # 新增事件 
    def on_created(self, event):
        try:
            fileDev = FileDev()
            filePath = event.src_path
            print "---------------"
            print "createrd"
            print event.src_path
            srcpath = iunion(event.src_path)
            # 如果是文件夹创建
            if event.is_directory:
                print "文件夹事件"
                pathX = srcpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
                if fileDev.isExists(pathX):
                    print "发现文件夹,但未处理"
                    pass
                else:
                    print "删除文件夹"
                    fileDev.removeDir(filePath)
                    pass
            else : # 如果是文件 需要判断源目录是否存在 如果存在 判断hash值 判断是否相等 如果相等不处理 否则删除掉
               
               pathX = srcpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
               pathX = iunion(pathX)
               if fileDev.isExists(pathX):
                   if fileDev.CalcMD5(pathX) == fileDev.CalcMD5(srcpath):
                       #print "两个值相等"
                       pass
                   else:
                       fileDev.removeFile(srcpath)
                       #os.remove(srcpath)
                   pass 
               else:
                   fileDev.removeFile(srcpath)
                   #os.remove(srcpath)
        except:
            pass
    # 删除文件操作
    def on_deleted(self, event):
        fileDev = FileDev()
        print "---------------"
        print "delete"
        print event.src_path
        srcpath = event.src_path
        print event.is_directory
        if not fileDev.isFile(srcpath):
            pathF = srcpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            print '-----------pathF ',pathF
            if fileDev.isExists(pathF):
                fileDev.copyFile(pathF, srcpath)
            else:
                print  "不存在的文件夹 ,不做处理"
        else:
            pathX = event.src_path.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            if fileDev.isExists(pathX):
                print pathX
                fileDev.copyFile(pathX, event.src_path)
            else:
                pass
    # 文件修改操作    
    def on_modified(self, event):
        try:
            fileDev = FileDev()
            print "---------------"
            print "modified"
            print event.src_path
            
            # 判断是否为文件夹触发
            if event.is_directory:
                pass
            else:
                pathX = event.src_path.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
                if fileDev.isExists(pathX):
                    if fileDev.CalcMD5(pathX) == fileDev.CalcMD5(event.src_path):
                        #print "两个值相等"
                        pass
                    else:
                        fileDev.removeFile(event.src_path)
                        #os.remove(event.src_path)
                    pass 
                else:
                    os.remove(event.src_path)
                    pass
        except:
            pass
    # 移动文件操作
    def on_moved(self, event):
        fileDev = FileDev()
        print "---------------"
        print "moved"
        print event.src_path
        print event.dest_path
        srcpath = event.src_path
        destpath = event.dest_path
        if event.is_directory:
            print "文件夹事件"
            pathX = destpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            if fileDev.isExists(pathX):
                print "发现文件夹,但未处理"
                pass
            else:
                print "删除文件夹"
                fileDev.removeDir(destpath)
                pass
            
            pathF = srcpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            print '-----------pathF ',pathF
            if fileDev.isExists(pathF):
                fileDev.copyFileTree(pathF, srcpath)
            else:
                print  "不存在的文件夹 ,不做处理"
                pass    
            
                        
        else:
            pathX = event.src_path.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            print pathX
            if fileDev.isExists(pathX):
                fileDev.copyFile(pathX, event.src_path)
                #shutil.copy(pathX, event.src_path)
            else:
                fileDev.removeFile(event.src_path)
                pass 

def iunion(str):
    print '--------------------',str
    return str
    pass

def start_watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHander(""), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
if __name__ == '__main__':
    start_watch("D:\\Soft\\norsebak", None)