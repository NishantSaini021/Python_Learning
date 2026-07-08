# OOP Mini Project
# Smart Employee Management System
#
# Concepts Covered:
# - Class
# - Object
# - Constructor
# - Inheritance
# - super()
# - Encapsulation
# - Getter
# - Setter
# - Class Variable
# - Static Method
# - Method Overriding
# - Polymorphism
# - isinstance()
# - Abstraction
#
# ==================================================
#
# STEP 1
#
# Create an Abstract Class:
#
# Employee
#
# Attributes:
#     name
#
# Class Variable:
#     total_employees = 0
#
# Constructor:
#     name
#
# Every time an employee object is created:
#     increase total_employees
#
# Abstract Method:
#
#     calculate_salary()
#
# ==================================================
#
# STEP 2
#
# Create:
#
# FullTimeEmployee(Employee)
#
# Additional Private Attribute:
#
#     __monthly_salary
#
# Constructor:
#
#     name
#     monthly_salary
#
# Use:
#
#     super().__init__(name)
#
# Implement:
#
#     calculate_salary()
#
# Return:
#
#     monthly_salary
#
# ==================================================
#
# STEP 3
#
# Create:
#
# PartTimeEmployee(Employee)
#
# Additional Private Attributes:
#
#     __hours_worked
#     __hourly_rate
#
# Constructor:
#
#     name
#     hours_worked
#     hourly_rate
#
# Use:
#
#     super().__init__(name)
#
# Implement:
#
#     calculate_salary()
#
# Return:
#
#     hours_worked * hourly_rate
#
# ==================================================
#
# STEP 4
#
# Encapsulation
#
# For FullTimeEmployee:
#
# Create:
#
#     get_salary()
#
#     set_salary(new_salary)
#
# Rule:
#
#     new_salary > 0
#
# Otherwise:
#
#     do nothing
#
# ==================================================
#
# STEP 5
#
# Method Overriding
#
# Add method:
#
#     employee_info()
#
# in Employee
#
# Return:
#
#     Employee: <name>
#
# Override it in:
#
# FullTimeEmployee
#
# Return:
#
#     Full Time Employee: <name>
#
# Override it in:
#
# PartTimeEmployee
#
# Return:
#
#     Part Time Employee: <name>
#
# ==================================================
#
# STEP 6
#
# Static Method
#
# Create:
#
# company_policy()
#
# Return:
#
#     "Employees must follow company rules."
#
# ==================================================
#
# STEP 7
#
# Create Objects
#
# emp1 = FullTimeEmployee("Alice", 50000)
#
# emp2 = PartTimeEmployee("Bob", 40, 500)
#
# ==================================================
#
# STEP 8
#
# Polymorphism
#
# employees = [emp1, emp2]
#
# Loop through employees:
#
# Print:
#
#     employee_info()
#
#     calculate_salary()
#
# ==================================================
#
# STEP 9
#
# Test:
#
# print(Employee.total_employees)
#
# print(Employee.company_policy())
#
# print(isinstance(emp1, Employee))
#
# print(isinstance(emp2, Employee))
#
# ==================================================
#
# STEP 10 (Important)
#
# Try:
#
# emp1.set_salary(-1000)
#
# Then:
#
# print(emp1.get_salary())
#
# Prediction:
#
# What should happen?
#
# Why?


from abc import ABC,abstractmethod
class Employee(ABC):
    total_employees = 0
    def __init__(self,name):
        self.name = name
        Employee.total_employees += 1

    def employee_info(self):
        return f"Employee: {self.name}"

    @abstractmethod
    def calculate_salary(self):
        pass
    @staticmethod
    def company_policy():
        return "Employees must follow company rules"

class FullTimeEmployee(Employee):
    def __init__(self,name,monthly_salary):
        super().__init__(name)
        self.__monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.__monthly_salary
    def get_salary(self):
        return self.__monthly_salary
    def set_salary(self,new_salary):
        if new_salary > 0:
            self.__monthly_salary = new_salary
    def employee_info(self):
        return f"Full Time Employee: {self.name}"


class PartTimeEmployee(Employee):
    def __init__(self,name,hours_worked,hourly_rate):
        super().__init__(name)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.__hours_worked*self.__hourly_rate
    def employee_info(self):
        return f"Part Time Employee: {self.name}"
    
emp1 = FullTimeEmployee("Alice", 50000)
emp2 = PartTimeEmployee("Bob", 40, 500)
emp3 = FullTimeEmployee("Nishant", 60000)
employees = [emp1, emp2, emp3]
for employee in employees:
    print(employee.employee_info())
    print(employee.calculate_salary())
    
print(Employee.total_employees)
print(Employee.company_policy())
print(isinstance(emp1, Employee))
print(isinstance(emp2, Employee))
emp1.set_salary(-1000)
print(emp1.get_salary())