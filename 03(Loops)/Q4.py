# 4. Reverse a String
# Problem: Reverse a string using a loop.


## Using For Loop
Name = "nishant"
Reversed = ""
for i in range(6,-1,-1):
    Reversed += (Name[i])
print(Reversed)


# Taking Input String from user using For Loop

s = input("Please Input a String to Reverse: ")
x = len(s)
y= x - 1           #last_index = len(s) - 1    #(y = index of last number)
Reversed_String = ""
for i in range(y,-1,-1):
     Reversed_String += (s[i])
print(Reversed_String)


### Using While Loop Starting loop from end
s = input("Please Input a String to Reverse: ")
i = len(s) - 1
Reversed_String2 = ""
while i >= 0:
     Reversed_String2 += s[i]
     i -= 1
print(Reversed_String2)



### Using While Loop Starting from Beginning
s = input("Please Input a String to Reverse: ")
i = 0
Reversed_String3 = ""
while i < len(s):
     Reversed_String3 = s[i] + Reversed_String3
     i += 1
print(Reversed_String3)