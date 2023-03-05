# Private members are those members that are accessible only inside the class . we cannot use private members outside the class .
# In python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore . this is known as weak internal use indicator and it is a convention only, not a strict rule . Code outside the class can still access these private variables and methods , but it is generally understood that these should not be accessed or modified
class Employee:
    def __init__(self):
        self.__name = "rahul"

    def printName(self):
        print(self.__name)


rahul = Employee()
rahul.printName()


# print(rahul.__name) --> this is not possible

# we can access private members like this
print(rahul._Employee__name)
