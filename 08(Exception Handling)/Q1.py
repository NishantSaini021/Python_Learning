# Safe Integer Input
# Ask the user for an integer.
# If they enter invalid input,
# print "Invalid Input".
try:
    x = int(input("Please Enter a Interger: "))
    print("Valid Input")
except ValueError:
        print("Please Enter a Valid Number")
    
    