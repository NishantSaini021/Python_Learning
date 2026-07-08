# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and
# ElectricCar classes, but with different behaviors.

class Vehicle:
    def fuel_type(self):
        print("Unknown")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol/Diesel")
class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Electricity")
vehicles = [Car(), ElectricCar()]
for car in vehicles:
    car.fuel_type()