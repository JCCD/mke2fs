#!-*-coding:utf-8 -*-
import time,threading,os
def ceshi():
    for i in range(0, 3600):
               print '\033[22m\033[34m[*]' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 打印实时时间
               time.sleep(1)
ceshi()