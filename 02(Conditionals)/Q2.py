# MOVIE TICKET PRICING and SPECIAL DAY DISCOUNT(WEDNESDAY)

x = int(input("Please Enter Your Age: "))
day = input("Enter Day: ")
valid_days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

if day.lower() not in valid_days:
    print("Please enter a valid day")
else: 
    if x < 18:
        ticket = 8
    else:
        ticket = 12

    if day.lower() == "wednesday":
        ticket -= 2

    print("Please Pay $", ticket, "at counter")