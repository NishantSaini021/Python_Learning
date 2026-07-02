# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

### Using For Loop:
# n = int(input("Enter a Number: "))
# for i in range (1,11):
#     if i == 5:
#         continue
#     print(n*i)



### Using While Loop
# n = int(input("Enter a Number: "))
# i = 0
# while i < 11:
#     if i == 5:
#         i += 1
#     print(n*i)
#     i += 1

### Also Using While Loop

n = int(input("Enter a Number: "))
i = 0
while i < 10:
    i += 1
    if i == 5:
        i += 1
    print(n*i)