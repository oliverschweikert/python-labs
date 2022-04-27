from collections import UserList


def sort_list(user_list):
    if len(user_list) == 0:
        print("Sorry, the list is empty.")
        return False
    elif len(user_list) == 1:
        print("There is only one item in the list, the list does not need to be sorted.")
        return False
    else:
        user_list.sort()
        print("The list has been sorted.")
        return True


def Test1():
    food_items = []
    return_value = sort_list(food_items)
    print(return_value)
    print(food_items)


def Test2():
    personal_items = ['Alpha']
    return_value = sort_list(personal_items)
    print(return_value)
    print(personal_items)


def Test3():
    shop_items = ['Bravo', 'Alpha']
    return_value = sort_list(shop_items)
    print(return_value)
    print(shop_items)


def Test4():
    reqd_items = ['Delta', 'Alpha', 'Bravo']
    return_value = sort_list(user_list=reqd_items)
    print(return_value)
    print(reqd_items)


# Test1()
# Test2()
# Test3()
# Test4()
