# Do a function that can return a string from a list


# the last value in these string have to have an 'and' before
# for this we fix the last value as list[-1] and to work from
# the rest range(len(list) - 2), 2 because we want all values minus
# the last one.

def list_string(arg):
    string = ''  # empty string to receive the values
    # looping in the list
    for i in arg:
        string += str(i)
        # if the new value fromm the list passed to string is before the last
        # one is going to add an 'and'
        if arg.index(i) == (len(arg) - 2):
            string += ', and '
        # if the new value is the last one we break the loop and print out
        elif arg.index(i) == (len(arg) - 1):
            break
        # otherwise will add ', ' comma between values
        else:
            string += ', '
    return string
