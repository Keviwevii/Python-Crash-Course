#Dictionaries in a list

me = {
    'first_name' : 'Kevin',
    'last_name' : 'Floyd',
    'age' : 100,
    'city' : 'Neverland',
}

candy = {
    'first_name' : 'Candy',
    'last_name' : 'Jones',
    'age' : 19,
    'city' : 'IDK',
}

johnny = {
    'first_name' : 'Johnny',
    'last_name' : 'Appleseed',
    'age' : 1300,
    'city' : 'Appleland',
}

users = [me, candy, johnny] #All of the dicts are in a list now

for user in users:
    print(user)