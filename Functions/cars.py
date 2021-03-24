#Using a function to store info about cars in a dictionary

def car_info(manufacturer,model_name,**kwargs):
    '''Making a dictionary of car info'''
    kwargs['Manufacturer'] = manufacturer.title()
    kwargs['Model Name'] = model_name.title()
    return kwargs

my_car = car_info('honda', 'civic', color='grey', wheels=4)
print(my_car)