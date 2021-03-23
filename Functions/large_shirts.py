#Modifying tshirt.py with default parameters

def make_shirt(size='L',message='I love Python'):
    print(f'You ordered a size {size.title()} and your message is {message}.')
    
#Large shirt with message    
make_shirt()

#Medium shirt with message
make_shirt('m')

#Any size and any message
make_shirt('s', "'Where is the cake?'")