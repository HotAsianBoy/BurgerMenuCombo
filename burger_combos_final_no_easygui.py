"""Burger Combos FINAL
Completed code without Easygui, using definitive list and functions
as well as while loops, however loop only ends when user decides to
exit the program"""
# List of each combo meal and price for each
combo_menu = {
    'Value':
        {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy':
        {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super':
        {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69},
}


# Allows the user to add combo wanted as well as asking if the new combo
# input has the correct info
def add_combo():
    name = input("Hello! Please enter the name of the new combo: ")
    items = input("Please enter the items in the combo, separated "
                  "by commas (,): ").split(',')
    price = float(input("Please enter the price of the new combo ($): "))
    combo_menu[name] = input(f"{name} = {items}, = {price}")
    print("New combo added!:", combo_menu[name])
    confirm = input("Is this information correct? (yes/no): ").lower()
    if confirm.lower() == 'no':
        add_combo()


# Allows the user to search for a combo already from the list
def search_combo():
    name = input("Enter the name of the combo to search: ")
    for combo_name, combo_info in combo_menu.items():
        if name.lower() == combo_name.lower():
            print("Combo found = ", {combo_name})
            for key, value in combo_info.items():
                print(f'{key}: {value}"')
            confirm = input("Is this information correct? (yes/no): ").lower()
            if confirm.lower() == 'no':
                update_combo(name)
    print("Combo not found.")


# Updates the list and adds the new combo from the user
def update_combo(name):
    items = input("Enter the new items for the combo separated "
                  "by commas: ").split(',')
    price = float(input("Enter the new price for the combo: "))
    combo_menu[name] = {'items': items, 'price': price}
    print("Combo updated:", combo_menu[name])


# Allows the user to delete a combo if necessary
def delete_combo():
    name = input("Enter the name of the combo to delete: ")
    if name in combo_menu:
        del combo_menu[name]
        print(f"{name} has been deleted from the menu.")
    else:
        print("Combo not found.")


# Allows the user to see the full menu list after editing or observing
def print_menu():
    print("Full Combo Menu:")
    for name, details in combo_menu.items():
        items_str = ', '.join(details['Items'])
        print(f"{name}: {items_str} - ${details['Price']}")


# Main loop
while True:
    print("\n*** Welcome! What would you like to do today? ***\nOptions:")
    print("****************************************")
    print("1 - Add a new combo meal")
    print("2 - Search for an existing combo meal")
    print("3 - Delete a combo meal")
    print("4 - Display the full menu")
    print("5 - Exit")
    print("****************************************")
    choice = input("Please choose an option: ")

    if choice == '1':
        add_combo()
    elif choice == '2':
        search_combo()
    elif choice == '3':
        delete_combo()
    elif choice == '4':
        print_menu()
    elif choice == '5':
        print("Thank you and farewell! Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")
