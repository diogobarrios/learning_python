# Do a function that can return a string from a list


# the last value in these string have to have an 'and' before
# for this we fix the last value as list[-1] and to work from
# the rest range(len(list) - 2), 2 because we want all values minus
# the last one.

def list_string(list):
      string = ''  # empty string to receive the values
       for i in list:
            string = string + str(i)
            if list.index(i) == (len(list) - 2):
                string = string + ', and '
            elif list.index(i) == (len(list) - 1):
                string = string
            else:
                string = string + ', '
        return string
