#Making a todo list

def make_list():
    '''Making a list to return'''
    todo_list =[]
    while True:
        list_item = input('''What do you need to do today? 
Enter one at a time or enter q to quit. ''')
        if list_item == 'q':
            break
        else:
            todo_list.append(list_item)
    return todo_list #Returns a list of the list_items
            
def show_list(list):
    '''Showing all of your todo's'''
    print('Here is what you need to do for today.')
    for item in list:
        print(item)
    return list
        
def add_to_file(todos):
    '''Writes all of our todos to a file.'''
    filename = 'todolist.txt'
    with open(filename, 'w') as f:
        for item in todos:
            f.write(f'{item}\n')
        
        
    
#Calls show list with make_list as an argument
add_to_file(show_list(make_list()))
