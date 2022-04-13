# Table Printer

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

<<<<<<< HEAD
# first find which string in the list is the longest
string_index = []
for string in range(len(table_data[0])):
    string_index.append(len(table_data[0][string]))
longest_string = max(string_index)

# print each longest string from each inner list
range_outer_list = range(len(table_data))
range_inner_list = range(len(table_data[min(range_outer_list)]))
print('Range of the outer list ' + str(range_outer_list) + '\n'
      'Range of the inner lists ' + str(range_inner_list))


for list in range_outer_list:
    string_index.append(len(table_data[list][string]))
print(string_index)

# Second iterate over the list with rjust() and with the length
# of the Longest string in the list
# for string in range(len(table_data[0])):
#    print(table_data[0][string].rjust(longest_string, ' '))
=======
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
>>>>>>> 5dd77da7e6e61417357c90d0c475056c38b2923c
