#Function that accepts a size and message 


def make_shirt(size,message):
    print(f'You ordered a size {size.title()} and your message is {message}.')

#Calling function with different arguments
#Positional arguments
make_shirt('m', 'I like potatoes')

#Keyword arguments
make_shirt(size='s',message='I like apples')




    