# the help() function is used to get help documentation for an object, including a description of its attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


a = Person("rahul", 20)
print(help(a))