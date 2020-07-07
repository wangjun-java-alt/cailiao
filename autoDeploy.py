# -*- coding: utf-8 -*-
from sys import stdin, stdout, stderr
from sys import argv
import os
import devOps

script,service = argv

#网关
def do_apigateway() :

    print '========begin server connecting....'
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-apigateway-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-apigateway/target/newsee-apigateway-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#注册发现
def do_eureka() :
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-registry-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/	newsee-registry/target/newsee-registry-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#配置
def do_config() :

    # print '========begin pull the last version'
    # os.chdir('G:/GitLab/newsee-config')
    # #output = os.popen('dir')
    # #print output.read()
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-config-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-config/target/newsee-config-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#监听
def do_monitor() :
    # os.chdir('G:/GitLab/newsee-monitor')
    # #output = os.popen('dir')
    # #print output.read()
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-monitor-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-monitor/target/newsee-monitor-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#监控
def do_turbine() :
    # os.chdir('G:/GitLab/newsee-turbine')
    # #output = os.popen('dir')
    # #print output.read()
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-turbine-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-turbine/target/newsee-turbine-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#kafka服务
def do_kafka() :
    # print '========begin pull the last version'
    # os.chdir('G:/GitLab/newsee-kafka')
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-kafka-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/kafka/newsee-kafka-rest/target/newsee-kafka-rest-1.0.0-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0#8880           #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)



#日志
def do_log() :


    print '========begin server connecting....'
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-log-rest-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-log/newsee-log-rest/target/newsee-log-rest-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port= 8765              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)


#业户
def do_owner() :
    # print '========begin pull the last version'
    # os.chdir('G:/GitLab/newsee-owner')
    # #output = os.popen('dir')
    # #print output.read()
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-owner-rest-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-owner/newsee-owner-rest/target/newsee-owner-rest-0.0.1-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#charge
def do_charge() :
    # print '========begin pull the last version'
    # os.chdir('G:/GitLab/newsee-owner')
    # #output = os.popen('dir')
    # #print output.read()
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-charge-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-charge/newsee-charge-rest/target/newsee-charge-rest-1.0.0-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=8778 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)


#sso
def do_sso() :
    # print '========begin pull the last version'
    # os.chdir('G:/GitLab/newsee-oAuth')
    # #output = os.popen('dir')
    # #print output.read()
    # output = os.popen('git pull')
    # print output.read()
    #
    # print '========begin maven pack'
    # output = os.popen('mvn clean')
    # output = os.popen('mvn package')
    # print output.read()


    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-oauth-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-oauth/newsee-oauth-rest/target/newsee-oauth-rest-1.0.0-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#system
def do_system() :

    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-system-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-system/newsee-system-rest/target/newsee-system-rest-1.0.0-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)
	
#system
def do_bill() :

    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-bill-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-bill/newsee-bill-rest/target/newsee-bill-rest-1.0.0-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#customForm
def do_customform() :

    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-custom-form-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-customform/newsee-custom-form-rest/target/newsee-custom-form-rest-1.0.0-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#devplatform
def do_devplatform() :

    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-dev-platform-rest-1.0.0-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-devplateform/newsee-dev-platfrom-rest/target/newsee-dev-platform-rest-1.0.0-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#fastdfs
def do_fastdfs() :

    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-fastdfs-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-fastdfs/target/newsee-fastdfs-0.0.1-SNAPSHOT.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=0 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#websocket
def do_websocket() :

    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-websocket-0.0.1-SNAPSHOT.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/websocket/target/newsee-websocket-0.0.1-SNAPSHOT.jar' #本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=9999 #8770             #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)
#soss
def do_soss() :
    print '========begin server connecting....' 
    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/data/'       #服务器文件地址
    log_path='/home/logs/'       #服务器日志文件地址
    file_name='newsee-soss-rest-1.0.0.jar' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-sosss/newsee-soss-rest/target/newsee-soss-rest-1.0.0.jar'#本地上传文件名称
    is_install_docker=0         #是否安装docker
    daemon_file=r'G:\daemon.json'   #docker 镜像加速
    is_init=0                   #是否对docker进行初始化设置
    open_port=8780 # 7777              #防火墙端口设置
    devOps.do(host_name,ssh_port,root_name,root_pwd,do_path,log_path,local_path,file_name,is_install_docker,daemon_file,is_init,open_port)

#front
def do_front() :
    print '========begin server connecting....'

    #初始化变量
    host_name='192.168.1.210'  #远程连接主机
    ssh_port = 22                #ssh 端口号
    root_name='root'            #远程主机登录名
    root_pwd='Newsee888'       #远程主机登录密码
    do_path='/home/www/web/'       #服务器文件地址
    file_name='dist.tar.gz' #文件名称
    local_path=r'/var/jenkins_home/workspace/newsee-front/dist/dist.tar.gz' #本地上传文件名称
    # local_path=r'G:\GitLab\devOps\devOps\dist.tar.gz'#本地上传文件名称

    devOps.doFront(host_name,ssh_port,root_name,root_pwd,do_path,local_path,file_name)

# print '请输入您要维护的服务，全部输入all:'.decode('utf-8').encode('cp936')
# while True:
#     line = stdin.readline()
#     if not line:
#         break
#     service = line.split()[0]

#sso
if service=='sso' or service=='all':
    do_sso()
#配置网关
if service=='zuul' or service=='all':
    do_apigateway()
#注册发现
if service=='eureka' or service=='all':
    do_eureka()
#配置
if service=='config' or service=='all':
    do_config()
#监听
if service=='monitor' or service=='all':
    do_monitor()
#监控
if service=='turbine' or service=='all':
    do_turbine()
#日志
if service=='log' or service=='all':
    do_log()
#业户
if service=='owner' or service=='all':
    do_owner()
#kafka消息
if service=='kafka' or service=='all':
    do_kafka()
#前端
if service=='front' or service=='all':
    do_front()
#系统
if service=='system' or service=='all':
    do_system()
#自定义表单
if service=='customform' or service=='all':
    do_customform()
if service=='devplatform' or service=='all':
    do_devplatform()
if service=='fastdfs' or service=='all':
    do_fastdfs()
if service=='websocket' or service=='all':
    do_websocket()
if service=='soss' or service=='all':
    do_soss()
if service=='charge' or service=='all':
    do_charge()
if service=='bill' or service=='all':
    do_bill()
