#Using inheritance to add on to our Restaurant class

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

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize attributes of parent class'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Chocolate', 'Raspberry', 'Vanilla']
        
    def show_flavors(self):
        print('These are the flavors that we have: ')
        for flavors in self.flavors:
            print(flavors)

#Creating an instance using the IceCreamStand class
parlor = IceCreamStand('Johnnys', 'Ice Cream')
parlor.show_flavors()
