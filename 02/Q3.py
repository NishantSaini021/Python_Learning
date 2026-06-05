# GRADE CALCULATOR FOR PCM/PCB

y = input("Write Yes if you have total marks available or No if subject wise marks available: ")

def grade(t):
    if t >= 90:
        print("Grade Obtained: A")

    elif t >= 80:
        print("Grade Obtained: B")

    elif t >= 70:
        print("Grade Obtained: C")

    elif t >= 60:
        print("Grade Obtained: D")

    else:
        print("Grade Obtained:n F")

if y.lower() == "yes":
    t = int(input("Please Enter total Marks Obtained out of 100: "))

    grade(t)
    

elif y.lower() == "no":
    a = int(input("Marks Obtained in Maths/Bio: "))
    b = int(input("Marks Obtained in Physcis: "))
    c = int(input("Marks Obtained in Chemistry: "))
    d = int(input("Marks Obtained in Hindi: "))
    e = int(input("Marks Obtained in English: "))

    t = round((a+b+c+d+e)/5)

    grade(t)
    print("Average Marks:",t)
