#Copying Lists

my_pizzas = ['cheese', 'sausage', 'pepperoni']
friends_pizza = my_pizzas[:]  #Copying my_pizzas list

my_pizzas.append('ham')
friends_pizza.append('pineapple')

#For loop to show the lists have both been changed seperately
print('My favorite pizzas are: ')
for pizza in my_pizzas:
    print(pizza)
    
print('\nMy friends favorite pizzas are: ')  
for pizza in friends_pizza:
    print(pizza)