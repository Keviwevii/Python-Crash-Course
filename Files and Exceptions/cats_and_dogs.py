#A program to read contents of a file with try and except

def read_file(filename):
    '''Reading contents of a file'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('Unfortunately you dont have that file!')
    else:
        print(contents)
        
read_file('cats.txt')
read_file('dogs.txt')