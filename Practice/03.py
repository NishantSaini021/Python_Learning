############ Printing Numbers From 1 to 10
# for x in range(1, 11):
#     print(x)


############ Printing Sum of Numbers
# x = int(input("Please Give Input: "))
# y = 0
# for i in range(1, x+1):
#     y = y+i
# print(y)


############ Multiplication Table
# x = int(input("Please Enter A Number for which you want table: "))
# for i in range(1,11):
#     print(x*i)


# Write a program that counts how many even numbers exist between two numbers.

m = int(input("Enter Starting Number: "))
n = int(input("Enter Final Number: "))
y = 0
for i in range(m,n+1):
    if i % 2 == 0:
        y += 1
print(y)
