# # Handle Missing File
# Ask the user for a filename.
# Try to read it.
# If the file does not exist.
# File Not Found
# instead of crashing.

name = input("Enter the name of file you want read: ")
try:
    f = open(name, "r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("FILE NOT FOUND")
