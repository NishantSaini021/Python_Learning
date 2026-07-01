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


########### Write a program that counts how many even numbers exist between two numbers.

# m = int(input("Enter Starting Number: "))
# n = int(input("Enter Final Number: "))
# y = 0
# for i in range(m,n+1):
#     if i % 2 == 0:
#         y += 1
# print(y)



########## Count How Many Digits are present in a String

# s = input("Please enter a String to Count number of Digits in it: ")
# count = 0
# for char in s:
#    if char.isdigit():
#     count += 1
# print(count)


############ Count Letters, Digits and Special Characters
# s = input("Please enter a String: ")
# letters = 0
# Numbers = 0
# Special = 0

# for char in s:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         Numbers += 1
#     else:
#         Special += 1

# print(f"{letters}Letters")
# print(f"{Numbers} Digits")
# print(f"{Special} Special Characters")




########## Check given string is a Palindrome ot not
# s = input("Please enter a String: ")
# y = len(s)-1
# reversed_s = ""
# for i in range(y,-1,-1):
#     reversed_s += s[i]
# if reversed_s == s:
#     print(f"{s} is a Palindrome")
# else:
#     print(f"{s} is not a Palindrome")




######### Count frequency of each character
s = input("Please enter a String: ").lower().strip()
seen = set()
for char in s:
    count = s.count(char)
    if char in seen:
        continue
    
    seen.add(char)
    print(f"{char}:{count}")
