# in object oriented programming , the term "protected" is used to describe a member of a class that can be accessed only inside the children of the class and inside the class.We can indicate that the member is protected by using a single underscore . We are not saying that it will protect the member but this is just a convention
# no indirect method is required we can access it directly

class Employee:
    _name = "rahul"


rahul = Employee()
# can be accessed directly-> it is just a convention
print(rahul._name)
