class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        print(f"The area is {self.x * self.y}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        print(f"the area is {3.14 * self.radius * self.radius}")


sq = Shape(10, 10)
sq.area()

rec = Shape(5, 10)
sq.area()

crcl = Circle(10, 20, 5)
crcl.area()
