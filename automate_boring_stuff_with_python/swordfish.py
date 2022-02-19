while True:
    print('Who are you?')
    name = input()
    if name != 'Diogo':
        continue  # the if stament is True (!=) goes to the first print
    print('Hello Joe. What is the passwword? (It is a fish.)')
    password = input()
    if password == 'Atum':
        # if statement is false goes to the first print because while is True
        break
print('Acess granted.')
