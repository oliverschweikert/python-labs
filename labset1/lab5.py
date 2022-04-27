from lab2 import get_option
from lab3 import get_item
from lab4 import get_total_items


def add_item(user_list=list):
    item = get_item("Please enter the item to be added: ")
    if item == '':
        print("No item was entered.")
        print(get_total_items(user_list))
        return False
    elif item in user_list:
        while True:
            user_choice = get_option(
                f"[{item}] is already in the list, please confirm that you want to add another (y/n): ")
            if user_choice == 'y':
                user_list.append(item)
                print("[{}] has been added to the list.".format(item))
                print(get_total_items(user_list))
                return True
            elif user_choice == 'n':
                print("[{}] was not added.".format(item))
                print(get_total_items(user_list))
                return False
            else:
                continue
    else:
        user_list.append(item)
        print(get_total_items(user_list))
        return True


def Test1():
    shop_items = []
    return_value = add_item(shop_items)
    print(f'The function returned: {return_value}')
    print(shop_items)
    return_value = add_item(shop_items)
    print(f'The function returned: {return_value}')
    print(shop_items)
    return_value = add_item(shop_items)
    print(f'The function returned: {return_value}')
    print(shop_items)


def Test2():
    items = ['One', 'Two']
    return_value = add_item(items)
    print(items)


def Test3():
    reqd_items = ['One']
    return_value = add_item(user_list=reqd_items)
    print(reqd_items)


def Test4():
    items = ['One']
    return_value = add_item(items)
    print(items)


# Test1()
# Test2()
# Test3()
# Test4()
