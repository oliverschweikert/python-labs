from lab02 import get_option


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


def Test1():
    current_contacts = {'Ms One': '101',
                        'Mr Two': '102',
                        'Mrs Three': '103'
                        }
    return_status = empty_contacts(contacts=current_contacts)
    print(return_status)
    print(f'The contacts dictionary is now: {current_contacts}')
    current_contacts = {'Ms One': '101',
                        'Mr Two': '102',
                        'Mrs Three': '103'
                        }
    return_status = empty_contacts(contacts=current_contacts)
    print(return_status)
    print(f'The contacts dictionary is now: {current_contacts}')
    current_contacts = {'Ms One': '101',
                        'Mr Two': '102',
                        'Mrs Three': '103'
                        }
    return_status = empty_contacts(contacts=current_contacts)
    print(return_status)
    print(f'The contacts dictionary is now: {current_contacts}')


def Test2():
    offsite_contacts = {'Ms One': '101'}
    return_status = empty_contacts(contacts=offsite_contacts)
    print(f'The contacts dictionary is now: {offsite_contacts}')


def Test3():
    dept_contacts = {}
    return_status = empty_contacts(contacts=dept_contacts)
    print(f'The contacts dictionary is now: {dept_contacts}')


# Test1()
# Test2()
# Test3()
