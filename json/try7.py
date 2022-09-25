from urllib import request, response
import requests
import json
import time

req = requests.get("https://skynet.mtailor.com/v1/config/preferences.json")
response = req.json()
final = []
for item in response["All Product Lines"]:
    gender = item["Gender"]
    for gen in gender:
        print("Gender:",item["Gender"])      
    name = item["Name"]
    for nam in gender:
        print("Name:",item["Name"])      

        
fabric = item["Options"]["Fabric"]
for fab in fabric:
    backndname = fab["BACKEND_NAME"]
    for item in backndname:
        print("BACKEND_NAME:",fab["BACKEND_NAME"])
                
        price = fab["PRICE"]
        for fab in fabric:
            print("PRICE",fab["PRICE"])

        text_d = fab["DETAILS_TEXT"]
        for DET in text_d:
            print("DETAILS_TEXT:",fab["DETAILS_TEXT"])

            
        DETAILS_IMAGES = fab["DETAILS_IMAGES"]
        for img in DETAILS_IMAGES:
            print("DETAILS_IMAGES:",fab["DETAILS_IMAGES"])

# print(response)
# for item  in response:
