def get_item(prompt_msg="Item: "):
    return ' '.join(input(prompt_msg).split()).capitalize()


def Test1():
    item = get_item()
    print(f'Function returned: {item}')
    print(f'Function returned: {len(item)} chr(s).')
    print(f'Function returned: {type(item)}.')
    print()
    item = get_item()
    print(f'Function returned: {item}')
    print(f'Function returned: {len(item)} chr(s).')
    print(f'Function returned: {type(item)}.')


def Test2():
    reqd_item = get_item()
    print(reqd_item)
    print()
    print(get_item())
    print()
    creature_prompt = 'hephalump or pushmepullyu?'
    print(get_item(prompt_msg=creature_prompt))
    print()
    get_item(prompt_msg='hephalump or pushmepullyu?')
    print()
    print(get_item(prompt_msg='What would you like to buy? '))
    print()
    print(get_item(prompt_msg=''))


# Test1()
# Test2()
