# 4. Reverse a String
# Problem: Reverse a string using a loop.

Name = "nishant"
Reversed = ""
for i in range(6,-1,-1):
    Reversed += (Name[i])
print(Reversed)


#Taking Input String from user

s = input("Please Input a String to Reverse: ")
x = len(s)
y= x - 1           #last_index = len(s) - 1    #(y = index of last number)
Reversed_String = ""
for i in range(y,-1,-1):
     Reversed_String += (s[i])
print(Reversed_String)
