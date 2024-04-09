"""Search Burger Combo v1
Allows the user to search for a existing burger combo
from the menu list"""


# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': ['Beef Burger', 'Fries', 'Fizzy Drink'], 'Price': 6.69},
    'Cheesy':
        {'Items': ['Cheese Burger', 'Fries', 'Fizzy Drink'], 'Price': 8.69},
    'Super':
        {'Items': ['Cheese Burger', 'Large Fries', 'Smoothie'], 'Price': 10.69}
}


# Allows the user to search for a combo already from the list
def search_combo():
    name = input("Enter the name of the combo to search: ")
    for combo_name, combo_info in combo_menu.items():
        if name.lower() == combo_name.lower():
            found = True
            print("Combo found = ", {combo_name})
            for key, value in combo_info.items():
                print(f'{key}: {value} "')
        confirm = input("Is this information correct? (yes/no): ").lower()
        if confirm.lower() == 'no':
            update_combo(name)
            found = False
    else:
        print("Combo not found.")

search_combo()