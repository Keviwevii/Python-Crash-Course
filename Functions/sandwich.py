#A module for the sandwiches.py script

def make_sandwich(*items):
    '''Collects all the items you want on your sandwich.'''
    print('You have the following items on your sandwich: ')
    for item in items:
        print(item)
