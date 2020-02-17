"""
Create a Rectangle and Square class with a method called calculate_perimeter
that calculates the perimeter of the shapes they represent.
Create Rectangle and Square objects and call the method on both of them.

"""
class Shape():
    def what_am_i(self):
        print("I am a shape")
        
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, num):
        self.side = self.side + num
        

my_rectangle = Rectangle(3, 5)
my_square = Square(2)

print(my_rectangle.calculate_perimeter())
print(my_square.calculate_perimeter())

my_square.change_size(5)

print(my_square.calculate_perimeter())

my_rectangle.what_am_i()

my_square.what_am_i()
