"""
Make a Hexagon class with a method called calculate_perimeter that
calculates and returns its perimeter. Then create a Hexagon object,
call calculate_perimeter on it, and print the result
"""

class Hexagon():
    def __init__(self, side1, side2, side3, side4, side5, side6):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

my_hexagon = Hexagon(6, 6, 6, 6, 6, 6)

result = my_hexagon.calculate_perimeter()

print(result)
