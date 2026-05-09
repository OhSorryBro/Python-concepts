# 8-6. City Names. 
# Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# Santiago, Chile
# Call your function with at least three city-country pairs, and print the value returned by it.
print("=====")
def city_country(city_name, country):
    print(f'{city_name.title()}, {country.title()}')

city_country('New York', 'USA')
city_country('Paris', 'France')
city_country('warsaw', 'poland')

# 8-7. Album. 
# Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title. 
# The return value should be a dictionary containing these two pieces of information. Use the function to create three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Using the special value None, add an optional parameter to make_album() that allows you to store the number of songs on the album. If the function call includes a value for the number of songs, add it to the album dictionary. 
# Make at least one new function call that also includes the number of songs.
print("=====")
def make_album(artist_name, album_title):
    album = {'artist_name': artist_name,
             'album_title': album_title}
    return album
album_1 = make_album('Dodo', 'Album 1')
album_2 = make_album('Dodo', 'Album 2')
album_3 = make_album('Dodo', 'Album 3')
print(album_1)
print(album_2)
print(album_3)

def make_album(artist_name, album_title,number_of_songs=None):
    if number_of_songs:
        album = {'artist_name': artist_name,
             'album_title': album_title,
             'number_of_songs': number_of_songs}
    else:    
        album = {'artist_name': artist_name,
                'album_title': album_title}
    return album

album_4 = make_album('Dodo', 'Album 4')
album_5 = make_album('Dodo', 'Album 5', 13)
print(album_4)
print(album_5)

# 8-8. User Albums. 
# Start with the program you wrote in Exercise 8-7. Add a while loop that allows users to enter an artist and an album title. 
# Once you have that information, call make_album() with the user's input and print the dictionary the program creates. 
# Make sure you've defined a value that lets the user exit the while loop.
print("=====")

def make_album(artist_name, album_title,number_of_songs=None):
    if number_of_songs:
        album = {'artist_name': artist_name,
             'album_title': album_title,
             'number_of_songs': number_of_songs}
    else:    
        album = {'artist_name': artist_name,
                'album_title': album_title}
    return album
active = True
while active:
    print("type 'q' to exit")
    artist_name = input('Type in artist name: ')
    if artist_name == 'q':
        active = False
    album_title = input('Type in album title: ')
    if album_title == 'q':
        active = False
    print(make_album(artist_name, album_title))
