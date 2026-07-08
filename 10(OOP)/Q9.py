# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self, name):
        self.name = name
class ElectricCar(Car):
    pass

my_tesla = ElectricCar("Tesla X4")
print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))