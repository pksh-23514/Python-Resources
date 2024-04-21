# Write a program to create a Bank Account Class that has two attributes: (owner and balance) and two methods: (deposit and withdraw).
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate the Class, make several deposits and withdrawals and test to make sure the account can't be overdrawn.
# I/P: print(acct1)
# O/P: Account owner:   Jose
#      Account balance: $100
# I/P: acct1.owner
# O/P: Jose
# I/P: acct1.balance
# O/P: 100
# I/P: acct1.deposit(50)
# O/P: Deposit Accepted.
# I/P: acct1.withdraw(75)
# O/P: Withdrawal Accepted.
# I/P: acct1.withdraw(500)
# O/P: Funds Unavailable!

"""
**************************************************************
**************************************************************
"""

class Account:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit (self, amount):
        self.balance = self.balance + amount
        print ("Deposit Accepted.")
    def withdraw (self, amount):
        if (self.balance < amount):
            print ("Funds Unavailable!")
        else:
            self.balance = self.balance - amount
            print ("Withdrawal Accepted.")
    def __str__ (self):
        return (f"Account owner:   {self.owner}\nAccount balance: ${self.balance}")

acct1 = Account ("Jose", 100)
print (acct1)
acct1.deposit (50)
acct1.withdraw (75)
print (acct1)
acct1.withdraw (500)
print (f"Account owner:   {acct1.owner}")
print (f"Account balance: ${acct1.balance}")
