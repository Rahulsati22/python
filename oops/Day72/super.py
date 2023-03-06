# the super keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

# Sometimes you want to use he methods of parent class in child class . To do this you can use the super() keyword

class Parent():
    def introParent(self):
        print("Hey i am a function of parent class")


class Child(Parent):
    # def introParent(self):
    #     print("rahul sati from child")

    def introChild(self):
        print("Hey i am a function from child class")
        super().introParent()


a = Child()
a.introChild()
a.introParent()
