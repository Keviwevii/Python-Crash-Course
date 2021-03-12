#Changing Guest List

guests = ['Lady Gaga', 'Mike Tyson', 'Evan Peters']

print(f'''Hi {guests[0]}, you are invited to my dinner!\n
Hi {guests[1]}, you are invited to my dinner!\n
Hi {guests[2]}, you are invited to my dinner!\n''')
print(f"Looks like {guests[2]} can't make it to the dinner.\n")

#Modify list

guests[2] = 'Xi Jingping'

print(f'''Hi {guests[0]}, you are again invited to my dinner!\n
Hi {guests[1]}, you are again invited to my dinner!\n
Hi {guests[2]}, you are invited to my dinner!\n''')