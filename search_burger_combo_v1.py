"""Search Burger Combo v1
Allows the user to search for a existing burger combo
from the menu list"""


# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'items': ['Beef Burger', 'Fries', 'Fizzy Drink'], 'price': 6.69},
    'Cheesy':
        {'items': ['Cheese Burger', 'Fries', 'Fizzy Drink'], 'price': 8.69},
    'Super':
        {'items': ['Cheese Burger', 'Large Fries', 'Smoothie'], 'price': 10.69}
}


# Allows the user to search for a combo already from the list
def search_combo():
    name = input("Enter the name of the combo to search: ")
    for combo_name, combo_info in combo_menu.items():
        if name.lower() == combo_name.lower():
            found = True
            print("Combo found = ", {combo_name})
            for key, value in combo_info.items():
                print(f'{key}: {value}"')
        confirm = input("Is this information correct? (yes/no): ").lower()
        if confirm.lower() == 'no':
            update_combo(name)
            found = False
    else:
        print("Combo not found.")