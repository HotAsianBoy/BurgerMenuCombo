"""Add Burger Combo v1
Allows the user to add new combos to the menu.
"""
# List of each combo meal and price for each, being a dictionary to store the combo meals with their details
combo_menu = {
    'Value': {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy': {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super': {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69}
}

# Allows the user to add a new combo
def add_combo():
    name = input("Enter the name of the new combo: ")
    items = input("Enter the items in the combo separated by commas: ").split(',')
    price = float(input("Enter the price of the combo: "))
    combo_menu[name] = {'items': items, 'price': price}
    print("New combo added:", combo_menu[name])
add_combo()

