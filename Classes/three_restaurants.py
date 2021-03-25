#Continuing with our restaurant class to make 3 instances

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
 
#Creating three instances        
chinese_restaurant = Restaurant('A1 Hibachi', 'Chinese Food')
jamaican_restaurant = Restaurant('Groove Grub', 'Jamaican Food')
american_restaurant = Restaurant('Phillies', 'American Food')

#Calling methods
chinese_restaurant.describe_restaurant()
jamaican_restaurant.describe_restaurant()
american_restaurant.describe_restaurant()