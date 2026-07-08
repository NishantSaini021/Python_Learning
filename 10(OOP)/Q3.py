# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class 
# and has an additional attribute battery_size.

class Car:
    def __init__(self, brand):
        self.brand = brand
class ElectricCar(Car):
    def __init__(self, brand, battery_size):
        Car.__init__(self, brand)
        self.battery_size = battery_size

e1 = ElectricCar("Tata", "50KwH")
e2 = ElectricCar("Audi", "45KwH")
print(e1.brand)
print(e1.battery_size)
print(e2.brand)
print(e2.battery_size)