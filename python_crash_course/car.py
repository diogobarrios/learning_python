class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, deal, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.deal = deal
        self.year = year
        self.odometer_reading = 0  # this is an attribute without
        # passed a parameter

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('Audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
