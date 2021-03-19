#Checking if an input number is a multiple of 10

number = input('What is your number? ')
number = int(number)

if (number % 10 == 0):
    print('Yes, it is a multiple of 10.')
else:
    print('No, this is not a multiple of 10.')