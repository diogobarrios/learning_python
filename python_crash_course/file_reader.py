filename = 'pi_digits.txt'

with open(filename) as file_object:  # with will close() the file properly when python have to
    lines = file_object.readlines()

pi_string = ''
for line in lines:  # this will create a list which can be work later
    pi_string += line.rstrip()  # rstrip() removes the blank line below the result

print(pi_string)
