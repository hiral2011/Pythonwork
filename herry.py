# from gzip import FNAME
# from symtable import SymbolTableFactory


class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else :
            return True

        
class programer(Employee): 
    def __init__(self, fname, lname, salary, prolang, expi):
        super().__init__(fname, lname, salary)
        self.prolang = prolang
        self.expi = expi

    def increase(self):  #overrideing of uper function increase
        self.salary = int(self.salary * (self.increment + 0.2))
        return self.salary
 
hiral = programer("hiral",'patel',5000,'python','0 year')
print(hiral.expi)
# print(hiral.increase())  #this will return none
# print(hiral.increase())  #this will return none




# hiral = Employee("hiral","tarpara",10000)
# print(hiral.fname)
# print(hiral.salary)
# print(hiral.isopen('monday'))
# print(hiral.isopen('sunday'))
