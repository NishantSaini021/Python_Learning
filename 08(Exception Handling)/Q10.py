# ATM Withdrawal System
#
# Starting Balance = 10000
#
# Ask user for withdrawal amount.
#
# Rules:
# 1. Amount must be a number.
# 2. Amount must be greater than 0.
# 3. Amount must not exceed balance.
# 4. If everything is valid:
#       print remaining balance.
#
# Use:
# - try
# - except
# - else
# - finally
# - raise


try:
    w = False
    s = 10000
    x = int(input("Please, Enter Amount to Withdraw: "))
    if x < 1:
        raise ValueError("Invalid Amount, Withdrawal Rejected")
    elif x % 100 != 0:
        raise ValueError("Amount Not in Multiples of Hundred, Withdrawal Rejected")
    elif x > s:
        raise ValueError("Low Balance, Withdrawal Rejected")
    else:
        print("Withdrawal Successfull")
        w = True
    
except ValueError as e:
    print(e)
except ValueError:
    print("Invalid")
finally:
    if w:
        print(f"Available Balance: {s - x}")
    if not w:
        print(f"Available Balance: {s}")