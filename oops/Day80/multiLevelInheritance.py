# multilevel inheritance
# multilevel inheritance means a derived class inherits from another derived class
# example dadaji->papaji->betaji
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def showDetails(self):
        print(
            "the name of the dog is {self.name} and the species of the dog is {self.species}")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def showDetails(self):
        print("the breed of the dog is {self.breed}")


class goldenRetriever(Dog):
    def __init__(self, name, species, breed, color):
        super().__init__(name, species, breed)
        self.color = color

    def showDetails(self):
        print("the color of the dog is {self.color}")


o = goldenRetriever("brownie", "mix", "golden retriever", "blue")
print(o.name, o.breed, o.color, o.species)
