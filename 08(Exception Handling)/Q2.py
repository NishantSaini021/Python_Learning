# Problem:
# Take two numbers from the user.
# Handle division by zero.

try:
    y = float(input("Please A Enter a Number : "))
    x = float(input("Please Enter Divisor: "))
    print((y)/(x))
except ZeroDivisionError:
    print("Divison from Zero Not Possible")