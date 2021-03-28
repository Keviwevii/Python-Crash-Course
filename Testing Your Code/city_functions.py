#Function for our city country

def city_and_country(city_name, country_name, population=''):
    if population:
        full_name = f'{city_name}, {country_name} - {population}'
    else:
        full_name = f'{city_name}, {country_name}'
    return full_name.title()

