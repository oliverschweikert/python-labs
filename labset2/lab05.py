from lab03 import get_name
from lab02 import get_option
from lab04 import get_number_as_string


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
        print(f"{name} has been updated with the number: {number}")
        return True
    contacts[name] = get_number_as_string("Contact number: ", 3)
    print(f"{name} has been added with the number: {contacts[name]}")
    return True


def Test1():
    personal_contacts = {'Ms One': '101',
                         'Mr Two': '102',
                         'Ms Tree': '103'
                         }
    modification_status = add_edit_contact(contacts=personal_contacts)
    print(personal_contacts)


def Test2():
    my_contacts = {'Ms One': 101,
                   'Mr Two': '102',
                   'Ms Tree': '103'
                   }
    modification_status = add_edit_contact(my_contacts)
    print(my_contacts)


def Test3():
    all_contacts = {'Ms One': 101,
                    'Mr Two': '102',
                    'Ms Tree': '103'
                    }
    modification_status = add_edit_contact(all_contacts)
    print(all_contacts)
    print()
    modification_status = add_edit_contact(all_contacts)
    print(all_contacts)


Test1()
Test2()
Test3()
