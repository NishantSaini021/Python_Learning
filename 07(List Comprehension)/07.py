nums = [num for num in range(1,6)]
# print(nums)

sqrs = [num*num for num in range(1,101)]
# print(sqrs)

evens = [i for i in range(1,11) if i%2 == 0]
# print(evens)

cubes = [i**3
for i in range(1,11)]
# print(cubes)


# s = input("Enter a String: ")
# ls = [char.upper() for char in s]
# print(ls)


s = input("Enter a Sting with Numbers: ")
ls = [char for char in s if char.isalpha() ]
ds = [char for char in s if char.isdigit()]
print(f"Letters: {ls}\n Digits: {ds}")