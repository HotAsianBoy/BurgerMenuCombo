"""Add Burger Combo Easygui
Added easygui to the finished code that allows the user to add a new
burger combo
"""
import easygui


# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy':
        {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super':
        {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69}
}


# Allows the user to add a new combo wanted as well
# as asking if the new combo input has the correct info
def add_combo():
    while True:
        name = easygui.enterbox("Hello! Please enter the name of the new combo: ")
        items = easygui.enterbox("Please enter the items in "
                                 "the combo, separated by commas (,): ").split(',')
        price = float(easygui.enterbox("Please enter the price of the new combo ($): "))
        combo_menu[name] = easygui.msgbox(f"{name} = {items}, = {price}")
        easygui.msgbox("New combo added!:", combo_menu[name])
        confirm = easygui.buttonbox("Is this information "
                                    "correct? (yes/no): ", choices=['Yes', 'No'])
        if confirm.lower() == 'yes':
            easygui.msgbox("New Combo Saved!:", combo_menu[name])
        elif confirm.lower() == "no":
            add_combo()
        else:
            easygui.msgbox("Invalid Output. Please try again.")


add_combo()
