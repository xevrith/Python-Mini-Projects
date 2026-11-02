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
    "Ice Cream": [2, 79.0]
}

cgst = 0.025
sgst = 0.025



cart = {}
order_details = []



def show_menu():

    for food_item,detail in burger_king.items():
        print(f"\n{food_item} \nPrice : {detail[-1]} | Available : {detail[0]}")


def orders(food_name,qty=1):

    if food_name in burger_king:
        if qty <= burger_king[food_name][0]:
            item_total = burger_king[food_name][-1] * qty
            order_details.append(qty)
            order_details.append(item_total)
            cart[food_name] = order_details
            burger_king[food_name][0] - qty
            print(f"{food_name} Added in the cart Successfully")

        else:
            print("Quantity Not available")
    else:
        print(f"{food_name} not Found")


def remove_item(food_name):
    if food_name in burger_king:
        cart.pop(food_name)
        print(f"{food_name} Removed from cart")

    else:
        print(f"{food_name} Not found")


def update_cart(food_name,qty):
    if food_name in cart:
        if qty <= burger_king[food_name][0]:
            cart[food_name][0] = qty
            cart[food_name][-1] = burger_king[food_name][-1] * qty
            print(f"Quantity Updated")        

        else:
            print(f"Quantity Not available")
    else:
        print(f"{food_name} not found")


    
print("=" * 50)
print("             BURGER KING INVOICE")
print("=" * 50)

orders("Whopper Burger",1)
orders("Veg Burger",1)
print(cart)
remove_item("Veg Burger")
print(cart)
update_cart("Whopper Burger",2)
print(cart)