from urllib import request, response
import requests
import json
import time

req = requests.get("https://skynet.mtailor.com/v1/config/preferences.json")
response = req.json()
all_pro = response["All Product Lines"]
# uni = response["UniversityLogoGraphic"]
final = []

for object in all_pro:
    temp = {}
    fabric = object["Options"]["Fabric"]
    for obj2 in fabric:
        bnd = obj2["BACKEND_NAME"]
    
    temp["BACKEND_NAME"]=bnd
    final.append(temp)
with open('try11.json','w')as f:
   f.write(json.dumps(final,indent=2))