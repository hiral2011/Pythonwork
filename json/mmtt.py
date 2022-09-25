from urllib.request import urlopen
import json

url = "https://skynet.mtailor.com/v1/config/preferences.json"
response = urlopen(url)
data_json = json.loads(response.read())
print(type(data_json))
with open('tailor_data.json', 'w') as file:
    file.write(json.dumps(data_json,indent=2))

data_json = {key: value for key, value in zip(categories, objects)}

    