# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]



# using for loop 
items = ["apple", "banana", "orange", "apple", "mango"]
seen = set()
Duplicate = False
for item in items:
    if item in seen:
        Duplicate = True
        break
    seen.add(item)
if Duplicate:
    print(item)
else:
    print("No Duplicate Found")



# Using while loop
