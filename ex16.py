# Exercise 16: Reading and Writing Files

from sys import argv

scrpit, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

# the input() here, will wait for a stdin as asked
input("?")

print("Opening the file...")
# we have here an argument 'w' for write
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# then we truncate, which is going to
# empty the file.
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file")

# then, write in the filename what was
# stdin in each variable line*
target.write(line1)
# Here will create a newline
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# Finally we close() as saving the filename.
target.close()
