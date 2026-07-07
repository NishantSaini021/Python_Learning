# Ask for two numbers and divide them.
#
# Handle:
# - ValueError
# - ZeroDivisionError

try:
    x = float(input("Enter a Number to Divide: "))
    y = float(input("Enter Divisor: "))
    print(f"Result: {x/y}")
except ValueError:
    print("Please Enter a Valid Number: ")
except ZeroDivisionError:
    print("Division From Zero Not Possible")




while True:
    try:
        x = float(input("Enter a Number to Divide: "))
        y = float(input("Enter Divisor: "))
        print(f"Result: {x/y}")
        break
    except ValueError:
        print("Please Enter a Valid Number: ")
    except ZeroDivisionError:
        print("Division From Zero Not Possible")