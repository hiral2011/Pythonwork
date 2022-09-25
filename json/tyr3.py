import json
from textwrap import indent
with open("mtailor.json") as jsonFile:
        data = json.load(jsonFile)
        jsonData = data["All Product Lines"]
        for x in jsonData:
            keys = x.keys()
            print(keys)
            values = x.values()
            print(values)

