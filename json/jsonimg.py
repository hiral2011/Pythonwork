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
    
    n = len(img)
    # for n in [len(img)]:  
    #     if n <= 2:
    #         temp["images1-2"]=img
    #         n+=1
    #         temp["images2-2"]=img
    #     else:
    #         # temp["images1-2"]=img
    #         pass
    # final.append(temp)
    # n = len(img)
    for n in range(len(img)):
        if n <= 7:
            if n==3:
                temp[f"images{n}-2"]=img[n]
            else:
                temp[f"images{n+1}-2"]=img[n]
            # temp["images1-2"]=img
        # else:
        #     pass
    final.append(temp)

with open('jsonimg.json','w')as f:
   f.write(json.dumps(final,indent=2))