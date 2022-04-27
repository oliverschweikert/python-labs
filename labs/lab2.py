def get_option(prompt_msg="Option"):
    return ' '.join(prompt_msg.split()).upper()


msg = input("Please enter the prompt message")
print(get_option(msg))
