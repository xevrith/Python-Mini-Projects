# Burger King Invoice Generator

burger_king = {
    "Whopper Burger": [2, 199.0],
    "French Fries": [1, 99.0],
    "Cold Coffee": [2, 120.0],
    "Chicken Nuggets": [1, 149.0],
    "Veg Burger": [2, 129.0],
    "Coke": [3, 60.0],
    "Chicken Burger": [1, 179.0],
    "Onion Rings": [2, 89.0],
    "Brownie": [1, 99.0],
    "Ice Cream": [2, 79.0],
}

CGST_RATE = 0.025
SGST_RATE = 0.025
cart = {}


def show_menu():
    print("\n" + "=" * 55)
    print("BURGER KING MENU")
    print("=" * 55)
    for item, (stock, price) in burger_king.items():
        print(f"{item:<22} ₹{price:>7.2f} | Available: {stock}")


def add_item(item_name, quantity):
    if item_name not in burger_king:
        print("Item not found.")
        return
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    available, price = burger_king[item_name]
    already_ordered = cart.get(item_name, 0)
    additional_available = available - already_ordered

    if quantity > additional_available:
        print(f"Only {additional_available} more unit(s) available.")
        return

    cart[item_name] = already_ordered + quantity
    print(f"{quantity} x {item_name} added to cart.")


def remove_item(item_name):
    if item_name in cart:
        del cart[item_name]
        print(f"{item_name} removed from cart.")
    else:
        print("Item is not in your cart.")


def update_quantity(item_name, quantity):
    if item_name not in cart:
        print("Item is not in your cart.")
        return
    if quantity <= 0:
        print("Use Remove Item to delete an item from the cart.")
        return

    available, _ = burger_king[item_name]
    if quantity > available:
        print(f"Only {available} unit(s) available.")
        return

    cart[item_name] = quantity
    print(f"{item_name} quantity updated.")


def display_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n" + "-" * 55)
    print(f"{'Item':<22}{'Qty':>6}{'Price':>12}{'Total':>12}")
    print("-" * 55)
    for item, quantity in cart.items():
        price = burger_king[item][1]
        print(f"{item:<22}{quantity:>6}{price:>12.2f}{price * quantity:>12.2f}")


def generate_invoice():
    if not cart:
        print("Your cart is empty. Add items first.")
        return

    subtotal = sum(burger_king[item][1] * qty for item, qty in cart.items())
    cgst = subtotal * CGST_RATE
    sgst = subtotal * SGST_RATE
    total = subtotal + cgst + sgst

    print("\n" + "=" * 55)
    print("                 BURGER KING INVOICE")
    print("=" * 55)
    for item, quantity in cart.items():
        price = burger_king[item][1]
        print(f"{item:<25} {quantity:>3} x ₹{price:>7.2f} = ₹{price * quantity:>8.2f}")
    print("-" * 55)
    print(f"{'Subtotal':<38} ₹{subtotal:>10.2f}")
    print(f"{'CGST (2.5%)':<38} ₹{cgst:>10.2f}")
    print(f"{'SGST (2.5%)':<38} ₹{sgst:>10.2f}")
    print("-" * 55)
    print(f"{'Grand Total':<38} ₹{total:>10.2f}")
    print("=" * 55)


def main():
    while True:
        print("\n1. Show Menu")
        print("2. Add Item")
        print("3. Update Cart Quantity")
        print("4. Remove Item")
        print("5. View Cart")
        print("6. Generate Invoice")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_menu()
        elif choice == "2":
            show_menu()
            name = input("Enter item name: ").strip().title()
            try:
                quantity = int(input("Enter quantity: "))
                add_item(name, quantity)
            except ValueError:
                print("Quantity must be a whole number.")
        elif choice == "3":
            name = input("Enter item name: ").strip().title()
            try:
                quantity = int(input("Enter new quantity: "))
                update_quantity(name, quantity)
            except ValueError:
                print("Quantity must be a whole number.")
        elif choice == "4":
            name = input("Enter item name: ").strip().title()
            remove_item(name)
        elif choice == "5":
            display_cart()
        elif choice == "6":
            generate_invoice()
        elif choice == "7":
            print("Thank you for visiting Burger King.")
            break
        else:
            print("Invalid choice. Select 1 to 7.")


if __name__ == "__main__":
    main()
