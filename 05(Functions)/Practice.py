###### Write a Function that returns larger from two numbers

# a = int(input("Enter a Number: "))
# b = int(input("Enter Another Number: "))
# def fun(a,b):
#     if a > b:
#         return(a)
#     else:
#         return(b)
# print(fun(a,b), "is Greater")




####### Even Number Checker
# Problem: Create a function is_even(n)
# that returns True if the number is even
# and False otherwise.

# x = int(input("Enter a Number to Check if its Even: "))
# def is_even(x):
#     return x % 2 == 0
# print(is_even(x))



###### find_max(numbers)
# sum_list(numbers)
# count_positive(numbers)
#use loop 

# numbers = [1, 2, 25, 24, 56, 45, 54, 85, 58, 78, 96, 52, 99]
# def find_max(numbers):
#     largest = numbers[0]
#     for num in numbers:
#         if largest < num:
#             largest = num
#     return largest

# def sum_list(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# def count_total_numbers(numbers):
#     count = 0
#     for num in numbers:
#         count += 1
#     return count

# print(find_max(numbers))
# print(sum_list(numbers))
# print(count_total_numbers(numbers))



#### Find Sum of n numbers using Recursion
# n = int(input("input: "))
# def sum_n(n):
#     if n == 1:
#         return 1
#     return n + sum_n(n-1)
# print(sum_n(n))


#### Find the sum of digits of a number recursively:
n = 1256
def fun_sum(n):
    if n // 10 == 0:
        return n
    return((n % 10) + fun_sum(n // 10))
print(fun_sum(n))