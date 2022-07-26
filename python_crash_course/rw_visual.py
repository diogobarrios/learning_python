import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keeep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.scatter(0, 0, c='green', s=100)  # Begin of the walk.
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)  # End of the walk.
    
    # Remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    

    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    