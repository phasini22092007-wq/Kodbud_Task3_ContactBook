import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []
contacts = load_contacts()

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()



def add_contact():
    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("Please enter a valid 10-digit phone number.")
        return

    email = input("Enter email address: ").strip()

    if "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()
    print("Contact added successfully!")


    contacts.append(contact)
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")

        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("--------------------")

def search_contact():
    search_name = input("Enter the name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True
            break

    if not found:
        print("Contact not found.")

def delete_contact():
    delete_name = input("Enter the name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")
