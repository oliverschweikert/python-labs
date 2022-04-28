from lab03 import get_name


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


def Test1():
    all_contacts = {'Ms One': '101',
                    'Mr Two': '102',
                    'Mrs Three': '103'
                    }
    return_status = show_contact(all_contacts)
    print(all_contacts)


def Test2():
    dept_contacts = {'Ms One': '101',
                     'Mr Two': '102',
                     'Mrs Three': '103'
                     }
    return_status = show_contact(dept_contacts)
    print(dept_contacts)


def Test3():
    personal_contacts = {}
    return_status = show_contact(contacts=personal_contacts)
    print(personal_contacts)


# Test1()
# Test2()
# Test3()
