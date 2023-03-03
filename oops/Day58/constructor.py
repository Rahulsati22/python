class Student:
    name = "Unknown"
    year = -1
    sec = "Unknown"

    def __init__(self, name, year, sec):
        self.name = name
        self.year = year
        self.sec = sec

    def info(self):
        print(
            f"The name of the student is {self.name}, year of the student is {self.year} and the section of the student is {self.sec}")


#!to solve this problem of writing lengthy code we have the concept of constructor
# a = Student()
# a.name = "rahul"
# a.year = 2
# a.sec = "H"
# a.info()

a = Student("rahul", 2, "H")
a.info()


# constructor always return None
# default constructor is that constructor that does not have any argument