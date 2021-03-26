#Using the random module

from random import randint

class Die:
    '''A class that represents a die'''
    
    def __init__(self):
        '''Initlizing attributes'''
        self.die = 6
    
    def roll_die(self):
        '''Rolling to get a side'''
        random_number = randint(1,self.die)
        print(f'The number you have is {random_number}.')

my_die = Die()
my_die.roll_die()
my_die.roll_die()       
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()