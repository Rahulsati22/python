class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the id of the employee is {self.id}")


class Programmer(Employee):
    def __init__(self, name, id,language):
        super().__init__(name, id)
        self.language = language

    def showDetails(self):
        print(f"The name of the programmer is {self.name}, id of the programmer is {self.id} and the language of the programmer is {self.language}")
        
rahul = Employee("rahul", 1)
rahul.showDetails()

rahul = Programmer("rahul", 1, "python")
rahul.showDetails()
