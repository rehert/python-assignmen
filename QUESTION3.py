class Shape:
    def __init__(self):
        print("Shape initialized.")

    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()
        return self.width * self.height


r = Rectangle(4, 5)
print("Rectangle area:", r.calculate_area())
