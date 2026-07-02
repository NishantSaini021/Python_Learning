# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

## Using For Loop

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0

for i in numbers:
    if i > 0:
        count += 1

print(count)


## Using While Loop
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] > 0:
        count += 1
    i += 1
print(count)