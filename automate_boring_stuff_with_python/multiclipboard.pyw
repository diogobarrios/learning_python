#! python3

# multiclipboard.pyw - Saves and loadss pieces of text to the clipboard.
# Usage: py.exe multiclipboard.pyw save <keyword> - Saves clipboard to keyword
#        py.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard.
#        py.exe multiclipboard.pyw list - Loads all keywords to clipboard.

# What the program does

# the command line argument for the keyword is checked
# If the argument is save, then the clipboard contents are saved to the
# keyword
# if the argument is list, then all the keywords are copied to the clipboard
# Otherwise, the text for the keyword is copied to the keyboard.

# This means the code will need to do the following:

# Read the command line arguments from sys.argv
# Read and write to the clipboard
# Save and load to a shelf file

# Step 1: Comments and Shelf Setup

import shelve
import pyperclip
import sys

multiclipboard_shelf = shelve.open('multiclipboard')

# Step 2: Save clipboard content with a Keyword.
if len(sys.argv) == 3 and sus.argv[1].lower() == 'save':
    multiclipboard.shelf[sys.argv[2]] == pyperclip.paste()
elif len(sys.argv) == 2:
    # Step 3: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(multiclipboard_shelf.keys())))
    elif sys.argv[1] in multiclipboard_shelf:
        pyperclip.copy(multiclipboard_shelf[sys.argv[1]])

multiclipboard_shelf.close()
