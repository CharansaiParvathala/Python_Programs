animes = ['attack on titan','death note','hunter x hunter','one piece','naruto']
characters = ['eren','L','gon','luffy','naruto']

anime_details = zip(animes, characters)
#we can convert the zip elements into specific type like list,dictinary,..,etc.
print(type(anime_details))

anime_details = list(anime_details)
print(f'\n{type(anime_details)}')
for elements in anime_details:
    print(f'Anime : {elements[0]} --> {elements[1]}')

anime_details = dict(anime_details) #converting into dictionary type
print(f'\n{type(anime_details)}')
for key,value in anime_details.items():
    print(f'anime : {key} --> {value}')