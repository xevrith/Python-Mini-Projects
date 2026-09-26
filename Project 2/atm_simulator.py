balance = 5000.00

while True:
    print("===ATM MENU===")
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Exit")

    options = int(input("Enter the opetions Given in the menu : "))

    if options == 1:
        print(f"Current Balance : {balance}")

    elif options == 2:
        deposite_amount = float(input("Enter the amount : "))

        if deposite_amount > 0:
            balance += deposite_amount
            print(f"Amount Deposited Successfully")

        else:
            print(f"Try again")

    elif options == 3:

        withdraw_amount = float(input("Enter the amount: "))

        if withdraw_amount > balance:
            print(f"Insufficient Balance")

        else:
            balance -= withdraw_amount
            print(f"Amount withdraw successfully")

    elif options == 4:
        print("Thanks for visiting our website")
        break

    else:
        print("Invalid Input Try again")