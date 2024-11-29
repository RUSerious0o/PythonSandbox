def check_password(password: str):
    has_num = False
    has_upper = False
    has_spec = False
    has_lower = False

    spec_symbols = "[!@#$%^&*(),.?\":{}|<>]"
    for letter in password:
        if letter.isnumeric():
            has_num = True

        if letter.isupper():
            has_upper = True

        if letter.islower():
            has_lower = True

        if letter in spec_symbols:
            has_spec = True

    if has_spec and has_upper and has_lower and has_num and len(password) <= 100:
        return 'Подходит'
    else:
        return 'Не подходит'

password = 'Password123!'
result = check_password(password)
print(result)