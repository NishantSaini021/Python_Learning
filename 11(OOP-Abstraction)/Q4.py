# Create abstract class: Shape
# Abstract Method:  area()

# ---------------------------------
# Create child class: Rectangle
# Attributes:
# length
# width
# area()
# returns:  length * width

# --------------------------------
# Create child class:  Square
# Attribute:  side
# area()
# returns:  side * side
# ---------------------------------
# Create:
# shapes = [  Rectangle(10, 5),  Square(4)]
# Use a loop:
# for shape in shapes:
#     print(shape.area())
# ------------------------------
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*self.side
shapes = [  Rectangle(10, 5),  Square(4)]
for shape in shapes:
    print(shape.area())