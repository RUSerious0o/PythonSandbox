def to_camel_case(text):
    # result = str(text).title().replace('-', '_').split('_')
    # if text[0].islower():
    #     result[0] = result[0].lower()
    # return ''.join(result)

    if text == '':
        return ''
    else:
        return text[0] + str(text).title().replace('-', '').replace('_', '')[1::]


print(to_camel_case('The_stealth_Warrior'))
