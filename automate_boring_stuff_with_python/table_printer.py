# Table Printer

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# First - Create a new list with the lenght of the table above


def table_printer(table):
    col_width = [0] * len(table)
# Second - Search for the longest string in each list
#          and put the number of characters in a list
    for j in range(len(table)):
        for i in table[j]:
            if col_width[j] < len(i):
                col_width[j] = len(i)

# Third - rotate and print the list of List
    range_j = range(len(table))
    range_i = range(len(table[min(range_j)]))

    for i in range_i:
        for j in range_j:
            print(table[j][i].rjust(col_width[j]), end=' ')
        print()


# Forth - print list of lists
table_printer(table_data)
