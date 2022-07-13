from random import choice

class RandomWalk:
    """A class that generates random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points
    
        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    # General axis step.
    # def get_step(self):
    #    """Calculate the direction and distance of which axis"""

        # Decide which direction to go and how far to go in that direction.
    #    direction = choice([1, -1])
    #    distance  = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    #    step = direction * distance
    #    return step

    # Custom x-axis step.
    def get_step_x(self):
        """Calculate the direction and distance for x-axis"""

        # Decide which direction to go and how far to go in that direction.
        x_direction = choice([0, 1])
        x_distance  = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_step = x_direction * x_distance
        return x_step
    
    # Custom y-axis step.
    def get_step_y(self):
        """Calculate the direction and distance for y-axis"""

        # Decide which direction to go and how far to go in that direction.
        y_direction = choice([-1, 1])
        y_distance  = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_step = y_direction * y_distance
        return y_step
    
    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_step_x()
            y_step = self.get_step_y()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x) 
            self.y_values.append(next_y)
        