"""Add Burger Combo v1
Allows the user to add new combos to the menu.
"""


# Allows the user to add a new combo
def add_combo():
    name = input("Enter the name of the new combo: ")
    items = input("Enter the items in the combo separated by commas: ").split(',')
    price = float(input("Enter the price of the combo: "))
    combo_meals[name] = {'items': items, 'price': price}
    print("New combo added:", combo_meals[name])

