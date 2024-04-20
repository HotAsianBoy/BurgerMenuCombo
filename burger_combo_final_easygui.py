"""Burger Combo FINAL Easygui
Finished code with easygui
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


# Allows the user to add a new combo wanted as well
# as asking if the new combo input has the correct info
def add_combo():
    while True:
        name = easygui.enterbox("Hello! Please enter the name of the new combo: ",
                                title="Gideon's Burgers!")
        items = easygui.enterbox("Please enter the items in "
                                 "the combo, separated by commas (,): ",
                                 title="Gideon's Burgers!").split(',')
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
        break


# Allows the user to search for a combo already on the list
def search_combo():
    while True:  # Start of the loop
        name = easygui.enterbox("Hello! Please enter the name of the "
                                "combo to search: ",
                                title="Gideon's Burgers!")
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


# Allows the user to delete a combo if necessary
def delete_combo():
    name = easygui.enterbox("Hello! Please enter "
                            "the name of the combo to delete: ",
                            title="Gideon's Burgers!")
    if name in combo_menu:
        del combo_menu[name]
        easygui.msgbox(f"Success! {name} has been deleted from the menu!")
    else:
        easygui.msgbox("Sorry, this combo was not found.")


# Allows the user to see the full menu list after editing or observing
def print_menu():
    easygui.msgbox("Full Combo Menu:")
    for name, details in combo_menu.items():
        items_str = ', '.join(details['Items'])
        easygui.msgbox(f"{name}: {items_str} - ${details['Price']}",
                       title="Gideon's Burger Menu!")


while True:
    choice = easygui.buttonbox("***Welcome to Gideon's Burgers!***\n "
                               "How Can I Help You?",
                               choices=["Add Combo", "Search Combo", "Delete Combo",
                                        "Print Menu", "Exit"],
                               title="Gideon's Burgers!")

    if choice == "Add Combo":
        add_combo()
    elif choice == "Search Combo":
        search_combo()
    elif choice == "Delete Combo":
        delete_combo()
    elif choice == "Print Menu":
        print_menu()
    elif choice == "Exit":
        easygui.msgbox("Thank you and farewell! Exiting program.",
                       title="Gideon's Burgers!")
        break
