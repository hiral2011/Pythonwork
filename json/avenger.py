import json

#convert string to python dict
# employee = '{"id":"09","name":"john","department":"devlopment"}'
# employee_dict = json.loads(employee)
# print(employee_dict)
# print(type(employee_dict))
# print("\n")

# #convet python dict to json

# json_object = json.dumps(employee_dict,indent=4)
# print(json_object)
# print(type(json_object))

Avengers = '''
{
  "people":[
        {
          "Name" : "Tony stark",
          "phone":"335626",
          "also known as" : "Iron man",
          "Abilities" : [ "Genius", "Billionaire",
                        "Playboy", "Philanthropist" ]
        },
        {
          "Name" : "Peter parker",
          "phone":"42752782",
          "also known as" : "Spider man",
          "Abilities" : [ "Spider web", "Spidy sense" ]
        },
        {
          "Name" : "Steve Rogers",
          "phone":"72525782",
          "also known as" : "Captain America",
          "Abilities" : [ "The First Avenger", "speed" ]
        },
        {
          "Name" : "Chris Hemsworth",
          "phone":"4282243298",
          "also known as" : "Thor",
          "Abilities" : [ "son of Odin", "God of Thunder" ]
        }
    ]
}
'''

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

data  =  json.loads(Avengers)

for person in data['people']:
    # print(person['name'])
  del person['phone']

new_string = json.dumps(data,indent = 3,sort_keys=True)

print(new_string)

############################

