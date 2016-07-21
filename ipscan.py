import time
import nmap
from m_mysql import *
import json
from mysql_conf import *

my=mysql(host,user,password,database,port)
def portscan():
	ipaddr= my.select('select ipdir,id from polls_task;')
	tempip=[]
	for x in ipaddr:
		tempip.append( x['ipdir'])
	iptoscan= '\n'.join(tempip)

	nm=nmap.PortScanner()
	nmresult= nm.scan(hosts=iptoscan,arguments='-p-  -sV -sS -T4')
	for host in nm.all_hosts():
		taskinfo=my.select('SELECT white_port,id FROM `polls_task` WHERE ipdir="%s"'%(host))
		whiteport=taskinfo[0]['white_port'].split(',')
		taskid=taskinfo[0]['id']
                my.query("DELETE FROM `polls_result` WHERE `polls_result`.`taskid` = %d;"%(taskid))
		insertinfo=[]
		for proto in nm[host].all_protocols():
			lport=nm[host][proto].keys()
			lport.sort()
			for port in lport:
				if str(port)  in whiteport:
					badport=1 # not allow
				else:
					badport=0
				port_detail=nm[host][proto][port]['name']
				insertinfo.append("('%d', '%d', '%d', '%s', '%d', '%d')"%(0,taskid,port,port_detail,badport,int(time.time())))	
		my.insert("INSERT INTO `polls_result` (`id`, `taskid`, `port`, `port_detail`, `bad_port`, `scan_time`) VALUES %s"%(','.join(insertinfo)))
		my.query("UPDATE `polls_task` SET `state` = '1' WHERE `polls_task`.`id` = %d;"%(taskid))

	my.close()
