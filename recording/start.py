import json
import requests
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
	cattura = sys.argv[1]
except:
	print("\nStart recording with Cattura Unit, it will upload to Kaltura if templateID is configured for that.")
	print("Use arg <ip-number> <templateID> <ownerID>")
	exit()
else:
	cattura = sys.argv[1]

try:
	templateID = sys.argv[2]
except:
	print("\nStart recording with Cattura Unit, it will upload to Kaltura if templateID is configured for that.")
	print("Use arg <ip-number> <templateID> <ownerID>")
	exit()
else:
	templateID = sys.argv[2]

try:
	ownerID = sys.argv[3]
except:
	print("\nStart recording with Cattura Unit, it will upload to Kaltura if templateID is configured for that.")
	print("Use arg <ip-number> <templateID> <ownerID>")
	exit()
else:
	ownerID = sys.argv[3]

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

with open('CaptureRequest.json') as json_file:
	data = json.load(json_file)
	data['templateID']=templateID
	data['publishingOverrides']['kaltura']['ownerID'] =  ownerID
    
url = "https://"+cattura+"/api/1/capture/start"
r = requests.post(url, data='captureRequest='+json.dumps(data), auth=(user, psw), verify=False)

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