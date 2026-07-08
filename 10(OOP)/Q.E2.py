# Inheritance 
# Create a dog object named "Rocky"
# Print its name

class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    pass
    def show_name(self):
        print(self.name)
Dog1 = Dog("Rocky")
Dog1.show_name()

#########################

class Vehicle:
    def __init__(self,brand):
        self.brand= brand
    def show_brand(self):
        print(self.brand)
class Bike(Vehicle):
    def ring_bell(self):
        print("Horn")
b1 = Bike("Hero")
b1.ring_bell()
b1.show_brand()

##########
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no
s1 = Student("Nishant", "24CS71")
print(s1.name)
print(s1.roll_no)