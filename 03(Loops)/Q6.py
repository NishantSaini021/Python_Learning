# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

n = int(input("Please Enter a Number to find its Factorial: "))
total = 1
while n >= 1:
    total = total*n
    n -= 1
print(total)