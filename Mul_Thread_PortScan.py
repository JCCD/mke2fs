#-*- coding:utf-8 -*-
import time,thread
import threading
import telnetlib

Port=[21,22,23,25,69,79,80,110,139,443,445,1080,1158,1433,1521,2100,3128,3306,3389,6379,7001,8080,8081,9080,9090]
def PortScan(ip,port):
    server = telnetlib.Telnet()
    #创建telnet对象
    try:
        server.open(ip,port)
        ## 利用Telnet对象的open方法进行tcp链接
        print '{0} port {1} is Open'.format(ip,port)
    except Exception as err:
        pass
    finally:
        server.close()
#输入ip地址，进行扫描
def MulPortScan(ip):
    threads = []
    ip = '124.160.214.51'
    for i in Port:
        t = threading.Thread(target=PortScan, args=(ip, i)) #调用扫描函数
        threads.append(t)   #根据ip:端口逐个分发线程，添加到线程池
    #print threads           #共计25个线程
    for i in range(len(Port)):
        threads[i].start()  #逐个启动线程
    for i in range(len(Port)):
        threads[i].join()
if __name__ =='__main__':
    ip = '124.160.214.51'
    MulPortScan(ip)
