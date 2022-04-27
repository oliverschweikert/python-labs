def get_option(prompt_msg="Option: "):
    return ' '.join(input(prompt_msg).split()).lower()


def Test1():
    option = get_option()
    print(f'Function returned: {option}')
    print(f'Function returned: {len(option)} chrs.')
    print(f'Function returned: {type(option)}.')
    print()
    option = get_option()
    print(f'Function returned: {option}')
    print(f'Function returned: {len(option)} chrs.')
    print(f'Function returned: {type(option)}.')


def Test2():
    reqd_option = get_option()
    print(reqd_option)
    print()
    print(get_option())
    print()
    user_prompt = 'Enter yes or no :'
    print(get_option(prompt_msg=user_prompt))
    print()
    get_option(prompt_msg='Enter y or n :')
    print()
    get_option(prompt_msg=':')


# Test1()
# Test2()
