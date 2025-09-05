# Question 1
# Vehicle -> Car, Bike (Method overriding)

class Vehicle:
    def start_engine(self):
        return "The vehicle engine starts."

class Car(Vehicle):
    def start_engine(self):
        return "The car engine starts with a roar!"

class Bike(Vehicle):
    def start_engine(self):
        return "The bike engine starts with a hum!"

# Test
print(Car().start_engine())
print(Bike().start_engine())

# Question 2
# Shapes: Circle, Rectangle (Polymorphism)

import math

class Shape:
    def area(self):
        pass  # Base class does nothing

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Test
shapes = [Circle(3), Rectangle(4, 5), Circle(2)]
print("Total area:", total_area(shapes))


# Question 3
# Using super() in Rectangle

class Shape:
    def __init__(self):
        print("Shape is being created")

    def calculate_area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()  # Call parent method (does nothing here)
        return self.width * self.height

# Test
rect = Rectangle(4, 6)
print("Rectangle area:", rect.calculate_area())


# Question 4
# Duck typing: process_sound() works with any object
# that has make_sound()

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

def process_sound(animal):
    print(animal.make_sound())

process_sound(Dog())
process_sound(Cat())

# Question 5
# Abstract Base Class for File Handlers

from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        return "Reading from text file..."

    def write(self, data):
        return f"Writing '{data}' to text file."

class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading from binary file..."

    def write(self, data):
        return f"Writing binary data: {data}"

txt = TextFileHandler()
bin = BinaryFileHandler()

print(txt.read())
print(txt.write("Hello World"))
print(bin.read())
print(bin.write(b"\x00\xFF"))
