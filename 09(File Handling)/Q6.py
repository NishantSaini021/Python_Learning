# Read Q1(Nishant).txt
# Print total number of lines

f = open("Q1(Nishant).txt", "r")
content = f.read().splitlines()
print(len(content))
f.close()