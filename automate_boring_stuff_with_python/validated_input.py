while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password(letters and numbers only):')
    password = input()
    if password.isalnum() and len(password) >= 8:
        break
    print('Password must have letters, numbers and 8 characters.')
