#Continuing album with a while loop

def make_album(artist_name, album_name,num_of_songs=None):
    album = {'Artist': artist_name.title(), 'Album Name': album_name.title()}
    if num_of_songs: #If number of songs is given an argument
        album['Number of Songs'] = num_of_songs
    return album

#While loop that takes inputs and calls the function with the info
while True:
    print('Lets make an album dictionary, press q at any time to quit.')
    name = input('Artist name: ')
    if name == 'q':
        break
    
    album = input('Album name: ')
    if album == 'q':
        break
    
    #Function call with info from input
    user_album = make_album(name,album)
    print(f'Here is your dictionary: {user_album}')