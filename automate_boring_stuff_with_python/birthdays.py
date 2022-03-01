# Dictionary Exercise

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        # if I want to exit the while loop I just enter without any info
        break
        # If I put a name (key) that is already in Dict.
        # it will stdout the value of the key + the key -self.
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        # or if I mention a new name (key) that is not in the
        # dict. it will prompt to create a new one
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        # Here 'name' var has the new value that is not in the dict.
        # I put the value to complete the pair using the 'bday var.'
        bday = input()
        # And then it creates the pair key(name)-value(bday)
        birthdays[name] = bday
        print('birthday database updated')
