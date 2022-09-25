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
        but = obj2["DEFAULT_BUTTON_COLOR"]
    
    temp["DEFAULT_BUTTON_COLOR"]=but
    final.append(temp)
with open('try12.json','w')as f:
   f.write(json.dumps(final,indent=2))