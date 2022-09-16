# class Person(object):
   
#   # Constructor
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id
 
#   # To check if this person is an employee
#   def Display(self):
#     print(self.name, self.id)


# # Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()

# ##############################################

# class Emp(Person):
   
#   def Print(self):
#     print("Emp class called")
     
# Emp_details = Emp("Mayank", 103)
 
# # calling parent class function
# Emp_details.Display()
 
# # Calling child class function
# Emp_details.Print()


# ###################################

# class Base1(object):
#     def __init__(self):
#         self.str1 = "Geek1"
#         # print("Base1")
 
 
# class Base2(object):
#     def __init__(self):
#         self.str2 = "Geek2"
#         # print("Base2")
 
 
# class Derived(Base1, Base2):
#     def __init__(self):
 
#         # Calling constructors of Base1
#         # and Base2 classes
#         Base1.__init__(self)
#         Base2.__init__(self)
#         # print("Derived")
 
#     def printStrs(self):
#         print(self.str1, self.str2)
 
 
# ob = Derived()
# ob.printStrs()
# ob.__init__()

###########################
class C(object):
    def __init__(self):
        self.c = 21
 
        # d is private instance variable
        self.__d = 42
 
 
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
 
 
object1 = D()
 
# produces an error as d is private instance variable
print(object1.c)
print(object1.e)

