# Class Variable
# Problem:
# Add a class variable total_cars
# that counts how many Car objects have been created.

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

car1 = Car("Audi", "A4")
car2 = Car("Mahindra", "Scorpio")
car3 = Car("BMW", "X5")
car4 = Car("Suzuki", "Baleno")
car5 = Car("Honda", "City")
print(Car.total_cars)