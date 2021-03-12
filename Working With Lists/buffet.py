#Working with tuples

#Five basic foods to store in a tuple

foods = ('pizza', 'ice cream', 'fries', 'burger', 'fish')
print('We offer the following foods today:\n')

for food in foods:
    print(food.title())
    
#Revised tuple and menu

food = ('pizza', 'ice cream', 'fries', 'burger', 'fish', 'turnips', 'potatoes')
print('\nOur menu has just changed, please take a look.\nWe are now offering:\n')

for food in foods:
    print(food.title())