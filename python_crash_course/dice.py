from random import randint

class Dice:
    """Rolling a 6-sided dice"""

    def __init__(self, sides=6):
        """Initialize the attributes"""
        self.sides = sides
    
    def roll_die(self):
        """Rolling the dice 10 times"""
        roll = 0
        while roll < 10:
            self.sides = randint(1, 6)
            roll += 1
            print(f"Rolling for the #{roll} time: side {self.sides}")

dice_1 = Dice()
dice_1.roll_die() 