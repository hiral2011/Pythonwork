class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        company.__init__(self)

    # def show(self):
        # print(f"name :{self.name} salay :{self.__salary}")

emp1 = employee("hiral",10000)

# print(f"name :{emp1.name} salay :{emp1.salary}")

# emp1.show()

print('salary:',emp1.name)
print('salary:',emp1._employee__salary)   #acsess private member