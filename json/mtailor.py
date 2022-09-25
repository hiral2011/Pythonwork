from urllib.request import urlopen
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://skynet.mtailor.com/v1/config/preferences.json"
  
# store the response of URL
response = urlopen(url)
# response.
# print(response.read())
# print(type(response.read()))

# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
print(type(data_json))
###### print(type(data_json))
with open('mtailor.json','w')as f:
   f.write(json.dumps(data_json,indent=2))
  
# print the json response
# print(type(data_json))