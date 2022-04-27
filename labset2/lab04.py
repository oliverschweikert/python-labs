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


def Test1():
    pin_message = 'Please enter your pin number: '
    min_digits = 4
    entered_number = get_number_as_string(message=pin_message,
                                          min_length=min_digits)
    print(f'The number is {entered_number}')


def Test2():
    landline_message = 'Please enter your landline number: '
    minimum_digits = 7
    mobile_number = get_number_as_string(landline_message,
                                         minimum_digits)
    print(f'The number is {mobile_number}')


def Test3():
    ext_message = 'Please enter your extension number: '
    min_dgts = 4
    extension_number = get_number_as_string(ext_message, min_dgts)
    print(f'The number is {extension_number}')


# Test1()
# Test2()
# Test3()
