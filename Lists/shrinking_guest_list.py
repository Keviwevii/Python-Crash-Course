#Changing guest list to more guests

guests = ['Lady Gaga', 'Mike Tyson', 'Evan Peters']

print(f'''Hi {guests[0]}, you are invited to my dinner!
Hi {guests[1]}, you are invited to my dinner!
Hi {guests[2]}, you are invited to my dinner!\n''')
print(f"Looks like {guests[2]} can't make it to the dinner.\n")

#Modify list

guests[2] = 'Xi Jingping'

print(f'''Hi {guests[0]}, you are again invited to my dinner!
Hi {guests[1]}, you are again invited to my dinner!
Hi {guests[2]}, you are now invited to my dinner!\n''')

print('Looks like we have found a bigger table!\n')

#Add guests to the beginning, middle and end of the list

guests.insert(0, 'Summer Walker')
guests.insert(2, 'Rina Sawayama')
guests.append('Erykah Badu')

print(f'''Hi {guests[0]}, you are invited to my dinner!
Hi {guests[2]}, you are invited to my dinner!
Hi {guests[-1]}, you are invited to my dinner!\n''')

print("I'm sorry everyone the table won't be here in time. I can only have two guests.\n")

#Pop guests and tell them they cannot come

first_guest = guests.pop()
second_guest = guests.pop()
third_guest = guests.pop()
fourth_guest = guests.pop()

print(f"""I am sorry {first_guest} you cannot come.
I am sorry {second_guest} you cannot come.
I am sorry {third_guest} you cannot come.
I am sorry {fourth_guest} you cannot come.\n
{guests[0]} you can still come.
{guests[1]} you can still come.
There are now {len(guests)} people on the list.""")

#Delete the last two people from the list and check

del guests[0]
del guests[0]

print(guests)


