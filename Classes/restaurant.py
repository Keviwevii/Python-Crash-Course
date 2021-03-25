#Making a restaurant class

class Restaurant:
    '''A representation of a restaurant.'''
    
    def __init__(self,restaurant_name,cuisine_type):
        '''Initialize resturant attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        '''Showing our restaurant name and cuisine type.'''
        print(f'Restaurant name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}')
    
    def open_restaurant(self):
        '''Message that shows restaurant is open.'''
        print('This restaurant is now open!')

#Making an instance of from our class
chinese_restaurant = Restaurant('A1 Hibachi', 'Chinese Food')

#Directly printing our two attributes for the restaurant
print(f'Restaurant Name: {chinese_restaurant.restaurant_name}')
print(f'Cuisine Type: {chinese_restaurant.cuisine_type}')

#Calling class methods with dot notation
chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()