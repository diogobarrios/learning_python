# Exercise 15: Reading Files

from sys import argv

# Here will be "ex15.py" & "ex15_sample.txt"
script, filename = argv

# first, we have to open the "filename"
txt = open(filename)

# Here will stdout the "filename"
print(f"Here's your file {filename}:")
# Here we're going to use variable "txt" with
# method .read() after open() the file
print(txt.read())

print("Type the filename again:")
# Another way to stdin the file with input()
# as opposite with argv
file_again = input("> ")

# then again, first, open() append it to a variable
txt_again = open(file_again)

# then print() the varible attached with the method .read()
print(txt_again.read())
