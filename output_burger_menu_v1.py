"""Output Burger Menu v2
Prints out the finished burger menu after changes made
or left by the user
"""

# List of each combo meal and price for each, being a dictionary to store the combo meals with their details
combo_menu = {
    'Value': {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy': {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super': {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69}
}

# Allows the user to see the full menu list after editing or observing
def print_menu():
    print("Full Combo Menu:")
    for name, details in combo_menu.items():
        items_str = ', '.join(details['Items'])
        print(f"{name}: {items_str} - ${details['Price']}")


print_menu()