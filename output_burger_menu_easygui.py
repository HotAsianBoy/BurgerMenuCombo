"""Output Burger Menu Easygui
Added Easygui into the finished printed burger menu
code which is used to be accessed easier for the user
"""
import easygui


# List of each combo meal and price for each, being a dictionary to store the combo meals with their details
combo_menu = {
    'Value': {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy': {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super': {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69}
}


# Allows the user to see the full menu list after editing or observing
def print_menu():
    easygui.msgbox("Full Combo Menu:")
    for name, details in combo_menu.items():
        items_str = ', '.join(details['Items'])
        easygui.msgbox(f"{name}: {items_str} - ${details['Price']}",
                title="Gideon's Burger Menu!")


print_menu()
