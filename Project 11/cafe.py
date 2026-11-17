# Cafe Management System

cafe = {
    "Coffee": 120.0, "Tea": 50.0, "Cappuccino": 180.0,
    "Latte": 200.0, "Espresso": 100.0, "Sandwich": 150.0,
    "Burger": 220.0, "Pizza": 300.0, "Pasta": 250.0, "Brownie": 130.0,
}


def display_menu():
    print("\n=== Cafe Menu ===")
    if not cafe:
        print("The menu is currently empty.")
    for item, price in cafe.items():
        print(f"{item}: ₹{price:.2f}")


def add_item(item_name, price):
    if not item_name:
        print("Item name cannot be empty.")
    elif item_name in cafe:
        print("Item already exists.")
    elif price <= 0:
        print("Price must be greater than zero.")
    else:
        cafe[item_name] = price
        print("Item added successfully.")


def remove_item(item_name):
    if item_name in cafe:
        del cafe[item_name]
        print(f"{item_name} removed successfully.")
    else:
        print("Item does not exist.")


def update_price(item_name, new_price):
    if item_name not in cafe:
        print("Item does not exist.")
    elif new_price <= 0:
        print("Price must be greater than zero.")
    else:
        cafe[item_name] = new_price
        print("Price updated successfully.")


def main():
    changes = 0
    while True:
        print("\n1. Show Menu")
        print("2. Add Item")
        print("3. Delete Item")
        print("4. Update Price")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_menu()
        elif choice == "2":
            name = input("Enter item name: ").strip().title()
            try:
                price = float(input("Enter item price: ₹"))
                before = len(cafe)
                add_item(name, price)
                if len(cafe) > before:
                    changes += 1
            except ValueError:
                print("Enter a valid numeric price.")
        elif choice == "3":
            name = input("Enter item name to delete: ").strip().title()
            if name in cafe:
                remove_item(name)
                changes += 1
            else:
                remove_item(name)
        elif choice == "4":
            name = input("Enter item name: ").strip().title()
            try:
                price = float(input("Enter new price: ₹"))
                old_price = cafe.get(name)
                update_price(name, price)
                if name in cafe and cafe[name] != old_price:
                    changes += 1
            except ValueError:
                print("Enter a valid numeric price.")
        elif choice == "5":
            print(f"Thank you. Menu changes made: {changes}")
            break
        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()
