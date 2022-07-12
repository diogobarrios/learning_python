import matplotlib.pyplot as plt

# Points for plotting.
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Set the style for the plot
plt.style.use('ggplot')

# Generate the plot
fig, ax = plt.subplots()

# Generate type of plot - scatter
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds , s= 10)

# Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the size of the ticks
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
ax.axis([0, 5100, 0, 130000000000])
# Generate the figure
plt.show()
