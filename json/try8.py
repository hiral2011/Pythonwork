from urllib import request, response
import requests
import json
import time

req = requests.get("https://skynet.mtailor.com/v1/config/preferences.json")
response = req.json()
all_pro = response["All Product Lines"]
final = []
for object in all_pro:
    temp = {}
    gender = object["Gender"]
    name = object["Name"]
    fabric = object["Options"]["Fabric"]
    # print(object)
    for obj2 in fabric:
        backndname = obj2["BACKEND_NAME"]
        price = obj2["PRICE"]
        text_d = obj2["DETAILS_TEXT"]
        det_img = obj2["DETAILS_IMAGES"]
        # print(det_img)

        temp["Gender:"]=gender
        temp["Name:"]=name
        temp["BACKEND_NAME:"]=backndname
        temp["PRICE"]=price
        temp["DETAILS_TEXT:"]=text_d
        temp["DETAILS_IMAGES:"]=det_img
        final.append(temp)
        # print(final)
with open('try8.json','w')as f:
   f.write(json.dumps(final,indent=2))
