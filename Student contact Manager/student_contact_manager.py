
contacts = {}
emails = set()
phones = set()


def add_contact():
    print("\n========== ADD CONTACT ==========")

    unique_id = input("Enter ID Number: ").strip()

    if not unique_id:
        print("Unique ID cannot be empty.")
        return

    if unique_id in contacts:
        print("ID already exists.")
        return

    full_name = input("Enter Full Name: ").strip()
    email = input("Enter Email: ").strip().lower()
    phone = input("Enter Phone Number: ").strip()
    role = input("Enter Role (Student/Parent/Teacher): ").strip().title()

    # Name validation
    if not full_name:
        print("Full name cannot be empty.")
        return

    # Email validation
    if '@' not in email or '.' not in email:
        print("Invalid email address.")
        return

    # Prevention of duplicate email
    if email in emails:
        print("This email has already been registered.")
        return

    # Phone number validation
    if not phone.isdigit():
        print("Phone number must only contain numbers.")
        return

    # Check for duplicate phone number
    if phone in phones:
        print("This phone number has already been registered.")
        return

    # Store the contact
    contacts[unique_id] = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "role": role
    }

    # Add email and phone to their sets
    emails.add(email)
    phones.add(phone)

    print("Contact added successfully.")


def update_contact():
    print("\n========== UPDATE CONTACT ==========")

    unique_id = input(
        "Enter the ID of the contact to update: "
    ).strip()

    if unique_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[unique_id]

    print("\nLeave a field empty if no change is needed.")

    new_name = input(
        f"Full Name [{contact['full_name']}]: "
    ).strip()

    new_email = input(
        f"Email [{contact['email']}]: "
    ).strip().lower()

    new_phone = input(
        f"Phone [{contact['phone']}]: "
    ).strip()

    new_role = input(
        f"Role [{contact['role']}]: "
    ).strip().title()

    # Update name
    if new_name:
        contact['full_name'] = new_name

    # Update email
    if new_email:

        if '@' not in new_email or '.' not in new_email:
            print("Invalid email address.")
            return

        if new_email != contact['email'] and new_email in emails:
            print("This email has already been registered.")
            return

        # Remove old email and add new email
        emails.remove(contact['email'])
        emails.add(new_email)

        contact['email'] = new_email

    # Update phone
    if new_phone:

        if not new_phone.isdigit():
            print("Phone number must only contain numbers.")
            return

        if new_phone != contact['phone'] and new_phone in phones:
            print("This phone number has already been registered.")
            return

        # Remove old phone and add new phone
        phones.remove(contact['phone'])
        phones.add(new_phone)

        contact['phone'] = new_phone

    # Update role
    if new_role:
        contact['role'] = new_role

    print("Contact updated successfully.")


def delete_contact():
    print("\n============ DELETE CONTACT ============")

    unique_id = input(
        "Enter the contact ID to delete: "
    ).strip()

    if unique_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[unique_id]

    # Remove email and phone from sets
    emails.remove(contact['email'])
    phones.remove(contact['phone'])

    # Delete the contact
    del contacts[unique_id]

    print("Contact deleted successfully.")


def search_contact():
    print("\n=========== SEARCH CONTACT ==========")

    search_term = input(
        "Enter ID, name, email, phone or role: "
    ).strip().lower()

    found = False

    for unique_id, contact in contacts.items():

        if (
            search_term in unique_id.lower()
            or search_term in contact['full_name'].lower()
            or search_term in contact['email'].lower()
            or search_term in contact['phone'].lower()
            or search_term in contact['role'].lower()
        ):

            print('\n-------------------')
            print('ID:', unique_id)
            print('Name:', contact['full_name'])
            print('Email:', contact['email'])
            print('Phone:', contact['phone'])
            print('Role:', contact['role'])

            found = True

    if not found:
        print("No matching contact found.")


def list_contacts():
    print("\n=========== ALL CONTACTS ===========")

    if not contacts:
        print("There are no contacts available.")
        return

    for unique_id, contact in contacts.items():

        print('\n----------------------')
        print('ID:', unique_id)
        print('Name:', contact['full_name'])
        print('Email:', contact['email'])
        print('Phone:', contact['phone'])
        print('Role:', contact['role'])


def main():

    while True:

        print('\n================================')
        print("     STUDENT CONTACT MANAGER")
        print('================================')

        print('1. Add contact')
        print('2. Update contact')
        print('3. Delete contact')
        print('4. Search contact')
        print('5. List All contacts')
        print('6. Exit')

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            add_contact()

        elif choice == '2':
            update_contact()

        elif choice == '3':
            delete_contact()

        elif choice == '4':
            search_contact()

        elif choice == '5':
            list_contacts()

        elif choice == '6':
            print("Thank you for logging in.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


main()
