# Exercise: BankAccount Encapsulation
# Create a class BankAccount
# Requirements:
# 1. Constructor should accept balance
# 2. Store balance in a private attribute:
#       self.__balance
#
# 3. Create a getter:
#       get_balance()
#    It should return the balance
#
# 4. Create a setter:
#       set_balance(balance)
#
# 5. Validation Rule:
#       Only update balance if balance >= 0
#       Otherwise do nothing
#
# 6. Create an object:
#       acc = BankAccount(1000)
#
# 7. Try:
#       acc.set_balance(-500)
#
# 8. Print the balance using:
#       print(acc.get_balance())


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return(self.__balance)
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        
acc = BankAccount(1000)
acc.set_balance(-500)
# print(acc.get_balance())


# Exercise: Improve BankAccount

# Modify the constructor so that:
#
# If balance >= 0
#     store the balance
#
# Otherwise
#     store 0
#
# Test:
#
# acc1 = BankAccount(1000)
# print(acc1.get_balance())
#
# acc2 = BankAccount(-500)
# print(acc2.get_balance())

class BankAccount:
    def __init__(self,balance):
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
    def get_balance(self):
        return(self.__balance)
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        
acc1 = BankAccount(1000)
acc2 = BankAccount(-100)
acc1.set_balance(-500)
print(acc1.get_balance())
print(acc2.get_balance())