#!/opt/python/bin/python3.6
# -*- coding: UTF-8 -*-
import requests
import json
import sys

try:
    req = requests.get('https://fsrm.experiant.ca/api/v1/combined')
except:
    print('Nao pode acessar')
    exit()

dic = json.loads(req.text)
rans = (dic['filters'])

sys.stdout=open("ranswares.conf","w")

print("veto files = ", end="")
#for x in rans[:10]:
for x in rans:
    print('/'+x, end="")

sys.stdout.close()
#sed 's/.//' | sed ':a;N;s/\n//g;ta'                                            