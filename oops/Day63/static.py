class Math:
    def __init__(self, a):
        self.a = a

# compulsary to add self in non static methods
    def addToNum(self, num):
        self.a += num

# we do not need to add self in static methods
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def pow(a, b):
        return a ** b


# dependent on the object
a = Math(10)
print(a.a)
a.addToNum(10)
print(a.a)


# dependent on the class but can also be accessed by object name
print(Math.add(1, 2))
print(Math.sub(1, 2))
print(Math.pow(2, 1))
