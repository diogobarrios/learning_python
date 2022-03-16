# Dictionaries in Dictionaries

# Dictionary
all_guests = {'Alice': {'apples':  5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

# function to see how much the guests brought


def total_brought(guests, item):
    # init a var with 0
    num_brought = 0
    # for loop with key-value pair, it'll look in key = guest
    # and key = item for the value associated
    for k, v in guests.items():
        # here with add all equal items iwht v as values in a item
        num_brought += v.get(item, 0)
    return num_brought


print('Number of things being brought:')
print(' - Apples           ' + str(total_brought(all_guests, 'apples')))
print(' - Cups             ' + str(total_brought(all_guests, 'cups')))
print(' - Ham sandwiches   ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Cakes            ' + str(total_brought(all_guests, 'cakes')))
print(' - Apple Pies       ' + str(total_brought(all_guests, 'apple pies')))
