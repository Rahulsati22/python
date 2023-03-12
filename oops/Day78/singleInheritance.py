class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makeSound(self):
        print("animal is making a sound")


# creating a dog class which will inherit animal
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def makeSound():
        print("Bark")


dog = Dog("sheru", "german shephard", "mix")
print(
    f"the name of the dog is {dog.name} and the breed of the dog is {dog.breed} and the species of the dog is {dog.species}")


class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.character = "jump"

    def makeSound(self):
        print("meow-meow")


cat = Cat("mechain", "junglee")
print(cat.character, cat.name, cat.species)
