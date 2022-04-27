from lab2 import get_option


def empty_list(user_list=list):
    if len(user_list) == 0:
        print("Sorry, the list is empty")
        return False
    if get_option("Please confirm that you want to empty the list (y/n): ") == 'y':
        user_list.clear()
        print("All the items have been removed from the list.")
        return True
    else:
        print("The list has not been emptied.")
        return False


def Test1():
    reqd_items = []
    return_value = empty_list(reqd_items)
    print(reqd_items)


def Test2():
    my_items = ['Alpha']
    return_value = empty_list(user_list=my_items)
    print(my_items)


def Test3():
    items_needed = ['Bravo', 'Alpha']
    return_value = empty_list(items_needed)
    print(items_needed)


def Test4():
    phonetic_items = ['Charlie', 'Bravo', 'Alpha']
    return_value = empty_list(phonetic_items)
    print(phonetic_items)


# Test1()
# Test2()
# Test3()
# Test4()
