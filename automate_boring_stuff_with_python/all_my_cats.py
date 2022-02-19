# An empty list to receive the name of the cats
cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
          # is add 1 to len() function because cat 0 logically doesn't make sense
          ' (Or enter nothing to stop.):')
    # collect one-by-one the name of the cats
    name = input()
    # but if i don't put more names, it breaks the while loop
    if name == '':
        break
    cat_names = cat_names + [name]  # list concatenation
print('The cat names are:')
for name in cat_names:
    print(' ' + name)
