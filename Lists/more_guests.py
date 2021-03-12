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
Hi {guests[2]}, you are invited to my dinner!\n''')

print('Looks like we have found a bigger table!\n')

#Add guests to the beginning, middle and end of the list

guests.insert(0, 'Summer Walker')
guests.insert(2, 'Rina Sawayama')
guests.append('Erykah Badu')

print(f'''Hi {guests[0]}, you are invited to my dinner!
Hi {guests[2]}, you are invited to my dinner!
Hi {guests[-1]}, you are invited to my dinner!''')
