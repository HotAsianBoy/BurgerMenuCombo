"""Main Loop v3
Added extra aesthetics to ensure an effective and simple program
for the user, including welcome speech during start of program to
allow user to feel more relaxed and easier use"""


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
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")