# Ask for an integer.
# If conversion succeeds, print:
# "Valid Number"
# using the else block.


try:
    x = int(input("Please Enter a Integer: "))
except ValueError:
    print("Invalid Input")
else:
    print("Input Validated")