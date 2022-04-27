from lab02 import get_option


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


def Test1():
    items = []
    return_value = remove_item(items)
    print(items)


def Test2():
    my_items = ['One']
    return_value = remove_item(my_items)
    print(my_items)


def Test3():
    items_needed = ['Zero', 1, 'Two', 3,
                    'Four', 5, 'Six', 7, 'Eight', 9, 'ten']
    return_value = remove_item(items_needed)
    print(items_needed)


def Test4():
    all_items = ['One', 'Two']
    return_value = remove_item(all_items)
    print(return_value)
    print(all_items)

    all_items = ['One', 'Two']
    return_value = remove_item(user_list=all_items)
    print(return_value)
    print(all_items)

    all_items = ['One', 'Two']
    return_value = remove_item(all_items)
    print(return_value)
    print(all_items)


# Test1()
# Test2()
# Test3()
# Test4()
