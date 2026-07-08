# Create a parent class Vehicle
# Constructor: brand

# Class Variable: total_vehicles = 0

# Every time an object is created,
# increase total_vehicles by 1
#
# Method:  show_brand()
# Returns:  brand

# Static Method: vehicle_info()
# Returns: "Vehicles are used for transportation"

# --------------------------------------
# Create a child class ElectricCar
# Inherits from Vehicle
#
# Additional attribute:  battery_size
# Use super().__init__()

# Override:  show_brand()

# It should return: "Electric Car Brand: <brand>"

# --------------------------------------
# Encapsulation
# Make battery_size private

# Create:  get_battery_size()
# Returns battery size

# Create: set_battery_size(size)
# Rule:  size must be > 0

# --------------------------------------
# Create:
# tesla = ElectricCar("Tesla", 100)

# --------------------------------------

# Test all of these:
# 1. show_brand()
# 2. get_battery_size()
# 3. set_battery_size(-50)
# 4. get_battery_size()
# 5. Vehicle.vehicle_info()te
# 6. isinstance(tesla, ElectricCar)
# 7. isinstance(tesla, Vehicle)
# 8. Vehicle.total_vehicles



class Vehicle:
    total_vehicles = 0
    def __init__(self,brand):
        self.brand = brand
        Vehicle.total_vehicles += 1

    def show_brand(self):
        return self.brand
    
    @staticmethod
    def vehicle_info():
        return "Vehicles are used for transportation"
    
class ElectricCar(Vehicle):
    def __init__ (self,brand, battery_size):
        super().__init__(brand)
        self.__battery_size = battery_size

    def show_brand(self):
        return f"Electric Car Brand: {self.brand}"

    def get_battery_size(self):
        return self.__battery_size
    
    def set_battery_size(self, battery_size):
        if battery_size > 0:
            self.__battery_size = battery_size

tesla = ElectricCar("Tesla", 100)

print(tesla.show_brand())
print(tesla.get_battery_size())
tesla.set_battery_size(500)
print(tesla.get_battery_size())
print(Vehicle.vehicle_info())
print(isinstance(tesla, ElectricCar))
print(isinstance(tesla, Vehicle))
print(Vehicle.total_vehicles)