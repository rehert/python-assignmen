# Question 1
# Create a Vehicle class with Car and Bike subclasses

class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Bike(Vehicle):
    def move(self):
        print("The bike is being pedaled.")

v = Vehicle()
c = Car()
b = Bike()

v.move()
c.move()
b.move()


# =======================
# Question 2
# Function that calculates total area of different shapes using polymorphism
# =======================

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

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
print("Total area:", total_area(shapes))


# Question 3
# Using super() in a subclass constructor and method


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


# Question 4

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

def process_sound(sound_object):
    print(sound_object.make_sound())

dog = Dog()
cat = Cat()

process_sound(dog)
process_sound(cat)


# Question 5
# Abstract Base Class (ABC) for file handlers

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
        return "Reading text file..."

    def write(self, data):
        print(f"Writing '{data}' to text file.")

class BinaryFileHandler(FileHandler):
    def read(self):
        return b"Binary data"

    def write(self, data):
        print(f"Writing binary data: {data}")

text_handler = TextFileHandler()
print(text_handler.read())
text_handler.write("Hello")

binary_handler = BinaryFileHandler()
print(binary_handler.read())
binary_handler.write(b"101010")



