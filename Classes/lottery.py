#Using the random module to make a lottery

from random import choice

possible_winner = [ 3, 4, 5, 6, 7, 8, 10, 11, 12, 'a', 'b', 'c', 'd', 'e']
first_character = choice(possible_winner)
second_character = choice(possible_winner)
third_character = choice(possible_winner)
fourth_character = choice(possible_winner)
winning_ticket = f'{first_character} {second_character} {third_character} {fourth_character}'

print('If you have these 4 characters you win a prize!')
print(winning_ticket)