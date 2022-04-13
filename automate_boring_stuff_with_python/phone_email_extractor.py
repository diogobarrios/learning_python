#! python3
# phone_email_extractor.py - Phone Number and Email Address Extractor

# To-Do:
# Get the text off the clipboard
#   Turns out using pyperclip module to copy and paste strings
# Find all phone numbers and email addresses in the text
#   Creating 2 regexes, one for matching phone numbers and the other
#   for matching email addresses
#   Find all the matches, not just first match, of both regexes
# Paste them onto the clipboard
#   Neatly format the matched strings into a single string to paste
#   Finally display a message if no matches were found in the text

# Libraries

import pyperclip
import re

# Step 1: Create a Regex for Phone Numbers

phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?             # area code
(\s|-|\.)                      # separator
(\d{3})                        # first 3 digits
(\s|-|\.)                      # separator
(\d{4})                        # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# Step 2: Create a Regex for Email Addresses

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+              # username
@                              # @ symbol
[a-zA-Z0-9.-]+                 # domain name
(\.[a-zA-Z]{2,4})              # dot-something
)''', re.VERBOSE)

# Step 3: Find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Step 4: Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
