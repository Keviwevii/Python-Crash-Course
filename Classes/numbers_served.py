#Modifying Attribute values in our restaurant class

class Restaurant:
    '''A representation of a restaurant.'''
    
    def __init__(self,restaurant_name,cuisine_type):
        '''Initialize resturant attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #Sets it directly
        
    def describe_restaurant(self):
        '''Showing our restaurant name and cuisine type.'''
        print(f'Restaurant name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}')
    
    def open_restaurant(self):
        '''Message that shows restaurant is open.'''
        print('This restaurant is now open!')
    
    def set_number_served(self, number):
        '''Modifys number of people served'''
        self.number_served = number
    
    def increment_number_served(self, customers_served):
        '''Increments number served'''
        self.number_served += customers_served
 
#Instance of Class       
chinese_restaurant = Restaurant('A1 Hibachi', 'Chinese Food')

#Using a method to change our attribute
chinese_restaurant.set_number_served(500)
print(f'This restaurant has served {chinese_restaurant.number_served} people!')

#Increment method
chinese_restaurant.increment_number_served(50)
print(f'This restaurant has served {chinese_restaurant.number_served} people!')

