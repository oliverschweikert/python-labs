def display_as_list(display_items: list, message='Item', counter_reqd=True):
    if len(display_items) == 0:
        print("Sorry, the list is empty.")
        return False
    print()
    for index, item in enumerate(display_items, start=1):
        if counter_reqd:
            print(f"{message} {index}: {item}")
        else:
            print(item)
    return True


def get_option(prompt_msg="Option: "):
    return ' '.join(input(prompt_msg).split()).lower()


def get_name(message):
    return ' '.join(input(message).split()).title()


def get_number_as_string(message, min_length):
    inp = ''.join(input(message).split())
    while True:
        if inp.isdigit():
            if len(inp) >= min_length:
                break
            print(f"The number must be at least {min_length} digits long.")
        print("Digits only please.")
        inp = ''.join(input(message).split())
    return inp


def add_edit_contact(contacts: dict):
    name = get_name("Contact: ")
    if name in contacts.keys():
        if get_option(f"{name} is already in the phone system.\nWould you like to change the phone number? y/n: ") != 'y':
            print(f"{name} has not been updated.")
            return False
        number = get_number_as_string("New number: ", 3)
        if number == contacts[name]:
            print(
                f"{name} already has the number {number}. The number has not been changed.")
            return False
        contacts[name] = number
        print(f"{name} has been updated with the number: {number}.")
        return True
    contacts[name] = get_number_as_string("Contact number: ", 3)
    print(f"{name} has been added with the number: {contacts[name]}.")
    return True


def remove_contact(contacts: dict):
    if len(contacts) != 0:
        contact = get_name(
            "Enter the contact to be removed (or press Enter to cancel): ")
        if contact in contacts:
            contacts.pop(contact)
            print(f"{contact} has been removed from the contacts.")
            return True
        print("Cancelling the remove request.") if contact == '' else print(
            f"Sorry, {contact} is not a contact.")
    else:
        print("Sorry, there are no contacts.")
    return False


def show_contact(contacts: dict):
    if len(contacts) != 0:
        contact = get_name("Contact: ")
        if contact in contacts:
            print(f"{contact}: {contacts[contact]}")
            return True
        print(f"{contact} is unknown.")
    else:
        print("Sorry, there are no contacts.")
    return False


def display_contacts(contacts: dict):
    if len(contacts) != 0:
        for contact in contacts:
            print(f"{contact:<15}: {contacts[contact]}")
        return True
    print("Sorry, there are no contacts.")
    return False


def empty_contacts(contacts: dict):
    if len(contacts) != 0:
        option = get_option(
            "Please confirm that you want to remove all the contacts. y/n: ")
        if option == 'y':
            contacts.clear()
            print("All the contacts have been removed.")
            return True
        print("The contacts have not been removed.")
    else:
        print("Sorry, there are no contacts.")
    return False


def Application():
    contact_options = [
        "Telephone contact options.",
        "A) Add/edit a contact.",
        "R) Remove a contact.",
        "F) Find a contact.",
        "D) Display all contacts.",
        "E) Empty all contacts.",
        "Q) Quit."
    ]
    contacts = {}
    while True:
        display_as_list(contact_options, counter_reqd=False)
        option = get_option()
        if option == 'a':
            add_edit_contact(contacts)
        if option == 'r':
            remove_contact(contacts)
        if option == 'f':
            show_contact(contacts)
        if option == 'd':
            display_contacts(contacts)
        if option == 'e':
            empty_contacts(contacts)
        if option == 'q':
            print("Bye.")
            break


Application()
