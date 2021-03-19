#Checking people in a dinner group

group_count = input('How many people are in your group? ')
group_count = int(group_count)

if group_count > 8:
    print('You will have to wait for a table.')
else:
    print('Right this way please.')