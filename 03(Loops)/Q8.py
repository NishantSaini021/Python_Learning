# 8. Prime Number Checker
# Problem: Check if a number is prime.

### Using For Loop
x = int(input("Please Enter a Number to Check if its Prime: "))
Prime = True
if x <= 1:
    Prime = False
for i in range (2,x):
    if x % i == 0:
        Prime = False
        break
if Prime:
    print(f"{x} is a Prime Number")
else:
    print(f"{x} is Non-Prime")
    

# # ### Using While Loop
x = int(input("Please Enter a Number to Check if its Prime: "))
Prime = True
if x <= 1:
    Prime = False
i = 2
while i < x:
    if x % i == 0:
        Prime = False
        break
    i += 1
if Prime:
    print(f"{x} is a Prime Number")
else:
    print(f"{x} is not a Prime Number")