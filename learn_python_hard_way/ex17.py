# Exercise 17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying form {from_file} to {to_file}")

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

# len is a function it will say how much chars has.
print(f"The input file is {len(indata)} bytes long")

# exists, it will see if new_file was created already
# to not duplicate
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to contine, CTRL-C to abort.")
input()

# open to_file with 'w' filename
out_file = open(to_file, 'w')
# write out_file with the new indata
out_file.write(indata)

print("Alright, all done.")

# finally close all files that we opened
out_file.close()
# in_file.close()
