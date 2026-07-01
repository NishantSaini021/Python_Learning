# x = int(input("Please enter a number: "))
# if x%2 == 0:
#     print(f"{x} is Even Number")
# else:
#     print(f"{x} is Odd Number")




# num1 = int(input("Enter 1st Number: "))
# num2 = int(input("Enter 2nd Number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num1} equals to {num2}")




# num = int(input("Please Enter your Number: "))
# if num < 0:
#     print(f"{num} is a Negative Number")
# elif num > 0:
#     print(f"{num} is a Positive Number")
# else:
#     print("Entered Number is Zero")





# age = int(input("Please Enter Your Age: "))
# if age < 0:
#     print("Please Enter Valid Age")
# elif age < 13:
#     print("Children")
# elif age < 20:
#     print("Teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior Citizen")




# age = int(input("Please Enter Your Age Before Buying a Ticket: "))
# p = 0
# if age < 0:
#     print("Please Enter Valid Age")
# elif age < 12:
#     p += 100
# elif age <60:
#     p += 200
# else:
#     p += 120

# Extra = (input("Is it Weekend ? (yes/no): ")).strip().lower()
# if Extra == "yes":
#     p += 50
# elif Extra != "no":
#     print("Please Enter Valid Input")


# print(f"Please Pay {p}INR at the Counter")




password = input("Please, Enter Password: ")

if len(password) < 6:
    print("Passwod is Weak")
elif len(password) < 11:
    print("Password is Medium")
else:
    print("Password is Storng")

for char in password:
    if char.isdigit():
        print("Contains Number: Yes")
        break
else:
    print("Contains Number: No")