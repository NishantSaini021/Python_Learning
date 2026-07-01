# 8. Prime Number Checker
# Problem: Check if a number is prime.

### Using For Loop
# x = int(input("Please Enter a Number to Check if its Prime: "))
# Prime = True
# i = 2
# while i < x:
#     if x % i == 0:
#         Prime = False
#     i += 1
# if Prime:
#     print(f"{x} is a Prime Number")
# else:
#     print(f"{x} is not a Prime Number")


    

### Using While Loop
x = int(input("Please Enter a Number to Check if its Prime: "))
Prime = True
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
