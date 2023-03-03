# set name class and marks of student using getters and setters
class Student:
    name = "Unknown"
    marks = -1
    _class = -1
    # creating getter

    @property
    def getName(self):
        print(f"name = {self.name}")

    @getName.setter
    def getName(self, name):
        self.name = name

    @property
    def getClass(self):
        print(f"class = {self._class}")

    @getClass.setter
    def getClass(self, _class):
        self._class = _class

    @property
    def getMarks(self):
        print(f"marks = {self.marks}")

    @getMarks.setter
    def getMarks(self, marks):
        self.marks = marks


rahul = Student()
rahul.getName = "rahul"
rahul.getMarks = 100
rahul.getClass = 'H'
rahul.getName
rahul.getClass
rahul.getMarks
