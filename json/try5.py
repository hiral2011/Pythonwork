import json
with open("/home/hiral/Desktop/json/mtailor.json") as jsonfile :
    # print(type("mtailor.json"))
    data = json.load(jsonfile)
    # print(type("mtailor.json"))
with open("mtailor.json") as jsonFile:
        data = json.load(jsonFile)
        # print(type("mtailor.json"))

        jsonData = data["All Product Lines"]
        for x in jsonData:
            keys = x.keys()
            # print(keys)
            values = x.values()
            # print(values)

with open('all.json','w')as f:
   f.write(json.dumps(jsonData,indent=2))
# print(type("all.json"))