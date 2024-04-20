"""Delete Burger Combo Easygui
Added EasyGui into the finished code,
which improves the usability relevant
implication, as well as improving the
experience of the code for the user
"""
import easygui
# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy':
        {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super':
        {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69},
}


# Allows the user to delete a combo if necessary
def delete_combo():
    while True:
        name = easygui.enterbox("Hello! Please enter the name of the combo to delete: ")
        if name in combo_menu:
            del combo_menu[name]
            easygui.msgbox(f"Success! {name} has been deleted from the menu!")
        else:
            easygui.msgbox("Sorry, this combo was not found. Please try again.")


delete_combo()
