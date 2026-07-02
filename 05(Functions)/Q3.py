# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

a = (input("Enter 1st Input: "))
b = (input("Enter 2nd Input: "))

def multiply(a,b):
     if a.isdigit() == False and b.isdigit() == False:
        return("Two Strings Cant be Multiplied")
     else:
        if a.isdigit():
            a = int(a)
        if b.isdigit():
            b = int(b)
     return(a*b)

print(multiply(a,b))