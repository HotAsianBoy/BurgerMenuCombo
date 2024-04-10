"""Main Loop Easygui
Added easygui into the finished main loop code
"""
import easygui


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
    elif choice == "Delete Combo":
        print_menu()
    elif choice == "Exit":
        easygui.msgbox("Thank you! Exiting program.")
        break