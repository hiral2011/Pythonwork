from textwrap import indent
import requests
import json

data = requests.get("https://skynet.mtailor.com/v1/config/preferences.json").json()
##### print(type(data))
with open('mt.json','w')as f:
   f.write(json.dumps(data,indent=2))

  