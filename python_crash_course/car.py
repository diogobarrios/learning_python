class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # this is an attribute without
        # passed a parameter

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back and odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odemeter(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles at it.")


class Battery:
    """A simple attempt to model a battery for an eletric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectriCar(Car):
    """Represents aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


# my_new_car = Car('Audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odemeter()

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)  # This is the same as 23500, but is
# my_used_car.read_odemeter()          # more readable


# my_used_car.increment_odometer(100)
# my_used_car.read_odemeter()
my_tesla = ElectriCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
