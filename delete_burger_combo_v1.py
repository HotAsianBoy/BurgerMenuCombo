"""Delete Burger Combo v1
Allows the user to delete a combo from the
menu if necessary
"""
# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy':
        {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super':
        {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69},
}


# Allows the user to delete a combo if necessary
def delete_combo():
    name = input("Enter the name of the combo to delete: ")
    if name in combo_menu:
        del combo_menu[name]
        print(f"{name} has been deleted from the menu.")
    else:
        print("Combo not found.")


delete_combo()