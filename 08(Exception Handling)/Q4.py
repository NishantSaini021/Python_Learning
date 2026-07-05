# numbers = [10, 20, 30, 40]

# Ask the user for an index.
# Print the value at that index.
# If the index is invalid,
# print an error message.


numbers = [10, 20, 30, 40]
try:
    x = int(input("Enter a Index to Print Value: "))
    print(numbers[x])
except IndexError:
    print("Please Enter a Valid Index")