# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Please give input: "))
count = 0
for i in range(0,n+1):
    if i%2 == 0:
        count += i

print(count)