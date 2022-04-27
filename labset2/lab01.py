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


def Test1():
    recipe_instructions = ['Toast bread', 'Spread butter', 'Spread marmite']
    shopping_message = 'Shopping item'
    purchase_message = 'Purchase item'
    return_value = display_as_list(recipe_instructions)
    return_value = display_as_list(display_items=recipe_instructions)
    return_value = display_as_list(
        display_items=recipe_instructions, message=shopping_message)
    print(f'The function returned {return_value}')
    return_value = display_as_list(display_items=recipe_instructions, message=purchase_message,
                                   counter_reqd=True)
    print(f'The function returned {return_value}')
    return_value = display_as_list(display_items=recipe_instructions, message=purchase_message,
                                   counter_reqd=False)
    print(f'The function returned {return_value}')


def Test2():
    recipe_instructions = []
    return_value = display_as_list(
        display_items=recipe_instructions, counter_reqd=True)
    instructions = []
    return_value = display_as_list(display_items=recipe_instructions, message="Don't display this",
                                   counter_reqd=False)
    instructions = []
    return_value = display_as_list(
        display_items=instructions, counter_reqd=False)


def Test3():
    telephone_menu = [
        'Telephone contact options.',
        'A) Add/modify a contact.',
        'R) Remove a contact.',
        'S) Show/find a contact.',
        'D) Display all contacts.',
        'E) Empty all contacts.',
        'Q) Quit.'
    ]
    return_value = display_as_list(telephone_menu, counter_reqd=False)
    return_value = display_as_list(
        display_items=telephone_menu, message="Don't display this message", counter_reqd=False)
    return_value = display_as_list(
        display_items=telephone_menu, message='Do display this message: ', counter_reqd=True)


# Test1()
# Test2()
# Test3()
