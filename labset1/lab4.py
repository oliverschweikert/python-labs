def get_total_items(user_list=list):
    return f"There are {len(user_list)} items in the list." if len(user_list) != 1 else f"There is {len(user_list)} item in the list."


def Test1():
    no_options = []
    msg = get_total_items(no_options)
    print(f'Function returned the message: {msg}')
    print(f'Function returned: {len(msg)} chrs.')


def Test2():
    progression_options = [
        '1) Onwards and upwards.'
    ]
    print(get_total_items(progression_options))


def Test3():
    recipe_instructions = ['Toast bread', 'Spread butter', 'Spread Marmite']
    total_items_msg = get_total_items(user_list=recipe_instructions)
    print(f'Function returned the message: {total_items_msg}')
    print(f'Function returned: {len(total_items_msg)} chrs.')


def Test4():
    shopping_options = [
        'Shopping list options.',
        'A) Add an item.',
        'R) Remove an item by its item number.',
        'T) Display the total number of items in the list.',
        'L) List all the items.',
        'S) Sort the list.',
        'E) Empty the list.',
        'C) Count the instances of an item in the list.',
        'Q) Quit.'
    ]
    msg = get_total_items(shopping_options)
    print(f'Function returned the message: {msg}')
    print(f'Function returned: {len(msg)} chrs.')


# Test1()
# Test2()
# Test3()
# Test4()
