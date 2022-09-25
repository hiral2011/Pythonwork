
from urllib.request import urlopen
# import json
import json
# def city_choices_python(): 
#     import requests
#     import json 
#     product_list = []
url = "https://skynet.mtailor.com/v1/config/preferences.json"
   
response = urlopen(url)


# data_json = json.loads(response.read())
# print(type(data_json))
# with open('mtailor.json','w')as f:
#    f.write(json.dumps(data_json,indent=2))

filtered_json = []
with open('mtailor.json', 'r') as file:
    for line in file:
        if '"gender": "man"' in line:
            filtered_json.append(line)

##############################

# keyVal = input("Enter a key value: \n")
# customer = json.loads(data_json)
# if keyVal in customer:
#     print("%s is found in JSON data" %keyVal)
#     print("The value of", keyVal,"is", customer[keyVal])
# else:
#     print("%s is not found in JSON data" %keyVal)

####################################

    # response = requests.get(URL)
    # r = json.loads(response.text)
    # # data_json = json.loads(response.read())
    # print(type(data_json))
    # with open('new_mtailor.json','w')as f:
    #     f.write(json.dumps(data_json,indent=2))
    # for nestedArr in r['items']:
    #     product_list.append(nestedArr['city'])
    # return sorted(product_list)