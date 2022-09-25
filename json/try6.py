import json

with open("/home/hiral/Desktop/json/all.json") as jsonfile :
    # print(type("mtailor.json"))
    data = json.load(jsonfile)
    # print(type("mtailor.json"))
with open("all.json") as jsonFile:
        data = json.load(jsonFile)
        # print(type("mtailor.json"))

input_dict = json.loads(jsonFile)

# Filter python objects with list comprehensions
jsonFile = [x for x in input_dict if x['type'] == '1']

# Transform python object back into json
output_json = json.dumps(jsonFile)

# Show json
print (jsonFile)