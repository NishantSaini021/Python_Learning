# class Student:
#     pass

# s1 = Student()

# s1.name = "Nishant"
# s1.age = 20
# s1.branch = "CSE"

# print(s1.name)
# print(s1.age)
# print(s1.branch)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_age(self):
        print("Age:",self.age)
    def show_name(self):
        print("Name:", self.name)
    def show_name_age(self):
        print(self.name,self.age)


s1 = Student("Nishant", 20)
s2 = Student("Raman", 19)
# print(s1.name)
# print(s2.age)
s1.show_name_age()
s2.show_name_age()

