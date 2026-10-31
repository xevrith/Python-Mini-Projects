# Cafe Management System 

cafe = {
    "Coffee": 120.0,
    "Tea": 50.0,
    "Cappuccino": 180.0,
    "Latte": 200.0,
    "Espresso": 100.0,
    "Sandwich": 150.0,
    "Burger": 220.0,
    "Pizza": 300.0,
    "Pasta": 250.0,
    "Brownie": 130.0
}
count = 0

option = ["see","update","delete","exit","display","add"]
# ============================ FUNCTIONS ===========================
def display_menu():
    for item,price in cafe.items():
        print(f"{item} : {price}")

def options():
    print(f"1. Show Menu")
    print(f"2. Add Item")
    print(f"3. Delete Item")
    print(f"4. Update Price")
    print(f"5. Exit")


def add_item(item_name,price):
    if item_name not in cafe:
        cafe[item_name] = price
        print(f"Item Added Successfully")

    else:
        print("Item Already Exist")


def remove_item(item_name):
    if item_name in cafe:
        del cafe[item_name]
        print(f"{item_name} Removed Successfully")

    else:
        print(f"{item_name} not exists")


def update_price(item_name,new_price):
    if item_name in cafe:
        if new_price > 0:
            cafe[item_name] = new_price
            print(f"Price Updated Successfully")

        else:
            print(f"{new_price} is less then 0 try again")
    else:
        print("Item not exists")

# ================================ FUNCTIONS ENDS HERE ============================

# ==================================== LOOPS ========================================
while True:
    print()
    options()

    choice = input("Enter your Choice : ").lower().strip()
    
    if choice == "show":
        count += 1
        display_menu()

    elif choice == "add":
        new_item = input("Enter item name : ").title()
        try:
            item_price = float(input("Enter item Price : "))
            add_item(new_item,item_price)
            count += 1
        except ValueError:
            print(f"Wrong Value Try again")

    elif choice == "delete":
        remove_name = input("Enter name you wanna remove : ").title()
        remove_item(remove_name)
        count += 1

    elif choice == "update":
        item_name = input("Enter item name : ").title()
        try:
            item_price = float(input("Enter item Price : "))
            update_price(item_name,item_price)
            count += 1
        except ValueError:
            print(f"Wrong Value Try again")

    elif choice == "exit":
        print("Thanks for Using our services")
        print(f"{count} time you changed the main menu")
        break

    else:
        print(f"Wrong Choice, try again")

# =================================================================
