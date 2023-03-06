class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


a = Person("rahul", 20)
print(a.__dict__)

# {'name': 'rahul', 'age': 20}
# this attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection
