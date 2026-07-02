# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

### Using For Loop
s = (input("Please Provide an Input: ")).lower().strip()

for char in s:
    count = s.count(char)
    if count == 1:
        print(char)
        break

### Using While Loop
s = (input("Please Provide an Input: ")).lower().strip()
i = 0
while i < len(s):
    count = s.count(s[i])
    if count == 1:
        print(s[i])
        break
    i += 1