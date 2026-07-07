# 1. Ask user for a name.
# 2. Open Q1(Nishant).txt in append mode.
# 3. Add:
#    Welcome <name>
# 4. Close file.

Name = input("Enter Your Name: ")
f = open("Q1(Nishant).txt", "a")
f.write(f"\nWelcome {Name}")
f.close()
