#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
Created on 2017-1-10 

@author: wyyw
'''
import time 

from setuptools.unicode_utils import filesys_decode

from com.wyyw.iGuard import polling
from com.wyyw.iGuard.File.FileDev import FileDev
from com.wyyw.iGuard.config.Config import Config


class pollingFloder:
    # 正向比较
    # 从源目录的文件与目标目录的文件进行比较
    def poolFloder(self):
        fileDev = FileDev()
        filelist = fileDev.iterationFolder(Config.SECFOLDERPATH)
        for srcpath in filelist:
            # pathX 目标文件夹
            pathX = srcpath.replace(Config.SECFOLDERPATH,Config.FOLDERPATH)
            
            if fileDev.isExists(pathX):
                   if fileDev.CalcMD5(pathX) == fileDev.CalcMD5(srcpath):
                       #print "两个值相等"
                       pass
                   else:
                       fileDev.removeFile(pathX)
                       fileDev.copyFile(srcpath, pathX)
                   pass 
            else:
               fileDev.copyFile(srcpath, pathX)
               #fileDev.removeFile(srcpath)
        pass
    def poolingFloderreverse(self):
        # 逆向对比 从目标文件夹到源文件夹进行对比
        fileDev = FileDev()
        #目标文件夹
        filelist = fileDev.iterationFolder(Config.FOLDERPATH)
        for srcpath in filelist:
            # pathX 目标文件夹
            pathX = srcpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            # 如果在源文件夹中找不到 那么意味着这是一个篡改文件
            if not fileDev.isExists(pathX):
                fileDev.removeFile(srcpath)
                
                
            else:
                if fileDev.CalcMD5(pathX) == fileDev.CalcMD5(srcpath):
                   #print "两个值相等"
                   pass
                else:
                   fileDev.removeFile(srcpath)
                   fileDev.copyFile(pathX, srcpath)
                   pass
            
    # 删除多余的文件夹
    def removeFloder(self):
        # 逆向对比 从目标文件夹到源文件夹进行对比
        fileDev = FileDev()
        #目标文件夹
        filelist = fileDev.iterationFolderF(Config.FOLDERPATH)    
        for srcpath in filelist:
            # pathX 目标文件夹
            pathX = srcpath.replace(Config.FOLDERPATH,Config.SECFOLDERPATH)
            # 如果在源文件夹中找不到 那么意味着这是一个篡改文件
            if not fileDev.isExists(pathX):
                fileDev.removeDir(srcpath)
            else:
                pass
        
    def getFloder(self):
        pass    

def runing():
    print u"轮询开始"
    
    pollingfloder = pollingFloder()
    print u"准备正向对比内容"
    
    pollingfloder.poolFloder()
    print u"正向对比结束"
    print u"准备逆向对比"
    pollingfloder.poolingFloderreverse()
    print u"逆向对比结束"
    print u"准备轮询文件夹"
    pollingfloder.removeFloder()
    print u"文件夹轮询结束"
    print u"轮询结束"
    
def runpolling():
    while 1:    
        runing()
        time.sleep(Config.POOLTIMES)
           
if __name__ == '__main__':
    runpolling()
#     pollingfloder = pollingFloder()
#     pollingfloder.poolFloder()
#     pollingfloder.poolingFloderreverse()
#     pollingfloder.removeFloder()
        

