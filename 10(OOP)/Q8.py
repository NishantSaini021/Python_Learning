# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    def get_brand(self):
        return(self.__brand)
    @property
    def model(self):
        return(self.__model)
Car1 = Car("Audi", "A4")
Car2 = Car("Mahindra", "Scorpio")
print(Car1.model)