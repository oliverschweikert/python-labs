from lab03 import get_name


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


def Test1():
    personal_contacts = {'Ms One': '101',
                         'Mr Two': '102',
                         'Mrs Three': '103'
                         }
    return_status = remove_contact(contacts=personal_contacts)
    print(personal_contacts)
    print()
    return_status = remove_contact(contacts=personal_contacts)
    print(personal_contacts)


def Test2():
    sales_contacts = {'Ms One': '101',
                      'Mr Two': '102',
                      'Mrs Three': '103'
                      }
    return_status = remove_contact(sales_contacts)
    print(sales_contacts)


def Test3():
    job_contacts = {}
    return_status = remove_contact(contacts=job_contacts)
    print(job_contacts)


# Test1()
# Test2()
# Test3()
