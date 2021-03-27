#Writing responses to a file

filename = 'programming_poll.txt'

with open(filename,'w') as file_object:
    while True:
        response = input('Why do you like programming? Enter q when finished.')
        if response == 'q':
            break
        else:
            file_object.write(f'{response.capitalize()}\n')