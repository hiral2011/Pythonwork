# class Family:  
#     # Constructor - parameterized  
#     members=5
#     def __init__(self, count):  
#         print("This is parametrized constructor")  
#         self.members = count
#     def show(self):  
#         print("No. of members are ",self.members)  
        
# object = Family(10)  
# object.show() 

##########################    # non-parameterized constructor

class Fruits:
    favourite = "Apple"

    def __init__(self):
        self.favourite = "Orange"

    # a method
    def show(self):
        print(self.favourite)


# creating object of the class
obj = Fruits()

# calling the instance method using the object obj
obj.show()


############## Default Constructor in Python

class Assignments:
    check= "not done"
    # a method
    def is_done(self):
        print(self.check)

# creating object of the class
obj = Assignments()

# calling the instance method using the object obj
obj.is_done()
