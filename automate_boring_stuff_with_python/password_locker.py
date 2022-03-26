#! python3

# pw.py - An insecure password locker program

import sys
import pyperclip
passwords = {'Facebook': 'Hekeo8373',
             'Instagram': 'Hegenecmsi12',
             'Snapchat': 'ThT43T2'}

# Step 2: Handle Command Line Args
# if doesn't start with 2 args, like "pw.py, [account]"
# it will display a message how to do it and exit()
if len(sys.argv) < 2:
    print('Usage: python pw.py [acount] - copy account passowrd')
    sys.exit()

# Otherwise it will save the arg in account variable
account = sys.argv[1]  # frist command line arg is the account name

# if 'account_name' is a "key" of the passwords dictonary, then copy
# with the pyperclip module
if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
