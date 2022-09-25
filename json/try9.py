from urllib import request, response
import requests
import json
import time

req = requests.get("https://skynet.mtailor.com/v1/config/preferences.json")
response = req.json()
all_pro = response["All Product Lines"]
# uni = response["UniversityLogoGraphic"]
final = {}

for object in all_pro:
    temp = []
    fabric = object["Options"]["Fabric"]
    for obj2 in fabric:
        # print(obj2)
        # time.sleep(20)
        img = obj2["DETAILS_IMAGES"]    
    
    
    # temp["DETAILS_IMAGES:"]=img
    temp.append(final)
    # final.append(temp)
    final["DETAILS_IMAGES:"]=img
with open('try9.json','w')as f:
   f.write(json.dumps(final,indent=2))

# images1-2: image1
# Images2-2: image2
# images3-2: image3
# Image4: image4
# Image5: image5