filename = 'guest.txt'

guest = input("Hi, can you write your first name and last name, please?: ")

with open(filename, 'a') as file_object:
    file_object.write(f"The guest's name: {guest}")
