def display_as_list(display_items=list, message='Item', counter_reqd=True):
    if len(display_items) == 0:
        print("Sorry, the list is empty.")
        return False
    for index, item in enumerate(display_items, start=1):
        if counter_reqd:
            print(f"\n{message} {index}: {item}")
        else:
            print(item)
    return True


def Test1():
    recipe_instructions = []
    return_value = display_as_list(
        display_items=recipe_instructions, counter_reqd=True)
    instructions = []
    return_value = display_as_list(
        display_items=instructions, counter_reqd=False)


def Test2():
    shopping_options = [
        'Shopping list options.',
        'A) Add an item.',
        'R) Remove an item by its item number.',
        'D) Display the total number of items in the list.',
        'L) List all the items.',
        'S) Sort the list.',
        'E) Empty the list.',
        'C) Count the instances of an item in the list.',
        'Q) Quit.'
    ]
    return_value = display_as_list(shopping_options, counter_reqd=False)


# Test1()
# Test2()
