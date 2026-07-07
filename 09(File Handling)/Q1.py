# Ask the user for their name.
# Save it in a file called:
# name.txt

name = input("Enter Your Name: ")
file = open(f"Q1({name}).txt", "w")
file.write(f"Hello {name}\n")
file.write("File Handling with Python")
file.close()