import random #importing random module

number = random.randint(0,10) #using randint method : it returns a random integer in specified range ( 0 to 10 )
print("Random integer number : ",number)

fruits = ('Apple','Banana','Grapes','Guava')
print('\nTuple of Fruits : ',fruits)
fruit = random.choice(fruits) #using choice method : it return a random value
print('Radom choice : ',fruit)

cards = ['2','3','4','5','6','7','8','9','A','J','Q','K']
print('\nList of items : ',cards,'\n')
random.shuffle(cards) #using shuffle method : it shuffles the list of values randomly
print('Shuffled Cards : ',cards)

