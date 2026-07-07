# Read Q1(Nishant).txt
# Ask user for a word
# Print:
# Found
# or
# Not Found
x = input("Enter the word you want to find in the given text file: ")
f = open("Q1(Nishant).txt", "r")
c = f.read()
if x in c:
    print("Word Found")
else:
    print("Not Found")
f.close()