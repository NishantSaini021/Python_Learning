
# Exercise: Polymorphism
# Create a class Bird
# Method:
#     sound()
# Prints:
#     Chirp

# Create a class Cow
# Method:
#     sound()
# Prints:
#     Moo

# Create a list containing:
#     Bird()
#     Cow()

# Use a loop to call:
#     sound()
#
# on every object in the list.

class Bird:
    def sound(self):
        print("Chirp")
class Cow:
    def sound(self):
        print("Moo")
Animals = [Bird(), Cow()]
for animal in Animals:
    animal.sound()

# Exercise: Inheritance + Polymorphism
# Create a parent class:
# Animal

# Method: sound()
# Prints: Some Sound

# Create child classes:
# Dog
# Cat

# Override sound()
# Dog -> Woof
# Cat -> Meow

# Create a list:
# [Dog(), Cat()]

# Use a loop to call:
# animal.sound()

class Animal:
    def sound(self):
        print("Some Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for i in animals:
    i.sound()