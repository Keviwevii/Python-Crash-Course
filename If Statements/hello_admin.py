#Username greeting

usernames = ['Jessie', 'Kev', 'admin', 'Nunu', 'Lux']

for name in usernames:
    if name == 'admin':
        print(f'Hello {name}, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again!')