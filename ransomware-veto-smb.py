#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import json
import sys, os
import datetime, dateutil.parser, time

# Mesmo diretório do smb.conf
dirsamba='/home/mauricio'

try:
    req = requests.get('https://fsrm.experiant.ca/api/v1/combined')
except:
    print('Problemas com acesso a página')
    exit()

dic = json.loads(req.text)
registros = (dic['api']['file_group_count'])
lastupdate = (dic['lastUpdated'])
lastupdate = dateutil.parser.parse(lastupdate).strftime('%d/%m/%Y - %H:%m')
print('Número de Ransomwares: '+str(registros)+'\nUltimo update: '+str(lastupdate))

rans = (dic['filters'])
sys.stdout=open(dirsamba+"/ransomwares.conf","w")
print("veto files = ", end="")

for x in rans:
    print('/'+x, end="")

sys.stdout.close()
# Reload Samba

# Por smbcontrol 
# os.system("smbcontrol smbd reload-config")
# os.system("smbcontrol nmbd reload-config")
#
# Port init
os.system("/etc/init.d/samba stop")
time.sleep(5)
os.system("/etc/init.d/samba start")
# Por System
#os.system("systemctl stop samba")
#time.sleep(5)
#os.system("systemctl start samba")

