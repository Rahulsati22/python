class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = 120


class Programmer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.lang = lang


rahul = Programmer("rahul", 120, "Python")
print(rahul.name, rahul.lang, rahul.salary)
