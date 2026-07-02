# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
r = float(input("Radius of Circle: "))
def circle(r):
    area = math.pi*r*r
    circumfrence = math.pi*r*2
    return(area,circumfrence)
area, circumference = circle(r)
print("Area:", area)
print("Circumference:", circumference)