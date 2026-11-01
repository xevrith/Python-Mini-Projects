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



order_detail = {}
order_detail2 = []

print("=" * 50)
print("             BURGER KING INVOICE")
print("=" * 50)


def show_menu():
    for food_item,detail in burger_king.items():
        print(f"\n{food_item} \nPrice : {detail[-1]} | Available : {detail[0]}")


def order(food_item,quantity):

    if food_item in burger_king:
        if quantity <= burger_king[food_item][0]:
            burger_king[food_item][0] -= quantity
            order_detail[food_item] = order_detail2.append(quantity,burger_king[food_item][-1] * quantity)
            order_detail[food_item] = order_detail2.append(burger_king[food_item][-1] * quantity)
        else:
            print(f"More then the quantity")
    else:
        print(f"{food_item} Not Available")


def remove_order(food_item):
    if food_item in order_detail:
        del order_detail[food_item]

    else:
        print(f"{food_item} Not found")


def change_quantity(food_item,new_quantity):
    if food_item in order_detail:
        if new_quantity <= burger_king[food_item][0]:
            order_detail[food_item] = order_detail2[0] = new_quantity
            print(f"Quantity Changed")

        else:
            print("Try Again, You enter quantity more then the available")
    else:
        print(f"{food_item} Not Found")


def invoice():
    if order_detail != None:
        sub_total = 0
        for food,food_detail in order_detail:
            sub_total += order_detail[food_detail][-1]
            print(f"{food}\t{food_detail[0]}t\{food_detail[-1]}")

        print(f"Subtotal\t\t{sub_total}")
        print(f"CGST @ 2.5%\t\t{sub_total*cgst}")
        print(f"SGST @ 2.5%\t\t{sub_total*sgst}")
        print(f"GRAND TOTAL\t\t{(sub_total*cgst)+(sub_total*sgst)+sub_total}")
        

