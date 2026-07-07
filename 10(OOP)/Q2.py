# Class Method and Self
# Problem: Add a method to the Car class
# that displays the full name of the car (brand and model).


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_car(self):
        print(self.brand, self.model)
Car1 = Car("Audi", "A4")
Car2 = Car("Mahindra", "Scorpio")
Car1.show_car()
Car2.show_car()