# class dog:
#     def __init__(self,dogbreed,dogEyeColor):
#         self.breed = dogbreed
#         self.eyecolor = dogEyeColor

# Tomita = dog("Fox Terrier","brown")
# print("this dog is ",Tomita.breed,"and its color is ",Tomita.eyecolor)

# ###############################        

# class Dog:                
 
#     def __init__(self, dogBreed="German Shepherd",dogEyeColor="Brown"): 
#         self.breed = dogBreed   
#         self.eyeColor = dogEyeColor
# Tomita = Dog()
# print("This dog is a",Tomita.breed,"and its eyes are",Tomita.eyeColor)

# ##################################

# class Dog:  
 
#     def __init__(self):
#         self.nbLegs = 4
 
# tomita = Dog()
# print("This dog has",tomita.nbLegs,"legs")


class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        # person.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)

x = student("gurleen","panu",2019)
x.welcome()
# print(x.graduationyear)



