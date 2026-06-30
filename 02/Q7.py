# #
# Electricity Bill Calculator

# Problem Statement:

# Write a Python program to calculate the electricity bill based on the number of units consumed.

# Billing Rules:
# For the first 100 units, charge ₹5 per unit
# For the next 100 units (101–200), charge ₹8 per unit
# For units above 200, charge ₹10 per unit

# Additional Requirements:
# If the user enters 0 or a negative number, display: Invalid input
# Display the total electricity bill at the end.

units_consumed = int(input("Enter the number of units consumed: "))
bill_amount = 0
if units_consumed < 1:
    print("Invalid Input")
elif units_consumed < 101:
    bill_amount = (units_consumed)*5
    Category = "Low Consumption"
elif units_consumed < 201:
    bill_amount = (100*5)+(units_consumed-100)*8
    Category = "Moderate Consumption"
else:
    bill_amount =(100*5)+(100*8)+(units_consumed-200)*10
    Category = "High Consumption"
print(f"Total Electricty Bill is {bill_amount}INR")
print(Category)