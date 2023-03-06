class Employee:
    company = "Apple"

    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

# first argument is as an instance
    def changeCompany(cls, newCompany):
        cls.company = newCompany

# first method is as a class
    @classmethod
    def changeOriginal(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Google")
e1.show()
print(Employee.company)

e2 = Employee()
Employee.changeOriginal("Tesla")
e1.show()
print(Employee.company)
e2.name = "Rahul"
e2.show()
