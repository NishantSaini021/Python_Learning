# Read Q1(Nishant).txt
# Print total number of words

f = open("Q1(Nishant).txt", "r")
content = f.read().split()
print(len(content))
f.close()