import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function to calculate total area
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


# Testing
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
print("Total area:", total_area(shapes))
