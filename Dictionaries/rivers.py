#looping through keys and values

#River dictionary
rivers = {
    'nile': 'Egypt',
    'mississippi river': 'Mississippi',
    'rainbow river': 'Neverland',
}

#Loop through each for a sentence
for river, place in rivers.items():
    print(f'The {river.title()} is in {place.title()}.')
    
#Loop through just keys 
print('\nThe following river have been mentioned:')
for river in rivers.keys():
    print(river.title())

#Loop through just values
print('\nThe following places have been mentioned:')
for place in rivers.values():
    print(place.title())

