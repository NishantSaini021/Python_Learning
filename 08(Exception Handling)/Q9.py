# Ask for a password.
# Keep asking until the correct password is entered.
#
# Correct password: python123
#
# If user enters an empty password,
# raise an error message.
while True:
    try:
        x = input("Enter Password to Access: ")
        if x == "":
            raise ValueError() #With raise we can create a exception
        if x == "python123":
            print("Access Granted")
            break
        else:
            print("Wrong Password")
    except ValueError:
        print("Password Cant be Empty")
