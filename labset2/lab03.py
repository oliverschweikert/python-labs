def get_name(message):
    return ' '.join(input(message).split()).title()


def Test1():
    contact_msg = 'Contact: '
    print(get_name(contact_msg))


def Test2():
    contact_msg = 'Contact name: '
    contact = get_name(contact_msg)
    print(contact)
    contact = get_name(contact_msg)
    print(contact)


def Test3():
    print(get_name('First name: '))


# Test1()
# Test2()
# Test3()
