# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def _sum(*args):
    total = 0
    for num in args:
        total += num
    return total
s = input("Enter numbers separated by spaces: ")

numbers = s.split()

numbers = [int(num) for num in numbers]

print(_sum(*numbers))