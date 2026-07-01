# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

x = int(input("Please give a INPUT: "))
while x < 0 or x > 10:
    x = int(input("Wrong Input Enter Again: "))    
print("Input Validated")