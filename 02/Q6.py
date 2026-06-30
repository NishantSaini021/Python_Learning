# ATM WITHDRAWAL SIMULATION

balance = int(input("Enter your current balance: "))
withdrawal_amount = int(input("Enter the amount you want to withdraw: "))



if withdrawal_amount > balance:
    print("Insufficient funds. Withdrawal denied.")
elif withdrawal_amount <= 0:
    print("Invalid withdrawal amount. Please enter a valid amount.")
elif withdrawal_amount % 100 != 0:
    print("Invalid withdrawal amount. Please enter a multiple of 100.")
else:
    balance -= withdrawal_amount
    print("Withdrawal successful. Remaining balance: ", balance)
