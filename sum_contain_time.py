# -*- coding: utf-8 -*-  
import MySQLdb
import paramiko
import os
#sys.setdefaultencoding('utf-8')
hosts_for_zabbix_name={
"10.200.254.169"	:"arm-app1-169",
"10.200.254.170"	:"arm-app2-170",
"10.200.254.171"	:"arm-bill1-171",
"10.200.254.175"	:"arm-bill2-175",
"10.200.254.181"	:"arm-broke1-181",
"10.200.254.185"	:"arm-broke2-185",
"10.200.254.176"	:"arm-repor1-176",
"10.200.254.177"	:"arm-repor2-177",
"10.200.254.166"	:"arm-web1-166",
"10.200.254.167"	:"arm-web2-167",
"10.200.254.195"	:"ebill-195",
"10.200.254.196"	:"ebill-196",
"10.200.254.197"	:"ebill-197",
"10.200.254.198"	:"ebill-198",
"10.200.254.98"	:"uat-app-98",
"10.200.254.162"	:"uat-arm-162",
"10.200.254.161"	:"uat-db-161",
"10.200.254.163"	:"uat-db-163",
"10.200.254.165"	:"uat-front-165",
"10.200.254.92"	:"uat-压测环境-92",
"10.200.254.93"	:"uat-压测环境-93",
"10.200.254.94"	:"uat-压测环境-94",
"10.200.254.95"	:"uat-压测环境-95"
}
hosts=["10.200.254.166",
'10.200.254.167',
'10.200.254.169',
'10.200.254.170',
'10.200.254.171',
'10.200.254.175',
'10.200.254.176',
'10.200.254.177',
'10.200.254.181',
'10.200.254.185',
'10.200.254.98',
'10.200.254.161',
'10.200.254.162',
'10.200.254.163',
'10.200.254.92',
'10.200.254.93',
'10.200.254.94',
'10.200.254.95',
'10.200.254.195',
'10.200.254.196',
'10.200.254.197',
'10.200.254.198'


]
port='22'

pkey='/root/.ssh/id_rsa'
print 111
conn=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="Newsee888",db="ysl",charset="utf8")
cursor=conn.cursor()
key=paramiko.RSAKey.from_private_key_file(pkey)
ssh = paramiko.SSHClient()

sql="truncate table sum_contain_time"
try:
    n = cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(e)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for host in hosts:
    ssh.connect(host,port,username='root',pkey=key)
    stdin,stdout,stderr=ssh.exec_command('docker ps -a --format "{{.Names}}\t{{.Status}}"')
    docker_ps_info=stdout.read().split("\n")
    for i in  docker_ps_info:
        if i:
            _i=i.split()
           # print("host",hosts_for_zabbix_name[host])     
           # print("grafana")     
           # print("container",_i[0])     
           # print("time"," ".join(_i[1:]).lower().replace("up ","") )   
            sql="insert into sum_contain_time(ip_host,grafana_name,contain_name,running_time) VALUES('%s','%s','%s','%s')"%(host,hosts_for_zabbix_name[host],_i[0]," ".join(_i[1:]).lower().replace("up ","").replace("about ","").replace("hours","小时").replace("hour","小时").replace("days","天").replace("minutes","分钟").replace("months","月").replace("an","1").replace("weeks","周").replace(" ago","").replace("exited","停掉").replace("seconds","秒"))
            try:
                n = cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(e)
 
ssh.close()
cursor.close()
conn.close()

