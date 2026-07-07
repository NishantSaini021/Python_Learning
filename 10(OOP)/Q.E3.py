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