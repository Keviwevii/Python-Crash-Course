# Checking that our list is not empty before continuing

#usernames = ['Jessie', 'Kev', 'admin', 'Nunu', 'Lux']
usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print(f'Hello {name}, would you like to see a status report?')
        else:
            print(f'Hello {name}, thank you for logging in again!')
else:
    print('We need to find some users')