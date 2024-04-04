"""Main v2
Edited the main loop so it looks more eye-catching and pleasing to
the eye"""


# Main loop
while True:
    print("\nOptions:")
    print("****************************************")
    print("1 - Add a new combo meal")
    print("2 - Search for an existing combo meal")
    print("3 - Delete a combo meal")
    print("4 - Display the full menu")
    print("5 - Exit")
    print("****************************************")
    choice = input("Choose an option: ")

    if choice == '1':
        add_combo()
    elif choice == '2':
        search_combo()
    elif choice == '3':
        delete_combo()
    elif choice == '4':
        print_menu()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")