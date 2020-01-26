#!-*-coding:utf-8 -*-
import telnetlib

#Port=[21,22,23,25,69,79,80,110,139,443,445,1080,1158,1433,1521,2100,3128,3306,3389,6379,7001,8080,8081,9080,9090]
#def PortScan(ip,port):
#    server = telnetlib.Telnet()
#    #创建telnet对象
#    try:
#        server.open(ip,port)
#        ## 利用Telnet对象的open方法进行tcp链接
#        print '{0} port {1} is Open'.format(ip,port)
#    except Exception as err:
#        pass
#    finally:
#        server.close()
#if __name__ =='__main__':
#    host='127.0.0.1'
#    for po in Port:
#        PortScan(host,po)

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
def scan(host):
    for po in Port:
        PortScan(host,po)