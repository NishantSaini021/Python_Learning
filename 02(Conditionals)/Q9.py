# Q9 - College Admission Eligibility Checker

# Problem Statement:
# Determine whether a student is eligible for admission.

# Take input:
# 1. Percentage
# 2. Entrance Exam Score

# Eligibility Rules:
# Percentage must be at least 60
# Entrance Exam Score must be at least 70

# If both conditions are satisfied:
#     Eligible for Admission

# Otherwise:
#     Not Eligible for Admission

# Bonus:
# If percentage >= 90 OR exam score >= 95
# Print:
#     Outstanding Candidate

name = input("Please Enter Your Name: ")
x = float(input("Please Enter Percentage Obtained in Senior Secondary: "))
if x < 0:
    print("Please Enter Valid Details")
    exit()
y = float(input("Please Enter Score Obtained in Entrance Exam: "))
if y < 0:
    print("Please Emter Valid Details")
    exit()

# Eligibility Check for Admission
eligible = True

# if x < 60:
#     print("Obtained Percenatage less than minimum required")
#     eligible = False
# if y < 70:
#     print("Obatined Score is Less than Minimum Required")
#     eligible = False

if x < 60 or y < 70:
    eligible = False

if eligible:
    if x >= 90 or y >= 95:
        print("Outstanding Candidate")
        print(f"{name}, You are Eligbile for Admission")
    else:
        print(f"{name}, You are Eligbile for Admission")
else :
    print(f"{name}, Sorry You are not eligible for Admission")