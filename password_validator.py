def validate_password(password):
    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print('Password must be between 6 and 10 characters')


    for el in password:
        if el.isdigit() and not el.isalpha():
            print('Password must consist only of letters and digits')
            break

    counter_digits = 0
    for el in password:

        if el.isdigit():
            is_valid = False
            counter_digits += 1
        if counter_digits < 2:
            print('Password must have at least 2 digits')

    return is_valid


password = input()

result = validate_password(password)

if is_valid:
    print('Password is valid')

