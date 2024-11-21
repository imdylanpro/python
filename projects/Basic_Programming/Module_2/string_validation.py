# Dylan Nelson
# November 21, 2024
# string_validation.py

user_str = input('Please enter a string under 50 characters. ')
isalnum_flag = False
isalpha_flag = False
isdigit_flag = False
islower_flag = False
isupper_flag = False

if len(user_str) < 50:
    print(f'You typed: {user_str}')
    print(f'Testing if {user_str} is entirely alphanumeric '
          '(a-z, A-Z, and 0-9). ')
    if user_str.isalnum():
        print('True')
    else:
        print('False')

    print(f'Testing if {user_str} is entirely alphabetical '
          '(a-z, A-Z).')
    if user_str.isalpha():
        print('True')
    else:
        print('False')

    print(f'Testing if {user_str} is entirely digits '
          '(0-9).')
    if user_str.isdigit():
        print('True')
    else:
        print('False')

    print(f'Testing if {user_str} is entirely lower case '
          '(a-z).')
    if user_str.islower():
        print('True')
    else:
        print('False')

    print(f'Testing if {user_str} is entirely upper case '
          '(A-Z).')
    if user_str.isupper():
        print('True')
    else:
        print('False')

    print('Testing if string contains any alphanumeric, alphabetical, digit, '
          'upper case, or lower case characters. ')
    for i in range(len(user_str)):
        if user_str[i-1].isalnum():
            isalnum_flag = True
        if user_str[i-1].isalpha():
            isalpha_flag = True
        if user_str[i-1].isdigit():
            isdigit_flag = True
        if user_str[i-1].isupper():
            isupper_flag = True
        if user_str[i-1].islower():
            islower_flag = True
    
    if isalnum_flag:
        print(user_str, 'has at least one alphanumeric character.')
    else:
        print(user_str, 'does not have any alphanumeric characters.')
    if isalpha_flag:
        print(user_str, 'has at least one alphabetical character.')
    else:
        print(user_str, 'does not have any alphabetical characters.')
    if isdigit_flag:
        print(user_str, 'has at least one digit character.')
    else:
        print(user_str, 'does not have any digit characters.')
    if isupper_flag:
        print(user_str, 'has at least one upper case character.')
    else:
        print(user_str, 'does not have any upper case characters.')
    if islower_flag:
        print(user_str, 'has at least one lower case character.')
    else:
        print(user_str, 'does not have any lower case characters.')

else:
    print('Your input was longer than 50 characters.')