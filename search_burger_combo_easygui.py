"""Search Burger Combo Easygui
Added easygui into the completed search burger
combo code, which allows the user to search for
an existing combo"""
import easygui


# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': ['Beef Burger', 'Fries', 'Fizzy Drink'], 'Price': 6.69},
    'Cheesy':
        {'Items': ['Cheese Burger', 'Fries', 'Fizzy Drink'], 'Price': 8.69},
    'Super':
        {'Items': ['Cheese Burger', 'Large Fries', 'Smoothie'], 'Price': 10.69},
}


# Allows the user to search for a combo already from the list
def search_combo():
    name = easygui.enterbox("Hello! Please enter the name of the combo to search: ")
    for combo_name, combo_info in combo_menu.items():
        if name.lower() == combo_name.lower():
            easygui.msgbox("This combo was found! = \n", {combo_name})
            for key, value in combo_info.items():
                easygui.msgbox(f'{key}: {value} "').upper()
            confirm = easygui.buttonbox(("Is this information "
                                        "correct? (Yes/No): "), choices=['Yes', 'No'])
            if confirm == 'No':
                search_combo()
    easygui.msgbox("Sorry, this combo was not found.")


search_combo()
