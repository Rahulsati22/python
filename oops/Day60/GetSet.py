class Car:
    def __init__(self, color):
        self.color = color

    def show(self):
        print(f"The color of the car is {self.color}")

    # this is a getter
    @property
    def ten_value(self):
        return self.color

    @ten_value.setter
    def ten_value(self, str):
        self.color = str


fortuner = Car("white")
print(fortuner.ten_value)
fortuner.ten_value = "Gray"
print(fortuner.ten_value)
