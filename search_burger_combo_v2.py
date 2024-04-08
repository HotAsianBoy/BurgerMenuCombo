"""Search Burger Combo v2
"""


# List of each combo meal and price for each
combo_menu = {
    'Combo 1 = Value':
        {'items': ['Beef Burger', 'Fries', 'Fizzy Drink'], 'price': 6.69},
    'Combo 2 = Cheesy':
        {'items': ['Cheese Burger', 'Fries', 'Fizzy Drink'], 'price': 8.69},
    'Combo 3 = Super':
        {'items': ['Cheese Burger', 'Large Fries', 'Smoothie'], 'price': 10.69}
}


def search_combo():
    combo_search = print("Please enter the name of the combo "
                         "you want to search for: ")

    found = False
    for combo_name, combo_info in combo_menu.items():
        if combo_search == combo_name:
            found = True
            print(f"\nCombo Name: {combo_name}", title="Combo Name")
            for key, value in combo_info.items():
                print(f"{key}: {value}", title="Menu Combo")
            break
    if not found:
        print("Combo not found in the Menu.", title="Error")
search_combo()