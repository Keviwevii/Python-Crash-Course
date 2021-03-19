#Adding pizza toppings until they want to stop

active = True

while active:
    topping = input('What topping do you want? Enter "quit" to quit. ' )
    topping = topping.lower()
    if topping == 'quit':
        break
    else:
        print(f'Adding {topping}')