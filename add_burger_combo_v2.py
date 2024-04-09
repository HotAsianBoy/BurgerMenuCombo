"""Add Burger Combo v2
Edited the code, adding the option to check if the information added is correct
before added the new combo to the menu, using more formal language and being more
welcoming and inclusive to allow the user to feel more relaxed
if they have never used code before
"""
# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy':
        {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super':
        {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69}
}

# Allows the user to add a new combo wanted as well as asking if the new combo input has the correct info
def add_combo():
    name = input("Hello! Please enter the name of the new combo: ")
    items = input("Please enter the items in the combo, separated by commas (,): ").split(',')
    price = float(input("Please enter the price of the new combo: "))
    combo_menu[name] = {'items': items, 'price': price}
    print("New combo added!:", combo_menu[name])
    confirm = input("Is this information correct? (yes/no): ").upper()
    if confirm.lower() == 'no':
        add_combo()
add_combo()