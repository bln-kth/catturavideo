import requests
import sys
import json
import csv

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

f = open("cattura-units.csv")
csv_f = csv.reader(f)

for row in csv_f:
	if not str(row[0]).startswith('#'):
		ip = row[0]
		user = row[1]
		psw = row[2]
		url = "https://"+ip+"/api/1/status/unit"
		r = requests.get(url, auth=(user, psw), verify=False)
		data=json.loads(r.text)
		#print(data)
		unitName=data['unitName']
		machineName=data['machineName']
		url = "https://"+ip+"/api/status/capture"
		r = requests.get(url, auth=(user, psw), verify=False)
		data=json.loads(r.text)
		state=data['state']
		print ("unitName=",unitName,", machineName=",machineName,", state=",state,", ip=",ip)