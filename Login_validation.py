'''
Exercise: Login Validation

Write a program that checks if a login is valid according to the following rules:
- Must start with an uppercase letter.
- Must be between 6 and 10 characters.
- Must contain at least 3 letters and 2 digits.
Store all approved and rejected logins in separate lists and show the result at the end.
'''

approved_logins = []
rejected_logins = []

while True:
    login = input('Enter a new login: ')
    login_ok = True  # Reset for each attempt

    # Validation rules
    if not login or not login[0].isupper():
        print('The login must start with an uppercase letter.')
        login_ok = False

    if not (6 <= len(login) <= 10):
        print('The login must have between 6 and 10 characters.')
        login_ok = False

    num_letters = sum(1 for char in login if char.isalpha())
    num_digits = sum(1 for char in login if char.isdigit())

    if num_letters < 3:
        print('The login must contain at least 3 letters.')
        login_ok = False

    if num_digits < 2:
        print('The login must contain at least 2 digits.')
        login_ok = False

    # Store login in the appropriate list and print a message
    if login_ok:
        approved_logins.append(login)
        print('Login approved:', login)
    else:
        rejected_logins.append(login)
        print('Login rejected:', login)

    # Ask if user wants to continue
    cont = input('Do you want to create another login? [y/n]: ').strip().lower()
    if cont != 'y':
        print('\nApproved logins:', approved_logins)
        print('Rejected logins:', rejected_logins)
        break
