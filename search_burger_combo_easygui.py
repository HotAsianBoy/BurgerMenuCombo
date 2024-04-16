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


# Allows the user to search for a combo already on the list
def search_combo():
    while True:  # Start of the loop
        name = easygui.enterbox("Hello! Please enter the name of the combo to search: ")
        combo_found = False

        for combo_name, combo_info in combo_menu.items():
            if name.lower() == combo_name.lower():
                combo_details = f"Items: {', '.join(combo_info['Items'])}\nPrice: ${combo_info['Price']}"
                easygui.msgbox(f"This combo was found! = \n{combo_name}\n{combo_details}")
                combo_found = True
                confirm = easygui.buttonbox("Is this information correct?", choices=['Yes', 'No'])
                if confirm == 'Yes':
                    return  # If information is correct, exit the function
                else:
                    break  # Breaks out of the for loop, goes back to start of while loop

        if not combo_found:
            easygui.msgbox("Sorry, this combo was not found. Please try again.")
            # Loop will continue, asking the question again


search_combo()
