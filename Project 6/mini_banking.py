# Banking System

balance = 10000.00
user = "admin"
password = "9554@python"
attempts = 3

# ====================================== 
# Check User balance 
def check_balance():
    print(f"Current Balance : {balance}")

# Deposite the amount
def deposite(amount):

    if amount > 0:
        balance += amount
        return balance

    else:
        print("Negative Input, Try Again")

# Withdraw Amount
def withdraw(amount):

    if amount < balance:
        balance -= amount
        return balance

    else:
        print("Insufficient Balance")

def options():
    print("Access Granted")
    print()
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Exit")
# ==========================================



print("=== Banking System ===")
username = input("Enter username : ")

if username == user:
    while attempts != 0:

        user_password = input("Enter the password : ")
        if user_password == password:
            options()

            while True:
                try:
                    choice = int(input("Enter Your Choice (Press 4 to exit): "))

                    if choice == 1:
                        check_balance()

                    elif choice == 2:
                        try: 
                            deposite_amount = float(input("Enter the amount : "))
                            deposite(deposite_amount)
                            print(f"Amount Added Successfully")
                            check_balance()
                        except ValueError:
                            print("Wrong input  ")

                    elif choice == 3:
                        try:
                            withdraw_amount = float(input("Enter the amount"))
                            withdraw(withdraw_amount)
                            print("Amount Withdraw Successfully")
                            check_balance()
                        except ValueError:
                            print("Wrong Input")

                    elif choice == 4:
                        print("Thanks for visiting")
                        break

                    else:
                        print("Wrong Number, Try Again")
                except ValueError:
                    print("Enter the number only")

        else:
            print("Wrong Password")
        attempts -= 1
        print(f"Wrong Password : Attempts Left : {attempts}")

else:
    print("Wrong Username")







