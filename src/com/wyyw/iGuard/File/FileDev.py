#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''

@author: wyyw
'''


import hashlib
import os
import shutil

from com.wyyw.iGuard.Util.UtilTool import UtilTool
from com.wyyw.iGuard.config.Config import Config
from wheel import paths


class FileDev:
    def isExists(self,path):
       try:
           if(os.path.exists(path)):
               return True
           else:
               return False
       except Exception,e:
           print e.message
           return False
           pass
    def isFile(self,path):
        try:
            if(self.isExists(path)):
                if(os.path.isfile(path)):
                    return True
                else:
                    return False
        except:
            pass
    def CalcSha1(self,filepath):
      try:
          with open(filepath,'rb') as f:
              sha1obj = hashlib.sha1()
              sha1obj.update(f.read())
              hash = sha1obj.hexdigest()
              print(hash)
              return hash
      except:
          pass
    def CalcMD5(self,filepath):
         try:
             with open(filepath,'rb') as f:
                 md5obj = hashlib.md5()
                 md5obj.update(f.read())
                 hash = md5obj.hexdigest()
#                  print(hash)
                 return hash
         except:
             pass
    def getBigFileMD5(self,filepath):  
        try:
            if self.isFile(filepath):  
                md5obj = hashlib.md5()  
                maxbuf = 8192  
                f = open(filepath,'rb')  
                while True:  
                    buf = f.read(maxbuf)  
                    if not buf:  
                        break  
                    md5obj.update(buf)  
                f.close()  
                hash = md5obj.hexdigest()  
                return str(hash).upper()  
            return None 
        except:
            pass
    def getFileMD5(self,filepath):  
        try:
            if self.isFile(filepath):  
                f = open(filepath,'rb')  
                md5obj = hashlib.md5()  
                md5obj.update(f.read())  
                hash = md5obj.hexdigest()  
                f.close()  
                return str(hash).upper()  
            return None  
        except:
            pass
    
    def removeDir(self,filePath):
        try:
            shutil.rmtree(filePath)
        except:
            pass
       
    def removeFile(self,filePath):
        fileDev = FileDev()
        utilTool = UtilTool()
        try:
            pathF = filePath.replace(Config.FOLDERPATH,fileDev.getBackUpF())
            
            fileDev.mkdirsF(pathF)
            endstr = str(utilTool.getTimes())+str(utilTool.getRandom(10000))
            pathF = pathF+str(endstr)
#             print pathF
            fileDev.copyFile(filePath,pathF)
            os.remove(filePath)
            
            floder = os.path.dirname(filePath)
            #if not self.isExists(floder):
                
            
            
        except Exception ,e:
            print e.message
            pass
    def copyFile(self,filepath,filetopath):
        try:
#             print 'filepath ',filepath
#             print 'filetopath',filetopath
            
            floder = os.path.dirname(filetopath)
            # 判断文件夹是否存在 若不存在就创建一个
            if not self.isExists(floder):
                os.makedirs(floder)
            shutil.copy(filepath, filetopath)
        except Exception ,e:
            print e.message
            pass
    def copyFileTree(self,filepath,filetopath):
      try:
        shutil.copytree(filepath, filetopath)
      except Exception ,e:
        print e.message
        pass
    #获取要备份的文件夹 并且以年月日命名
    def getBackUpF(self):
        fileDev = FileDev()
        utilTool = UtilTool()  
        backupF = Config.BACKUPFOLDERPATH+'/'+utilTool.getData('%Y%m%d')
        return backupF
    def mkdirsF(self,filePath):
        fileDev = FileDev()
        # 根据路径获取文件夹路径
        paths = os.path.dirname(filePath)
        if not fileDev.isExists(paths):
            os.makedirs(paths)
        
    # 迭代文件夹
    def iterationFolder(self,filePath):
        afiles = []
        for root, dirs , files in os.walk(filePath):
            for f in files:
                afiles.append(root + "/" + f)
        return afiles
    
    # 迭代所有的文件夹(不包含文件名) 
    def iterationFolderF(self,filepath):
        floderList = []
        pathDir =  os.listdir(filepath)
        for allDir in pathDir:
            path = filepath+"/"+allDir
            if not self.isFile(path):
                floderList.append(path)
                self.iterationFolderF(path)
        return floderList
if __name__ == '__main__':
    fileDev = FileDev()
    fileDev.eachFile('D:\\Soft\\norsebak')    