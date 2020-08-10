import requests
import sys
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
	cattura = sys.argv[1]
except:
	print("\nStop recording with Cattura Unit.")
	print("Use arg <ip-number>")
	exit()
else:
	cattura = sys.argv[1]

user = input("Username for "+cattura+": ")
psw = input("Password for "+cattura+": ")

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