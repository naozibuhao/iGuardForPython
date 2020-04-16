#!/usr/bin/env python
# -*- coding=utf-8 -*-
#获取配置文件参数

class Config:
    #被文件夹路径  (后期期望添加多个文件夹按照|分隔) 也就是要保护网站的根目录
    FOLDERPATH= "D:\\RDPback"
    #受保护文件夹路径 (当文件被篡改,从该文件夹中获取文件将其替换)   
    SECFOLDERPATH= "D:\\RDP"
    #样本文件夹 将所有的变更的文件进行备份
    BACKUPFOLDERPATH="D:\\backup"
    #日志文件路径 (系统运行日志存放路径)
    LOGPATH= "D://log"
    #日志打印级别  从高到低依次是： SEVERE->WARNING->INFO->CONFIG->FINE->FINER->FINESET
    LOGLEVEL = "INFO"
    #备份文件夹路径(当发现新增,修改操作时,将文件保存到此目录提供样本)
    BACKUPPATH="D://log"
    #格式化日期 ( 我也不知道干啥的,先留着吧,说不定以后会用的上)
    FORMATDATE="%Y%m%d"
    #轮询时间 (每间隔时间N,将轮询文件夹,防止事件抓取不准确,单位 毫秒 s)
    POOLTIMES= 0.1
    # smtp 服务器
    SMTP = "smtp.163.com"
    # SMTP服务器端口
    SMTPPORT = 25
    # 发送邮件的邮箱
    MAIL_FROM_ADDRES = ""
    # 接收邮件的邮箱
    MAIL_TO_ADDRESSES = ""
    # 邮箱密码
    MAIL_PASSWORD = ""
