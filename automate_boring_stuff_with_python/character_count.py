# to print prettier
import pprint
# a string to count the character within
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# empty dictionary
count = {}

# a loop to count the string is a value of message variable
for character in message:
    # setting each unique key with a value of 0 to start counting
    count.setdefault(character, 0)
    # adding 1 on 1 when the unique character repeat in the above string
    # the same as: count[character] = count[character] + 1
    count[character] += 1

# print the dicitonary
pprint.pprint(count)
