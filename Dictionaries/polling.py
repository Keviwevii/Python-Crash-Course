#Checking a dictionary during loop

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

sample_people = ['sarah', 'kevin'] #Checking list

for name in favorite_languages:
    if name not in sample_people:
        print(f'{name.title()} thank you for already taking the poll!')
    else:
        print(f'{name.title()} you need to take the poll again!')
       