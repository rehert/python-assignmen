# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

# Subclass Bike
class Bike(Vehicle):
    def move(self):
        print("The bike is being pedaled.")

# Testing
v = Vehicle()
c = Car()
b = Bike()

v.move()   # The vehicle is moving.
c.move()   # The car is driving on the road.
b.move()   # The bike is being pedaled.

