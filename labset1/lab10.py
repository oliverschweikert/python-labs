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


def get_option(prompt_msg="Option: "):
    return ' '.join(input(prompt_msg).split()).lower()


def get_item(prompt_msg="Item: "):
    return ' '.join(input(prompt_msg).split()).capitalize()


def get_total_items(user_list: list):
    return f"There are {len(user_list)} items in the list." if len(user_list) != 1 else f"There is {len(user_list)} item in the list."


def add_item(user_list: list):
    item = get_item("Please enter the item to be added: ")
    if item == '':
        print("No item was entered.")
        print(get_total_items(user_list))
        return False
    if item in user_list:
        if get_option(
                f"[{item}] is already in the list, please confirm that you want to add another (y/n): ") != 'y':
            print("[{}] was not added.".format(item))
            print(get_total_items(user_list))
            return False
    user_list.append(item)
    print("[{}] has been added to the list.".format(item))
    print(get_total_items(user_list))
    return True


def remove_item(user_list: list):
    if len(user_list) == 0:
        print("Sorry, the list is empty.")
        return False
    option = get_option(
        "Please enter the item number of the item to remove or 0 to cancel: ")
    while not option.isdigit() or int(option) < 0:
        print("The item number must be a positive integer.")
        option = get_option(
            "Please enter the item number of the item to remove or 0 to cancel: ")
    if option == '0':
        print("Remove request cancelled.")
        return False
    if int(option) > len(user_list):
        print(f"Sorry, item {option} does not exist in the list")
        return False
    if get_option("Are you sure (y/n)?") != 'y':
        print(
            f"Item {option} [{user_list[int(option)-1]}] was not removed from the list.")
        return False
    print(
        f"Item {option} [{user_list.pop(int(option)-1)}] has been removed from the list.")
    return True


def sort_list(user_list: list):
    if len(user_list) > 1:
        user_list.sort()
        print("The list has been sorted.")
        return True
    print("Sorry, the list is empty.") if len(user_list) == 0 else print(
        "There is only one item in the list, the list does not need to be sorted.")
    return False


def empty_list(user_list: list):
    if len(user_list) != 0 and get_option("Please confirm that you want to empty the list (y/n): ") == 'y':
        user_list.clear()
        print("All the items have been removed from the list.")
        return True
    print("Sorry, the list is empty") if len(
        user_list) == 0 else print("The list has not been emptied.")
    return False


def count_instances(user_list: list):
    if len(user_list) == 0:
        print("Sorry, the list is empty.")
        return False
    item = get_item("Please enter the item to be counted: ")
    count = user_list.count(item)
    print(f"There is 1 instance of [{item}] in the list") if count == 1 else print(
        f"There are {count} instances of [{item}] in the list.")
    return True


def Application():
    shopping_list_options = [
        "Shopping list options.",
        "A) Add an item.",
        "R) Remove an item by its item number.",
        "D) Display the total number of items in the list.",
        "L) List all the items.",
        "S) Sort the list.",
        "E) Empty the list.",
        "C) Count the instances of an item in the list.",
        "Q) Quit."
    ]
    shopping_list_items = []
    while True:
        display_as_list(shopping_list_options, counter_reqd=False)
        option = get_option()
        if option == 'a':
            add_item(shopping_list_items)
        if option == 'r':
            remove_item(shopping_list_items)
        if option == 'd':
            print(get_total_items(shopping_list_items))
        if option == 'l':
            display_as_list(shopping_list_items)
        if option == 's':
            sort_list(shopping_list_items)
        if option == 'e':
            empty_list(shopping_list_items)
        if option == 'c':
            count_instances(shopping_list_items)
        if option == 'q':
            print("Shopping time.")
            break


Application()
