# Method Overriding
class Animal:
    def speak(self):
        print("xyz sound")
class Dog(Animal):
    def speak(self):
        print("Woof")
# d = Dog()
# d.speak()

### Overriding + Parent Method(Extending Parent Method)
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
# d = Dog()
# d.speak()

#############
class Person():
    def introduce(self):
        print("Hello, I am a Person")
class Student(Person):
    def introduce(self):
        super().introduce()
        print("Hello, I am a Student")
s1 = Student()
s1.introduce()
