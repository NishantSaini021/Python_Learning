# Q1 - Guess the Secret Number

# Problem Statement:
# Create a number guessing game using a while loop.

# A secret number is already set to:
#     7

# Ask the user to enter a number repeatedly until they guess the correct number.

# Rules:
# - If the user enters the wrong number, print:
#       Wrong Guess
#
# - If the user enters the correct number, print:
#       Correct Guess!
#
# - The program should stop after the correct guess.

# Example:

# Enter Number: 3
# Wrong Guess

# Enter Number: 10
# Wrong Guess

# Enter Number: 7
# Correct Guess!

# Concepts to Practice:
# - while loop
# - user input
# - comparison operators
# - loop termination

x = int(input("Try to Guess the Correct Number: "))
while x != 7:
        x = int(input("Try Again: "))
print("Correct Guess")