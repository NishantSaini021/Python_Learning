# Import: ABC abstractmethod
# Create abstract class: Shape

# Abstract method:  area()

# Create child class:  Rectangle

# Constructor: length width

# Implement:  area()
# Return: length * width

# Create: Rectangle(10, 5)
# Print:  area()

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length= length
        self.width = width
    def area(self):
        return(self.length*self.width)
r = Rectangle(10, 5)
x = r.area()
print(x)