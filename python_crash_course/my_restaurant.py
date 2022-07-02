from restaurant import Restaurant, IceCreamStand

icecreamstand = IceCreamStand('Luigi', 'Dessert')
icecreamstand.describe_restaurant()
icecreamstand.describe_flavors()

restaurant = Restaurant('Itali', 'italian')
restaurant_mex = Restaurant('Caliente', 'mexican')
restaurant_yen = Restaurant('Yin&Yan', 'japanese')
restaurant.describe_restaurant()
restaurant.increment_number_served(10)
restaurant.set_number_served()
restaurant.open_restaurant()
print('\n')
restaurant_mex.describe_restaurant()
restaurant_mex.open_restaurant()
print('\n')
restaurant_yen.describe_restaurant()
restaurant_yen.open_restaurant()