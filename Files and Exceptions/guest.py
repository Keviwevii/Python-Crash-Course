#Program to make a guest list

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input('What is your name? ')
    file_object.write(name)