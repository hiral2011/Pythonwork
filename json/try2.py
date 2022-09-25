import json
from urllib.request import urlopen
# import itertools

url = "https://skynet.mtailor.com/v1/config/preferences.json"

response = urlopen(url)
data_json = json.loads(response.read())     # our dict name(data_json)
print(type(data_json))              #we get dict type


print(data_json.get("Gender"))
print(data_json.get("Name"))
print(data_json.get("BACKEND_ANME"))
print(data_json.get("DETAILS_TEXT"))
print(data_json.get("PRICE"))

res = data_json.get("Gender", {}).get("Name")
# for i in data_json[0]:       # for keys
#     print(i)

# data_json2 = {}
# # print(type(family))

# data_json2['Gender']="Man"
# data_json2['last_name']="alwyn"
# data_json2['age']=35
# data_json2['spouse']="srishti jain"
# data_json2['children']=["raju","munna","surya","khusi"]
# data_json2['pets']={'dog':'fido','cat':'sox'}

# print(data_json2.get('name'))

# print(data_json2.get('hiral',-9))
# for i in data_json:
#     if i == "All Product Lines":
#         with open('all.json','w')as f:
#             f.write(json.dumps(data_json,indent=2))
#         break
#     # else:









