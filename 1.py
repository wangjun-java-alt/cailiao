import MySQLdb
import paramiko
import os
#sys.setdefaultencoding('utf-8')
hosts=["10.200.254.166",
'10.200.254.167',
'10.200.254.169',
'10.200.254.170',
'10.200.254.171',
'10.200.254.175',
'10.200.254.181',
'10.200.254.185',
'10.200.254.98',
'10.200.254.161',
'10.200.254.162'

]
port='22'

pkey='/root/.ssh/id_rsa'

conn=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="Newsee888",db="ys_jvm",charset="utf8")
cursor=conn.cursor()
key=paramiko.RSAKey.from_private_key_file(pkey)

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for host in hosts:
    ssh.connect(host,port,username='root',pkey=key)
    stdin,stdout,stderr=ssh.exec_command("docker ps|grep java|awk '{print $NF}'")
    docker_ps_info=stdout.read().split()
    for contain in docker_ps_info:
        con_name=contain.split('-')[1]
        if con_name=="dev":
            con_name="dev-platform"
        if con_name=="config":
            continue
        if con_name=="registry":
            continue
        con_name_ip=host+"-"+con_name
        stdin,stdout,stderr=ssh.exec_command("docker exec %s jstat -gc 1|grep -iv s"%contain)
        contain_jvm_status_list=stdout.read().split()
        sql="INSERT INTO ysl_jvm_sum(host,contain,contain_name,S0C,S1C,S0U,S1U,EC,EU,OC,OU,YGC,YGCT,FGC,FGCT) VALUES('%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(host,con_name_ip,con_name,float(contain_jvm_status_list[0]),float(contain_jvm_status_list[1]),float(contain_jvm_status_list[2]),float(contain_jvm_status_list[3]),float(contain_jvm_status_list[4]),float(contain_jvm_status_list[5]),float(contain_jvm_status_list[6]),float(contain_jvm_status_list[7]),float(contain_jvm_status_list[12]),float(contain_jvm_status_list[13]),float(contain_jvm_status_list[14]),float(contain_jvm_status_list[15]))
        try:
            n = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)   
        for row in  cursor.fetchall():
            print(row)
    ssh.close()
cursor.close()
conn.close()
