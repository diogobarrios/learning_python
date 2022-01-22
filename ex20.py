# Exercise 20: Functions and Files

from sys import argv

script, input_file = argv

# Function to read input_file


def print_all(f):
    print(f.read())


# function to go back for read a file
# again from the beginning.
def rewind(f):
    f.seek(0)


# function to read one line
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")


# file will be opened first
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1  # = 2 (1 + 1)
print_a_line(current_line, current_file)

current_line += 1  # = 3 (2 + 1)
print_a_line(current_line, current_file)


# the shorthand notation += is the same as
# var = var + 1 <=> var += 1
