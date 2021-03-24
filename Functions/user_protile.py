#Using a function mixing positional and arbitrary arguments

def build_profile(first,last, **user_info):
    '''Build a user dictionary with info provided'''
    user_info['First Name'] = first
    user_info['Last Name'] = last
    return user_info

kevin = build_profile('Kevin', 'Floyd', age=25)
print(kevin)