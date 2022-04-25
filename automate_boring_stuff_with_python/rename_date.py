#! python3

# rename_date.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

# Here's what the program does:

# It searches all the filenames in the current working directory for
# American-style dates

# When on is found, it renames the file with the month and day swapped
# to make it European-style

# This means the code will need to do the following:
# Create a regex that can identify the text pattern of American-style dates
# Call os.listdir() to find all the files in the working directory
# Loop over each filename, using the regex to check whether it has a date
# if it has a date, rename the file with shutil.move()

# Step 1: Create a Regex for American-Style Dates
import shutil
import os
import re

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r'''
                ^(.*?)              # all the text before the date
                ((0|1)?\d)-         # one or two digits for the month
                ((0|1|2|3)?\d)-     # one or two digits for the day
                ((19|20)\d\d)       # four digits for the year
                (.*?)$              # all text after the date
                ''', re.VERBOSE)

# Step 2: Identify the Date Parts from the Filenames
# Loop over the file in the working directory.
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the differnt parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.gorup(8)
