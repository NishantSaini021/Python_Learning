# Ask for a number.
#
# Whether the input is valid or invalid,
# print:
#
# "Program Ended"
#
# using finally.


try:
    x = int(input("Please a Enter a Number: "))
    print("Valid Input")
except ValueError:
    print("Invalid Input")
finally:
    print("Program Ended")

