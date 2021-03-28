#Asking for a favorite number and using json to load it into a file

import json

print('Let us get your favorite number and store it.')
fav_number = input('What is your favorite number? ')

filename = 'fav_number.json'

with open(filename, 'w') as f:
    json.dump(fav_number, f )