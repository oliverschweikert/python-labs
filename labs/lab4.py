def get_total_items(user_list):
    return "There are {} items in the list".format(len(user_list)) if len(user_list) != 1 else "There is {} item in the list".format(len(user_list))


print(get_total_items(["banana"]))
print(get_total_items(["banana", "apple", "strawberry"]))
print(get_total_items([]))
