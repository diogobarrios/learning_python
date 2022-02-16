# This program says hello and asks for my name

# print out the text in the string 'Hello World'
print('Hello World!')

# print out the text in the string "What's your name?"
print("what's your name?")

# the input() function is waiting for stdin or some text typed in the keyboard
my_name = input()

# print out the text in the string 'It is goot to meet you' and the value
# stored in the my_name variable
print('It is good to meet you, ' + my_name)

# print out the text in the string 'the length of your name is:'
print('The length of your name is:')

# print out the len function that gives the total of characters of the Value
# stored in the my_name variable
print(len(my_name))

# print out the text in the string "What's your age?"
print("What's your age?")

# The input() fnction is waiting some text typed from the keyboard
my_age = input()

# print out the text that starts with the strings 'You will be ' and ends
# 'in a year.'. Concatenate both strings with the value stored in the variable
# my_age that is passed to the int() function which will coerce the value
# to an integer , add 1 and then passed to the str() function which will
# coerce the value to a string.
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
