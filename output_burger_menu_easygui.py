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


easygui.msgbox(combo_menu)
