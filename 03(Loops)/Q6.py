# 6. Factorial Calculator
# Problem: Compute the factorial of a number using Loop.

### Using For Loop
n = int(input("Please Enter a Number to find its Factorial: "))
total = 1
for i in range (1,n+1):
    total = total*i
print(total)

### Using While Loop
n = int(input("Please Enter a Number to find its Factorial: "))
total = 1
while n >= 1:
    total = total*n
    n -= 1
print(total)

