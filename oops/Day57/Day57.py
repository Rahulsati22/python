class Person:
    name = "Harry"
    occupation = "Software Developer"
    netWorth = 10
    # self is like this {means vo objexct jiske liye ye method call kiya ja rha hai}

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()
print(a.name)
a.name = "Rahul Sati"
a.occupation = "Software developer"
a.info()
b.name = "Ayush Sati"
b.occupation = "Web Developer"
c.name = "Nitika"
c.occupation = "HR"
b.info()
c.info()
