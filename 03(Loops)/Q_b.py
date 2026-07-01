# Q2 - Password Checker
# Problem Statement:
# Keep asking the user to enter a password
# until they enter:
#     python123

# Rules:
# - If the password is incorrect:
#       Incorrect Password
#
# - If the password is correct:
#       Access Granted
#
# - Stop the program after the correct password.



s = input("Please Enter password: ")
count = 4
while s != "python123" and count > 0 :
    s = input(f"wrong Password {count} Attempts Left, try again: ")
    count -= 1
if s == "python123":
    print("Access Granted")
else:
    print("Access Denied")

