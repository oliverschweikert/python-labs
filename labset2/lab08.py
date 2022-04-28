def display_contacts(contacts: dict):
    if len(contacts) != 0:
        for contact in contacts:
            print(f"{contact:<15}: {contacts[contact]}")
        return True
    print("Sorry, there are no contacts.")
    return False


def Test1():
    onsite_contacts = {'Ms One': '101',
                       'Mr Two': '102',
                       'Mrs Three': '103'
                       }
    return_status = display_contacts(onsite_contacts)


def Test2():
    current_contacts = {'Ms One': '101'}
    return_status = display_contacts(current_contacts)


def Test3():
    personal_contacts = {}
    return_status = display_contacts(contacts=personal_contacts)


# Test1()
# Test2()
# Test3()
