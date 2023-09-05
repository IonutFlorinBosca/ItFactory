"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"This vehicle has a top speed of {self.max_speed}, mileage of {self.mileage}"

v1 = Vehicle(110, 123444)
print(v1)
print("--"*40)

"""
OOP Exercise 2: Create a Vehicle class without any variables and methods
"""
from abc import ABC, abstractmethod
# class Vehicle:
#     pass

"""
OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""

"""
OOP Exercise 4: Class Inheritance
Given:

Create a Bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_capacity() a default value of 50.
"""
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, name):
        super().__init__(max_speed, mileage)
        self.name = name

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers!"



b1 = Bus(90, 233400, "The Rocket")
print(b1.name, b1.max_speed, b1.mileage)
print(b1.seating_capacity(50))
print("--"*40)

