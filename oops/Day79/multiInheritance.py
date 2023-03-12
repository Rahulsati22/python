class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("hey i am employee class")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print("hey i am dancer class")

# agar employee pehle likhenge to employee ka show method pehle run hoga
# agar dancer pehle likhenge to dancer ka show method pehle run hoga


class DanceEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

    # def show(self):
    #     print("hey i am dance employee class")


o = DanceEmployee("rahul", "bachata")
print(o.name)
print(o.dance)
o.show()
print(DanceEmployee.mro())

# what is method resolution order
# it will tell the order in which function inside the classes will be called