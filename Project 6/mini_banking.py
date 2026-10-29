import os
from getpass import getpass


def check_balance(balance):
    print(f"Current Balance: ₹{balance:,.2f}")


def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance

    balance += amount
    print("Deposit successful.")
    check_balance(balance)
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance

    else:
        print("Negative Input, Try Again")

# Withdraw Amount
def withdraw(amount):

    if amount < balance:
        balance -= amount
        return balance

    balance -= amount
    print("Withdrawal successful.")
    check_balance(balance)
    return balance


def authenticate(username, password, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        entered_username = input("Enter username: ")
        entered_password = getpass("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Access granted.\n")
            return True

        remaining = max_attempts - attempt
        print(f"Invalid username or password. Attempts left: {remaining}")

    print("Too many failed attempts. Exiting.")
    return False


def banking_menu(balance):
    while True:
        print("\n=== Banking Menu ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            check_balance(balance)

        elif choice == 2:
            try:
                amount = float(input("Enter deposit amount: "))
                balance = deposit(balance, amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == 3:
            try:
                amount = float(input("Enter withdrawal amount: "))
                balance = withdraw(balance, amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == 4:
            print("Thank you for visiting.")
            return balance

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


def main():
    # Keep the password out of the public source code.
    username = os.getenv("BANKING_USERNAME", "admin")
    password = os.getenv("BANKING_PASSWORD")

    if not password:
        print("BANKING_PASSWORD is not set.")
        print("Set it in your terminal before running this practice project.")
        print('PowerShell example: $env:BANKING_PASSWORD = "your-demo-password"')
        return

    print("=== Banking System ===")
    if authenticate(username, password):
        banking_menu(10000.00)


if __name__ == "__main__":
    main()
