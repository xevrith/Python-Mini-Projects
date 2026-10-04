# Employee Banking System

balance = 10000.00
password = "9554@python"
attempts = 3


# Check User balance 
def check_balance():
    return balance

def deposite(amount):
    balance += amount
    return balance 

def withdrawl(amount):
    balance -= amount