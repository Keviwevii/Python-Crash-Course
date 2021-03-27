#Using a while loop to write to a file

filename = 'guest_book.txt'


with open(filename, 'w') as file_object:
    #Writing names to the file
    while True:
        name = input('Enter a name, enter q when you are done. ')
        if name.lower() == 'q':
            break
        else: 
            file_object.write(f'{name.title()}\n')