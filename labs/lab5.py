from lab2 import get_option
from lab3 import get_item
from lab4 import get_total_items


def add_item(user_list):

    item = get_item()
    if item == '':
        print("No item was entered")
        print(get_total_items(user_list))
        return False
    elif item in user_list:
        while True:
            user_choice = get_option()
            if user_choice == 'y':
                user_list.append(item)
                print(get_total_items(user_list))
                return True
            elif user_choice == 'n':
                print("Item not added to list")
                print(get_total_items(user_list))
                return False
            else:
                print("Invalid input - please enter 'y' or 'n'")
    else:
        user_list.append(item)
        print(get_total_items(user_list))
        return True
