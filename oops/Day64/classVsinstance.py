# in python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

# class variable are defined at the class level and shared among all the instances of the class .They are defined outside of any method and used to share information that are common to all the instances of the class. For example, a class variable can be used to store the number of instances of the class that have been created

class Employee:
    companyName = "Apple"
    population = 0

    def __init__(self, name, amount):
        self.name = name
        self.raiseAmount = amount
        Employee.population += 1

    def showDetails(self):
        print(
            f"The name of the employee is {self.name} and the raise amount is {self.raiseAmount} and the company name is {self.companyName}")


# instance variable like name and raise in salary can be changed by instance variables of class
emp1 = Employee("rahul", 10)
emp1.companyName = "Google"
emp1.showDetails()
Employee.showDetails(emp1)
print(Employee.population)

emp2 = Employee("ayush", 20)
emp2.showDetails()
print(emp2.companyName)
Employee.showDetails(emp2)
print(Employee.population)
