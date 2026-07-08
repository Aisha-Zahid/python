phonebook = {}

while True:
    print("\n===== PHONEBOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")
        phonebook[name] = number
        print("Contact Added Successfully!")

    # Search Contact
    elif choice == "2":
        name = input("Enter Name to Search: ")

        if name in phonebook:
            print("Phone Number:", phonebook[name])
        else:
            print("Contact Not Found!")

    # Show All Contacts
    elif choice == "3":
        if len(phonebook) == 0:
            print("Phonebook is Empty!")
        else:
            print("\nAll Contacts:")
            for name, number in phonebook.items():
              print(name, ":", number)

    # Delete Contact
    elif choice == "4":
        name = input("Enter Name to Delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact Deleted!")
        else:
            print("Contact Not Found!")

    # Exit
    elif choice == "5":
        print("Thank You for Using Phonebook!")
        break

    else:
        print("Invalid Choice!")