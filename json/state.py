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

with open('states2.json')as f:
  data=json.load(f)

# for state in data['states']:
#   print(state['language'])
  # del state['population']

# with open('new_states.json','w')as f:
#   json.dump(data, f,indent=2)

with open('new_states2.json','w')as f:
   f.write(json.dumps(data))



# with open('new_states2.json','w')as f:
  #  json.dump(data,f)