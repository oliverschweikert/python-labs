def get_option(prompt_msg="Option"):
    return prompt_msg.strip().lower()


message = input("Please enter the prompt message")
print(get_option(message))
