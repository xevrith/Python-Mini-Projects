# Expense Tracker
expense = []



# =============================== Functions
# Show the Options
def menu():
    print("=== Expense Tracker ===")
    print()
    print("1. Add Expense")
    print("2. View All Expenses")
    print("2. View Summary")

def menu2():
    print("1. Remove Expense")
    print("2. Change Expense")

def menu3():
    print("1. Change Name")
    print("2. Change Amount")
    print("3. Change Category")

# Add Expense details in the data structure
def add_data(exp_name, exp_amount, exp_category):
    exp_details = {}
    exp_details[exp_name] = {"Amount" : exp_amount,"Category":exp_category}
    expense.append(exp_details)

def remove_data(exp_name):
    if exp_name in expense:
        expense.remove(expense)
        print(f"{exp_name} Removed Successfully")

    else:
        print("Not exists")
# ====================================================


while True:
    menu()

    try:
        print("Type 0 to stop the loop")
        choice = int(input("Enter Your Choice : "))
        
        if choice == 1:
            while True:
                try:
                    name = input("Enter the Name : ").title().strip()
                    amount = float(input("Enter the amount : "))
                    category = input("Enter the Category : ").title().strip()
                    if isinstance(amount,float):
                        add_data(name, amount, category)
                        print("Your Expense Added Successfully")
                        for i in expense:
                            print(i)  

                        choice2 = input("Do you want to change anything ? ('Yes' or 'No')").lower()
                        if choice2 == "yes":
                            menu2()
                            try:
                                choice3 = int(input("Enter Your Choice : "))
                                if choice3 == 1:
                                    remove_item = input("Enter the Item : ").title().strip()
                                    remove_data(remove_item)
                                elif choice3 == 2:
                                    choice4 = input("Enter What you want to change : ")
                            except ValueError:
                                print("Wrong Input")
                            
                        elif choice2 == "no":
                            print("Okay")
                            break
                        else:
                            print("Wrong Input Try Again")        
                except ValueError:
                    print("Check the Value, Try Again")

        elif choice == 2:
            pass 

        elif choice == 3:
            pass

        elif choice == 0:
            print(f"Thanks For Using our service")
            break

        else:
            print(f"Wrong Option : Try Again")






    except ValueError:
        print("Wrong Value Check Again")