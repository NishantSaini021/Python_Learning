# Q8 - Bank Loan Eligibility Checker

# Problem Statement:
# Write a Python program to determine whether a person is eligible for a bank loan.

# Take the following inputs from the user:
# 1. Age
# 2. Monthly Income
# 3. Credit Score

# Eligibility Criteria:
# - Age must be at least 18 years.
# - Monthly Income must be at least ₹25,000.
# - Credit Score must be at least 650.

# Output:
# If all conditions are satisfied:
#     Eligible for Loan
#
# Otherwise:
#     Not Eligible for Loan

# Bonus Challenge:
# Also tell the user why they are not eligible.

age = int(input("Please Enter Your Age: "))
if age < 0:
    print("Please Enter a Valid Age")
    exit()
income = float(input("Please Enter Your Monthly Income: "))
if income < 0:
    print("Please Enter a Valid Income")
    exit()
score = int(input("Pleasec Enter your Civil Score: "))
if score < 0:
    print("Please Enter a Valid Civil Core")
    exit()
#Eligibility Check:
eligible = True
if age < 18:
    print("Ineligible because youe age is less than Minimum Age Requiremenmt")
    eligible = False
if income < 25000:
    print("Ineligible because your income is less than minimum requiremenmt")
    eligible = False
if score < 650:
    print("Ineligible because your Civil Score is less than minimum requiremenmt")
    eligible = False
if eligible:
    print("Congratulations you are Eligible for Loan")
else:
    print("Not Eligible for Loan")