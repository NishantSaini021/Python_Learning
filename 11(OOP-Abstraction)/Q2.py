# Multiple Abstract Methods
# Import:
#     ABC
#     abstractmethod
#
# Create abstract class:
#     Vehicle
#
# Abstract methods:
#     start()
#     stop()
#
# Create child class:
#     Car
#
# Implement:
#     start()
#         print("Car Started")
#
#     stop()
#         print("Car Stopped")
#
# Create object:
#     c1 = Car()
#
# Call:
#     start()
#     stop()

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
c1 = Car()
c1.start()
c1.stop()