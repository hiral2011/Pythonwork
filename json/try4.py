from urllib.request import urlopen

import json

url = "https://skynet.mtailor.com/v1/config/preferences.json"
  
response = urlopen(url)
data = json.load(response,indent=2)

print(type(response))

with open('all.json','w')as f:
#    f.write(json.dumps(data_json,indent=2))
    data = json.load(response,indent=2)
    jsonData = data["All Product Lines"]
    for x in jsonData:
        keys = x.keys()
        print(keys)
        values = x.values()
        print(values)

  
