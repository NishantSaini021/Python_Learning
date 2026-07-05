###Tried to Handle Exception Without Try and Except Method but it cant handle all type of values
n = input("Give Input: ")
if n.isdigit():
    n = int(n)
    print(n**5)
else:
    print("Enter a Valid Number")




try:
    x = int(input("Enter a Number to Square: "))
    print(x**2)
except ValueError:
    print("Please Enter a Valid Number")

