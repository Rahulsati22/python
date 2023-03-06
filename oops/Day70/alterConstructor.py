class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromString(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])

    @classmethod
    def fromString2(cls, string):
        return cls(string.split(" ")[0], string.split(" ")[1])


e = Employee("rahul", 120)
print(e.name, e.salary)
# rahul 120


string = "rahul-120"
e2 = Employee.fromString(string)
print(e2.name, e2.salary)
# rahul 120


string = "rahul 200"
e3 = Employee.fromString2(string)
print(e3.name, e3.salary)
