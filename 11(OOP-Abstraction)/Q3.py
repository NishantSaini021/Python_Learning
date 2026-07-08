# Create abstract class:
#     Employee
#
# Constructor:
#     name
#
# Abstract Method:
#     calculate_salary()
#
# Create child class:
#     FullTimeEmployee
#
# Additional Attribute:
#     monthly_salary
#
# Implement:
#     calculate_salary()
#
# Return:
#     monthly_salary
#
# Create:
#     emp = FullTimeEmployee("Nishant", 50000)
#
# Print:
#     emp.calculate_salary()
#
# ----------------------------------


from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name,monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary
emp = FullTimeEmployee("Nishant", 50000)
print(emp.name)
print(emp.calculate_salary())