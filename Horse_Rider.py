"""
Create a class called Horse and a class called Rider.
Use composition to model a horse that has a rider.
"""

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider
        

class Rider():
    def __init__(self, name):
        self.name = name


my_rider = Rider("Tim")
my_horse = Horse("Horsie", my_rider)

print(my_horse.rider.name)
