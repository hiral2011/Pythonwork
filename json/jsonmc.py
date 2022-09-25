import json
json1 = '{"hiii":"hiral","ip":"1.1.12.20"}'

dict1 = json.loads(json1) 

print(type(json1))
print(type(dict1))
# print(dict1.get(ip))        # errror   ip is not define
print(dict1.get('ip'))      #get a value of keky

################ dict to json 

# dict1 = {"hiii":"hiral","ip":"1.1.12.20"}

# json1 = json.dumps(dict1) 

# print(type(dict1))
# print(type(json1))
# print(json1)
# print(json.get('ip'))       ##errror  json has no atribute get 
