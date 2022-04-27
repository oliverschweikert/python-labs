def get_item(prompt_msg="Item"):
    return ' '.join(prompt_msg.split()).upper()


msg = input("Please enter your message ")
print(get_item(msg))
