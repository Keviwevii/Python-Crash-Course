#Program that stimulates how websites ensure everyone has unique usernames

current_users = ['Kev', 'Jerry', 'Tate', 'Apple', 'Lewis']
current_users_copy = [user.lower() for user in current_users] # A copy list that contains usernames in lowercase


new_users = ['Jenny', 'KEV', 'Ginny', 'Lewis', 'Pini']

for user in new_users:
    if user.lower() in current_users_copy:
        print(f'Im sorry {user}, that name is taken.')
    else:
        print(f'This username is avaliable')
        
