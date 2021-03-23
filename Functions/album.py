#Making a dictionary describing a music album

def make_album(artist_name, album_name,num_of_songs=None):
    album = {'Artist': artist_name.title(), 'Album Name': album_name.title()}
    if num_of_songs: #If number of songs is given an argument
        album['Number of Songs'] = num_of_songs
    return album

#3 dictionaries
haim = make_album('Haim', 'days are gone')
gaga = make_album('lady gaga', 'born this way')
rina = make_album('rina sawayama', 'rina sawayama')

print(haim, gaga, rina)

#Dictionary using the optional parameter
jackson = make_album('Michael Jackson', 'Idk', 6)
print(jackson)
    