class Restaurant:
    """Describe the restaurant and open hours"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe the name of the restaurant and the type
            of cuisine"""
        print(f"Restaurant {self.name} has a {self.cuisine} cuisine!")

    def open_restaurant(self):
        """Describe a message indicating the restaurant is open"""
        print(f"The Restaurant {self.name} is now open!")


restaurant = Restaurant('Itali', 'italian')
restaurant_mex = Restaurant('Caliente', 'mexican')
restaurant_yen = Restaurant('Yin&Yan', 'japanese')

restaurant.describe_restaurant()
restaurant.open_restaurant()
print('\n')
restaurant_mex.describe_restaurant()
restaurant_mex.open_restaurant()
print('\n')
restaurant_yen.describe_restaurant()
restaurant_yen.open_restaurant()
