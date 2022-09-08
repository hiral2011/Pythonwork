import json
from urllib.request import urlopen

with urlopen("https://skynet.mtailor.com/v1/config/preferences.json") as response:
    source = response.read()

# print(source)



data = json.loads(source)
# with open('jinfi.json','w')as f:
    # json.dump(source,f,indent=2)
print(json.dumps(data, indent=2))

# print(len(data['list']['resources']))

##########################################

# usd_rates = dict

# for item in data['list']['resources']:
#     # print(item)
#     name = item['resources']['fields']['name']
#     price = item['resources']['fields']['name']
#     print(name,price)