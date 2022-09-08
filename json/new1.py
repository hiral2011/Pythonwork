import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)

# print( person_dict)

# print(type(person_dict))

f = open('state.json',)
data = json.load(f)
for i in data['states']:
    print(i)

f.close()

