from collections import namedtuple

nametup = namedtuple('nametup','value1,value2,value3')
mytuple = nametup('hello','topics','python')

print(mytuple.value1)
print(mytuple.value2)
print(mytuple.value3)

##########

# tuple1 = namedtuple('tupe1',['name','address','profesion'])
# mytuple = tuple1('abc','surat','teacher')

# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])

# print(mytuple)