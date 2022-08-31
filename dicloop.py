class_A ={"student":{101:"riya",102:"jiya",103:"priya",107:"priya"},
          "top_student":{105:"diya",109:"hiya",106:"siya"}
        }

# class_A["student"][108]= "siya"
# print(class_A)


for k in class_A:
        print()
        print(k)
        for v in class_A[k]:
                print(v,class_A[k][v])
print()

 ##################only dictionary name

# for k in (class_A):
#     print(k)
# print()

####################value and key

# for k in (class_A):
#     print(class_A[k])
# print()

################dictionary name with key and value

# for k in (class_A):
#     print(k,class_A[k])
# print()

##################only for key

# for k in (class_A):
#     print(class_A[k].keys())
# print()

#################only key and value

# for k in class_A:
#         for v in class_A[k]:
#                 print(v,class_A[k][v])
# print()

#################only value

# for k in (class_A):
#     print(class_A[k].values())
# print()

###############################
        #user input in dict

# course = {}
 
# n=int(input("enter number of elements = "))

# for i in range(n):
#     k=input("enter key =")
#     v=input("enter value =")
#     course.update({k:v})

# print(course)

     
############################
   ##loop in python



# class triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     # pass

#     def get_perimeter(self):
#         perimeter = self.a + self.b + self.c
#         return perimeter

# t1 = triangle(3,4,5)

# perimeter = t1.get_perimeter()
# print(perimeter)


################################

from sre_constants import AT_MULTILINE


# family = {}
# # print(type(family))

# family['name']="john"
# family['last_name']="alwyn"
# family['age']=35
# family['spouse']="srishti jain"
# family['children']=["raju","munna","surya","khusi"]
# family['pets']={'dog':'fido','cat':'sox'}

# print(family.get('name'))

# print(family.get('hiral',-9))

# list(family.items())[1][0]

#################################

###################Dictionary of tuples with tuples as keys

# food = {('roti','sabji','salad'):'india',
#         ('burger','bread','coffe'):'usa',
#         ('noodle','manchuriyan'):'chaina'
#         }


# for k in (food):  #only tuple(key)
#     print(food[k])
# print()

# for k in (food):     #only value
#     print(k)
# print()

####Dictionary of tuples with tuples as values

# food = {'india':('roti','sabji','salad'),
#         'usa':('burger','bread','coffe'),
#         'chaina':('noodle','manchuriyan')
#         }


# food = (('india','usa'),('roti','sabji'))

# final= dict((value,key)for key,value in food)
# print(final)