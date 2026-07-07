# Problem
# Read:
# Q1(Nishant).txt
# and copy all its content into:
# backup.txt

f1 = open("Q1(Nishant).txt", "r")
f2 = open("Q8(Backup).txt", "w")
c = f1.read()
f2.write(c)
f1.close()
f2.close()