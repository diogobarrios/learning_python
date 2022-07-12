import matplotlib.pyplot as plt

# Points to plot.
x_values = range(1, 1001)  # Starting with a range from 1 to 1000
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 'c' - Can be used for color a name like 'red' or RGB from 0 to 1
# or even with built-in colormaps

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
# if the goal is to save instead to show, we use
# plt.savefig('squares_plot.png', bbox_inches='tight') instead plt.show()
# the second arg from plt.savefig is to trim the whitspace from the plot.