"""
Mini Project: Banking Application
Task: Create a banking application class called Account that has the following features:

Properties:

account_no: The unique account number.
balance: The current balance of the account.
Methods:

debit(amount): Deducts the specified amount from the balance and prints a message indicating the transaction and the new balance. If the debit amount exceeds the balance, it should print an insufficient funds message.
credit(amount): Adds the specified amount to the balance and prints a message indicating the transaction and the new balance.
get_balance(): Returns the current balance and optionally prints a message showing the balance.
"""



class Account:
    def __init__(self,account_no,balance=0):
        self.account_no = account_no
        self.balance = balance

    def debit(self,amount):
        self.balance -= amount
        print(f"Your account has been debited by {amount}")
        print(f"Your current account balance is {self.balance}")

    def credit(self,amount):
        self.balance += amount
        print(f"Your account has been credited by {amount}")
        print(f"Your current account balance is {self.balance}")  

    def get_balance(self):
        print(f"Current Balance is {self.balance}")


a1 = Account(201,25000)
a2 = Account(202,15000)
a3 = Account(203,26000)

a3.get_balance()
