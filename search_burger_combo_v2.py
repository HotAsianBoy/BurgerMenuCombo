"""Search Burger Combo v2
Fixed error of search burger combo v1 combo not showing
up
"""


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
            print("Combo found = ", {combo_name})
            for key, value in combo_info.items():
                print(f'{key}: {value} "')
            confirm = input("Is this information correct? (yes/no): ").lower()
            if confirm.lower() == 'no':
                search_combo()
    print("Combo not found.")

search_combo()
