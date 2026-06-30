# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


s = (input("Please Provide an Input: ")).lower().strip()

for char in s:
    count = s.count(char)
    if count == 1:
        print(char)
        break