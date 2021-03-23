#Function for cities and countries

def city_country(city,country):
    '''Return a city and country with a comma in between'''
    return f"{city.title()}, {country.title()}"
 
#3 function calls assigned to variables   
atl = city_country('atlanta', 'united states')
shang = city_country('shanghai', 'china')
paris = city_country('paris', 'france')

print(atl)
print(shang)
print(paris)