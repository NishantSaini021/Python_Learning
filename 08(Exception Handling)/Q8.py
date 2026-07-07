# Calculator

# Ask for:
# First Number
# Operator (+, -, *, /)
# Second Number

# Perform the operation.

# Handle:
# ValueError
# ZeroDivisionError


try:
    x = float(input("Enter a Number: "))
    y = input("Enter Operation you want to perform(+, -, *, /): ")
    z = float(input("Enter Another Number: "))
    r = None
    if y == "+":
        r = (x+z)
    elif y == "-":
        r = (x-z)
    elif y == "*":
        r = (x*z)
    elif y == "/":
        r = (x/z)
    else:
        print("Please Enter a Valid Operator")
except ZeroDivisionError:
    print("Division From Zero isn't possible")
    r = None

except ValueError:
    print("Invalid Input")
    r = None

if r is not None:
    print(f"Result: {r}")