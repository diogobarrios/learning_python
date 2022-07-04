filename = 'guest_book.txt'


while True:
    print("If you want to finish, please do with the keyboard CTRL + C")
    guest = input("Hi, can you write your first name and last name, please?: ")
    with open(filename, 'a') as file_object:
        file_object.write(f"Guest's name: {guest}\n")
