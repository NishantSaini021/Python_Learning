# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private,
# and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return(self.__brand)
Car1 = Car("Audi", "A4")
Car2 = Car("Mahindra", "Scorpio")
print(Car2.get_brand())