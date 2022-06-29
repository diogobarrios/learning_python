class Restaurant:
    """Describe the restaurant and open hours"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the name of the restaurant and the type
            of cuisine"""
        print(f"Restaurant {self.name} has a {self.cuisine} cuisine!")

    def open_restaurant(self):
        """Describe a message indicating the restaurant is open"""
        print(f"The Restaurant {self.name} is now open!")

    def set_number_served(self):
        """How many clients were served"""
        print(
            f"This Restaurant {self.name} served {self.number_served} clients")

    def increment_number_served(self, serving):
        """Increment the clients were served in a business day"""
        self.number_served += serving


restaurant = Restaurant('Itali', 'italian')
# restaurant_mex = Restaurant('Caliente', 'mexican')
# restaurant_yen = Restaurant('Yin&Yan', 'japanese')

restaurant.describe_restaurant()
restaurant.increment_number_served(10)
restaurant.set_number_served()
# restaurant.open_restaurant()
# print('\n')
# restaurant_mex.describe_restaurant()
# restaurant_mex.open_restaurant()
# print('\n')
# restaurant_yen.describe_restaurant()
# restaurant_yen.open_restaurant()
