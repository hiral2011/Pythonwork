
class Company:
    def __init__(self):
        self._project = "NLP"

class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

print('Project:', c._project)