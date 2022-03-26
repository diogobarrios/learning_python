# Table Printer

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# first find which string in the list is the longest
string_index = []
for string in range(len(table_data[0])):
    string_index.append(len(table_data[0][string]))
longest_string = max(string_index)

# Second iterate over the list with rjust() and with the length
# of the Longest string in the list
for string in range(len(table_data[0])):
    print(table_data[0][string].rjust(longest_string, ' '))

# third print as a table right justified
range_outer_list = range(len(table_data))
range_inner_list = range(len(table_data[min(range_outer_list)]))
print('Range of the outer list ' + str(range_outer_list) + '\n'
      'Range of the inner lists ' + str(range_inner_list))
