# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.


### Using For Loop
n = int(input("Please give input: "))
count = 0
for i in range(0,n+1):
    if i%2 == 0:
        count += i

print(count)


### Using While Loop
n = int(input("Please give input: "))
sum_ = 0
i = 0
while i <= n:
    if i % 2 == 0:
        sum_ += i
    i += 1
print(sum_)