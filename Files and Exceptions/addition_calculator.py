# Same code as addition.py but with a while loop


def addition():
    '''Function that checks and lets us add numbers as long as we want'''
    print('Let us add some numbers. Enter q at any time to quit.')
    while True:
        first_num = input('What is the first number? ')
        if first_num == 'q':
            break
        second_num = input('What is your second number? ')
        if second_num == 'q':
            break
        try:
            first_num = int(first_num)
            second_num = int(second_num)
        except ValueError:
            print('You did not give me a number!')
            addition()
        else:
            answer = first_num + second_num
            print(f'Your answer is {answer}.')


addition()
