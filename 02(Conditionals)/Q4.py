# BANANA RIPENESS CHECK FROM USER INPUT
userinput = input("Please enter color of the Banana\neg. Green, Yellow, Brown: ").strip().upper()
x = userinput
if x == "GREEN":
    print("Banana is Unripe")

elif x == "YELLOW":
    print("Banana is Ripe")

elif x == "BROWN":
    print("Banana is overripe")

else:
    print("Please Eat another fruit 😅🤢😷")