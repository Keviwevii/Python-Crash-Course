#cats_and_dogs.py but with a silent fail with the try/except block

def read_file(filename):
    '''Reading contents of a file'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
        
read_file('cats.txt')
read_file('dogs.txt')