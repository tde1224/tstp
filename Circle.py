"""
Create a Circle class with a method called
area that calculates and returns its area.
Then create a Circle object, call area on it, and print the result.
Use Python's pi function in the built-in math module.
"""

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2



my_circle = Circle(5)

result = my_circle.area()

print(result)
