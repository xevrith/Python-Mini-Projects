# Expense Tracker
expenses = []


def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Edit Expense")
    print("5. Remove Expense")
    print("0. Exit")


def add_expense(name, amount, category):
    if not name or not category:
        print("Name and category cannot be empty.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n--- All Expenses ---")
    for index, item in enumerate(expenses, start=1):
        print(f"{index}. {item['name']} | {item['category']} | ₹{item['amount']:.2f}")


def show_summary():
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: ₹{total:.2f}")
    print(f"Number of expenses: {len(expenses)}")
    category_totals = {}
    for item in expenses:
        category = item["category"]
        category_totals[category] = category_totals.get(category, 0) + item["amount"]
    print("Category-wise totals:")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def edit_expense(index, field, new_value):
    if index < 1 or index > len(expenses):
        print("Invalid expense number.")
        return
    if field == "name" or field == "category":
        if not new_value.strip():
            print("Value cannot be empty.")
            return
        expenses[index - 1][field] = new_value.strip().title()
    elif field == "amount":
        try:
            amount = float(new_value)
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            expenses[index - 1][field] = amount
        except ValueError:
            print("Enter a valid amount.")
            return
    else:
        print("Choose name, amount, or category.")
        return
    print("Expense updated successfully.")


def remove_expense(index):
    if index < 1 or index > len(expenses):
        print("Invalid expense number.")
        return
    removed = expenses.pop(index - 1)
    print(f"{removed['name']} removed successfully.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Expense name: ").strip().title()
            category = input("Category: ").strip().title()
            try:
                amount = float(input("Amount: ₹"))
                add_expense(name, amount, category)
            except ValueError:
                print("Enter a valid numeric amount.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            view_expenses()
            try:
                index = int(input("Expense number to edit: "))
                field = input("Field (name/amount/category): ").strip().lower()
                value = input("New value: ").strip()
                edit_expense(index, field, value)
            except ValueError:
                print("Enter a valid expense number.")
        elif choice == "5":
            view_expenses()
            try:
                index = int(input("Expense number to remove: "))
                remove_expense(index)
            except ValueError:
                print("Enter a valid expense number.")
        elif choice == "0":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid choice. Select 0 to 5.")


if __name__ == "__main__":
    main()
