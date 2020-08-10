import requests
import sys
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
	cattura = sys.argv[1]
except:
	cattura = input("ip-number: ")
else:
	cattura = sys.argv[1]

with open('secret.txt') as secret:
	line = secret.readline()
	line = line.rstrip()
	line = line.split(",")
	user=line[0]
	psw=line[1]

url = "https://"+cattura+"/api/1/status/unit"
r = requests.get(url, auth=(user, psw), verify=False)
data=json.loads(r.text)
unitName=data['unitName']
machineName=data['machineName']
url = "https://"+cattura+"/api/status/capture"
r = requests.get(url, auth=(user, psw), verify=False)
data=json.loads(r.text)
state=data['state']
print ("unitName=",unitName,", machineName=",machineName,", state=",state)

url = "https://"+cattura+"/api/1/capture/stop"
r = requests.post(url, auth=(user, psw), verify=False)

url = "https://"+cattura+"/api/1/status/unit"
r = requests.get(url, auth=(user, psw), verify=False)
data=json.loads(r.text)
unitName=data['unitName']
machineName=data['machineName']
url = "https://"+cattura+"/api/status/capture"
r = requests.get(url, auth=(user, psw), verify=False)
data=json.loads(r.text)
state=data['state']
print ("unitName=",unitName,", machineName=",machineName,", state=",state)