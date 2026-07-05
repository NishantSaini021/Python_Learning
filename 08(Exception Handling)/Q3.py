# Keep Asking Until Valid Integer
# Problem:
# Keep asking the user for an integer
# until they enter a valid one.

while True:
    try:
         x = int(input("Please Enter a Interger: "))
         print("Valid Input")
         break
    except ValueError:
        print("Please Enter a Valid Number")
    