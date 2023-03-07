# magic methods -> dunder methods -> start from double underscore and ends at double underscore
class Employee:
    def __init__(self):
        self.name = "Rahul"
        self.age = 10

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"The name of the employee is {self.name} and the age of the employee is {self.age}"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print(f"My name is {self.name}")
