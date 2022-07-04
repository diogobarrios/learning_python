filename = 'pi_million_digits.txt'

with open(filename) as file_object:  # with will close() the file properly when python have to
    lines = file_object.readlines()  # will transform in a list

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()  # rstrip() removes the blank line below the result
    pi_string += line.strip()  # removes all blanks spaces

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi")
# print(pi_string)  # this will give me 32 digits
# print(f"{pi_string[:52]}...")  # If I want only the first 52 results
# print(len(pi_string))
