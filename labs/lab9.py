from calendar import formatstring
from lab3 import get_item


def count_instances(user_list=list):
    if len(user_list) == 0:
        print("Sorry, the list is empty.")
        return False
    item = get_item("Please enter the item to be counted: ")
    count = user_list.count(item)
    if count == 1:
        print("There is 1 instance of [{}] in the list".format(item))
    else:
        print
        print("There are {} instances of [{}] in the list.".format(
            count, item))
    return True


def Test1():
    reqd_items = []
    return_value = count_instances(reqd_items)


def Test2():
    items = ['Alpha']
    return_value = count_instances(items)


def Test3():
    simple_items = ['Alpha']
    return_value = count_instances(user_list=simple_items)


def Test4():
    phonetic_items = ['Alpha', 'Bravo', 'Alpha']
    return_value = count_instances(phonetic_items)
    print(phonetic_items)


# Test1()
# Test2()
# Test3()
# Test4()
