# Ask user for:
# Name
# Marks
#
# Save them in students.txt
#
# Example:
# Nishant - 85
# Student2 - 90
#
# Every new entry should be appended.
#
# Handle invalid marks using try/except.

n = input("Enter the name of student: ")
try:
    m = int(input("Enter the marks scored: "))
    f = open("students.txt", "a")
    f.write(f"{n}: {m}\n")
except ValueError:
    print("Enter valid Marks")
f.close()