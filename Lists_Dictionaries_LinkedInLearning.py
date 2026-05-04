fav_movies = ["Sandlot","The Lego Movie", "Dune"]
print(fav_movies[0])

fav_numbers = [0,1,2]
print(fav_numbers[0])

print(len(fav_movies))
fav_movies.append('Iron Man')

print(len(fav_movies))

print(fav_movies)

fav_movies.insert(1,"Batman")
print(fav_movies)
del(fav_movies[2])

print(fav_movies)
del(fav_movies[1])
del(fav_movies[1])
del(fav_movies[1])

print(fav_movies)
fav_movies = ["Sandlot","The Lego Movie", "Dune"]

for number in range(3):
    print("===")

for movie in fav_movies:
    print(movie)

for loop_no in range(40):
    loop_no = (loop_no + 1) * 2
    print(loop_no)
print('===')
cats ={
    'Jane' : 6,
    'Tom' : 14,
    'Sara' : 8,
}
cats['Wilson'] = 1
print(cats['Tom'])
del cats["Tom"]
print(cats)
print(len(cats))

bool_dictionary = {
    1 : True,
    2 : False,
    3 : True,
    4 : False,
}