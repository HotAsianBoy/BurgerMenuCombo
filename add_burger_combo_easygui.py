"""Add Burger Combo Easygui
Added easygui to the finished code that allows the user to add a new
burger combo
"""
import easygui


# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'price': 6.69},
    'Cheesy':
        {'items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'price': 8.69},
    'Super':
        {'items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'price': 10.69}
}


# Allows the user to add a new combo wanted as well as asking if the new combo input has the correct info
def add_combo():
    name = easygui.enterbox("Hello! Please enter the name of the new combo: ")
    items = easygui.enterbox("Please enter the items in the combo, separated by commas (,): ").split(',')
    price = float(easygui.enterbox("Please enter the price of the new combo: "))
    combo_menu[name] = {'items': items, 'price': price}
    easygui.msgbox("New combo added!:", combo_menu[name])
    confirm = easygui.buttonbox(("Is this information correct? (yes/no): "), choices=['Yes', 'No'])
    if confirm.lower() == 'No':
        add_combo()


add_combo()
