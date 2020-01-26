#!-*-coding:utf-8 -*-
import socket
#端口列表
Port=[21,22,23,25,69,79,80,110,443,1080,1158,1433,1521,2100,3128,3306,3389,7001,8080,8081,9080,9090]
Servers=['FTP(文件传输)','SSH(安全登录)','Telnet(远程登录)','SMTP(SimpleMailTransferProtocol)','TFTP(TrivialFileTransferProtocol)','Finger','Http','Pop3','Https','SOCKS','ORACLEEMCTL','MSSQL,MYSQL','Oracle数据库','OracleXDBFTP服务','HTTP','TerminalServices','RemoteDesktopServices','WebLogic','TOMCAT/JBOSS','SymantecAV/FilterforMSE','Webshpere应用程序','webshpere管理工具']
def get_ip_status(ip,ip_port):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个sock对象
    #AF_INET 使用ipv4   SOCK_STREAM使用tcp套接字
    try:
        server.connect((ip,ip_port)) #创建tcp连接
        print '{0} port {1} is Open'.format(ip,ip_port)
    except Exception as err:#不显示未开启的端口
        pass
        #print '{0} port {1} is Not Open'.format(ip,ip_port)
    finally:
        server.close()
if __name__ == '__main__':
    host='112.80.248.76'
    for P0rt in Port:
        get_ip_status(host,P0rt)

