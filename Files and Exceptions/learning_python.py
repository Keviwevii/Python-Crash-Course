#Reading from my file learningpython.txt

filename = 'learning_python.txt'

with open(filename) as file_object: #Entire file
    contents = file_object.read()
    
with open(filename) as file_object: #Looping through the file
    for line in file_object:
        print(line) #Print with spaces due to no rstrip
        
with open(filename) as file_object:
    lines = file_object.readlines() #This stores each line in a list
    
    
for line in lines:
    print(line)

