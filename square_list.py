"""
Add a square_list class variable to a class called Square so that every time you
create a new Square object, the new object gets added to the list
"""


class Square():
    square_list = []
    

    def __init__(self, side):
        self.side = side
        self.square_list.append(side)

    def __repr__(self):
        return str(self.side) + " by " + str(self.side) + " by " + str(self.side) + " by " + str(self.side)



my_square1 = Square(10)
my_square2 = Square(5)

print(Square.square_list)

print(my_square2)
