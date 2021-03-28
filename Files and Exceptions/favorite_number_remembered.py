#Combining programs to make one program to remember numbers with json

import json

filename = 'my_favorite_number.json'

#This will tell you your favorite number if it is stored
#If not it will have you tell your favorite number and store it
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    your_number = input('What is your favorite number? ')
    with open(filename, 'w') as f:
        json.dump(your_number,f)
else:
    print(f'Your favorite number is {favorite_number}')      