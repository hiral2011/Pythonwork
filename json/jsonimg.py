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
        img = obj2["DETAILS_IMAGES"]
    
    temp["images1-2:"]=img
    final.append(temp)
with open('jsonimg.json','w')as f:
   f.write(json.dumps(final,indent=2))