def display_as_list(display_items, message='Item', counter_reqd=True):
    if len(display_items) == 0:
        return False
    else:
        print()
        for item in display_items:
            if counter_reqd:
                print(message, item)
            else:
                print(item)


display_as_list(["apple", "banana", "turnip"])
