# COFFEE ORDER SYSTEM
price = 0
size = input("Cup Size for your Coffee (Small,Medium,Large): ").strip().lower()
s = input("Want extra shot (Yes/No): ").strip().lower()

x = size

if x == "small":
    price = 3

elif x == "medium":
    price = 4

elif x == "large":
    price = 5

else:
    print("Please enter valid size")

if s == "yes":
    price += 1

elif s == "no":
     price = price

else:
    print("Please valid Input Yes or No")

print("Your Total for Coffee is $",price,"Thanks, Visit Again")