turtles = ['Hey', 'Hello', 'Bonjour']
new_turtles = []

def show_messages(messages_list,new_message_list):
    '''Print each message in a list'''
    for message in messages_list:
        print(f'Adding message to new list: {message}')
        new_message_list.append(message)
        messages_list.pop()
    
    print(new_message_list)
    print(messages_list)
       
print(show_messages(turtles,new_turtles))