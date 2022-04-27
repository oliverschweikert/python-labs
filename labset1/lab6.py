from lab2 import get_option


def remove_item(user_list):
    if len(user_list) == 0:
        print("Sorry, the list is empty.")
        return False
    else:
        option = get_option(
            "Please enter the item number of the item to remove or 0 to cancel: ")
        while not option.isdigit():
            print("The item number must be a positive integer.")
            option = get_option(
                "Please enter the item number of the item to remove or 0 to cancel: ")
        if option == '0':
            print("Remove request cancelled.")
            return False
        elif int(option) < 1 or int(option) > len(user_list):
            print("Sorry, item {} does not exist in the list".format(option))
            return False
        else:
            while True:
                user_input = get_option("Are you sure (y/n)?")
                if user_input == 'y':
                    item = user_list.pop(int(option)-1)
                    print(
                        "Item {} [{}] has been removed from the list.".format(option, item))
                    return True
                elif user_input == 'n':
                    print("Item {} [{}] was not removed from the list.".format(
                        option, user_list[int(option)-1]))
                    return False
                else:
                    print("Please enter either 'y' or 'n'")
                    print(user_input)


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
