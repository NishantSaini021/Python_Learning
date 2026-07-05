My_Self = { "Name" : "Nishant",
           "Age" : 20,
           "City": "Ajmer"
           }
My_Self["Surname"] = "Saini"
My_Self["Collge"] = "GEC Ajmer"
My_Self["Age"] = 21

# print(My_Self.get("Age"))
# print(My_Self)
# print(My_Self.keys())
# print(My_Self.values())
# print(My_Self.items())
# for key in My_Self:
#     print(key)
# for key , value in My_Self.items():
#     print(f"{key}: {value}")



#### Count Frequcny of Each Character in a String using Dictionary
s = input("Enter a String: ").strip().upper()
di = {}

for char in s:
    if char in di:
        di[char] += 1
    else:
        di[char] = 1


for char in s:
    di[char] = di.get(char , 0) + 1


print(di)



