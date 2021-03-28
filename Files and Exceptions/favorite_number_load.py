#loading our number from favorite_number_dump.py

import json

filename = 'fav_number.json'

with open(filename) as f:
    fav_number = json.load(f)
    print(f'Your favorite number is {fav_number}')