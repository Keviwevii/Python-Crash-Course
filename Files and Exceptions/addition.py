#Using try and except blocks to catch a problem

def addition():
    '''Function that checks and lets us add numbers'''
    print('Let us add some numbers.')
    try:
        first_num = int(input('What is the first number? '))
        second_num = int(input('What is the second number? '))
    except ValueError:
        print('You did not give me a number!')
        addition()
    else:
        answer = first_num + second_num
        return f'Your answer is {answer}.'
    
print(addition())