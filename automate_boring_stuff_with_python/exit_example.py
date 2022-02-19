import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':  # if it's false, give me a string of what was typed.
        sys.exit()  # This will exit the program aka script
    print('You typed ' + response + '.')
